from tkinter import *

#use this to know the coordinates of the canvas to draw your desired figure
#def motion(event):
   # x, y = event.x, event.y
   # print('{}, {}'.format(x, y))

#Doraemon.bind('<Motion>', motion)


#defining expressions
def angry():
    if not c.no_anger:
        c.itemconfigure(angry_mouth , state = NORMAL)
        c.itemconfigure(angryeyel , state = NORMAL)
        c.itemconfigure(angryeyer , state = NORMAL)

        c.no_anger = True
    else:
        c.itemconfigure(angry_mouth , state = HIDDEN)
        c.itemconfigure(angryeyel , state = HIDDEN)
        c.itemconfigure(angryeyer , state = HIDDEN)

        c.no_anger = False

def punch(event):
    angry()
    hide_all(event)
    Doraemon.after(3000,angry)
    return


def show_happy(event):
    if(20<= event.x and event.x <= 350) and (20<= event.y and event.y <= 350):
        #c.itemconfigure(cheek_left , state = NORMAL)
       # c.itemconfigure(cheek_right , state = NORMAL)
        c.itemconfigure(happy_mouth , state = NORMAL)
        c.itemconfigure(normal_mouth , state = HIDDEN)
        c.itemconfigure(sad_mouth, state = HIDDEN)
        c.itemconfigure(sadeyel , state = HIDDEN)
        c.itemconfigure(sadeyer , state = HIDDEN)
        c.itemconfigure(eyel_happy,state=NORMAL)
        c.itemconfigure(eyer_happy,state=NORMAL)
        c.itemconfigure(iris_happyl, state=NORMAL)
        c.itemconfigure(iris_happyr, state=NORMAL)
        c.happy_level = 10
    return


def hide_happy(event):
    c.itemconfigure(happy_mouth , state = HIDDEN)
    c.itemconfigure(normal_mouth , state = NORMAL)
    c.itemconfigure(sad_mouth, state = HIDDEN)
    c.itemconfigure(sadeyer, state=HIDDEN)
    c.itemconfigure(sadeyel, state=HIDDEN)
    c.itemconfigure(eyel_happy, state=HIDDEN)
    c.itemconfigure(eyer_happy, state=HIDDEN)
    c.itemconfigure(iris_happyl, state=HIDDEN)
    c.itemconfigure(iris_happyr, state=HIDDEN)

    return

def hide_all(event):
    c.itemconfigure(happy_mouth , state = HIDDEN)
    c.itemconfigure(normal_mouth , state = HIDDEN)
    c.itemconfigure(sad_mouth, state = HIDDEN)
    c.itemconfigure(sadeyer, state=HIDDEN)
    c.itemconfigure(sadeyel, state=HIDDEN)
    c.itemconfigure(eyel_happy, state=HIDDEN)
    c.itemconfigure(eyer_happy, state=HIDDEN)
    c.itemconfigure(iris_happyl, state=HIDDEN)
    c.itemconfigure(iris_happyr, state=HIDDEN)

    return



def sad():
    if c.happy_level == 0 :
        c.itemconfigure(happy_mouth , state = HIDDEN)
        c.itemconfigure(normal_mouth , state = HIDDEN)
        c.itemconfigure(sad_mouth , state = NORMAL)
        c.itemconfigure(sadeyel , state = NORMAL)
        c.itemconfigure(sadeyer , state =NORMAL)
        c.itemconfigure(eyel_happy, state=HIDDEN)
        c.itemconfigure(eyer_happy, state=HIDDEN)
        c.itemconfigure(iris_happyl, state=HIDDEN)
        c.itemconfigure(iris_happyr, state=HIDDEN)




    else:
        c.happy_level -= 1
    Doraemon.after(5000,sad)

def doexp():
    text1 = text.get()
    for word in text1.split(' '):


        if word.lower() in action.keys():
            try:
                action[word.lower()]()



            except:
                type.delete(0,END)
                type.insert(END,'something went wrong ')
            finally:
                break

        elif word.lower() not in action.keys():
            type.delete(0,END)
            type.insert(END,'something went wrong')

def show_happy1():
     c.itemconfigure(happy_mouth, state=NORMAL)
     c.itemconfigure(normal_mouth, state=HIDDEN)
     c.itemconfigure(sad_mouth, state=HIDDEN)
     c.itemconfigure(sadeyel, state=HIDDEN)
     c.itemconfigure(sadeyer, state=HIDDEN)
     c.itemconfigure(eyel_happy, state=NORMAL)
     c.itemconfigure(eyer_happy, state=NORMAL)
     c.itemconfigure(iris_happyl, state=NORMAL)
     c.itemconfigure(iris_happyr, state=NORMAL)
     c.happy_level = 10
     return


def blush():
    c.itemconfigure(happy_mouth, state=NORMAL)
    c.itemconfigure(normal_mouth, state=HIDDEN)
    c.itemconfigure(sad_mouth, state=HIDDEN)
    c.itemconfigure(sadeyel, state=HIDDEN)
    c.itemconfigure(sadeyer, state=HIDDEN)
    c.itemconfigure(eyel_happy, state=NORMAL)
    c.itemconfigure(eyer_happy, state=NORMAL)
    c.itemconfigure(iris_happyl, state=NORMAL)
    c.itemconfigure(iris_happyr, state=NORMAL)
    c.itemconfigure(cheek_left ,state=NORMAL)
    c.itemconfigure(cheek_right,state=NORMAL)
    Doraemon.after(2000, hide)
    return

def angry1():
        c.itemconfigure(angry_mouth , state = NORMAL)
        c.itemconfigure(angryeyel , state = NORMAL)
        c.itemconfigure(angryeyer , state = NORMAL)
        c.itemconfigure(normal_mouth, state=HIDDEN)
        c.itemconfigure(sad_mouth, state=HIDDEN)
        c.itemconfigure(sadeyer, state=HIDDEN)
        Doraemon.after(2000,hide)

def sad1():

        c.itemconfigure(happy_mouth , state = HIDDEN)
        c.itemconfigure(normal_mouth , state = HIDDEN)
        c.itemconfigure(sad_mouth , state = NORMAL)
        c.itemconfigure(sadeyel , state = NORMAL)
        c.itemconfigure(sadeyer , state =NORMAL)
        c.itemconfigure(eyel_happy, state=HIDDEN)
        c.itemconfigure(eyer_happy, state=HIDDEN)
        c.itemconfigure(iris_happyl, state=HIDDEN)
        c.itemconfigure(iris_happyr, state=HIDDEN)
        Doraemon.aftre(2000,hide)
def hide():
     c.itemconfigure(angry_mouth , state = HIDDEN)
     c.itemconfigure(angryeyel , state = HIDDEN)
     c.itemconfigure(angryeyer , state = HIDDEN)
     c.itemconfigure(cheek_left, state=HIDDEN)
     c.itemconfigure(cheek_right, state=HIDDEN)

Doraemon= Tk()
Doraemon.title("Screen Buddy")

c=Canvas(Doraemon ,width= 500 ,height=600)
c.configure(bg='lightblue',highlightthickness=1)

#defining the dictionary
action={'cute':blush,'cool':blush,'love':blush,'handsome':blush,'hi':show_happy1,'hello':show_happy1,'useless':angry1,'idiot':angry1,
        'fool':angry1,'racoon':angry1,'hate':sad1}

#drawing
c.body_color = '#1a92c8'

head  = c.create_oval(120,20,380,240,outline='black' , fill='#1a92c8')



feet= c.create_oval(135,440,245,494 , outline='black', fill='white')
feet1= c.create_oval(270,440,380,494 , outline='black', fill='white')

body=c.create_rectangle(176,235,318,395,outline='#1a92c8',fill='#1a92c8')
body1=c.create_rectangle(174,310,327,418,outline='#1a92c8',fill='#1a92c8')
body3=c.create_rectangle(175,419,239,449,outline='#1a92c8',fill='#1a92c8')
body=c.create_rectangle(272,410,333,441,outline='#1a92c8',fill='#1a92c8')



hand=c.create_polygon(114,291,179,235,183,275,131,308,outline='#1a92c8',fill='#1a92c8',width=3)

c.create_line(114,291,134,272, 168,241, 179,235, fill='black',smooth=1,width=1)
c.create_line(184,265,174,289, 177,411,172,451, fill='#1a92c8',smooth=1,width=6)
c.create_line(184,265,173,286, 171,327,174,385,170,451, fill='black',smooth=1,width=1)


lss=c.create_line(172,432,200,451,236,443, fill='#1a92c8',smooth=1,width=20)
l=c.create_line(172,451,202,457,240,456, fill='black',smooth=1,width=4)

l1=c.create_line(276,450,310,450,340,440, fill='#1a92c8',smooth=1,width=17)
l1=c.create_line(276,456,315,455,344,445, fill='black',smooth=1,width=3)


h1=c.create_polygon(319,236,371,290,366,301,346,297,312,272,outline='#1a92c8',fill='#1a92c8',width=5)
h11=c.create_line(319,236,385,291,368,318,312,272, fill='black',smooth=1,width=1)

b12=c.create_line(308,239,325,302,324,319,326,381,334,444, fill='#1a92c8',smooth=1,width=16)
b1=c.create_line(319,236,335,325,330,345,342,447, fill='black',smooth=1,width=1)

bleg=c.create_line(229,453,256,370,274,411,280,456, fill='#1a92c8',smooth=1,width=18)
bleg=c.create_line(240,456,256,380,276,456, fill='black',smooth=1,width=2)




fist= c.create_oval(98,285,135,324, outline='black',fill='white')
fist2= c.create_oval(360,288,396,324, outline='black',fill='white')
stomach=c.create_oval(190,204,324,403,outline='black' , fill='white')
pouch=c.create_arc(218, 250, 293,332, start=0, extent=-180, fill="white",outline='black')


face = c.create_oval(140,70,362,242 , outline='black' , fill='white')

eye = c.create_oval(205,50,250,108 , outline='black' , fill='white')
iris1 = c.create_oval(230,78,240,95 , outline='black' , fill='black')
iris2 = c.create_oval(233,85,238,92 , outline='black' , fill='white')
eye1 = c.create_oval(250,50,295,108 , outline='black' , fill='white')
eye1iris1 = c.create_oval(260,78,270,95 , outline='black' , fill='black')
eye1iris2 = c.create_oval(263,85,268,92 , outline='black' , fill='white')
eyel_happy= c.create_oval(205,50,250,108 , outline='black' , fill='white')
eyer_happy = c.create_oval(250,50,295,108  , outline='black' , fill='white')
iris_happyl= c.create_line(224,89,229,84,234,89,smooth=1,width=3)
iris_happyr= c.create_line(263,89,268,84,273,89,smooth=1,width=3)


sadeyel=c.create_line(207,85,245,62,state=HIDDEN)
sadeyer=c.create_line(254,63,294,85,state=HIDDEN)

angryeyel=c.create_line(208,65,249,77,width=2,state=HIDDEN)
angryeyer=c.create_line(252,77,291,65,width=2,state=HIDDEN)


line1 =c.create_line(284,135,353,95)
line2 =c.create_line(222,135,155,95)
line3 =c.create_line(288,151,362,148)
line4 =c.create_line(222,154,136,151)
line5 =c.create_line(287,168,354,192)
line6 =c.create_line(224,168,152,199)

normal_mouth=c.create_line(215,173,250,195,290,173,smooth=1,state=NORMAL)
happy_mouth=c.create_arc(190, 110, 310,220, start=0, extent=-180, fill="#9a1111",outline='black',state=HIDDEN)
sad_mouth=c.create_line(214,176,250,160,291,176,width=2,smooth=1,state=HIDDEN)
angry_mouth=c.create_line(198,195,286,176,298,195,smooth =1,width=1,state=HIDDEN    )



linestrai =c.create_line(250,116,250,160)

nose = c.create_oval(238,95,261,120 , outline='black' , fill='#b60015')

belt = [180, 235, 320, 235, 320, 225, 180, 225]
c.create_polygon(belt, outline='black', fill='#b30217', width=1)
c.create_rectangle(211,236,296,244,fill='white',outline='white')

cheek_left = c.create_oval(179,124,215,169,outline='pink' , fill='pink',state=HIDDEN)
cheek_right = c.create_oval(294,124,334,169,outline='pink' , fill='pink',state=HIDDEN)


c.pack()

c.bind('<Motion>' , show_happy)
c.bind('<Leave>' , hide_happy)
c.bind('<Double-1>' , punch)

c.happy_level = 10
c.no_anger =False

Doraemon.after(5000,sad)

text=StringVar()
type=Entry(Doraemon,width=35,textvariable=text,font='arial 15')
type.place(x=40,y=550,height=40)

Tell = Button(Doraemon,text='Search',command=doexp)
Tell.place(x=430,y=550,height=40)

Doraemon.mainloop()