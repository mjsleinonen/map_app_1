from flask import Blueprint, render_template, request, redirect, url_for
from application.extensions import db
from application.models.tehtava import Tehtava

# Luodaan Blueprint-olio. 
# Ensimmäinen parametri on Blueprintin nimi, jota käytetään url_for-funktioissa.
paasivu_bp = Blueprint('paasivu', __name__)

@paasivu_bp.route('/')
def index():
    #kaikki_tehtavat = Tehtava.query.all()
    kaikki_tehtavat = [piste.to_dict() for piste in Tehtava.query.all()]

    return render_template('index.html', tehtavat=kaikki_tehtavat)

@paasivu_bp.route('/lisaa0', methods=['POST'])
def lisaa0():
    uusi_sisalto = request.form.get('sisalto')
    if uusi_sisalto:
        uusi_tehtava = Tehtava(sisalto=uusi_sisalto)
        db.session.add(uusi_tehtava)
        db.session.commit()
    return redirect(url_for('paasivu.index'))  # Huom: 'paasivu.index' Blueprintin nimen mukaan

@paasivu_bp.route('/lisaa', methods=['POST'])
def lisaa():
    uusi_sisalto = request.form.get('sisalto')
    # Haetaan koordinaatit lomakkeelta ja muutetaan ne numeroiksi (float)
    uusi_lat = request.form.get('lat')
    uusi_lng = request.form.get('lng')
    
    if uusi_sisalto and uusi_lat and uusi_lng:
        uusi_tehtava = Tehtava(
            sisalto=uusi_sisalto,
            lat=float(uusi_lat),
            lng=float(uusi_lng)
        )
        db.session.add(uusi_tehtava)
        db.session.commit()
        
    return redirect(url_for('paasivu.index'))

@paasivu_bp.route('/poista/<int:id>')
def poista(id):
    poistettava = Tehtava.query.get_or_404(id)
    db.session.delete(poistettava)
    db.session.commit()
    return redirect(url_for('paasivu.index'))