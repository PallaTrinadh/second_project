from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

Database_url = "mysql+pymysql://root:root@localhost:3306/mydatabase"
engine=create_engine(Database_url)

SessionLocal = sessionmaker(autoflush=False,autocommit=False, bind=engine)

Base=declarative_base()





