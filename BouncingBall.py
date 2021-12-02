from tkinter import *
import time
import random
win=Tk()
def main():
    global score
    score=0
    class Ball:
        def __init__(self,canvas,bat):
            self.canvas=canvas
            self.bat=bat
            self.img=canvas.create_oval(75,75,50,50,fill='Lightgreen')
            self.x=10
            self.y=10
            self.hit_bottom=False
        def hit_bat(self,ball_pos):
            bat_pos=self.canvas.coords(self.bat.img)
            if ball_pos[2]>=bat_pos[0] and ball_pos[0]<=bat_pos[2]:
                if ball_pos[3]>=bat_pos[1] and ball_pos[3]<=bat_pos[3]:
                    return True
            return False
        def move(self,canvas):
            self.canvas.move(self.img,self.x,self.y)
            ball_pos=canvas.coords(self.img)
            lp,tp,rp,bp=ball_pos[0],ball_pos[1],ball_pos[2],ball_pos[3]
            if lp<=0 or rp>=450:
                self.x=-self.x
            if tp<=0:
                self.y=-self.y
            if bp>=390:
                self.hit_bottom=True
            if self.hit_bat(ball_pos)==True:
                global score 
                score+=1
                Score=Label(win,text="Your score : "+str(score)).place(x=500,y=20)
                self.y=-self.y
            
    class Bat:
        def __init__(self,canvas):
            self.canvas=canvas
            self.img=canvas.create_rectangle(150,360,250,355,fill="blue")
            self.x=15
        def moveLeft(self):
            lp,tp,rp,bp=self.canvas.coords(self.img)
            if lp>0:
                self.canvas.move(self.img,-self.x,0)
        def moveRight(self):
            lp,tp,rp,bp=self.canvas.coords(self.img)
            if rp<=430:
                self.canvas.move(self.img,self.x,0)
    win.title("Bouncing Ball")
    win.geometry("600x400")
    win.maxsize(600,400)
    win.minsize(600,400)
    canvas=Canvas(win,width=450,height=400,bg='brown')
    canvas.grid(row=0,column=1)
    sidenav=Frame(win,width=150,height=400,bg='orange')
    sidenav.grid(row=0,column=0)
    bat=Bat(canvas)
    ball=Ball(canvas,bat)
    win.update()
    global is_paused
    is_paused=False
    Score=Label(win,text="Your score : "+str(score),fg='blue').place(x=500,y=20)
    def pause():
        global is_paused
        if is_paused:
            is_paused=False
        else:
            is_paused=True
    def myClick():
        while 1:
            if not is_paused:
                def moveLeft(event):
                    if not is_paused:
                        bat.moveLeft()
                def moveRight(event):
                    if not is_paused:
                        bat.moveRight()
                win.bind('<Left>',moveLeft)
                win.bind('<Right>',moveRight)
                if ball.hit_bottom==False:
                    ball.move(canvas)
                elif ball.hit_bottom==True:
                    end=Label(win,text="GameOver!",font=("Georgia",30)).place(x=280,y=180)
                    break
            win.update()
            time.sleep(0.05)
    s_button=Button(win,text="Start Game",command=myClick,fg="Green").place(x=50,y=150)
    p_button=Button(win,text="Pause Game",command=pause,fg="Red").place(x=50,y=180)
    r_button=Button(win,text="Restart",command=main).place(x=50,y=210)
main()
win.mainloop()

    
