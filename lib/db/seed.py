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

    session.query(Content).delete()
    session.query(Viewer).delete()
    session.query(Review).delete()
    session.commit()

    contents = []

    hp = Content(
        orig_title = "Harry Potter Series",
        orig_type = "Book",
        orig_release = 1998,
        adapt_title = "Harry Potter Series",
        adapt_type = "Movie",
        adapt_release = 2001,
        genre = "Fantasy"
    )
    contents.append(hp)
     
    mk = Content(
        orig_title = "Mortal Kombat",
        orig_type = "Game",
        orig_release = 1992,
        adapt_title = "Mortal Kombat",
        adapt_type = "Movie",
        adapt_release = 2021,
        genre= "Action"
     )
    contents.append(mk)

    tlou = Content(
        orig_title = "The Last of Us",
        orig_type = "Game",
        orig_release = 2013,
        adapt_title = "The Last of Us",
        adapt_type = "TV series",
        adapt_release = 2023,
        genre = "Adventure"
    )
    contents.append(tlou)
    
    gl = Content(
        orig_title = "All-American Comics no. 16",
        orig_type = "Comic",
        orig_release = 1940,
        adapt_title = "Green Lantern",
        adapt_type = "Movie",
        adapt_release = 2011,
        genre = "Action"
    )
    contents.append(gl)
    
    iw = Content(
        orig_title = "The Infinity War",
        orig_type = "Comic",
        orig_release = 1992,
        adapt_title = "Avengers: Infinity War",
        adapt_type = "Movie",
        adapt_release = 2018,
        genre = "Action"
    )
    contents.append(iw)

    fpp = Content(
        orig_title = "Flashpoint ",
        orig_type = "Comic",
        orig_release = 2011,
        adapt_title = "Justice League: The Flashpoint Paradox",
        adapt_type = "Movie",
        adapt_release = 2013,
        genre = "Action"
    )
    contents.append(fpp)

    dn = Content(
        orig_title = "Deathnote",
        orig_type = "Light Novel",
        orig_release = 2006,
        adapt_title = "Deathnote",
        adapt_type = "Anime",
        adapt_release = 2007,
        genre = "Mystery"
    )
    contents.append(dn)

    silsil = Content(
        orig_title = "Shrek!",
        orig_type = "Book",
        orig_release = 1990,
        adapt_title = "Shrek",
        adapt_type = "Movie",
        adapt_release = 2001,
        genre = "Action"
    )
    contents.append(silsil)
    
    lctr = Content(
        orig_title = "Tomb Raider",
        orig_type = "Book",
        orig_release = 1996,
        adapt_title = "Lara Croft: Tomb Raider",
        adapt_type = "Movie",
        adapt_release = 2001,
        genre = "Action"
    )
    contents.append(lctr)

    fi = Content(
        orig_title = "Flatiron School",
        orig_type = "School",
        orig_release = 2012,
        adapt_title = "Flatiron School: Flex",
        adapt_type = "Online Prog",
        adapt_release = 2021 ,
        genre = "Action"
    )

    got = Content(
        orig_title = "A Game of Thrones",
        orig_type = "Book",
        orig_release = 1996,
        adapt_title = "A Game of Thrones",
        adapt_type = "Tv Series",
        adapt_release = 2011 ,
        genre = "Action"
    )
    contents.append(fi)

    session.add_all(contents)
    session.commit()

    # Harry Potter
    # Mortal Kombat
    # The Last of Us
    # Game of Thrones
    # Green Lantern 
    # Infinity Wars 
    # Flashpoint paradox
    # Deathnote  
    # Shrek
    # Laura Croft's Tomb raider
    # Flatiron 

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
        viewer_ids = list(range(1, 10))
        for i in range(random.randint(3, 5)):
            review = Review(
                viewer_id=random.choice(viewer_ids),
                content_id=content.id,
                orig_rating=random.randint(1, 10),
                adapt_rating=random.randint(1, 10)
            )
            viewer_ids.remove(review.viewer_id)
            reviews.append(review)
            session.add(review)
            session.commit()
    session.close()