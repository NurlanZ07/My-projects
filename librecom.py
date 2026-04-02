class Library:
    def __init__(self):
        self.users=[]
        self.books=[]
    
    def add_user(self):
        new_user=User(name=input('Enter the name: '))
        self.users.append(new_user)
    
    def add_book(self):
        type_of_book=input('Is the book physcial or electronic?').strip().lower()
        if type_of_book=='physcial':
            new_book=PhysicalBook(name=input('Enter these:  title, author, genre, copies,shelf_location.'))
        elif type_of_book=='electronic':
            new_book=eBook('Enter these: title, author, genre, copies,file_size,format.')
        self.books.append(new_book)
    def borrow_book(self,user, book):
        if book in self.books:
            user.borrowed_books.append(book)
            exist=True
        else:
            print('There is no such registrated book.')
            exist=False
        return exist

    def return_book(self,user, book):
        if book in self.borrowed_books:
            user.borrowed_books.remove(book)
            exist=True
        else:
            print('There is no such borrowed book.')
            exist=False
        return exist
            
    def recommend_books(user):
        pass

class User:
    def __init__(self,name):
        self.name=name
        self.borrowed_books=[]
        self.ratings={}

    def borrow(self,lib,book):
        exist=lib.borrow_book(self,book)
        if exist:
            self.borrowed_books.append(book)            

    def return_book(self,lib,book):
        exist=lib.return_book(self,book)
        if exist:
            self.borrowed_books.remove(book)

    def rate_book(self):
        type_of_book=input('Is the book physcial or electronic?').strip().lower()
        
        while True:
            try:
                score=int(input('Enter the score: '))
                if 0<score<=10:
                    break
                else:
                    print('The score must be 0<score<=10.')

            except ValueError:
                print('The score must be an int')

        self.ratings[book]=score
        

class Book:
    def __init__(self,title,author,genre,copies):
        self.title=title
        self.author= author
        self.genre=genre
        self.copies=copies

    def info(self,title):
        return f'{self.title} by {self.author} is a {self.genre} book with {self.copies} number of copies.'

class eBook(Book):
    def __init__(self, title, author, genre, copies,file_size,format):
        super().__init__(title, author, genre, copies)
        self.file_size=file_size
        self.format=format

    def info(self):
        base=super().info()
        return base + f'\nFile size of the ebook:{self.file_size}, format:{self.format}.'

class PhysicalBook(Book):
    def __init__(self, title, author, genre, copies,shelf_location):
        super().__init__(title, author, genre, copies)
        self.shelf_location=shelf_location

    def info(self):
        base=super().info()
        return base + f'\nFile shelf location: {self.shelf_location}.'

    
        