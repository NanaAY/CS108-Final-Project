'''
This models the paddle for a game of Ping Pong
Created Spring 2018
Final Project
@author Nana Osei Asiedu Yirenkyi (na29)
'''

    
from helpers import *
from gui import *
import math

DAMPENING_FACTOR = 0.88 #HELPER CODE FROM LAB 12

class Ball:
    '''Models the ping pong ball to be rendered on the canvas'''
    
    def __init__(self, x = 50, y = 50, velX = 2.5, velY = 5, radius = 10, tag= 'Ball'):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._velX = velX
        self._velY = velY
        self._radius = radius
        self._color = 'gold'
        self._tag = tag
        
        
    def hits(self, other): #HELPER CODE FROM LAB 12
        if (self == other):
            # I can't collide with myself.
            return False
        else:
            # Determine if I overlap with the target particle.
            return (self._radius + other.get_radius()) >= distance(self._x, self._y, other.get_x(), other.get_y())
           
    
    def bounce(self, target): #HELPER CODE FROM LAB 12
        ''' This method modifies this Particle object's velocities based on its
            collision with the given target particle. It modifies both the magnitude
            and the direction of the velocities based on the interacting magnitude
            and direction of particles. It only changes the velocities of this
            object; an additional call to bounce() on the other particle is required
            to implement a complete bounce interaction.
         
            The collision algorithm is based on a similar algorithm published by K.
            Terzidis, Algorithms for Visual Design.
         
            target  the other particle
         '''
        if self.hits(target):
            angle = math.atan2(target.get_y() - self._y, target.get_x() - self._x)
            targetX = self._x + math.cos(angle) * (self._radius + target.get_radius())
            targetY = self._y + math.sin(angle) * (self._radius + target.get_radius())
            ax = targetX - target.get_x()
            ay = targetY - target.get_y()
            self._velX = (self._velX - ax) * DAMPENING_FACTOR
            self._velY = (self._velY - ay) * DAMPENING_FACTOR
            
    def hits_paddle(self, paddle): #HELPER CODE FROM LAB 12
#             if (self == paddle):
#                 # I can't collide with myself.
#                 return False
#             else:
                # Determine if I overlap with the target particle.
            return (self._radius + (paddle.get_height()) ) >= distance(self._x, self._y, paddle.get_x() + (paddle.get_width()/2), paddle.get_y() + (paddle.get_height()) )
        
     
    
    def bounce_paddle(self, target): #HELPER CODE FROM LAB 12
        if self.hits_paddle(target) and self._velY > 0:
            self._velY = -self._velY
        
            
        
        
            
    def render(self, canvas):
        '''A method that receives a canvas and uses the canvas as 
        instance variables to draw the ball'''
        
        canvas.create_oval(self._x - self._radius,
                           self._y - self._radius,
                           self._x + self._radius,
                           self._y + self._radius,
                           fill = self._color)
        
        
    def move(self, canvas):
        '''This method updates the x and y coordinates 
        of the balls according to their velocities'''
        
        self._x += self._velX
        self._y += self._velY
        
        if ( (self._x + self._radius > canvas.winfo_reqwidth() and self._velX > 0)
              or (self._x - self._radius < 0 and self._velX < 0) ):
            self._velX = -self._velX
            
             
#         elif ( (self._y + self._radius > 775 and self._velY > 0)
#               or  (self._y - self._radius < 0 and self._velY < 0) ):
#             self._velY = -self._velY
    
    def remove_ball(self, balls_list):
        ''''''
        for ball in list:
            if ( (self._y + self._radius > 800 and self._velY > 0)
              or  (self._y - self._radius < 0 and self._velY < 0) ):
                balls_list.remove(ball)
                
    
    def score_count1(self):
        player1 = 0
        if  (self._y + self._radius > 800 and self._velY > 0):
            player1 += 1
            return player1
            
    def score_count2(self):
        player2 = 0
        if  (self._y - self._radius < 0 and self._velY < 0):
            player2 += 1
        
        
    def winner(self):
        winner_text = ''
        if self.score_count1 > 10:
            winner_text = 'Player 1 Wins!!'
            
        elif self.score_count2 > 10:
            winner_text = 'Player 2 Wins!!'
            
        return winner_text
            

        
        
            
            
            
        
        
             
            
    def get_x(self):
        '''Accesses and returns the x coordinate of the ball'''
        return self._x
    
    def get_y(self):
        '''Accesses and returns the y coordinate of the ball'''
        return self._y
    
    def get_radius(self):
        '''Accesses and returns the radius of the ball'''
        return self._radius
    
    def get_velY(self):
        '''Accesses and returns the velocity of the ball'''
        return self._velY
    
    def get_velX(self):
        '''Accesses and returns the velocity of the ball'''
        return self._velX
    
    def set_velX(self, newval):
        ''''Assigns the velocity to a new value'''
        self._velX = newval
        
    def set_velY(self, newval):
        '''Assigns the velocity to a new value'''
        self._velY = newval
    
#     def set_velocity(self, new_velY):
#         '''sets the velocity of the ball to the new values passed in'''
#         self._velY = new_velY
        
    
class Paddle:
    '''Models the paddle to be rendered on the canvas'''
    
    def __init__(self, x=325, y=775, width=150, height=20, velocity=40, color= 'red', tag= 'Paddle'):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._velocity = velocity
        self._color = color
        self._tag = tag
        
        
    def render(self, canvas):
        '''A method that receives a canvas and uses the canvas as 
    instance variables to draw the paddle'''
        
        canvas.create_rectangle(self._x,
                                self._y,
                                self._x + self._width,
                                self._y + self._height,
                                outline = 'black',
                                fill= self._color)
        
        
        
    def move_left(self, canvas):
        '''This method moves the paddles left by updating their x coordinates 
     according to their velocities'''
        
        if self._x  >= 10:
            self._x -= self._velocity  
        
        
    def move_right(self, canvas):
        '''This method moves the paddles right by updating their x coordinates 
     according to their velocities'''
        
        if self._x + self._width <= canvas.winfo_reqwidth()-12:
            self._x += self._velocity
        
        
    def get_x(self):
        '''Accesses and returns the x coordinate of the Paddle'''
        return self._x
    
    def get_y(self):
        '''Accesses and returns the y coordinates of the Paddle'''
        return self._y
    
    def get_width(self):
        '''Accesses and returns the width of the Paddle'''
        return self._width
    
    def get_height(self):
        '''Accesses and returns the height of the Paddle'''
        return self._height
    
    def get_velocity(self):
        '''Accesses and returns the velocity of the Paddle'''
        return self._velocity
    
    def set_velocity(self, newvel):
        '''Assigns the velocity to a new value'''
        self._velocity = newvel
        
            
            
            
            
            
            