class Book:
    author = ''
    title = ''
    def __init__(self, author, title):
        self.author = author
        self.title = title
    #@classmethod
    def display(Book):
        print(f"{Book.title}, written by {Book.author}")
        
Book_1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
Book_2 = Book("Walter Scott", "Ivanhoe: A Romance")

Book_1.display()
Book_2.display()
