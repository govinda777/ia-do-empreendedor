import streamlit as st
from services.form_service import FormService
from services.data_processor import DataProcessor
from utils.report_generator import generate_html_report

def main():
    st.sidebar.title("IA do Empreendedor - Menu")
    option = st.sidebar.selectbox("Escolha uma opção", ["Preencher Formulário", "Ver Relatório"])

    form_service = FormService()

    if option == "Preencher Formulário":
        form_data = form_service.render_form()
        if form_data:
            st.success("Dados coletados com sucesso!")
            data_processor = DataProcessor(form_data)
            processed_data = data_processor.process()
            st.session_state['processed_data'] = processed_data

    elif option == "Ver Relatório":
        if 'processed_data' in st.session_state:
            report_html = generate_html_report(st.session_state['processed_data'])
            st.markdown(report_html, unsafe_allow_html=True)
        else:
            st.warning("Nenhum relatório gerado ainda. Preencha o formulário primeiro.")

if __name__ == "__main__":
    main()
