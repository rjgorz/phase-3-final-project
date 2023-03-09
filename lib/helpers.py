###############################################################
###################### HELPER FUNCTIONS #######################
###############################################################
from sqlalchemy.orm import Session
from sqlalchemy import func
from db.models import Content, Viewer, Review

def display_all_content(contents):
    print('-' * 102)
    print(f'|{" " * 47}CONTENT{" " * 46}|')
    print('-' * 102)
    print('|ID  |Orig Title                  |Orig Type   |Adapt Title                             |Adapt Type  |')
    print('-' * 102)
    for content in contents:
        id_spaces = 4 - len(str(content.id))
        orig_title_spaces = 28 - len(content.orig_title)
        orig_type_spaces = 12 - len(content.orig_type)
        adapt_title_spaces = 40 - len(content.adapt_title)
        adapt_type_spaces = 12 - len(content.adapt_type)
        print(f'|{content.id}{" " * id_spaces}' + \
              f'|{content.orig_title}{" " * orig_title_spaces}' + \
              f'|{content.orig_type}{" " * orig_type_spaces}' + \
              f'|{content.adapt_title}{" " * adapt_title_spaces}' + \
              f'|{content.adapt_type}{" " * adapt_type_spaces}|')
    print('-' * 102)

def display_content_details(content):
    orig_title_spaces = 40 - len(content.orig_title)
    orig_type_spaces = 12 - len(content.orig_type)
    orig_release_spaces = 14 - len(str(content.orig_release))
    genre_spaces = 12 - len(content.genre)
    adapt_title_spaces = 40 - len(content.adapt_title)
    adapt_type_spaces = 12 - len(content.adapt_type)
    adapt_release_spaces = 14 - len(str(content.adapt_release))
    genre_spaces = 12 - len(content.genre)

    print('-' * 166)
    print(f'|{" " * 33}ORIGINAL CONTENT{" " * 32}||{" " * 32}ADAPTATION CONTENT{" " * 31}|')
    print('-' * 166)
    print('|Title                                   |Type        |Release Year  |Genre       |' * 2)
    print('-' * 166)

    print(f'|{content.orig_title}{" " * orig_title_spaces}' + \
          f'|{content.orig_type}{" " * orig_type_spaces}' + \
          f'|{content.orig_release}{" " * orig_release_spaces}' + \
          f'|{content.genre}{" " * genre_spaces}|' + \
          f'|{content.adapt_title}{" " * adapt_title_spaces}' + \
          f'|{content.adapt_type}{" " * adapt_type_spaces}' + \
          f'|{content.adapt_release}{" " * adapt_release_spaces}' + \
          f'|{content.genre}{" " * genre_spaces}|')
    print('-' * 166)

def display_all_viewers(viewers):
    print('-' * 28)
    print('|ID  |Name                 |')
    print('-' * 28)

    for viewer in viewers:
        id_spaces = 4 - len(str(viewer.id))
        name_spaces = 21 - len(viewer.name)
        print(f'|{viewer.id}{" " * id_spaces}' + \
              f'|{viewer.name}{" " * name_spaces}|')
        
    print('-' * 28)

def display_viewer_details(viewer):
    side_spaces = int((50 - len(viewer.name)) / 2)
    print('-' * 50)
    print(f'{" " * side_spaces}{viewer.name}{" " * side_spaces}')
    print('-' * 50)

    for review in viewer.reviews:
        print(f'|{review.id} |Review of "{review.content.orig_title}" vs "{review.content.adapt_title}"')

def get_all_reviews(content):
    if len(content.reviews) == 0:
        print('No reviews have been left for this content!')
    else:
        print('====== REVIEWS ======')
        for review in content.reviews:
            print(" ")
            print(f'{review.viewer.name}')
            print(f'{content.orig_type}: {review.orig_rating}/10')
            print(f'{content.adapt_type}: {review.adapt_rating}/10')
            print(" ")

def display_review_details(review):
    print(" ")
    print(f'"{review.content.orig_title}" vs "{review.content.adapt_title}"')
    print(f'{review.content.orig_type}: {review.orig_rating}/10')
    print(f'{review.content.adapt_type}: {review.adapt_rating}/10')
    if review.orig_rating > review.adapt_rating:
        print(f'{review.viewer.name} prefers the original!')
    else:
        print(f'{review.viewer.name} prefers the adaptation!')
    print(" ")

# This will be the helper function to get a sum of all reviews and display the prefferred type
def get_overall_preference(content, session) -> dict:


    orig_rating = session.query(func.avg(Review.orig_rating)).filter(Review.content_id == content.id).scalar() or 0
    adapt_rating = session.query(func.avg(Review.adapt_rating)).filter(Review.content_id == content.id).scalar() or 0
    if orig_rating > adapt_rating:
        result = 'Original rating is higher!'
    elif orig_rating < adapt_rating:
        result = 'Adaptation rating is higher!'
    else:
        result = 'Both ratings are equal!'

    print(result)
    return result

#testing
def get_pref(content):
    orig_sum = 0
    adapt_sum = 0

    if len(content.reviews) == 0:
        print('No reviews have been left for this content!')
    else:
        for review in content.reviews:
            orig_sum += review.orig_rating
            adapt_sum += review.adapt_rating
        orig_avg = orig_sum / len(content.reviews)
        adapt_avg = adapt_sum / len(content.reviews)
        
        print(f'Original Average Rating: {orig_avg}/10')
        print(f'Adapted Average Rating: {adapt_avg}/10')

        if orig_avg > adapt_avg:
            print(f'{review.content.orig_title} ({review.content.orig_type}) is preferred by viewers!')
        else:
            print(f'{review.content.adapt_title} ({review.content.adapt_type}) is preferred by viewers!')
