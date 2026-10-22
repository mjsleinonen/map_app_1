def test_karttasivu_latautuu(client):
    """Testataan, että karttasivun reitti palauttaa HTTP 200 OK"""
    response = client.get('/')  # Tehdään simuloitu GET-pyyntö reittiisi
    assert response.status_code == 200
    assert b'id="map"' in response.data or b'id="kartta"' in response.data

def test_pisteen_tallennus_post(client):
    """Testataan, että kartalta lähetetyt koordinaatit otetaan vastaan"""
    testidata = {
        'lat': '60.1699',
        'lon': '24.9384',
        'sisalto': 'Testipiste'
    }
    # Simuloidaan HTML-lomakkeen POST-lähetystä
    response = client.post('/lisaa', data=testidata, follow_redirects=True)
    assert response.status_code == 200
    assert b'Testipiste' in response.data
