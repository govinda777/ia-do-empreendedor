# 🎬 Movies Dataset App

Uma aplicação simples em Streamlit que mostra dados de filmes do [The Movie Database (TMDB)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movies-dataset-template.streamlit.app/)

## Como instalar, configurar e executar na sua máquina

### Pré-requisitos

- Python 3.11 ou superior
- Pip (gerenciador de pacotes do Python)

### Passos para instalação

1. Clone o repositório para a sua máquina local:

   ```sh
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

### Executando a aplicação

1. Execute o aplicativo Streamlit:

   ```sh
   streamlit run streamlit_app.py
   ```

2. Acesse a aplicação no seu navegador em `http://localhost:8501`.

### Estrutura do Projeto

```plaintext
.devcontainer/
.github/
config/
data/
services/
templates/
tests/
utils/
app.py
streamlit_app.py
requirements.txt
README.md
```

- **`streamlit_app.py`**: Arquivo principal da aplicação Streamlit que visualiza os dados dos filmes.
- **`app.py`**: Outro exemplo de aplicação Streamlit com funcionalidades adicionais.
- **`data/`**: Contém os arquivos CSV com os dados dos filmes.
- **`services/`**: Contém serviços para processamento de dados e formulários.
- **`utils/`**: Contém utilitários como geradores de relatórios.
- **`tests/`**: Contém testes unitários para os serviços.

### Contribuindo

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
4. Faça um push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

### Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
