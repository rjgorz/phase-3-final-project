from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Content, Viewer, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///media_adaptations.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()