from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Content, Viewer, Review
from helpers import (display_all_content, display_all_viewers, display_content_details, display_viewer_details,
                     get_all_reviews, display_review_details, get_overall_preference)

engine = create_engine('sqlite:///db/media_adaptations.db')
session = sessionmaker(bind=engine)()

if __name__ == '__main__':
    print('******************************************************************************************************************')
    print(' __  __ ______ _____ _____                       _____          _____ _______    _______ _____ ____  _   _  _____ ')
    print('|  \/  |  ____|  __ \_   _|   /\           /\   |  __ \   /\   |  __ \__   __|/\|__   __|_   _/ __ \| \ | |/ ____|')
    print('| \  / | |__  | |  | || |    /  \         /  \  | |  | | /  \  | |__) | | |  /  \  | |    | || |  | |  \| | (___  ')
    print('| |\/| |  __| | |  | || |   / /\ \       / /\ \ | |  | |/ /\ \ |  ___/  | | / /\ \ | |    | || |  | | . ` |\___ \ ')
    print('| |  | | |____| |__| || |_ / ____ \     / ____ \| |__| / ____ \| |      | |/ ____ \| |   _| || |__| | |\  |____) |')
    print('|_|  |_|______|_____/_____/_/    \_\   /_/    \_\_____/_/    \_\_|      |_/_/    \_\_|  |_____\____/|_| \_|_____/ ')
    print('                                                                                                                  ')
    print('******************************************************************************************************************')
    
    cont = True
    while cont:
        print('Welcome! Choose to browse by:')
        print('(1) Content')
        print('(2) Viewers')
        display_choice = input('=> ')
        print(" ")

        if display_choice == '1':
            display_all_content(session.query(Content).all())
            id_choice = input('Select the content by ID for details: ')
            print(" ")
            content_choice = session.query(Content).filter(Content.id == id_choice).first()
            display_content_details(content_choice)

            print('Choose an action:')
            print('(1) See all reviews')
            print('(2) Get overall preference')
            choice = input('=> ')
            print(" ")

            if choice == '1':
                get_all_reviews(content_choice)
            elif choice == '2':
                get_overall_preference(content_choice, session)

        elif display_choice == '2':
            display_all_viewers(session.query(Viewer).all())
            choice = input('Select the viewer by ID for details: ')
            print(" ")
            viewer_choice = session.query(Viewer).filter(Viewer.id == choice).first()
            display_viewer_details(viewer_choice)

            if len(viewer_choice.reviews) != 0:
                review_choice = input('Select a review by ID for details: ')
                print(" ")
                display_review_details(session.query(Review).filter(Review.id == review_choice).first())
    
        print(" ")
        another = input('Continue browsing? (y/n): ')
        while another != 'y' or another != 'n':
            if another == 'y':
                print(" ")
                break
            elif another == 'n':
                cont = False
                print('Thanks for browsing!')
                break
            else:
                another = input('Please enter y or n: ')

        