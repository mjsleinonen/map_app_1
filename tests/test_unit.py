import pytest
import unittest

import sys
from pathlib import Path

# Import ylempää
nykyinen_kansio = Path(__file__).resolve().parent
ylempi_kansio = nykyinen_kansio.parent
sys.path.insert(0, str(ylempi_kansio))

from application.models import Tehtava
from application import db
from application import create_app

app = create_app()

class TestKarttaSovellus(unittest.TestCase):

    def setUp(self):
        """Suoritetaan AUTOMAATTISESTI ennen JOKAISTA testifunktiota."""
        # 1. Luodaan sovellusinstanssi tehtaan kautta
        self.app = create_app()
        
        # 2. Päivitetään testiasetukset (käytetään esim. muistitietokantaa)
        self.app.config.update({
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
        })

        # 3. Luodaan testiasiakas pyyntöjen simulointia varten
        self.client = self.app.test_client()

        # 4. AKTIVOIDAAN SOVELLUSKONTEKSTI (Erittäin tärkeää Application Factoryssa!)
        self.app_context = self.app.app_context()
        self.app_context.push()

        # 5. Alustetaan tietokantataulut puhtaina tätä testiä varten
        db.create_all()

    def tearDown(self):
        """Suoritetaan AUTOMAATTISESTI jokaisen testifunktion jälkeen."""
        # Tyhjennetään tietokanta ja poistetaan konteksti, jotta seuraava testi alkaa puhtaalta pöydältä
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_karttasivu_palauttaa_ok(self):
        """Testataan, että karttasivu latautuu oikein."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_pisteen_tallennus_tietokantaan(self):
        """Testataan lomakelähetystä ja tietokantatallennusta."""
        testidata = {
            'lat': '60.1699',
            'lon': '24.9384',
            'sisalto': 'Helsinki'
        }
        
        # Tehdään simuloitu POST-pyyntö reittiin
        response = self.client.post('/lisaa', data=testidata)
        self.assertEqual(response.status_code, 302)

        # Tarkistetaan SQLAlchemy-mallilla, että piste todella tallentui muistitietokantaan
        piste = Tehtava.query.filter_by(sisalto='Helsinki').first()
        self.assertIsNotNone(piste)
        self.assertEqual(piste.lat, 60.1699)

if __name__ == '__main__':
    unittest.main()