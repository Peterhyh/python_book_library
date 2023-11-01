class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        self.current_page = 0
    
    def next_page(self):
        if self.current_page < self.pages:
            self.current_page += 1
        else:
            print('No More Pages')

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
        else:
            print('No More Pages')
        