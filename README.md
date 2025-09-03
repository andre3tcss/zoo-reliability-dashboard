# Zoo Reliability Dashboard

## Visão Geral

Este projeto é um dashboard simples para análise de dados de performance de sistemas, simulando um cenário de monitoramento de infraestrutura (SRE). O script carrega dados de um arquivo CSV, processa-os com a biblioteca Pandas e gera visualizações de métricas chave (CPU, Memória, Latência) usando Matplotlib.

Este trabalho foi desenvolvido como parte do portfólio da disciplina de Linguagem Python no Centro Universitário ENIAC.

## Pré-requisitos

* Python 3.9+
* pip e venv

## Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1.  *Clone o repositório:*
    `bash`
    `git clone [https://github.com/seu-usuario/zoo-reliability-dashboard.git](https://github.com/seu-usuario/zoo-reliability-dashboard.git)`
    `cd zoo-reliability-dashboard`
    
2.  *Crie e ative o ambiente virtual:*
    bash
    `python -m venv venv`
    # No Windows:
    # venv\Scripts\activate
    # No macOS/Linux:
    # source venv/bin/activate
    
3.  *Instale as dependências:*
    `bash`
    `pip install -r requirements.txt`
    

## Uso

Para executar o script e gerar os gráficos, rode o seguinte comando no seu terminal:

`bash`
`python` main.py

Os gráficos serão salvos como arquivos de imagem no diretório do projeto.

## Testes

Para rodar os testes unitários e verificar a integridade da função de carregamento de dados, use o Pytest:

`bash`
`pytest`
