import pytest

from application import create_app, db

@pytest.fixture()
def app():
    # Luodaan sovellus testikonfiguraatiolla
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"  # Käytetään nopeaa välimuistitietokantaa testeissä
    })

    # Alustetaan tietokantataulut testejä varten
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
