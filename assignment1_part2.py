class Book:
    def __init__(self, author, title):
        '''Constructor of the Book class'''
        self.author = author
        self.title = title
    #@classmethod
    def display(Book):
        '''Prints the book title and author'''
        print(f"{Book.title}, written by {Book.author}")
        
if __name__ == "__main__":
    Book_1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
    Book_2 = Book("Walter Scott", "Ivanhoe: A Romance")

    Book_1.display()
    Book_2.display()
