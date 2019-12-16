#!/usr/bin/python3
'''
Change the name of the state whose id is 2
'''

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)()
    states = session.query(State).filter(State.id == 2)

    for state in states:
        state.name = 'New Mexico'
    session.commit()
    session.close()
