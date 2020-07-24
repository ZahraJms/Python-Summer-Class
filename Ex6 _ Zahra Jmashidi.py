#45
total=0
while total<50:
    total+=int(input("Enter A Number : "))
    print("The Total Is : {} ".format(total))

#46
list=[]
x=0
while x<=5:
    x=int(input("Enter A Number : "))
    list.append(x)
print("The Last Number You Entered Was {}".format(list[-2]))

#47
sum=int(input("Enter A Number : "))
answer="y"
while answer=="y":
    sum+=int(input("Enter A Number : "))
    answer=input("Do You Want To Add Another Number ? ( y or n ) : ")
print(sum)

#48
count=0
answer="y"
while answer=="y":
    name=input("Enter A Name That You Want To Invite To Party : ")
    print("{} Has Now Been Invited ".format(name))
    count+=1
    answer = input("Do You Want To Add Another Name ? ( y or n ) : ")
print(count," Person Has Been Invited. ")

#49
compnum=50
count=0
guess=0
while guess!=compnum:
    guess=int(input("Guess A Number : "))
    count+=1
    if guess==compnum:
        print("Well Done , You Took {} Attempts".format(count))
    elif guess>compnum:
        print("Too High")
    else:
        print("Too Low")

#50
while True:
    num=int(input("Enter A Number Between 10 And 20 : "))
    if num<10:
        print("Too Low")
    elif num>20 :
        print ("Too High")
    else:
        print("Thank You")
        break

#51
bottle=10
while bottle>0:
    answer=int(input("There Are {} Green Bottles Hanging On The Wall , {} Bottles Hanging On The Wall , And If 1 Green Bottles Should Accidentally Fall \nHow Many Green Bottles Will Be Hanging On The Wall ? ".format(bottle,bottle)))
    if answer==bottle-1 :
        bottle-=1
        if answer==0:
            print("There Are No More Green Bottles Hanging On The Wall")
        else:
            print("There Will Be {} Green Bottles Hanging On The Wall".format(bottle))
    else:
        print("No , Try Again")