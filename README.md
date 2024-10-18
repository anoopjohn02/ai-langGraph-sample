# AI Assistant using LangChain and OpenAI #

This is an AI-driven chatbot that answers the queries for the user's questions. The chatbot will answer the questions from different data sources such as:
* Documents uploaded (RAG architecture)
* Data from specific tables in database. For example
  * Questions about the user devices. Check device table. Use postman to insert data.
  * Questions about the token usages. Provide approx value os token usages and costs

Once you have run the application go to [http://localhost:8080/ui](http://localhost:8080/ui) to see the chatbot

### Libraries used: ###

* LangChain - Language processing
  * Chains, LangGraph - State, Graph, edges
* OpenAI - LLM
* FastApi - APIs
* SQLAlchemy - ORM
* Alembic - DB Migration
* pypdf - PDF Processing
* ChromaDB - Vector Database
* jinja - UI / Template
* PyJWT - OAuth2 and Token validation and extraction


### Set ENV variable ###

* Clone the repository
* Create .env file at root and add the following

| name                   | value                                                          | 
|------------------------|----------------------------------------------------------------|
| DB_CONNECTION_URL      | postgresql+psycopg2://postgres:postgres@localhost:5432/test_db | 
| DB_SCHEMA              | ai_assistant                                                   | 
| KEYCLOAK_AUTH_URL      |                                                                | 
| OPENAI_API_KEY         |                                                                | 
| OPEN_AI_MODEL          | gpt-3.5-turbo                                                  | 
| CHROMA_COLLECTION      | ai_collection                                                  | 
| EUREKA_URL             | <Disabled for time being>                                      | 

## How do I set up locally? ##

### Prerequisite ###

Following should be installed in machine

* Python 3.11
* Docker if required

Run following command to make sure python installed and configured

    python --version

### Run application ###
Install [PIP](https://pip.pypa.io/en/stable/installation/)

Run
    
    pip install pipenv

Run command to install dependencies

    pipenv install

Run command to load ENV variables to virtual env

    pipenv shell

## Migration ##

[Alembic](https://alembic.sqlalchemy.org/en/latest/) is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.

Install alembic to create scripts

    pip install alembic

Run command to execute all migration scripts

    alembic upgrade head

To revert last migration

    alembic downgrade -1

For creating a revision

    alembic revision -m "A migration "

For reference: [Example](https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a)
