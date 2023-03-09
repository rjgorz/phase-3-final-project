###############################################################
###################### HELPER FUNCTIONS #######################
###############################################################

from db.models import Content, Viewer, Review

def display_all_content(contents):
    print('-' * 102)
    print(f'|{" " * 46}CONTENT{" " * 45}|')
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
    # print('-' * 166)

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






# def search_content_by_name():
#     search = input("Enter a name or ID to search for: ")
#     if search.isnumeric():
#         search_by_id = True
#         search = int(search)
#     else:
#         search_by_id = False
#     display_all_content(search, search_by_id)
