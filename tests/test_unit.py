import pytest
import unittest

import unittest

import sys
from pathlib import Path

# Haetaan nykyisen tiedoston kansio ja sen ylempi kansio (parent)
nykyinen_kansio = Path(__file__).resolve().parent
ylempi_kansio = nykyinen_kansio.parent

# Lisätään ylempi kansio sys.path-listan alkuun
sys.path.insert(0, str(ylempi_kansio))

from app1 import app, db, User

class FlaskTestCase(unittest.TestCase):

    # Ajoa ennen jokaista testiä: luodaan tyhjä testikanta muistiin
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Testataan muistikannalla
        self.client = app.test_client()
        
        with app.app_context():
            db.create_all()

    # Siivous testin jälkeen
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # 1. Testaa, että etusivu vastaa HTTP 200 (OK)
    def test_etusivu(self):
        vastaus = self.client.get('/')
        self.assertEqual(vastaus.status_code, 200) 

    # 2. Testaa rekisteröintisivun latautuminen (GET)
    def test_register_sivu_latautuu(self):
        vastaus = self.client.get('/lisaa')
        self.assertEqual(vastaus.status_code, 200)

    # 3. Testaa lomakkeen lähetys ja tallennus kantaan (POST)
    def test_kayttajan_rekisterointi(self):
        vastaus = self.client.post('/lisaa', data=dict(
            name='testiukko',
            rooli='rooli'
        ), follow_redirects=True)
        
        # Tarkistetaan, että pyyntö meni läpi (200)
        self.assertEqual(vastaus.status_code, 200)
        
        # Tarkistetaan vielä suoraan tietokannasta, että käyttäjä todella tallentui
        with app.app_context():
            kayttaja = User.query.filter_by(name='testiukko').first()
            self.assertIsNotNone(kayttaja)
            self.assertEqual(kayttaja.name, 'testiukko')

    # 4. testaa user lista
    def test_users_sivu_latautuu(self):
        vastaus = self.client.get('/kayttajat')
        self.assertEqual(vastaus.status_code, 200)

if __name__ == '__main__':
    unittest.main()