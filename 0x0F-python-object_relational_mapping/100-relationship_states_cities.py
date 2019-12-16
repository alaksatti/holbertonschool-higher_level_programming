#!/usr/bin/python3
'''
links cities class to database
'''
 

if __name__ == "__main__":
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    sf_city = City(name='San Francisco')
    state = State(name='California', cities=[sf_city])
    session.add(sf_city)
    session.add(state)
    session.commit()
    session.close()
