'''
Graphical User Interface for the Kingpong game
Created Spring 2018
Final Project
@author Nana Osei Asiedu Yirenkyi (na29)
'''

from tkinter import *
from random import randint
from kingpong import *
from helpers import *


class Gui:
    '''The Graphical User Interface'''
    
    def __init__(self, window): 
        '''Constructor for the game simulator'''
        self.window = window
        self._frame_1 = Frame(self.window)
        self._photo = PhotoImage(file='pong.gif')
        self._show_page_1()
        
        
    def _show_page_1(self):
        self.width = 400
        self.canvas1 = Canvas(self._frame_1, 
                             width= self.width, height= self.width)
        self.canvas1.create_image(0, 0, image=self._photo, anchor=NW)
        self.canvas1.pack()
        Label(self._frame_1, text="Welcome to KingPong by na29").pack()
        Button(self._frame_1, text="Instructions", command=self._show_page_2).pack(side= BOTTOM)
        Button(self._frame_1, text="Start", command=self._show_page_3).pack(side= BOTTOM)
        self._frame_1.pack()
        
    def _show_page_2(self):
        
        # unpack frame 1 and show frame 2
        self._frame_2 = Frame(self.window)
        self.width = 400
        self.canvas1 = Canvas(self._frame_2, 
                             width= self.width, height= self.width)
        self.canvas1.create_image(0, 0, image=self._photo, anchor=NW)
        self.canvas1.pack()
        Label(self._frame_2, text="For Player 1(Red Paddle), use left and right arrow\nkeys to move the paddle.\nFor Player 2(Blue Paddle), use the x and z keys to move the paddle. ").pack()
        Button(self._frame_2, text="Start", command=self._show_page_3).pack(side= BOTTOM)
        # remove frame 1 with its label and button
        self._frame_1.pack_forget()
        # show frame 2 with its label and button
        self._frame_2.pack()
       
        
    def _show_page_3(self): 
        # remove frame 1 with its label and button

        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self.width = 800
        self.canvas = Canvas(self.window, bg= 'dark green', 
                             width= self.width, height= self.width)
        self.canvas.pack()
        self.terminated = False
        self.ball_list = []
        self.paddle1 = Paddle(tag='Paddle1')
        self.paddle2 = Paddle(325, 10, color= 'blue', tag='Paddle2')
        self.render_ball()
        self.render_paddle()
        
        
        
        
        
        difficulty_btn = Button(self.window, text='Difficulty', command=self.difficulty)
        difficulty_btn.pack()
        
        speed_btn = Button(self.window, text='Speed', command=self.speed)
        speed_btn.pack()
        
        start_btn = Button(self.window, text='Start Game', command=self.start_game)
        start_btn.pack()
        
        player1_label = Label(self.window, text= 'Player1:')
        player1_label.pack(side= LEFT)
        
        player2_label = Label(self.window, text= 'Player2:')
        player2_label.pack(side= RIGHT)
        
#         self.score1 = 
        
        self.canvas.bind('<Key-Left>', self.paddle1_left)
        self.canvas.bind('<Key-Right>', self.paddle1_right)
        self.canvas.bind('<Key-z>', self.paddle2_left)
        self.canvas.bind('<Key-x>', self.paddle2_right)
        self.canvas.focus_set()
        
        # remove frame 1 with its label and button
        self._frame_1.pack_forget()
        self._frame_2.pack_forget()
        
        
    def render_ball(self):
        '''This method makes the ball appear to move around the screen'''
        
        if self.terminated == False:
            self.canvas.delete('Ball') #MIGHT WANT TO DELETE ONLY BALL
            for ball in self.ball_list:
                ball.move(self.canvas)
                ball.render(self.canvas)
                ball.bounce_paddle(self.paddle1)
                ball.bounce_paddle(self.paddle2)
                for ball2 in self.ball_list:
                    ball.bounce(ball2)
            self.canvas.after(2, self.render_ball)
            
            
#     def hit_paddle(self):
#             for ball in self.ball_list:
#                 ball.bounce_paddle(self.paddle1)
#                 ball.bounce_paddle(self.paddle2)
            
    def render_paddle(self):
        '''This method makes the kingpong appear to move around the screen'''
         
        if self.terminated == False:
            self.canvas.delete(ALL) #MIGHT WANT TO DELETE ONLY PADDLE
            self.paddle1.render(self.canvas)
            self.paddle2.render(self.canvas)
        self.canvas.after(1, self.render_paddle)
        
        
    def paddle1_left(self, event):
        '''This method moves paddle1 left'''
        self.paddle1.move_left(self.canvas)
        
            
    def paddle1_right(self, event):
        '''This method moves paddle1 right'''
        self.paddle1.move_right(self.canvas)
        
    def paddle2_left(self, event):
        '''This method moves paddle2 left'''
        self.paddle2.move_left(self.canvas)
        
            
    def paddle2_right(self, event):
        '''This method moves paddle2 right'''
        self.paddle2.move_right(self.canvas)
        
    def remove_ball(self):
        '''This method removes any ball that goes out of the canvas'''
        self.remove_ball(self.ball_list)
        

    def speed(self):
        '''This method increases the velocity of the ball ball when the speed button is clicked'''
        for ball in self.ball_list:
            ball._velX += 5
            ball._velY += 5
        
    
            
    def difficulty(self):
        '''This method adds a new ball when the difficulty button is clicked'''
        new_ball = Ball(randint(0,self.width), randint(0,self.width))
        self.ball_list.append(new_ball)
        
    
    def start_game(self):
        '''This method starts the game with a new ball when the start button is clicked'''
        new_ball = Ball()
        self.ball_list.append(new_ball)
          
            
    def safe_exit(self):
        ''' Turn off the event loop before closing the GUI '''
        self.terminated = True
        self.window.destroy()
            
            
            
            
            
if __name__ == '__main__':
    root = Tk()
    root.title('King Pong')    
    app = Gui(root)
    root.mainloop()
        
        
        
        
        
        