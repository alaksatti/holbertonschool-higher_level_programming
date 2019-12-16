#!/usr/bin/python3
'''
Adds Louisiana as aa state obj
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
    session.add(State(name='Louisiana'))
    Louisiana = session.query(State).filter(State.name == 'Louisiana')[0]
    session.commit()
    print(Louisiana.id)
    session.close()
