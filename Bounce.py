from tkinter import *

import random

from time import sleep

tk = Tk()
tk.title("Bounce Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width= 500, height=500,bd = 0, highlightthickness = 0,bg="white")
canvas.pack()
tk.update()

class Ball:
    def __init__(self,canvas,paddle,color="red"):
        self.canvas = canvas
        self.paddle = paddle
        self.__id = canvas.create_oval(10,10,25,25,fill = color)
        self.canvas.move(self.__id,245,100)
        start = [-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False



    def draw(self):
        self.canvas.move(self.__id,self.x,self.y)
        pos = self.canvas.coords(self.__id)
        if pos[1] <= 0:
            self.y = 1
        if pos[0] <= 0:
            self.x = 1
        if pos[2] >= self.canvas_width:
            self.x = -2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            text = canvas.create_text(200,200,text="GAME OVER!!!",font=("Times",30),fill="red")
        if self.hit_paddle(pos) == True:
            self.y = -2


class Paddle:
    def __init__(self, canvas, color="blue"):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,15,fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <=0:
            self.x = 2
        if pos[2] > self.canvas_width:
            self.x = 0
        
    def turn_left(self,evt):
        self.x = -1

    def turn_right(self,evt):
        self.x = 1

paddle = Paddle(canvas,"green")
    
ball = Ball(canvas,paddle)


while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        tk.update_idletasks()
        tk.update()
        sleep(0.01)
    
