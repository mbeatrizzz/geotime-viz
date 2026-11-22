from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import database_url

# Caminho do novo banco de dados para o frontend
FRONTEND_DATABASE_URL = database_url("frontend_data")

engine_frontend = create_engine(FRONTEND_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocalFrontend = sessionmaker(autocommit=False, autoflush=False, bind=engine_frontend)
BaseFrontend = declarative_base()
