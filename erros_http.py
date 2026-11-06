erros_http = {
    "400": {
        "nome": "Bad Request",
        "descricao": "A requisição contém dados inválidos.",
        "solucao": "Verifique os campos, parâmetros e JSON."
    },
    "401": {
        "nome": "Unauthorized",
        "descricao": "A requisição não possui autenticação válida.",
        "solucao": "Verifique o token e o Authorization."
    },
    "403": {
        "nome": "Forbidden",
        "descricao": "O servidor recusou o acesso.",
        "solucao": "Verifique as permissões da aplicação."
    },
    "404": {
        "nome": "Not Found",
        "descricao": "O recurso não foi encontrado.",
        "solucao": "Confira a URL e o endpoint."
    },
    "500": {
        "nome": "Internal Server Error",
        "descricao": "O servidor encontrou um erro inesperado.",
        "solucao": "Verifique os logs e o estado do serviço."
    }
}
