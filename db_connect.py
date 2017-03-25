from models import *


def connect_to_database():
    """Connects to the database and returns an sqlalchemy session object."""
    engine = create_engine('sqlite:///catalog.db')
    Base = declarative_base()
    Base.metadata.bind = engine
    db_session = sessionmaker(bind=engine)
    session = db_session()
    return session
