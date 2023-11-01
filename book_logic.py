# from main import book_status

class Book:
    def __init__(self, book_status):
        self.books = book_status
        self.pages = 0
        self.current_page = 0

    def book_selection(self):
        print('Please select a book below:')
        for book in self.books:
            if book['status'] == 'inactive':
                print(book['name'])
        user_selection = input()
        self.active_books(user_selection)
        return user_selection

    def active_books(self, selected_book):
        for book in self.books:
            if selected_book == book['name']:
                book['status'] = 'active'

    def next_page(self, selected_book):
        for book in self.books:
            if book['name'] == selected_book:
                self.pages = book['pages']
        for _ in range(self.pages):
            
            while True:
                print(f'Page: {self.current_page + 1}')
                user_selection = input('1. Next Page\n2. Close Book\n')
                if user_selection == '1':
                    self.current_page += 1
                elif user_selection == '2':
                    print(f'Closed book on page: {self.current_page + 1}')
                    return False
                else:
                    print('Invalid Choice')