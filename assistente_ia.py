import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors
from google.genai import types

# Carrega as variáveis do arquivo .env

load_dotenv()

chave_api = os.getenv("GEMINI_API_KEY")

if not chave_api:
    try:
        import streamlit as st
        chave_api = st.secrets.get("GEMINI_API_KEY")
    except (FileNotFoundError, KeyError):
        chave_api = None


def perguntar_ia(pergunta):
    if not chave_api:
        return "Erro: chave de API não configurada."

    try:
        # Conecta o sistema com a IA Gemini
        cliente = genai.Client(
    api_key=chave_api,
    http_options=types.HttpOptions(
        timeout=20000
    )
)

        # Instruções para a IA
        prompt = f"""
        Você é um assistente especializado em APIs REST
        e códigos de status HTTP.

        Você é um assistente especializado em APIs financeiras

        Responda em português, com linguagem simples.

        Explique possíveis causas do problema e
        sugira verificações para investigação.

        Não invente informações sobre sistemas,
        logs ou integrações que você não analisou.

        Pergunta do usuário:
        {pergunta}
        """

        # Envia a pergunta ao modelo
        resposta = cliente.models.generate_content(
     model="gemini-3.5-flash",
            contents=prompt
        )

        return resposta.text or "A IA não retornou uma resposta."

    
    except errors.APIError as erro:
        print(f"Erro na API Gemini: {erro.code} - {erro.message}")
        if erro.code == 404:
            return "O modelo de IA solicitado não está disponível."

        elif erro.code == 429:
            return "Limite de requisições atingido. Tente novamente mais tarde."

        elif erro.code == 503:
            return "O serviço de IA está temporariamente indisponível. Tente novamente em alguns instantes."

        else:
            return f"Não foi possível consultar a IA (erro {erro.code})."

    except Exception as erro:
        print(f"Erro inesperado: {type(erro).__name__}")
        return "Ocorreu um erro inesperado ao consultar a IA."

