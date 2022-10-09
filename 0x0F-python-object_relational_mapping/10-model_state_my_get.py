#!/usr/bin/python3
"""prints the State object with the name\
    passed as argument from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    arg = argv[4]

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

    state_name = session.query(State).filter_by(name=arg).first()

    if state_name is not None:
        print(state_name.id)
    else:
        print("Not found")

    session.close()
