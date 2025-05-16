# 📊 SuperStore Dashboard - Python + Streamlit + Docker

Este projeto demonstra a criação de um dashboard interativo para análise de dados de vendas com **Python**, **Streamlit**, **SQLite** e **Docker**. Ele foi construído com boas práticas de engenharia de dados, organização em pastas, uso de notebooks para tratamento dos dados e deploy com Docker.

---

## 🧰 Tecnologias Utilizadas

- **Python 3.9**
- **Streamlit** – para o dashboard web
- **Pandas** – para análise e tratamento de dados
- **SQLite** – banco de dados leve e local
- **Docker** e **Docker Compose** – para empacotamento e execução da aplicação

---

## 📁 Estrutura do Projeto

```
SUPERSTORE/
├── app/
│   └── dashboard.py           # Código principal do Streamlit
│
├── data/
│   ├── raw/
│   │   └── DadosBrutos.csv    # Dataset original
│   └── processed/
│       └── dados_tratados.csv # Dataset após limpeza
│
├── db/
│   └── superstore.db          # Banco de dados SQLite
│
├── notebooks/
│   └── tratamento.ipynb       # Notebook para tratamento e análise de dados
│
├── criar_banco.py             # Script para gerar o banco superstore.db
├── Dockerfile                 # Dockerfile para criar a imagem da aplicação
├── docker-compose.yml         # Compose para facilitar execução com Docker
├── requirements.txt           # Dependências Python
└── README.md                  # Este arquivo
```

---

## 🚀 Como Rodar com Docker

1. **Clone o repositório:**

```bash
git clone https://github.com/macauli10/Dashboard-python-docker.git
cd Dashboard-python-docker
```

2. **Crie o banco de dados (uma única vez):**

```bash
docker run --rm -v ${PWD}:/app -w /app python:3.9 python criar_banco.py
```

3. **Rode a aplicação com Docker Compose:**

```bash
docker-compose up --build
```

4. **Acesse o dashboard no navegador:**

```
http://localhost:8501
```

---

## 📝 Funcionalidades do Projeto

- Visualização de vendas por categoria, estado, data, entre outros
- Tratamento de dados e verificação de nulos/duplicados com Pandas
- Conversão do CSV limpo em banco SQLite com o `criar_banco.py`
- Aplicação leve, empacotada em container Docker para portabilidade

---

## 📚 Notebook de Tratamento

O notebook `notebooks/tratamento.ipynb` mostra:

- Leitura dos dados brutos
- Limpeza de valores nulos
- Remoção de duplicados
- Exportação para CSV limpo (`dados_tratados.csv`)

---

## 💡 Sugestões Futuras

- Adicionar autenticação ao dashboard
- Incluir filtros dinâmicos por data, região e categoria
- Exportar relatórios em PDF ou Excel

---

## 🧑‍💻 Autor

**Macauli Missouri**  
🔗 [www.linkedin.com/in/macauli-missouri-3ab2a6272]

---
