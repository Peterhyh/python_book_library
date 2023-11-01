class Library:
    def __init__(self, book_list):
        self.book_list = book_list
        self.status = 'inactive'

    def make_active(self, title):
        for book in self.book_list:
            if title == book['title']:
                self.status = 'active'
    
    def make_inactive(self, title):
        for book in self.book_list:
            if title == book['title']:
                self.status = 'inactive'