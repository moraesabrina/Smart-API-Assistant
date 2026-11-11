
from unittest.mock import patch, MagicMock
from assistente_ia import perguntar_ia


def test_resposta_ia():
    resposta_simulada = MagicMock()
    resposta_simulada.text = "HTTP 500 é um erro interno do servidor."

    with patch("assistente_ia.genai.Client") as cliente_mock:
        cliente_mock.return_value.models.generate_content.return_value = resposta_simulada

        resposta = perguntar_ia("O que significa HTTP 500?")

        assert resposta == "HTTP 500 é um erro interno do servidor."

  
def test_erro_503():
    from google.genai.errors import ServerError

    with patch("assistente_ia.genai.Client") as cliente_mock:
        cliente_mock.return_value.models.generate_content.side_effect = ServerError(
            503,
            {"error": {"message": "Serviço indisponível"}},
        )

        resposta = perguntar_ia("O que significa HTTP 500?")

        assert "temporariamente indisponível" in resposta

