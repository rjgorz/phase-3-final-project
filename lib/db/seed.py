from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

faker = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///media_adaptations.db')
    Session = sessionmaker(bind=engine)
    session = Session()