import logging
from config.config import db_user, db_pass, db_host, db_name

class DatabaseConnection:
    def __init__(self):
        self.host = db_host
        self.user = db_user
        self.password = db_pass
        self.database = db_name
        self.connected = False
    
    def connect(self):
        # Fake database connection
        self.connected = True
        logging.info(f"Connected to database at {self.host} as {self.user}.")

    def execute_query(self, query: str):
        # This would normally execute SQL
        if not self.connected:
            logging.warning("Tried to execure query without connection.")
            return None
        
        # Pretending to execute the query
        logging.info(f"Executing query: {query}")
        return f"Results of {query}"