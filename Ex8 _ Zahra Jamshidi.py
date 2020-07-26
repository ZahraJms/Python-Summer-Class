def date(year,month,day):
    m=[31,28,31,30,31,30,31,31,30,31,30,31]
    sum=day
    if year%4==0:
        if year%400==0 or year%100!=0:
            leapyear=1
        else :
            leapyear=0
    else :
        leapyear=0
    for i in range(0,month-1):
        sum+=m[i]
    if leapyear==0:
        return str(sum)+" Day Of Year"
    else :
        if month>=3:
            return str(sum+1)+" Day Of Year"
        else :
            return str(sum)+" Day Of Year"