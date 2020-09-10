import tkinter
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
import random

# Create Word List
response = requests.get("https://www.vocabulary.com/lists/172112")
soup = BeautifulSoup(response.text, 'html.parser')
words = soup.find_all('a', attrs={'word dynamictext'})
vocablist = []
for word in words:
    vocablist.append(word.text)

game = True
while game :
    #Create Rand Word
    randomword=random.choice(vocablist)
    print(randomword)
    guessword=[]
    for i in range (0,len(randomword)):
        guessword.append("_")

    guessletters=[]
    point=0

    #Win
    win = tkinter.Tk()
    win.resizable(False,False)
    win.geometry('710x500')
    win.title("Hangman Game")
    word=tkinter.Label(win,text=" ".join(guessword))
    word.config(font=('nazanin',50,'bold'))
    word.place(x=150,y=100)
    pointcan=tkinter.Canvas(height=100,width=200)
    pointcan.place(x=0,y=0)
    pointcan.create_oval(5,5,35,35,fill="blue")
    pointcan.create_oval(40,5,70,35,fill="blue")
    pointcan.create_oval(75,5,105,35,fill="blue")
    pointcan.create_oval(110,5,140,35,fill="blue")
    pointcan.create_oval(145,5,175,35,fill="blue")

    def find_a():
        global point
        global game
        global word
        if 'a' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'a' in randomword:
                place=-1
                guessletters.append('a')
                for i in range(0,randomword.count('a')):
                    place=randomword.find('a',place+1)
                    if place==0:
                        guessword[place]='A'
                    else :
                        guessword[place]='a'
            else:
                point-=1
                guessletters.append('a')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()

    def find_b():
        global point
        global game
        global word
        if 'b' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'b' in randomword:
                place=-1
                guessletters.append('b')
                for i in range(0,randomword.count('b')):
                    place=randomword.find('b',place+1)
                    if place==0:
                        guessword[place]='B'
                    else :
                        guessword[place]='b'
            else:
                point-=1
                guessletters.append('b')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_c():
        global point
        global game
        global word
        if 'c' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'c' in randomword:
                place=-1
                guessletters.append('c')
                for i in range(0,randomword.count('c')):
                    place=randomword.find('c',place+1)
                    if place==0:
                        guessword[place]='C'
                    else :
                        guessword[place]='c'
            else:
                point-=1
                guessletters.append('c')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_d():
        global point
        global game
        global word
        if 'd' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'd' in randomword:
                place=-1
                guessletters.append('d')
                for i in range(0,randomword.count('d')):
                    place=randomword.find('d',place+1)
                    if place==0:
                        guessword[place]='D'
                    else :
                        guessword[place]='d'
            else:
                point-=1
                guessletters.append('d')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_e():
        global point
        global game
        global word
        if 'e' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'e' in randomword:
                place=-1
                guessletters.append('e')
                for i in range(0,randomword.count('e')):
                    place=randomword.find('e',place+1)
                    if place==0:
                        guessword[place]='E'
                    else :
                        guessword[place]='e'
            else:
                point-=1
                guessletters.append('e')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_f():
        global point
        global game
        global word
        if 'f' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'f' in randomword:
                place=-1
                guessletters.append('f')
                for i in range(0,randomword.count('f')):
                    place=randomword.find('f',place+1)
                    if place==0:
                        guessword[place]='F'
                    else :
                        guessword[place]='f'
            else:
                point-=1
                guessletters.append('f')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_g():
        global point
        global game
        global word
        if 'g' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'g' in randomword:
                place=-1
                guessletters.append('g')
                for i in range(0,randomword.count('g')):
                    place=randomword.find('g',place+1)
                    if place==0:
                        guessword[place]='G'
                    else :
                        guessword[place]='g'
            else:
                point-=1
                guessletters.append('g')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_h():
        global point
        global game
        global word
        if 'h' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'h' in randomword:
                place=-1
                guessletters.append('h')
                for i in range(0,randomword.count('h')):
                    place=randomword.find('h',place+1)
                    if place==0:
                        guessword[place]='H'
                    else :
                        guessword[place]='h'
            else:
                point-=1
                guessletters.append('h')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_i():
        global point
        global game
        global word
        if 'i' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'i' in randomword:
                place=-1
                guessletters.append('i')
                for i in range(0,randomword.count('i')):
                    place=randomword.find('i',place+1)
                    if place==0:
                        guessword[place]='I'
                    else :
                        guessword[place]='i'
            else:
                point-=1
                guessletters.append('i')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_j():
        global point
        global game
        global word
        if 'j' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'j' in randomword:
                place=-1
                guessletters.append('j')
                for i in range(0,randomword.count('j')):
                    place=randomword.find('j',place+1)
                    if place==0:
                        guessword[place]='J'
                    else :
                        guessword[place]='j'
            else:
                point-=1
                guessletters.append('j')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_k():
        global point
        global game
        global word
        if 'k' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'k' in randomword:
                place=-1
                guessletters.append('k')
                for i in range(0,randomword.count('k')):
                    place=randomword.find('k',place+1)
                    if place==0:
                        guessword[place]='K'
                    else :
                        guessword[place]='k'
            else:
                point-=1
                guessletters.append('k')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_l():
        global point
        global game
        global word
        if 'l' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'l' in randomword:
                place=-1
                guessletters.append('l')
                for i in range(0,randomword.count('l')):
                    place=randomword.find('l',place+1)
                    if place==0:
                        guessword[place]='L'
                    else :
                        guessword[place]='l'
            else:
                point-=1
                guessletters.append('l')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_m():
        global point
        global game
        global word
        if 'm' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'm' in randomword:
                place=-1
                guessletters.append('m')
                for i in range(0,randomword.count('m')):
                    place=randomword.find('m',place+1)
                    if place==0:
                        guessword[place]='M'
                    else :
                        guessword[place]='m'
            else:
                point-=1
                guessletters.append('m')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_n():
        global point
        global game
        global word
        if 'n' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'n' in randomword:
                place=-1
                guessletters.append('n')
                for i in range(0,randomword.count('n')):
                    place=randomword.find('n',place+1)
                    if place==0:
                        guessword[place]='N'
                    else :
                        guessword[place]='n'
            else:
                point-=1
                guessletters.append('n')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_o():
        global point
        global game
        global word
        if 'o' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'o' in randomword:
                place=-1
                guessletters.append('o')
                for i in range(0,randomword.count('o')):
                    place=randomword.find('o',place+1)
                    if place==0:
                        guessword[place]='O'
                    else :
                        guessword[place]='o'
            else:
                point-=1
                guessletters.append('o')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_p():
        global point
        global game
        global word
        if 'p' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'p' in randomword:
                place=-1
                guessletters.append('p')
                for i in range(0,randomword.count('p')):
                    place=randomword.find('p',place+1)
                    if place==0:
                        guessword[place]='P'
                    else :
                        guessword[place]='p'
            else:
                point-=1
                guessletters.append('p')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_q():
        global point
        global game
        global word
        if 'q' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'q' in randomword:
                place=-1
                guessletters.append('q')
                for i in range(0,randomword.count('q')):
                    place=randomword.find('q',place+1)
                    if place==0:
                        guessword[place]='Q'
                    else :
                        guessword[place]='q'
            else:
                point-=1
                guessletters.append('q')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_r():
        global point
        global game
        global word
        if 'r' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'r' in randomword:
                place=-1
                guessletters.append('r')
                for i in range(0,randomword.count('r')):
                    place=randomword.find('r',place+1)
                    if place==0:
                        guessword[place]='R'
                    else :
                        guessword[place]='r'
            else:
                point-=1
                guessletters.append('r')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_s():
        global point
        global game
        global word
        if 's' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 's' in randomword:
                place=-1
                guessletters.append('s')
                for i in range(0,randomword.count('s')):
                    place=randomword.find('s',place+1)
                    if place==0:
                        guessword[place]='S'
                    else :
                        guessword[place]='s'
            else:
                point-=1
                guessletters.append('s')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_t():
        global point
        global game
        global word
        if 't' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 't' in randomword:
                place=-1
                guessletters.append('t')
                for i in range(0,randomword.count('t')):
                    place=randomword.find('t',place+1)
                    if place==0:
                        guessword[place]='T'
                    else :
                        guessword[place]='t'
            else:
                point-=1
                guessletters.append('t')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_u():
        global point
        global game
        global word
        if 'u' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'u' in randomword:
                place=-1
                guessletters.append('u')
                for i in range(0,randomword.count('u')):
                    place=randomword.find('u',place+1)
                    if place==0:
                        guessword[place]='U'
                    else :
                        guessword[place]='u'
            else:
                point-=1
                guessletters.append('u')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_v():
        global point
        global game
        global word
        if 'v' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'v' in randomword:
                place=-1
                guessletters.append('v')
                for i in range(0,randomword.count('v')):
                    place=randomword.find('v',place+1)
                    if place==0:
                        guessword[place]='V'
                    else :
                        guessword[place]='v'
            else:
                point-=1
                guessletters.append('v')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_w():
        global point
        global game
        global word
        if 'w' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'w' in randomword:
                place=-1
                guessletters.append('w')
                for i in range(0,randomword.count('w')):
                    place=randomword.find('w',place+1)
                    if place==0:
                        guessword[place]='W'
                    else :
                        guessword[place]='w'
            else:
                point-=1
                guessletters.append('w')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_x():
        global point
        global game
        global word
        if 'x' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'x' in randomword:
                place=-1
                guessletters.append('x')
                for i in range(0,randomword.count('x')):
                    place=randomword.find('x',place+1)
                    if place==0:
                        guessword[place]='X'
                    else :
                        guessword[place]='x'
            else:
                point-=1
                guessletters.append('x')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_y():
        global point
        global game
        global word
        if 'y' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'y' in randomword:
                place=-1
                guessletters.append('y')
                for i in range(0,randomword.count('y')):
                    place=randomword.find('y',place+1)
                    if place==0:
                        guessword[place]='Y'
                    else :
                        guessword[place]='y'
            else:
                point-=1
                guessletters.append('y')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()
    def find_z():
        global point
        global game
        global word
        if 'z' in guessletters:
            messagebox.showwarning("Error" ,"Repetetive Letter !")
        else :
            if 'z' in randomword:
                place=-1
                guessletters.append('z')
                for i in range(0,randomword.count('z')):
                    place=randomword.find('z',place+1)
                    if place==0:
                        guessword[place]='Z'
                    else :
                        guessword[place]='z'
            else:
                point-=1
                guessletters.append('z')
            if point ==-1:
                pointcan.create_oval(5, 5, 35, 35, fill="red")
            if point == -2:
                pointcan.create_oval(40, 5, 70, 35, fill="red")
            if point == -3:
                pointcan.create_oval(75, 5, 105, 35, fill="red")
            if point == -4 :
                pointcan.create_oval(110, 5, 140, 35, fill="red")
            if point == -5 :
                pointcan.create_oval(145, 5, 175, 35, fill="red")
        word.destroy()
        word = tkinter.Label(win, text=" ".join(guessword))
        word.config(font=('nazanin', 50, 'bold'))
        word.place(x=150,y=100)
        if "".join(guessword).lower()==randomword:
            game = messagebox.askyesno("You Win !", "Your Guesses Were Right , Do You Want To Play Again ? ")
            win.destroy()
        if point==-5:
            game = messagebox.askyesno("You Lose !" ,"You Couldn't Guess The Right Word , Do You Want To Play Again ? ")
            win.destroy()

    # Maing Letter Button
    z=tkinter.Button(win,text='Z',command=find_z,height=3,width=6,bg="green")
    z.place(x=653,y=440)
    y=tkinter.Button(win,text='Y',command=find_y,height=3,width=6,fg="blue")
    y.place(x=599,y=440)
    x=tkinter.Button(win,text='X',command=find_x,height=3,width=6,bg="green")
    x.place(x=545,y=440)
    w=tkinter.Button(win,text='W',command=find_w,height=3,width=6,fg="blue")
    w.place(x=491,y=440)
    v=tkinter.Button(win,text='V',command=find_v,height=3,width=6,bg="green")
    v.place(x=437,y=440)
    u=tkinter.Button(win,text='U',command=find_u,height=3,width=6,fg="blue")
    u.place(x=383,y=440)
    t=tkinter.Button(win,text='T',command=find_t,height=3,width=6,bg="green")
    t.place(x=329,y=440)
    s=tkinter.Button(win,text='S',command=find_s,height=3,width=6,fg="blue")
    s.place(x=275,y=440)
    r=tkinter.Button(win,text='R',command=find_r,height=3,width=6,bg="green")
    r.place(x=221,y=440)
    q=tkinter.Button(win,text='Q',command=find_q,height=3,width=6,fg="blue")
    q.place(x=167,y=440)
    p=tkinter.Button(win,text='P',command=find_p,height=3,width=6,bg="green")
    p.place(x=113,y=440)
    o=tkinter.Button(win,text='O',command=find_o,height=3,width=6,fg="blue")
    o.place(x=59,y=440)
    n=tkinter.Button(win,text='N',command=find_n,height=3,width=6,bg="green")
    n.place(x=5,y=440)
    m=tkinter.Button(win,text='M',command=find_m,height=3,width=6,fg="green")
    m.place(x=653,y=383)
    l=tkinter.Button(win,text='L',command=find_l,height=3,width=6,bg="blue")
    l.place(x=599,y=383)
    k=tkinter.Button(win,text='K',command=find_k,height=3,width=6,fg="green")
    k.place(x=545,y=383)
    j=tkinter.Button(win,text='J',command=find_j,height=3,width=6,bg="blue")
    j.place(x=491,y=383)
    i=tkinter.Button(win,text='I',command=find_i,height=3,width=6,fg="green")
    i.place(x=437,y=383)
    h=tkinter.Button(win,text='H',command=find_h,height=3,width=6,bg="blue")
    h.place(x=383,y=383)
    g=tkinter.Button(win,text='G',command=find_g,height=3,width=6,fg="green")
    g.place(x=329,y=383)
    f=tkinter.Button(win,text='F',command=find_f,height=3,width=6,bg="blue")
    f.place(x=275,y=383)
    e=tkinter.Button(win,text='E',command=find_e,height=3,width=6,fg="green")
    e.place(x=221,y=383)
    d=tkinter.Button(win,text='D',command=find_d,height=3,width=6,bg="blue")
    d.place(x=167,y=383)
    c=tkinter.Button(win,text='C',command=find_c,height=3,width=6,fg="green")
    c.place(x=113,y=383)
    b=tkinter.Button(win,text='B',command=find_b,height=3,width=6,bg="blue")
    b.place(x=59,y=383)
    a = tkinter.Button(win, text='A', command=find_a, height=3, width=6, fg="green")
    a.place(x=5, y=383)
    win.mainloop()
