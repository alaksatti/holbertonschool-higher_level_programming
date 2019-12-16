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

    session = sessionmaker(bind=engine)()
    cities = City(name='San Francisco')
    session.add(State(name='California', cities=[cities]))
    session.add(cities)
    session.commit()
    session.close()
