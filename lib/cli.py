from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Content, Viewer, Review
from helpers import (display_all_content, display_all_viewers, display_content_details, display_viewer_details)

engine = create_engine('sqlite:///db/media_adaptations.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    cont = True

    while cont:
        print('Browse by:')
        print('(1) Content')
        print('(2) Viewers')
        display_choice = input('= ')

        if display_choice == '1':
            display_all_content(session.query(Content).all())
            choice = input('Select the content by ID for details: ')
            display_content_details(session.query(Content).filter(Content.id == choice).first())
        elif display_choice == '2':
            display_all_viewers(session.query(Viewer).all())
            choice = input('Select the viewer by ID for details: ')
            display_viewer_details(session.query(Viewer).filter(Viewer.id == choice).first())
    
        another = input('Continue browsing? (y/n): ')

        while another != 'y' or another != 'n':
            if another == 'y':
                print(" ")
                break
            elif another == 'n':
                cont = False
                break
            else:
                another = input('Please enter y or n: ')

        