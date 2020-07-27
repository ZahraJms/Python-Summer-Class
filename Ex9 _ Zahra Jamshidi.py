class Time():
    def __init__(self,Hour,Minute,Second):
        self.Hour=Hour
        self.Minute=Minute
        self.Second=Second
    def  __str__(self):
        return str(self.Hour) + " : " + str(self.Minute) + " : " + str(self.Second)
    def __repr__(self):
        return str(self.Hour) + " : " + str(self.Minute) + " : " + str(self.Second)
    def __add__(self, other):
        sec=self.Second+other.Second
        min=self.Minute+other.Minute
        hur=self.Hour+other.Hour
        if sec>60:
            min+= (sec//60)
            sec-= (sec%60)
        if min>60:
            hur+= (sec//60)
            min-= (sec%60)
        return Time(str(hur),str(min),str(sec))
    def __sub__(self, other):
        sec = self.Second - other.Second
        min = self.Minute - other.Minute
        hur = self.Hour - other.Hour
        if sec < 0:
            min -= 1
            sec += 60
        if min < 0:
            hur -= 1
            min += 60
        if hur < 0:
            hur+=24
        return Time(str(hur),str(min),str(sec))
    def __lt__(self,other):
        if self.Hour < other.Hour :
            return True
        elif self.Hour > other.Hour:
            return False
        else:
            if self.Minute < other.Minute:
                return True
            elif self.Minute > other.Minute:
                return False
            else:
                if self.Second < other.Second:
                    return True
                else:
                    return False
    def __gt__(self,other):
        if self.Hour > other.Hour:
            return True
        elif self.Hour < other.Hour:
            return False
        else:
            if self.Minute > other.Minute:
                return True
            elif self.Minute < other.Minute:
                return False
            else:
                if self.Second > other.Second:
                    return True
                else:
                    return False
    def __eq__(self, other):
        if self.Second == other.Second and self.Minute == other.Minute and self.Hour == other.Hour:
            return True
        else:
            return False
    def show(self):
        return Time(str(self.Hour), str(self.Minute), str(self.Second))
t1=Time(4,50,20)
t2=Time(18,50,20)
print(t2-t1)