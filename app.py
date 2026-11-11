
import streamlit as st

from erros_http import erros_http
from assistente_ia import perguntar_ia

st.set_page_config(
    page_title="Smart API Assistant",
    page_icon="🤖",
    layout="wide"
)

# Cabeçalho
st.title("🤖 Smart API Assistant")
st.markdown(
    "### Inteligência artificial aplicada ao suporte de APIs"
)
st.caption(
    "Consulte códigos HTTP e investigue problemas "
    "em integrações de APIs REST."
)

st.divider()

# Navegação
aba_http, aba_ia = st.tabs([
    "🔎 Consultar HTTP",
    "🤖 Assistente IA"
])

with aba_http:
    st.subheader("Consulta de códigos HTTP")
    st.write("Descubra o significado de erros e possíveis soluções.")

    codigo = st.text_input(
        "Código HTTP",
        placeholder="Exemplo: 404"
    )

    if st.button("Consultar código", type="primary"):
        codigo = codigo.strip()

        if not codigo:
            st.warning("Digite um código HTTP.")

        elif codigo in erros_http:
            erro = erros_http[codigo]

            st.success(f"HTTP {codigo} - {erro['nome']}")
            st.markdown("**Descrição:**")
            st.write(erro["descricao"])

            st.markdown("**Possível solução:**")
            st.info(erro["solucao"])

        else:
            st.warning("Código ainda não cadastrado.")

with aba_ia:
    st.subheader("Assistente de Inteligência Artificial")
    st.write(
        "Faça perguntas sobre APIs REST, códigos HTTP "
        "e investigação de erros."
    )

    pergunta = st.text_area(
        "Sua pergunta",
        placeholder="Exemplo: Como investigar um erro HTTP 500?",
        height=120
    )

    if st.button("Enviar pergunta", type="primary"):
        if not pergunta.strip():
            st.warning("Digite uma pergunta.")

        else:
            with st.spinner("Analisando sua pergunta..."):
                resposta = perguntar_ia(pergunta)

            st.markdown("### 🤖 Resposta do assistente")
            st.markdown(resposta)

st.divider()

st.caption(
    "Desenvolvido por Sabrina Moraes | "
    "Python • Streamlit • Google Gemini"
)
