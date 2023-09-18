#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).first()

    if instance is None:
        print("Nothing")
    else:
        print(f"{instance.id}: {instance.name}")

    session.close()
