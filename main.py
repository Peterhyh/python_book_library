from book_class import Book
from data import book_data
from library_class import Library

num_loops = 0

book_list = []

for book in book_data:
    title = book['title']
    pages = book['pages']
    book_info = {'title': title, 'pages': pages, 'status': 'inactive'}
    book_list.append(book_info)

in_list = False

while True:
    if num_loops == 0:
        print('\nPlease select a book:')
        for book in book_list:
            print(book['title'])
        book_selection = input()
        for i in range(len(book_list)):
            if book_selection in book_list[i]['title']:
                in_list = True
        if in_list:
            for book in book_list:
                if book_selection in book['title']:
                    title = book['title']
                    pages = book['pages']

        book = Book(title, pages)
        library = Library(book_list)
        library.make_active(title)
    
    else:
        main_menu_selection = input('\n1. Select Another Book\n2. Resume Book\n3. Exit\n')
        if main_menu_selection == '1':
            library.make_inactive(title)
            print('\nPlease select a book:')
            for book in book_list:
                if book['status'] == 'inactive':
                    print(book['title'])
            book_selection = input()
            for book in book_list:
                if book_selection == book['title']:
                    title = book['title']
                    pages = book['pages']
            book = Book(title, pages)
            library = Library(book_list)
            library.make_active(title)
        elif main_menu_selection == '2':
            pass
        elif main_menu_selection == '3':
            exit()
        else:
            print('Invalid Selection')
    

    

    while True:
        print(f'\nSelected book: {book.title}\nPage: {book.current_page} of {book.pages}')
        user_selection = input('\n1. Next Page\n2. Previous Page\n3. Exit\n')

        if user_selection == '1':
            book.next_page()
        elif user_selection == '2':
            book.previous_page()
        elif user_selection == '3':
            num_loops += 1
            break
    


