year=int(input("Enter The Year"))
if year%4==0:
    if year%400==0 or year%100!=0:
        print("Leap Year")
    else :
        print("Not Leap Year")
else :
    print("Not Leap Year")
