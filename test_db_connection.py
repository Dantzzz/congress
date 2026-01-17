import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

"""
To manage database connection. 
"""

# read creds
load_dotenv()
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

# conn string and engine
conn = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(conn)

# context manager
with engine.connect() as conn:
    result = conn.execute(text("SELECT version();"))
    version = result.fetchone()
    print("Connection successful!")
    print(version)