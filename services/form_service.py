import streamlit as st


class FormService:
    def render_form(self):
        st.title("Formulário de Coleta de Dados")
        num_funcionarios = st.selectbox(
            "Quantidade de funcionários:", ["0 - 5", "6 - 15", "16 ou mais"]
        )
        faturamento = st.selectbox(
            "Faturamento mensal (R$):",
            ["0", "2500 - 5000", "5001 - 15000", "15001 ou mais"],
        )
        segmento = st.selectbox(
            "Segmento:",
            ["Comércio", "Indústria", "Saúde", "Tecnologia", "Educação", "Outros"],
        )

        if st.button("Enviar"):
            form_data = {
                "num_funcionarios": num_funcionarios,
                "faturamento": faturamento,
                "segmento": segmento,
            }
            return form_data
        return None
