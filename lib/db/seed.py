from faker import Faker
import random
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Content, Viewer, Review

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///media_adaptations.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    fake = Faker()

    # session.query(Content).delete()
    # session.query(Viewer).delete()
    # session.query(Review).delete()

    genres = ['action', 'romance', 'thriller', 'horror',
            'adventure', 'comedy', 'drama']
    
    media_types = ['book', 'game', 'movie', 'comic',
                   'manga', 'anime', 'series']

    contents = []
    for i in range(50):
        content = Content(
            orig_title=fake.unique.name(),
            orig_type=random.choice(media_types),
            orig_release=datetime.now(),
            adapt_title=fake.unique.word(),
            adapt_type=random.choice(media_types),
            adapt_release=datetime.now(),
            genre=random.choice(genres)
        )

        session.add(content)
        session.commit()

        contents.append(content)

    viewers = []
    for i in range(10):
        viewer = Viewer(
            name=fake.unique.name()
        )

        session.add(viewer)
        session.commit()

        viewers.append(viewer)

    reviews = []
    for content in contents:
        for i in range(random.randint(1, 3)):
            review = Review(
                viewer_id=random.randint(1, 10),
                content_id=random.randint(1, 50),
                orig_rating=random.randint(1,10),
                adapt_rating=random.randint(1,10)
            )
            reviews.append(review)

    session.add_all(reviews)
    session.commit()