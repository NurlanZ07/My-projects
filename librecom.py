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
            data=input('Enter these:  title, author, genre, copies,shelf_location.').split(',')
            new_book=PhysicalBook(*data)
        elif type_of_book=='ebook':
            data=input('Enter these: title, author, genre, copies,file_size,format.').split(',')
            new_book=eBook(*data)
        self.books.append(new_book)

    def recommend_books(self,user):
        for other in self.users:
            similarity=len(user.__ratings&other.__ratings)/len(user.__ratings|other.__ratings)
            if similarity>=0.5:
                print(f'{other._ratings.keys()-self.__ratings.keys()} are recomended by {other.name}')
    
    def validating_user(self,user,):
        while True:
            user=input('Enter the user`s name: ')
            for userl in self.users:
                if user==userl.title:
                    return user
                else:
                    print('There is no such user.')

    def validating_book(self,book):
        while True:
            book=input('Enter the book`s name: ')
            for bookl in self.books:
                if book==bookl.title:
                    return book
                else:
                    print('There is no such book.')

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
        self.__borrowed_books.append(book)            

    def return_book(self,lib,book):
        self.__borrowed_books.remove(book)

    def rate_book(self,lib,rated_book):
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

    def info(self):
        return f'{self.name} has {len(self.__borrowed_books)} number of books and {len(self.__ratings)} number of ratings'


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

    def info(self):
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

        choice=input('1.Show the list of the books\n2.Show the list of the users\n3.Add a book\n4.Add a user\n5.Borrow a book\n6.Return a book\n7.Rate a book\n8.Save all the data\nWhich one do you choose? ')
            
        match choice:
            case '1':
                for book in lib.books:
                    print(book.info())
            case '2':
                for user in lib.user:
                    print(user.info())
            case '3':
                lib.add_book()
            case '4':
                lib.add_user()
            case '5': 
                user=lib.validating_user()
                book=lib.validating_book()
                user.borrow(lib,book)

            case '6':
                user=lib.validating_user()
                book=lib.validating_book()
                user.return_book(lib,book)

            case '7':
                user=lib.validating_user()
                rated_book=lib.validating_book()
                user.rate_book(lib,rated_book)

            case '8':   
                lib.loading_lib_data()
                if instance_created_user:
                    user=lib.validating_user
                    user.loading_user_data()
                else:
                    print('You haven`t created any user yet. ')


if __name__=='__main__':
    main()

                
                    


                    



            
