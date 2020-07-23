#12
num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))
if num1>num2:
    print(num2," - ",num1)
else :
    print(num1," - ", num2)

#13
num=int(input("Enter Your Number ( Lower Than 20 ) : "))
if num>=20:
    print("Too High")
else :
    print("Thank You")

#14
num=int(input("Enter Your Number ( Between 10 And 20 ) : "))
if num>10 and num<20:
    print("Thank You")
else :
    print("Incorrect Answer")

#15
Help = ["Red","red","RED"]
colour=input("Enter Your Favorite Colour : ")
if colour in Help :
    print("I Like Red Too")
else :
    print("I Don't Like {} , I Prefer Red".format(colour))

#16
answer=input("If It Is Raining : ").lower()
if answer=="yes":
    answer=input("If It Is Windy : ").lower()
    if answer=="yes":
        print("It Is Too Windy For An Umbrella")
    else:
        print("Take An Umbrella")
else :
    print("Enjoy Your Day")

#17
age=int(input("Enter Your Age : "))
if age>=18:
    print("You Can Vote")
elif age==17:
    print("You Can Learn To Drive")
elif age==16 :
    print("You Can Buy A Lottery Ticket")
else:
    print("You Can Go Trick Or Treating")

#18
num=int(input("Enter Your Number : "))
if num>20:
    print("Too High")
elif num>=10 and num<=20 :
    print("Correct")
else:
    print("Too Low")

#19
num=input("Enter A Number From 1 To 3 : ")
if num=="1":
    print("Thank You")
elif num=="2":
    print("Well Done")
elif num=="3":
    print("Correct")
else:
    print("Error Message")
