#!/usr/bin/python3
'''
lists first state object from the database hbtn_0e_6_usa
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
    lists = session.query(State).all()

    if state in lists:
        if 'a' in str(state):
            print("{}: {}".format(state.id, state.name))

    else:
        print("Nothing")

    session.close()
