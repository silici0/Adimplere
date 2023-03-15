from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ping():
    response = client.get("/games")
    assert response.status_code == 200
    assert response.json() == [
                                {
                                  "uuid": "2de052d3-9453-4cfd-949f-6eb71457099f",
                                  "short_description": "Esqueça tudo que você sabe sobre os jogos da série The Legend of Zelda. Entre em um mundo de descobertas, exploração e aventura em The Legend of Zelda: Breath of the Wild, o novo jogo da famosa série que veio para romper barreiras. Viaje pelos vastos campos, florestas e montanhas enquanto descobre o que aconteceu com o reino de Hyrule nesta deslumbrante aventura a céu aberto. E agora no Nintendo Switch, a sua jornada tem mais liberdade do que nunca. Leve o seu console para qualquer lugar e viva aventuras na pele de Link da maneira que quiser."
                                },
                                {
                                  "uuid": "7c6cc13b-0a0f-4325-a1c4-2f5738c957ee",
                                  "short_description": "Assassin's Creed® ORIGINSO O Antigo Egito, uma terra de grandeza e intriga, está desaparecendo sob um conflito implacável por poder."
                                }
                              ]
