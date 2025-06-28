from fastapi.testclient import TestClient
from starlette import status

from app.main import app

client = TestClient(app)

def test_recommend_success():
    data = {
        "gender": "male",
        "height": 175,
        "weight": 65,
        "age": 34,
        "goal": "lean-bulking"
    }
    response = client.post("/recommend/", json=data)
    assert response.status_code == status.HTTP_200_OK

    res = response.json()
    assert "bmi" in res
    assert "bmr" in res
    assert "recommended_intake" in res
    assert "recommended_menu" in res
    assert len(res["recommended_menu"]) == 3

def test_recommend_with_zero_height():
    data = {
        "gender": "male",
        "height": 0,
        "weight": 65,
        "age": 34,
        "goal": "lean-bulking"
    }
    response = client.post("/recommend/", json=data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_recommend_with_invalid_gender():
    data = {
        "gender": "alien",
        "height": 0,
        "weight": 65,
        "age": 34,
        "goal": "lean-bulking"
    }
    response = client.post("/recommend/", json=data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_recommend_with_negative_weight():
    data = {
        "gender": "male",
        "height": 162,
        "weight": -35,
        "age": 34,
        "goal": "lean-bulking"
    }
    response = client.post("/recommend/", json=data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

def test_recommend_with_extreme_weight():
    data = {
        "gender": "female",
        "height": 162,
        "weight": 285,
        "age": 34,
        "goal": "lean-bulking"
    }
    response = client.post("/recommend/", json=data)
    assert response.status_code == status.HTTP_200_OK
    res = response.json()
    assert res["bmi"] > 50