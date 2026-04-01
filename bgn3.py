class Recom:
    def __init__(self,taste):
        self.data=taste
        
    def calc_similarity(self,user):
        max_sim=0
        user2=None
        for person in self.data.keys():
            if not person==user:
                similarity=len(self.data[user] & self.data[person])/len(self.data[user] | self.data[person])
                if similarity>=max_sim:
                    max_sim=similarity
                    user2=person

        return user2

    def recoms(self,user,user2,max_sim):
            print(f'The most similar user is {user2}(with a rate of {max_sim:.2f})')
            print(f'{self.data[user2]-self.data[user]} are recommended to {user}.')

    def process(self,user):
        user2 = self.calc_similarity(user)
        self.recoms(user,user2)



def main():
    taste={
    "A": {"Naruto", "One Piece", "Bleach"},
    "B": {"Naruto", "Attack on Titan"},
    "C": {"Bleach", "Death Note","Naruto"}
    }

    recom=Recom(taste)
    

    user=input('Who are you? ')
    if user not in recom.data:
        print('Invalid user')


    recom.process(user)

if __name__=='__main__':
    main()
    




    
