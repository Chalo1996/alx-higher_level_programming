#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1],
            argv[2],
            argv[3]
        )
    )

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    Session = session()

    for state in Session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    Session.close()
