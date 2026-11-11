# 🚀 Smart API Assistant

Assistente inteligente desenvolvido em **Python**, com integração à API do **Google Gemini**, para auxiliar na compreensão de códigos HTTP e na investigação de problemas em integrações de APIs REST.

## 📌 Sobre o projeto

O Smart API Assistant é um projeto desenvolvido para facilitar a compreensão de erros HTTP e apoiar a investigação de problemas técnicos em APIs.

A ideia surgiu a partir da minha experiência profissional com suporte técnico a desenvolvedores e clientes que utilizam APIs co foco no sistema financeiro, como recebimento de PIX, emissão de boletos, gestão de pagamentos, conciliação, entre outros.

O projeto combina consultas locais a códigos HTTP com inteligência artificial generativa, permitindo que o usuário obtenha explicações, possíveis causas de falhas e sugestões de investigação.

## ⚙️ Funcionalidades

- Consulta de códigos de status HTTP.
- Exibição de nomes, descrições e possíveis soluções.
- Identificação de códigos não cadastrados.
- Menu interativo pelo terminal.
- Integração com a API do Google Gemini.
- Perguntas em linguagem natural sobre APIs REST.
- Sugestões de investigação de problemas técnicos.
- Tratamento de erros da API de IA, incluindo HTTP 404, 429 e 503.
- Configuração de timeout para requisições.
- Testes automatizados utilizando unittest, pytest e mocks.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem principal do projeto.
- **Google Gemini API:** integração com inteligência artificial generativa.
- **Google Gen AI SDK:** comunicação com os modelos Gemini.
- **python-dotenv:** gerenciamento de variáveis de ambiente.
- **pytest:** execução de testes automatizados.
- **unittest.mock:** simulação de respostas e falhas da API.
- **Git e GitHub:** versionamento e hospedagem do código.
- **Visual Studio Code:** ambiente de desenvolvimento.

## 📂 Estrutura do projeto

```text
Smart-API-Assistant/
│
├── main.py
├── assistente_ia.py
├── erros_http.py
├── test_erros_http.py
├── teste_assistente_ia.py
├── requirements.txt
├── .gitignore
└── README.md
```

O arquivo `.env` deve ser criado localmente e não deve ser publicado no repositório.

## ▶️ Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/moraesabrina/Smart-API-Assistant.git
cd Smart-API-Assistant
```

### 2. Criar um ambiente virtual

```bash
python -m venv .venv
```

No Windows (PowerShell), ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Configurar a chave da API

Crie um arquivo chamado `.env` na raiz do projeto e adicione:

```env
GEMINI_API_KEY=sua_chave_aqui
```

A chave pode ser obtida no Google AI Studio.

**Importante:** nunca compartilhe ou publique sua chave de API.

### 5. Executar o assistente

```bash
python main.py
```

O programa apresenta um menu interativo:

```text
===== MENU PRINCIPAL =====
1 - Consultar erro HTTP
2 - Perguntar para a IA
3 - Sair

Escolha uma opção:
```

## 🧪 Testes automatizados

O projeto possui testes para verificar o comportamento das funcionalidades e simular respostas da API.

Para executar todos os testes com pytest:

```bash
python -m pytest -v
```

Os testes da integração com IA incluem:

- Validação de uma resposta simulada do Gemini.
- Simulação de indisponibilidade da API (HTTP 503).

Os testes com mocks não exigem chamadas reais ao Gemini.

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, pratiquei:

- Lógica de programação em Python.
- Estruturas condicionais e laços de repetição.
- Funções, módulos e dicionários.
- Integração com APIs externas.
- Inteligência artificial generativa.
- Engenharia de prompts.
- Gerenciamento de variáveis de ambiente.
- Tratamento de exceções.
- Testes automatizados e utilização de mocks.
- Ambientes virtuais e gerenciamento de dependências.
- Versionamento de código com Git.

## 🔮 Próximas melhorias

- Ampliar a base de códigos HTTP.
- Implementar novas verificações automatizadas.
- Melhorar a experiência de interação com o usuário.
- Desenvolver uma interface web.
- Expandir os testes automatizados.
- Explorar novas funcionalidades de análise de erros em APIs.

## 👩‍💻 Desenvolvedora

**Sabrina Moraes**

Estudante de Engenharia de Software, com interesse em desenvolvimento back-end, APIs, automação e inteligência artificial generativa.

[Meu GitHub](https://github.com/moraesabrina)