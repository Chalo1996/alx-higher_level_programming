#!/usr/bin/python3
"""that prints all City objects from the database hbtn_0e_14_usa
"""


from sys import argv

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1],
            argv[2],
            argv[3]
        )
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cityObjs = session.query(
        City,
        State).filter(
        City.state_id == State.id).order_by(
            City.id).all()

    for city, state in cityObjs:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
