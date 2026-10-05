from app import app
def test_home_page():
    app.config["Testing"] == True
    client= app.test_client()
    response= client.get("/")
    assert response.status_code == 200
def test_predict_page():
    app.config["Testing"] == True
    clients = app.test_client()
    responses= clients.post(
        "/predict",
        data= {"area" : "1000"}
    )