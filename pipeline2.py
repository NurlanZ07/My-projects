import math
import datetime as dt
import json
import re   
import random
import sys
from faker import Faker
fake=Faker()

def missing_values():
    

def show_summary():
    print(f'The number of records: {len(dataset)}')
    for line in dataset:
        if name=='invalid name' or age=='invalid age' or email=='invalid email' or not 0<=score<=1 or country=='invalid country' or time='invalid time':



def load_json():
    dataset_file=input()
    with open(dataset_file) as file:
        dataset=json.load(file)
    return dataset


def generate_syn_dataset(dataset,id):
    id=1
    for _ in range(100):
        if random.random()<0.03:
            name='invalid name'
        else:
            name=fake.name()    
        if random.ranmdon()<0.05:
            age='invalid age'
        else:
            age=random.randint(1,100):
        if random.random()<0.1:
            email='invalid email'
        else:
            email=fake.email()
        if random.random()<0.08:
             score=round(random.random(-0.5,1.5))
        else:
            score=round(random.random())
        if random.random<0.05:
            country='invalid country'
        else:
            country=fake.country()
        if random.random()<0.05:
            time='invalid time'
        else:
            time=dt.datetime.now().date()
        record={
            'id':id,
            'name':name,
            'age':age,
            'email':email,
            'score':score,
            'country':country,
            'time':time,
        }
        dataset.append(record)
        id+=1
    return dataset


def main():
    dataset=[]
    while True:
        choice=int(input('AI DATA PIPELINE TOOL\n1 Generate synthetic dataset\n2 Load dataset from JSON\n3 Show dataset summary\n4 Validate dataset\n5 Clean dataset\n6 Detect anomalies\n7 Generate statistics\n8 Train/Test split\n9 Export cleaned dataset\n10 Exit\n\n Enter your choice: '))
        
        match choice:
            
            case 1:
                dataset=generate_syn_dataset()

            case 2:
                dataset=load_json()

            case 3:
                show_summary():

            case 4:

            case 5:

            case 6:

            case 7:

            case 8:

            case 9:

            case 10:

            case _:
                print('There is no such choice.')


