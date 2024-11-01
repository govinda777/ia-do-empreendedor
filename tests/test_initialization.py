from streamlit.web import cli as stcli
from unittest.mock import patch
import subprocess
import time


def test_app_initialization():
    """Testa se o aplicativo Streamlit inicializa sem erros de forma silenciosa e não bloqueante."""
    with patch.object(stcli, "main"):
        try:
            # Executa o comando de forma silenciosa e não bloqueante
            process = subprocess.Popen(
                ["streamlit", "run", "streamlit_app.py"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )

            # Aguarda alguns segundos para garantir que o Streamlit iniciou
            time.sleep(5)

            # Verifica se o processo ainda está ativo (o que indica que iniciou sem erros)
            assert process.poll() is None, "O aplicativo Streamlit falhou ao iniciar"

        finally:
            # Termina o processo para evitar que ele continue rodando em background
            process.terminate()
            process.wait()
