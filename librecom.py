import  csv

class Library:
    instance_created_lib=True

    def __init__(self):
        self.users = []
        self.books = []
    
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
        for bookl in self.books:
            if book==bookl.title:
                user.borrowed_books.append(book)
                exist=True
                return exist

        if exist==False:
            print('There is no such registrated book.')
            return exist
        

    def return_book(self,user, book):
        for bookl in self.books:
            if book==bookl.title:
                user.borrowed_books.remove(book)
                exist=True

        if exist==False:
            print('There is no such borrowed book.')
            return exist
            
    def recommend_books(self,user):
        for other in self.users:
            similarity=len(user.__ratings&other.__ratings)/len(user.__ratings|other.__ratings)
            if similarity>=0.5:
                print(f'{other._ratings.keys()-self.__ratings.keys()} are recomended by {other.name}')
    
    def validation(self,user):
        while True:
            user=input('Enter the user`s name: ')
            for userl in self.users:
                if user==userl.title:
                    return True
            return False
                    
            



            



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
    instance_created_user=True

    def __init__(self,name):
        self.name=name
        self.__borrowed_books=[]
        self.__ratings={}


    def borrow(self,lib,book):
        exist=lib.borrow_book(self,book)
        if exist:
            self.__borrowed_books.append(book)            

    def return_book_user(self,lib,book):
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
    instance_created_lib=False
    instance_created_user=False


    while True:

        lib=Library()


        ask=input('1.Show the list of the books\n2.Show the list of the users\n3.Add a book\n4.Add a user\n5Borrow a book\n6.Return a book\n7.Rate a book\n8.Save all the data')
            

        match ask:
            case '1':
                print(lib.books)
            case '2':
                print(lib.users)
            case '3':
                lib.add_book()
            case '4':
                lib.add_user()
            case '5': 
                while True:
                    if lib.validation(user=input('Enter the user`s name: ')):
                        break                        
                user.borrow(lib,book=input('Enter the name of the book:'))

            case '6':

                if lib.validation():


                    user.return_book_user(lib,book=input('Enter the name of the book:'))

            case '7':

                 while True:
                    user=input('Enter the user`s name: ')
                    if lib.validation(user):
                        break

                
                    


                    



            
