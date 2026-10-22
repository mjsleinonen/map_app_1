from application.extensions import db

class Tehtava(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    sisalto = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Tehtävä {self.id}: {self.sisalto}>'

    def to_dict(self):
        """Tämä metodi muuttaa rivin JSON-yhteensopivaksi"""
        return {
            'id': self.id,
            'sisalto': self.sisalto,
            'lat': self.lat,
            'lon': self.lon
    }

    