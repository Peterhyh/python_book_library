from book_logic import Book
from data import book_list

book_status = []


for book in book_list:
    name = book['name']
    pages = book['pages']
    book_dict = {'name': name, 'status': 'inactive', 'pages': pages}
    book_status.append(book_dict)
    
book = Book(book_status)
selected_book = book.book_selection()

reading_session = True

while reading_session:
    book.next_page(selected_book)

    user_selection = input('1. Resume Reading\n2. Exit\n')
    if user_selection == '2':
        reading_session = False
    else:
        print('Invalid Choice')