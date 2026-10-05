from app import app


def test_home_page():
    app.config["TESTING"] = True
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_predict_page():
    app.config["TESTING"] = True
    client = app.test_client()

    response = client.post(
        "/predict",
        data={"area": "1000"},
    )

    assert response.status_code == 200
