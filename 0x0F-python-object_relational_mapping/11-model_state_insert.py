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

    session.add(State(name='Louisiana'))
    state_name = session.query(State).filter_by(name='Louisiana').first()
    print(state_name.id)
    session.commit()
    session.close()
