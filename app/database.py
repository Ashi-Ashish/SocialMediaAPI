from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# 'postgresql://<username>:<password>@<ip-adress/hostname?/<database_name>'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:@{settings.database_hostname}/{settings.database_name}?password={settings.database_password}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind= engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# For reference only to connect database
# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost',
#                                 database = 'fastapi', 
#                                 user = 'postgres',
#                                 password = 'Dell@123',
#                                 cursor_factory = RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successfull!")
#         break
#     except Exception as error:
#         print("Connection to database failed!")
#         print("Error: ", error)
#         time.sleep(2)