from starlette.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_list_games():
    response = client.get("/games")
    assert response.status_code == 200
    assert response.json()[0]['uuid']
    assert response.json()[0]['short_description']


def test_list_game_by_name():
    response = client.get("/games/Zelda")
    assert response.status_code == 200
    assert response.json()[0]['uuid']
    assert response.json()[0]['long_description']
