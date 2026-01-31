import json
import sys

def main():
    notes=load_file(filename='notes.txt')
    for key in notes.keys():
         key=int(key)
    note_id=max(notes.keys(), default=-1)+1
    while True:
        print('1. Add new note: ')
        print('2. View all notes: ')
        print('3. View full note by id: ')
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
            add(note_id,notes)
            note_id+=1
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


def load_file(filename="notes.txt"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            for key in data:
                title, content, tags_list, date, difficulty = data[int(key)]
                data[int(key)] = (title, content, set(tags_list), date, difficulty)
            return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    except KeyError:
        return{}

def add(note_id,notes):
    while True:
        title=input('Enter the title: ')
        if not title:
            print('Title mustn`t be empty. ')
        else:
            break
    content=input('Enter the content: ')
    tags=set(input("Enter the tags (comma separated): ").strip().lower().split(','))
    date=input('Enter the date: ')
    while True:   
        try: 
            difficulty=int(input('Entet the difficulty(between 1-5): '))
            if 1<=difficulty<=5:
                    break
            else:
                print('Difficulty must be between 1-5.  ')
        except ValueError:
            print('Difficulty mustn`t be empty. ')

    note=(title,content,tags,date,difficulty)     
    notes[note_id]=note
           
def view_all(notes):
    for note_id,note in notes.items():
        print(note_id,note)

def view_by_id(notes):
    while True:
        try:
            ask=int(input('Enter the id: '))
            print(notes[ask])
            break
        except ValueError:
            print('id must be an integer.')

def search(notes):
    while True:
        try:
            ask=int(input('By which parameter do you want to search? \n 1.Tags \n 2.Diffulty \n 3. A word in title'))
            if ask==1:
                search_word=input('Enter the tag(s): ').strip().lower()
                for key in notes:
                    if search_word in notes.get(key,0)[2]:
                        print(notes[key])
                        
            elif ask==2:
                search_word=int(input('Enter the difficulty: '))
                for key in notes:
                    if search_word == notes.get(key,0)[4]:
                        print(notes[key])
        
            elif ask==3:
                search_word=input('Enter the word: ').strip()
                for key in notes:
                    if search_word in notes.get(key,0)[0]:
                        print(notes[key])
            break                    
        except ValueError:
            print('Parameter should be determined by its number.')    

def delete(notes):
    while True:
        try:
            ask=int(input('Enter the id: '))
            if ask in notes.keys():
                del notes[ask]
                break
            else:
                print('There is no such id. ')
        except ValueError:
            print('The id must be an integer.')

def edit(notes):
    while True:
        try:
            ask=int(input('Enter the id: '))
            title=input('Enter the new title: ')
            if not title:
                title=notes[ask][0]
            content=input('Enter the new content: ')
            if not content:
                content=notes[ask][1]
            tags=set(input('Enter the new tags: ')).strip().lower().split(',')
            if not tags:
                tags=notes[ask][2]
            difficulty=input('Enter the new difficulty: ')
            if not difficulty:
                difficulty=notes[ask][4]
            notes[ask]=(title,content,tags,notes[ask][3],difficulty)    
            break
            
        except ValueError:
            print('The id must be an integer.')

def show_stats(notes):
    counts=dict()
    for key in notes.keys():
        for tag in notes[key][2]:
            if tag in counts:
                counts[tag]=counts.get(tag,0)+1
            else:
               counts[tag]=1
    
    for tag,count in counts.items():
        print(f'{tag} is used in {count} notes.')
    print(sorted(counts.keys()))    

def save(notes, filename='notes.txt'):
    notes_to_save = {k: (v[0], v[1], list(v[2]), v[3], v[4]) for k, v in notes.items()}
    with open(filename, 'w') as file:
        json.dump(notes_to_save, file)


def exits():
    sys.exit()      

main()

    
