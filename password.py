import string
import random


def passtyyyy():

     
     nouns = ['apple', 'dinosaur', 'ball',
     'toaster', 'goat', 'dragon',
     'hammer', 'duck', 'panda','python','hello']

     adjectives = ['sleepy', 'slow', 'smelly',
     'wet', 'fat', 'red',
     'orange', 'yellow', 'green',
     'blue', 'purple', 'fluffy',
     'white', 'proud', 'brave']

     noun=random.choice(nouns)
     adjective=random.choice(adjectives)
     number=str(random.randrange(0,100))
     string_p=random.choice(string.punctuation)
     password=noun+adjective+number+string_p 


     return password

print('password finder')
while True:
    pas=passtyyyy()
    print('Your new password is: ', pas)
    print('like password!')
    ans = input('enter yes or no')
    if ans=='yes':
        break
 input("press enter to exit")



    



