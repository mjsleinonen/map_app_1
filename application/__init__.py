from flask import Flask

from application.extensions import db
from application.reitit.paasivu import paasivu_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tietokanta.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Liitetään tietokanta sovellukseen
    db.init_app(app)
    
    # Rekisteröidään sivujen reitit (Blueprint)
    app.register_blueprint(paasivu_bp)

    with app.app_context():
        # Tuodaan mallit TÄÄLLÄ sovelluksen sisällä, jotta SQLAlchemy rekisteröi ne.
        from .models.tehtava import Tehtava
        
        # Luodaan .db-tiedosto ja taulut, jos niitä ei ole olemassa
        db.create_all()
    
    return app