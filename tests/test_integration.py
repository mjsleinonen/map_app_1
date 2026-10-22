def test_etusivu_latautuu(client):
    # Tehdään simuloitu GET-pyyntö etusivulle, index-sivu /
    vastaus = client.get('/')

    assert vastaus.status_code == 200
    assert b"Paikkapohjainen" in vastaus.data
