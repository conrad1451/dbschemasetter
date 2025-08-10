# migration.py
import os
from sqlalchemy import create_engine

# Import the database file which contains the Base and all models
from database import Base

# Get the connection string from an environment variable or use a default
conn_string = os.getenv('AVIEN_DB_CONNECTION', 'sqlite:///mydatabase.db')
engine = create_engine(conn_string)

print("Creating database tables...")
Base.metadata.create_all(engine)
print("Tables created successfully!")