import  csv

class Library:
    def __init__(self):
        self.users = [
    {
        "name": "Alice",
        "borrowed_books": [],
        "ratings": {
            "Harry Potter": 5,
            "The Hobbit": 4
        }
    },
    {
        "name": "Bob",
        "borrowed_books": [],
        "ratings": {
            "Harry Potter": 4,
            "Game of Thrones": 5
        }
    },
    {
        "name": "Charlie",
        "borrowed_books": [],
        "ratings": {
            "The Hobbit": 5,
            "Game of Thrones": 3
        }
    }
]
        
        self.books = [
            PhysicalBook("Harry Potter", "J.K. Rowling", "Fantasy", 3, "Shelf A3"),
            PhysicalBook("The Hobbit", "J.R.R. Tolkien", "Fantasy", 2, "Shelf B1"),
            PhysicalBook("Game of Thrones", "George R.R. Martin", "Fantasy", 1, "Shelf C2")
]


        self.books += [
            eBook("1984", "George Orwell", "Dystopian", 5, 2.0, "PDF"),
            eBook("Brave New World", "Aldous Huxley", "Dystopian", 3, 1.5, "EPUB")
        ]
    
    def add_user(self):
        new_user=User(name=input('Enter the name: '))
        self.users.append(new_user)
    
    def add_book(self):
        type_of_book=input('Is the book physcial or ebook?').strip().lower()
        if type_of_book=='physcial':
            new_book=PhysicalBook(name=input('Enter these:  title, author, genre, copies,shelf_location.'))
        elif type_of_book=='ebook':
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
            
    def recommend_books(self,user):
        for other in self.users:
            similarity=len(user.__ratings&other.__ratings)/len(user.__ratings|other.__ratings)
            if similarity>=0.5:
                print(f'{other._ratings.keys()-self.__ratings.keys()} are recomended by {other.name}')
    
    def loading_lib_data(self):
        with open('books.csv','a',newline='') as f:
            writer=csv.DictWriter(f)
            for book in self.books:
                record=[]
                for value in book.__dict__.items():
                    record.append(value)
                writer.writerow(record)
        
        with open('user.csv','a',newline='') as f:
            writer=csv.DictWriter(f)
            for user in self.user:
                record=[]
                for value in user.__dict__.items():
                    record.append(value)
                writer.writerow(record)
        



class User:
    def __init__(self,name):
        self.name=name
        self.__borrowed_books=[]
        self.__ratings={}


    def borrow(self,lib,book):
        exist=lib.borrow_book(self,book)
        if exist:
            self.__borrowed_books.append(book)            

    def return_book(self,lib,book):
        exist=lib.return_book(self,book)
        if exist:
            self.__borrowed_books.remove(book)

    def rate_book(self):
        type_of_book=input('Is the book physcial or ebook?').strip().lower()

        if type_of_book=="ebook":
            rated_book=eBook(input('Enter these:  title, author, genre, copies,shelf_location.'))
        elif type_of_book=="physical":
            rated_book=PhysicalBook(input('Enter these:  title, author, genre, copies,shelf_location.'))
        else:
            print('There is no such kind of book.')


        while True:
            try:
                score=int(input('Enter the score: '))
                if 0<score<=10:
                    break
                else:
                    print('The score must be 0<score<=10.')

            except ValueError:
                print('The score must be an int')

        if rated_book in self.__ratings:
            update=input((f"{rated_book.title} is already rated. Do you want to update?")).strip().lower()
            if update=='yes':
                self.__ratings[rated_book]=score
        else:
            self.__ratings[rated_book]=score

    def loading_user_data(self):
        with open('borrowed_books.csv','a',newline='') as f:
            writer=csv.DictWriter(f)
            for borrowed_book in self.__borrowed_books:
                record=[]
                for value in borrowed_book.__dict__.items():
                    record.append(value)
                writer.writerow(record)
        
        with open('ratings.csv','a',newline='') as f:
            writer=csv.DictWriter(f)
            for key,value in self.__ratings.items():
                record=[]
                for value2 in key.__dict__.values():
                    record.append(value2)
                record.append(value)
                writer.writerow(record)
        

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


def main():
    while True:
        try:
            ask=int(input('1.Show the list of users\n2.Show the list of the book\n3.Add a book\n4.Add a user\n5Borrow a book\n6.Return a book\n7.Rate a book\n8.Save all the data'))
            

        match ask:
            case 
