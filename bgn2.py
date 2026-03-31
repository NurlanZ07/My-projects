import csv
import statistics as st

class Student:
    def __init__(self,file):
        with open(file,newline='',encoding='utf-8') as f:
            self.file=list(csv.DictReader(f))
            
    
    def stats(self):
        print(self.file)
        scores=[]
        passing_students=[]
        for row in self.file:
            scores.append(int(row['score']))
            if int(row['score'])>=70:
                passing_students.append(row)
        print(f'The avg score is {st.mean(scores)}.')
        print(f'The highest score of {max(scores)} achieved by {self.file[((scores.index(max(scores))))]['name']}')
        print(f'The lowest score of {min(scores)} achieved by {self.file[((scores.index(min(scores))))]['name']}')
        return passing_students

    def adding_new_st(self,file):
        record=input('Enter the info: ').strip().split(',')
        with open(file,'a') as f:
            writer=csv.writer(f)
            writer.writerow([record[0],record[1]])

    
def main():
    file='students.csv'
    student = Student(file)
    while True:
        user_choice=input('1.Stats\n2.List of passing students\n3.Adding a new student\nWhat do you wanna do?\n')
        match user_choice:
            case '1':
                passing_students=student.stats()
            case '2':
                for row in passing_students:
                    print(f'{row['name']} passed with the score of {row['score']}')
            case '3':
                student.adding_new_st(file)

if __name__=='__main__':
    main()
    



        

