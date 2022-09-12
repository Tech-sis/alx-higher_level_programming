#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine

if __name__ == "__main__":
    """Create engine and link to database
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]))
    """Create all tables in the engine"""
    Base.metadata.create_all(engine)
