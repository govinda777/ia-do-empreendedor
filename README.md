# IA do Empreendedor

**IA do Empreendedor** é uma aplicação que oferece insights personalizados para empreendedores, ajudando a avaliar a maturidade de suas empresas, gerar análises competitivas (gráfico Blue Ocean) e relatórios de SEO. A aplicação foi desenvolvida com uma arquitetura modular, separando a interface gráfica da lógica de negócio para garantir escalabilidade e fácil manutenção.

## 🚀 Funcionalidades

1. **Preenchimento de Formulário**: O usuário preenche um formulário com informações do negócio, como número de funcionários, faturamento e segmento de mercado.
2. **Processamento da IA**: A aplicação processa os dados coletados para avaliar a maturidade da empresa, gerar o gráfico Blue Ocean e o mapa de maturidade.
3. **Relatório Personalizado**: O relatório gerado para o usuário inclui:
   - **Nível de Maturidade**: Avaliação da maturidade da empresa.
   - **Gráfico Blue Ocean**: Análise competitiva do mercado.
   - **Mapa da Empresa**: Visão geral da empresa.
   - **Relatório SEO**: Avaliação e recomendações de SEO.

## 📋 Pré-Requisitos

Para rodar este projeto, você precisa de:

- **Python 3.8** ou superior
- **Pip** para instalação de dependências

## 🛠 Instalação

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/seu-usuario/ia_do_empreendedor.git
   cd ia_do_empreendedor
   ```

2. **Instale as Dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Rode a Aplicação**
   ```bash
   streamlit run main.py
   ```

## 🏗 Estrutura do Projeto

```plaintext
ia_do_empreendedor/
├── main.py                   # Arquivo principal para rodar a aplicação
├── domain/                   # Camada de Domínio
│   ├── __init__.py
│   ├── business_logic.py     # Lógica de negócios central (maturidade, Blue Ocean, mapa)
│   └── report_logic.py       # Lógica de geração dos relatórios de SEO
├── application/              # Camada de Aplicação
│   ├── __init__.py
│   └── orchestrator.py       # Orquestrador que gerencia o fluxo entre domínio e interface
├── interface/                # Camada de Interface
│   ├── __init__.py
│   └── streamlit_ui.py       # Interface com Streamlit
├── static/
│   └── assets/               # Recursos estáticos como imagens e gráficos
└── templates/
    └── report_template.html  # Template HTML para os relatórios
```

### 📚 Descrição das Camadas

- **Camada de Domínio** (`domain/`): Contém a lógica de negócios, incluindo regras para avaliar a maturidade do negócio, criar o gráfico Blue Ocean e o mapa de maturidade.
  - `business_logic.py`: Define o processamento dos dados do negócio.
  - `report_logic.py`: Responsável pela geração dos relatórios, incluindo SEO.

- **Camada de Aplicação** (`application/`): Coordena o fluxo entre a interface e o domínio. Conecta os dados de entrada do usuário à lógica de negócios.
  - `orchestrator.py`: Orquestra o fluxo de dados entre o formulário do usuário e a camada de lógica de negócio.

- **Camada de Interface** (`interface/`): Gerencia a interação com o usuário, apresentando o formulário e exibindo os resultados dos relatórios.
  - `streamlit_ui.py`: Controla a interface gráfica com Streamlit, exibindo o formulário e os relatórios finais.

## 🔄 Fluxo de Execução

1. **Usuário Preenche o Formulário**: A interface exibe o formulário com os campos necessários para coleta de dados do negócio.
2. **Processamento de Dados**: A camada de aplicação (orquestrador) passa os dados para a lógica de negócios, que gera os gráficos e relatórios.
3. **Exibição do Relatório**: A interface exibe o relatório personalizado, incluindo o nível de maturidade, gráfico Blue Ocean, mapa de maturidade e o relatório de SEO.

## 📊 Resultados e Visualização

Após o processamento, os resultados são exibidos em formato de gráficos e relatórios:

- **Nível de Maturidade**: Análise textual da maturidade empresarial.
- **Gráfico Blue Ocean**: Um gráfico que demonstra a posição competitiva da empresa no mercado.
- **Mapa da Empresa**: Visão geral dos processos e estratégias da empresa.
- **Relatório SEO**: Avaliação detalhada da performance digital com recomendações para melhorias.

## 📄 Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um **Pull Request** ou **Issue** com sugestões, melhorias ou correções.
