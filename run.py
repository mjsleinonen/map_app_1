import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from application import create_app

import webbrowser as wb

app = create_app()

"""
# Määritetään SQLite-tietokannan tallennuspaikka (tulee instance-kansioon)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tietokanta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# TIETOKANTAMALLI (Database Model)
class Tehtava(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sisalto = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Tehtävä {self.id}>'

# REITIT (Routes)

# 1. Pääsivu: Näytetään kaikki tehtävät tietokannasta
@app.route('/')
def index():
    kaikki_tehtavat = Tehtava.query.all()
    return render_template('index.html', tehtavat=kaikki_tehtavat)

# 2. Tehtävän lisääminen tietokantaan
@app.route('/lisaa', methods=['POST'])
def lisaa():
    uusi_sisalto = request.form.get('sisalto')
    if uusi_sisalto:
        uusi_tehtava = Tehtava(sisalto=uusi_sisalto)
        db.session.add(uusi_tehtava)
        db.session.commit()
    return redirect(url_for('index'))

# 3. Tehtävän poistaminen tietokannasta
@app.route('/poista/<int:id>')
def poista(id):
    poistettava = Tehtava.query.get_or_404(id)
    db.session.delete(poistettava)
    db.session.commit()
    return redirect(url_for('index'))

# ALUSTUS: Luodaan tietokantapohja automaattisesti, jos sitä ei ole
with app.app_context():
    db.create_all()
"""

if __name__ == '__main__':
    local_url = "http://127.0.0.1:5000"
    wb.open(local_url)
    app.run(debug=True)
