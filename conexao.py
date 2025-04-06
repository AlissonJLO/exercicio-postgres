import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

class Conexao :

    def __init__(self) :
        self.con = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
    
    def __enter__(self) :
        return self.con

    def __exit__(self, exc_type, exc_val, exc_tb) :
        self.con.close()