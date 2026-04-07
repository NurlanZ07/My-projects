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
        while True:
            
            type_of_book=input('Is the book physical or ebook?').strip().lower()
            if type_of_book=='physical':
                data=input('Enter these:  title, author, genre, copies,shelf_location.').split(',')
                new_book=PhysicalBook(*data)
                break
            elif type_of_book=='ebook': 
                data=input('Enter these: title, author, genre, copies,file_size,format.').split(',')
                new_book=eBook(*data)
                break
            else:
                print('There is no such kind.')

        self.books.append(new_book)

    def recommend_books(self,user):
        for other in self.users:
            similarity=len(set(user._ratings.values())&set(other._ratings.values()))/len(set(user._ratings.values())|set(other._ratings.values()))
            if similarity>=0.5:
                print(f'{other._ratings.keys()-self._ratings.keys()} are recomended by {other.name}')
    
    def validating_user(self):
        while True:
            user=input('Enter the user`s name: ')
            for userl in self.users:
                if user==userl.name:
                    return userl
            print('There is no such user.')

    def validating_book(self):
        while True:
            book=input('Enter the book`s name: ')
            for bookl in self.books:
                if book==bookl.title:
                    return bookl
            print('There is no such book.')

    def loading_lib_data(self):
        with open('books.csv','a',newline='') as f:
            writer=csv.writer(f)
            for book in self.books:
                record=[]
                record = list(book.__dict__.values())
                writer.writerow(record)
        
        with open('user.csv','a',newline='') as f:
            writer=csv.writer(f)
            for user in self.users:
                record=[]
                record = list(user.__dict__.values())
                writer.writerow(record)
        

class User:
    instance_created_user=True

    def __init__(self,name):
        self.name=name
        self._borrowed_books=[]
        self._ratings={}


    def borrow(self,book):
        self._borrowed_books.append(book)            

    def return_book(self,book):
        try:
            self._borrowed_books.remove(book)
        except ValueError:
            print('Invalid')

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

        if rated_book in self._ratings:
            update=input((f"{rated_book.title} is already rated. Do you want to update?")).strip().lower()
            if update=='yes':
                self._ratings[rated_book]=score
        else:
            self._ratings[rated_book]=score

    def info(self):
        return f'{self.name} has {len(self._borrowed_books)} number of borrowed books and {len(self._ratings)} number of ratings\n'


    def loading_user_data(self):
        with open('borrowed_books.csv','a',newline='') as f:
            writer=csv.writer(f)
            for borrowed_book in self._borrowed_books:
                record=[]
                for value in borrowed_book.__dict__.items():
                    record.append(value)
                writer.writerow(record)
        
        with open('ratings.csv','a',newline='') as f:
            writer=csv.writer(f)
            for key,value in self._ratings.items():
                record=[]
                record.append(self.name)
                for value2 in key.__dict__.values():
                    
                    record.append(value2)
                record.append(value)
                writer.writerow(record)


    
        

class Book:
    instance_created_book=True

    def __init__(self,title,author,genre,copies):
        self.title=title
        self.author= author
        self.genre=genre
        self.copies=copies

    def info(self):
        return f'{self.title} by {self.author} is a {self.genre} book with {self.copies} number of copies.\n'

class eBook(Book):


    def __init__(self, title, author, genre, copies,file_size,formatt):
        super().__init__(title, author, genre, copies)
        self.file_size=file_size
        self.formatt=formatt

    def info(self):
        base=super().info()
        return base + f'\nFile size of the ebook:{self.file_size}, format:{self.formatt}.'

class PhysicalBook(Book):
    def __init__(self, title, author, genre, copies,shelf_location):
        super().__init__(title, author, genre, copies)
        self.shelf_location=shelf_location

    def info(self):
        base=super().info()
        return base + f'\nFile shelf location: {self.shelf_location}.'



def main():

    lib = Library()


    lib.users = [
    User("Ali"),
    User("Nurlan"),
    User("Leyla"),
    User("Murad"),
    User("Aysel")
]

     
    lib.books = [
    PhysicalBook("1984", "George Orwell", "Dystopia", "5", "A1"),
    PhysicalBook("Clean Code", "Robert Martin", "Programming", "3", "B2"),
    eBook("Deep Learning", "Ian Goodfellow", "AI", "10", "5MB", "PDF"),
    eBook("Python Crash Course", "Eric Matthes", "Programming", "7", "3MB", "EPUB"),
    PhysicalBook("The Hobbit", "J.R.R. Tolkien", "Fantasy", "4", "C3")
]
    while True:


        choice=input('1.Show the list of the books\n2.Show the list of the users\n3.Add a book\n4.Add a user\n5.Borrow a book\n6.Return a book\n7.Rate a book\n8.See the recommendations.\n9.Save all the data\nWhich one do you choose? ')
            
        match choice:
            case '1':
                for book in lib.books:
                    print(book.info())
            case '2':
                for user in lib.users:
                    print(user.info())
            case '3':
                lib.add_book()
            case '4':
                lib.add_user()
            case '5': 
                user=lib.validating_user()
                book=lib.validating_book()
                user.borrow(book)

            case '6':
                user=lib.validating_user()
                book=lib.validating_book()
                user.return_book(book)

            case '7':
                user=lib.validating_user()
                rated_book=lib.validating_book()
                user.rate_book(lib,rated_book)
            case '8':
                user=lib.validating_user()
                lib.recommend_books(user)
            case '9':   
                lib.loading_lib_data()
                if lib.users:
                    for user in lib.users:
                        user.loading_user_data()
                else:
                    print('You haven`t created any user yet. ')

            case _:
                print('Invalid choice ')


if __name__=='__main__':
    main()

                
                    


                    



            
