from sqlmodel import SQLModel, Session , create_engine

DATABASE_URL = "sqlite:///rangmanch.db" # use rangmanch.db file from current directory 

engine = create_engine(DATABASE_URL,echo=True) 

def create_table():
    """Create all tables defined by SQLModel Class"""
    SQLModel.metadata.create_all(engine) # create all table define in metadata in database if they don't exist


def get_session():
    with Session(engine) as session:
        yield session