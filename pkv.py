def main():
    while True:
        notes=load_file()
        print('1. Add new note: ')
        print('2. View all notes: ')
        print('3. View full note by ID: ')
        print('4. Search notes: ')
        print('5. Delete note: ')
        print('6. Edit note: ')
        print('7. Show tag statistics: ')
        print('8. Save to file: ')
        print('9. Exit: ')


        while True:
            try:
                choice=int(input('Enter your choice: '))
                break
            except ValueError:
                print('Choice must be an integer.')


        if choice==1:
            add(notes)
        elif choice==2:
            view_all(notes)                                           
        elif choice==3:
            view_by_id(notes)
        elif choice==4:
            search(notes)
        elif choice==5:
            delete(notes)
        elif choice==6:
            edit(notes)
        elif choice==7:
            show_stats(notes)
        elif choice==8:
            save(notes)
        elif choice==9:
            exits()
        else:
            print('There is no such choice.')

def load_file():
    return {}

def add(notes):
    title=input('Enter the title: ')
    content=input('Enter the content: ')
    tags = set(input("Enter the tags (comma separated): ").strip().lower().split(','))
    date=input('Enter the date: ')
    while True:
        if 
        
    difficulty=input('Entet the difficulty(between 1-5): ')
    note=(title,content,tags,date,difficulty)
    while True:
        try:
            notes[ID]=note
            break
        except UnboundLocalError:
            ID=0
    ID=+1

def view_all(notes):
    for note in notes:
        print(note)


def view_by_id(notes):
    while True:
        try:
            ask=int(input('Enter the ID: '))
            print(notes[ask])
            break
        except ValueError:
            print('ID must be an integer.')


def search(notes):
    while True:
        try:
            ask=int(input('By which parameter do you want to search? \n 1.Tags \n 2.Diffulty \n 3. A word in title'))
            if ask==1:
                search_word=input('Enter the tag(s): ')
                for i in range(len(notes)):
                    if search_word in notes.get(i,0)[2]:
                        print(notes[i])
            elif ask==2:
                search_word=input('Enter the difficulty: ')
                for i in range(len(notes)):
                    if search_word in notes.get(i,0)[4]:
                        print(notes[i])
            elif ask==1:
                search_word=input('Enter the tag(s): ')
                for i in range(len(notes)):
                    if search_word in notes.get(i,0)[0]:
                        print(notes[i])
            break            
        except ValueError:
            print('Parameter shoulw be determined by its number.')    

def delete(notes):
    while True:
        try:
            ask=int(input('Enter the ID: '))
            del notes[ask]
            break
        except ValueError:
            print('The ID must be an integer.')


def edit(notes):
     while True:
        try:
            ask=int(input('Enter the ID: '))
            title=input('Enter the new title: ')
            if not title:
                title=notes[ask][0]
            content=input('Enter the new content: ')
            if not content:
                content=notes[ask][1]
            tags=input('Enter the new tags: ')
            if not tags:
                tags=notes[ask][2]
            difficulty=input('Enter the new difficulty: ')
            if not difficulty:
                difficulty=notes[ask][4]
            notes[ask]=(title,content,tags,notes[ask][3],difficulty)   
            
        except ValueError:
            print('The ID must be an integer.')

def show_stats(notes):
    counts=dict()
    tags_order=set()
    for i in range(len(notes)):
        for tag in notes[i][2]:
            if tag in counts:
                counts[tag]=counts.get(tag,0)+1
            else:
               tags_order.add(tag)
               counts[tag]=0
    
    for tag in tags_order:
        print(f'{tag} is used in {counts.get(tag)} notes.')

def save(notes):
    with open('pkv.txt', 'w') as file:
        file.write(notes)

def exits():
    return        







main()

    
