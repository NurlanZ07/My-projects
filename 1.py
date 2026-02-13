import random
import sys

def main():
    while True:
        play_game()


def play_game():
    print('''Choose difficulty:
        1 - Easy (10 attempts)
        2 - Medium (7 attempts)
        3 - Hard (5 attempts)''')
     
    while True: 
      try:
           choice=int(input('Enter your choice:'))
           if choice in [1,2,3]:
               break
           else:
               print('There is such choice.Please try again.')
      except ValueError:
          print('Your choice must be an int.')
    if choice==1:
        attempts=10
    elif choice==2:
        attempts=7
    else:
        attempts=5
        
      
    secret=generate_number()
    get_user_guess(attempts, secret)  

    replay=input('Do you want to replay?').lower()
    if replay=='yes':
        play_game()
    else:
        sys.exit()


def generate_number():
    return random.randint(1,100)
    

def get_user_guess(attempts,secret):
    for i in range(1,attempts+1):
        while True:
            try:
                guess=int(input('Enter your guess:'))
                if 1<=guess<=100:
                    break
                else:
                    print('Your guess must be between 1 and 100.')
            except ValueError :
                print('Your guess must be an int.') 

    
        if check_guess(guess,secret):
            used_attempts=attempts-i
            print('You have won in {used_attempts} attempts')
            break

        
    


def check_guess(guess,secret):
    if guess == secret:
        print('Correct answer')
        return True
    elif 1 <= abs(secret - guess) <= 3:
        print('Very close')
    elif guess > secret:
        print('Too high')
    else:
        print('Too low')
    return False
  
        


main()



        


        

     


    

