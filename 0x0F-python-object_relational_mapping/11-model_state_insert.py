#!/usr/bin/python3
""" a module that prints the State object from the name
passed as argument from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    # unit of work
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    if (new_instance):
        print(new_instance.id)
    session.commit()
