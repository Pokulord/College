from tkinter import *
import tkinter.messagebox as mb
from PIL import  Image,ImageTk
from tkinter import ttk
from random import randint
import time
import pygame
import os
#Процедурная часть
def generate_res():
    global chet,im,a,chet_frames,chet_mass_game,mass_game,result,flag
    p1_name=en_1.get()
    p2_name=en_2.get()
    p1_bet=cb_1.get()
    p2_bet=cb_2.get()
    if p1_name=="" or p1_bet=="" or p2_name=="" or p2_bet=="":
        flag=False
        root_2p.lift()
        mb.showerror("Внимание","Заполнены не все поля")
    else:
        flag=True
        en_1.configure(state=DISABLED)
        en_2.configure(state=DISABLED)
        while chet_mass_game<1:
            mass_game[0].append(p1_name)
            mass_game[0].append(p1_bet)
            mass_game[1].append(p2_name)
            mass_game[1].append(p2_bet)
            chet_mass_game+=1
        print(mass_game)
        while chet<1:
            a=randint(1,100)
            print(a)
            chet+=1
        if a>50:
            im = [PhotoImage(file="coin.gif", format=f"gif -index {i}") for i in range(11)]  # орёл
            result="Орёл"
            chet_frames+=1
            if chet_frames==12:
                lb_coin.configure(image=im[-1])

        if a<50:
            im = [PhotoImage(file="coin.gif", format=f"gif -index {i}") for i in range(20)]  # решка
            result="Решка"
            chet_frames+=1
            if chet_frames==21:
                lb_coin.configure(image=im[-1])
        print("res",result)
def animaton(count):
    global anim,chet,chet_frames,mass_game,chet_mass_game,result,chet_sound
    try:
        generate_res()
        while chet_sound==0 and flag==True:
            pygame.mixer.init(44100, -16, 2, 2048)  # для корректного воспроизведения
            sound = pygame.mixer.Sound("sounds/coin flip sound effect.mp3")
            sound.play()
            chet_sound+=1
        img=im[count]
        lb_coin.configure(image=img)
        count+=1
        anim=root.after(30,lambda : animaton(count))
    except:
        mass_final=[]
        chet=0
        chet_frames=0
        print("mass",mass_game)
        print("len",len(mass_game))
        for i in mass_game:
            print("i",i)
            if i[-1]!=result:
                print("Удалён",i)
                del mass_game[mass_game.index(i)]
            for j in mass_game:
                if j[-1]!=result:
                    del mass_game[mass_game.index(j)]
        print("Результат",mass_game)
        if len(mass_game)==1:
            time.sleep(1)
            mb.showinfo("Победа","Победил"+"\n"+mass_game[0][0])
            canv_game=Canvas(root_2p,width=510,height=220,highlightthickness=0)
            canv_game.create_image(0,0,anchor="nw",image=game_over)
            canv_game.place(x=0,y=0)
            root_2p.mainloop()

        elif len(mass_game)==2 or len(mass_game)==0:
            mb.showinfo("Ничья!","Ничья! Но победителем должен выйти лишь один игрок. Посему давайте переиграем")
        mass_game=[[],[]]
        chet_mass_game=0
        result=""
        print(mass_game)



def EXIT():
    root.destroy()
def start():
    global frames_col,im,count,anim,lb_coin,chet,massiv_vipad,chet,chet_frames,cb_1,cb_2,en_1,en_2,chet_mass_game,mass_game,root_2p,chet_sound
    chet_mass_game=0
    chet=0
    chet_frames=0
    mass_game=[[],[]]
    ch=int(choice.get())
    choice.current("0")
    coin=Image.open("coin.gif")
    #im = [PhotoImage(file="coin.gif", format=f"gif -index {i}") for i in range(20)]#решка
    #im = [PhotoImage(file="coin.gif", format=f"gif -index {i}") for i in range(11)]#орёл
    #im = [PhotoImage(file="coin.gif", format=f"gif -index {i}") for i in range(16)]#ребром
    if ch==2:
        chet_sound=0
        count=0
        root_2p=Toplevel()
        root_2p.resizable(False,False)
        root_2p.iconbitmap("icon.ico")
        root_2p.title("Орлянка.2 игрока")
        root_2p.geometry("510x220+500+400")
        root_2p.grab_set()#Модальность
        half_canv=Canvas(root_2p,width=330,bg="gray36",highlightthickness=0)
        half_canv.create_image(0,0,anchor="nw",image=image)
        half_canv.place(x=0,y=0)
        but_play=Button(root_2p,text="Играть",width=20,command=lambda : animaton(count),font="Areal 13")
        but_play.place(x=90,y=170)
        lb_coin=Label(root_2p,width=0,height=0)
        lb_coin.place(x=350,y=20)
        anim=None
        cb_1=ttk.Combobox(root_2p,width=10,values=["","Орёл","Решка"])
        cb_1.place(x=230,y=40)
        en_1=Entry(root_2p,width=20,font="Areal 10")
        en_1.place(x=30,y=40)
        lb_p_1=Label(root_2p,text="Введите имя 1-го игрока и сделайте ставку",font="Areal 11",bg="gray36",fg="white")
        lb_p_1.place(x=27,y=0)
        lb_p_2=Label(root_2p,text="Введите имя 2-го игрока и сделайте ставку",font="Areal 11",bg="gray36",fg="white")
        lb_p_2.place(x=27,y=90)
        en_2=Entry(root_2p,width=20,font="Areal 10")
        en_2.place(x=30,y=130)
        cb_2=ttk.Combobox(root_2p,width=10,values=["","Орёл","Решка"])
        cb_2.place(x=230,y=130)
        root_2p.mainloop()




def play():
    global choice
    root_play=Toplevel()
    root_play.grab_set()
    root_play.iconbitmap("icon.ico")
    root_play.resizable(False,False)
    root_play.geometry("500x200+500+400")
    play_back=Canvas(root_play,width=500,height=200,highlightthickness=0)
    play_back.place(x=0,y=0)
    play_back.create_image(0,0,anchor="nw",image=image)
    lb_choice=Label(root_play,text="Выберите количество игроков",bg="gray36",font="Italic 13",fg="white")
    lb_choice.place(x=130,y=30)
    choice=ttk.Combobox(root_play,values=["","2"],font="Italic 13")
    choice.place(x=145,y=70)
    but_play=Button(root_play,text="Старт",font="Italic 13",command=start)
    but_play.place(x=210,y=110)


    root_play.mainloop()

#Интерфейс
root=Tk()
root.geometry("500x300+500+400")
root.title("Орлянка")
root.resizable(False,False)
root.iconbitmap("icon.ico")
canv_back=Canvas(root,width=500,height=300,highlightthickness=0)
canv_back.place(x=0,y=0)
image=Image.open("imgonline-com-ua-Resize-jQzejPT4uJcEG.jpg")
image=ImageTk.PhotoImage(image)
canv_back.create_image(0,0,anchor="nw",image=image)
#Кнопки
but_play=Button(root,text="Играть",font="Areal 14",width=15,command=play)
but_play.place(x=160,y=60)
but_exit=Button(root,text="Выход",font="Areal 14",width=15,command=EXIT)
but_exit.place(x=160,y=150)
image_b=Image.open("game_over.jpg")
game_over=ImageTk.PhotoImage(image_b)
root.mainloop()