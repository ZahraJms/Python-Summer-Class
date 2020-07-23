#69
countries=("Iran","South Korea","Japan","America","Germany")
for country in countries :
    if country!="Germany":
        print(country,end=" - ")
    else:
        print(country)
c=input("Enter Your Country : ")
print(countries.index(c))

#70
countries=("Iran","South Korea","Japan","America","Germany")
for country in countries :
    if country != "Germany":
        print(country, end=" - ")
    else:
        print(country)
c=int(input("Enter Your Number ( Between 0 And 4 ) : "))
print(countries[c])

#71
sport=["Basketball","Football"]
sport.append(input("Enter Your Favorite Sport : "))
print(sorted(sport))

#72
subjects=["Math","Physics","Biology","History","English","Art"]
for subject in subjects :
    if subject!="Art":
        print(subject,end=" - ")
    else:
        print(subject)
s=input("Choose One Of Them That You Don't Like : ")
subjects.remove(s)
for i in range(len(subjects)) :
    if i!=len(subjects)-1:
        print(subjects[i],end=" - ")
    else:
        print(subjects[i])

#73
food={}
for i in range(4):
    x=input("Enter Your Favorite Food : ")
    food[i+1]=x
for x,y in food.items():
    print(x," : ",y)
x=int(input("Which Do You Want To Get Ride Of It ? ( Choose Number ) "))
food.pop(x)
sortedfood=sorted(food.items(), key=lambda x: x[1])
for x,y in sortedfood:
    print(x," : ",y)

#74
colourlist=input("Enter Your 10 Favorites Colour Like [Red,Blue,...] : ")[1:-1].split(",")
low=int(input("Enter Starting Number From 0 To 4 : "))
high=int(input("Enter Ending Number From 5 To 9 : "))
for i in range(low+1,high):
    print(colourlist[i])

#75
numbers=[234,789,567,123]
for number in numbers:
    print(number)
num=int(input("Enter Your Three-Digit Number : "))
if num in numbers:
    print(numbers.index(num))
else:
    print("That Is Not In The List")

#76
names=input("Enter Your 3 People Name That You Want To Invite To Party Like [Name1,Name2,Name3] : ")[1:-1].split(",")
x=input("Do You Want To Add Another ? ").lower()
while x=="yes":
    names.append(input("Enter The Name : "))
    x = input("Do You Want To Add Another ? ").lower()
print(len(names))

#77
names=input("Enter Your 3 People Name That You Want To Invite To Party Like [Name1,Name2,Name3] : ")[1:-1].split(",")
for name in names :
    print(name,end="  ")
x=input("----> Enter One of The Names : ")
y=input("The Name Index Is {} , Do You Still Want To Invite {} ? ".format(names.index(x),x)).lower()
if y=="no":
    names.remove(x)
print("These Are Names : " , end="")
for name in names :
    print(name,end="  ")

#78
tv=["A","B","C","D"]
for ch in tv:
    print(ch)
x=input("Enter TV Show And A Position Like ( Name , Position ) : ")[1:-1].split(",")
tv.insert(int(x[1]),x[0])
for ch in tv:
    print(ch,end=" ")

#79
nums=[]
for i in range(3):
    nums.append(int(input("Enter Your Number : ")))
    if i==2 :
        x=input("Do You Want To Save You Last Number ? ").lower()
        if x=="no":
            nums.remove(nums[2])
print("This Is Your List : ",nums)