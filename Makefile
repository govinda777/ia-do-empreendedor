# Makefile para IA do Empreendedor

# Nome do ambiente virtual
VENV = venv

# Caminho para o interpretador Python no ambiente virtual
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Verifica o sistema operacional para ajustar os caminhos no Windows
ifeq ($(OS),Windows_NT)
    PYTHON = $(VENV)\Scripts\python.exe
    PIP = $(VENV)\Scripts\pip.exe
endif

# Cria o ambiente virtual
$(VENV):
	python -m venv $(VENV)

# Instala as dependências no ambiente virtual
install: $(VENV)
	$(PIP) install -r requirements.txt

# Executa a aplicação Streamlit
run: $(VENV)
	$(PYTHON) -m streamlit run streamlit_app.py

# Executa os testes
test: $(VENV)
	$(PYTHON) -m pytest tests/

# Remove o ambiente virtual
clean:
	rm -rf $(VENV)
