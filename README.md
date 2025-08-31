# Projeto-TDD
Funcionamento do Desenvolvimento Orientado por Testes

# 📌 Projeto: API com FastAPI + MongoDB usando TDD

## 📖 Descrição
Este projeto implementa uma **API REST** utilizando **FastAPI** com banco de dados **MongoDB**, aplicando **TDD (Test Driven Development)** com **Pytest**.

---

## 📂 Estrutura do Projeto
```
project/
│── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── crud.py
│
│── tests/
│   ├── __init__.py
│   ├── test_unit.py
│   └── test_integration.py
│
│── requirements.txt
│── README.md
```

## 🚀 Executando a API
```bash
uvicorn app.main:app --reload
```

## 🧪 Rodando os Testes
```bash
pytest -v
```

## 📚 Tecnologias
- FastAPI
- MongoDB
- Pytest
- Pydantic
```
