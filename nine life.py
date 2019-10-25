import random



words=['hello','fine','brilliant','amigos']
guess=random.choice(words)
z=len(guess)
#print(guess)
#print(z)

list = []
for x in range(0,z):
    list.append("?")
print(list)

#print(guess)
word=[]
x=0
for let in guess:
    
    word.append(let)
    

def str(char):
    y=0
    for letr in word:
        if letr==char:
            return(y)
        y=y+1
tou=int(input('''SELECT DIFFICULTY LEVEL
      EASY-1,
      MEDIUM-2,
      HARD-3
     '''))
if tou==1
    c=12
elif tou==2
    c=9
elif tou==3
    c=6

    
a=0
b=0

heart=u'\u2765'
while(a!=z and c!=0):

    char=input('enter your guess:')


    if char in word:
        print('you guessed right!')
        numb=str(char)
        list[numb]=char
        print(list)
        a=a+1
        print('you have',c,'lives left',heart*c)


    elif char==guess:
        print('you have guessed it right!')
        break



    
    else:
        print('you guessed wrong!')
        print('try again')
        c=c-1
        print('you have',c,'lives left',heart*c)


print("the game ends") 


if a==z:
    print('you won!')
elif c==tou:
    print('you lost!')
elif char==guess:
    print('''hurrah!
          you won''')







