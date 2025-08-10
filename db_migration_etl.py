# db_migration_etl.py 
import os
from sqlalchemy import create_engine

from schema_base import Base
from UserModel import User  # This import is necessary to register the User class.

# conn_string = "sqlite:///mydatabase.db"
AVIEN_DB_CONNECTION = os.getenv('AVIEN_DB_CONNECTION')

conn_string = AVIEN_DB_CONNECTION

engine = create_engine(conn_string)


Base.metadata.create_all(engine)