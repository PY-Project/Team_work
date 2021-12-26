''' The is the main file of our Project '''

import pygame
import os
from pygame.locals import *
from random import randint

# Initalize the Game Window
pygame.init()

clock = pygame.time.Clock()
fps = 60 # frame per Second

# define font
font  = pygame.font.SysFont('Bauhaus 93',50)

# define color
color = (255,12,12)

# Initalize the dimensions of the Window
screen_width = 864
screen_height = 777

# create the Screen (window) of the Game
screen = pygame.display.set_mode((screen_width,screen_height))

# Set Caption to the Window
pygame.display.set_caption('FlappyBird')

'''load images''' 

# background_image 
bg = pygame.image.load('images\bg.png') 

# Scrolling_ground_img
ground_img = pygame.image.load('images\ground.png') 

# Restart button_image
restart_button = pygame.image.load('images\restart.png')

# Exit button_image
exit_button = pygame.image.load('images\exit.png')

# define Game Variables
ground_scroll = 0
scroll_speed = 8
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 700 # milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

'''Game Function'''

# score function 
def draw_text (text,font,text_col,x,y):

    ''' this function to draw score on the screen'''

    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

# check score 
def check_score(bird_group,pipe_group):

    ''' this function to check the score'''
    global pass_pipe

    if len(pipe_group):
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
            and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
            and not pass_pipe:
            pass_pipe = True

    _pass()

# check Passing the pipe
def _pass():

    ''' this function to chek if the flappy pass the pipe or not'''
    global pass_pipe , score
    if pass_pipe:

        try:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score+=1
                pass_pipe = False
        except IndexError:
            pass

# collision between flappy_bird and pipe
def check_collision (bird_group,pipe_group,flappy):

    '''This function to check collisoin between 
    the flappy and (the pipe or the top of the screen)
    '''
    global game_over , score 
    if pygame.sprite.groupcollide(bird_group,pipe_group,False,False)\
        or flappy.rect.top < 0:
        # flappy.rect.top < 0 (means he crached the top of the screen)
        game_over = True
        new_score = read_score()
        write_score(max(score,new_score))

# check_scroll function:
def check_scroll():

    '''This function to check on the scroll ground
    we have about 24 hash in the Scrolling_ground_img so we need to
    return the ground_scroll to start from zero when it exceeds the width 
    between two hashes to repeat the operation while the image is displayed
    width between two hashes =  (screen_width/number of hashes) = (864/24) = 36
    '''
    global ground_scroll
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 36 :
        ground_scroll = 0

# check if bird has hit the ground
def hit_ground(flappy):

    global game_over,flying
    '''This function to check if flappy hit the ground'''

    if flappy.rect.bottom >= 650:
        game_over = True
        flying = False 

# game_over function
def Game_Over():

    """This function to check contntinuity of the Whole Game"""

    global flying,last_pipe,game_over,pipe_frequency

    if not game_over and flying == True:

        # generate new pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            # instantiate an object from Pipe
            pipe_height = randint(-100,100)
            btm_pipe = Pipe(screen_width,screen_height//2+pipe_height,1)
            top_pipe = Pipe(screen_width,screen_height//2+pipe_height,-1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

        # check Scroll function
        check_scroll()
        pipe_group.update()

    elif game_over == True:

        if reset_button.draw_restart_button():
            game_over = False
            reset_game()

        quit_button.draw_quit_button()

# restrat function
def reset_game():

    global score
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = screen_height//2
    score = 0

# quit Game
def quit_game():

    pygame.quit()

'''Game Classes'''

# Bird Class
class Bird(pygame.sprite.Sprite):

    '''Creating the bird class'''

    def __init__(self,x,y):

        '''building Bird Constructor'''
        pygame.sprite.Sprite.__init__(self) # inherit some functionality (from pygame.sprite.Sprite) class
        self.images = []
        self.index = 0
        self.counter = 0

        # fill the list with all bird images for animation
        for num in range(1,4):
            img =  pygame.image.load(f'bird{num}.png')
            self.images.append(img)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0 # velocity
        self.clicked = False

    # update the animation of the bird wings
    def update(self):

        '''handle the animation'''

        # gravity
        if flying:
            self.vel += 0.5
            if self.vel>8:
                self.vel = 8
            if self.rect.bottom < 650:
                self.rect.y += int(self.vel)

        if not game_over:
            # jump 
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
                self.vel = -10
                self.clicked = True

            if pygame.mouse.get_pressed()[0]==0 :
                self.clicked = False

            self.counter += 1
            flapp_cooldown = 5

            if self.counter > flapp_cooldown:
                self.counter = 0
                self.index+=1
                if self.index>=len(self.images):
                    self.index = 0

            self.image = self.images[self.index]

            # rotate the bird
            self.image = pygame.transform.rotate(self.images[self.index],self.vel*-2)

        else:
            self.image = pygame.transform.rotate(self.images[self.index],-90)

# pipe Class
class Pipe(pygame.sprite.Sprite):

    '''Creating the Pipe class'''

    def __init__(self,x,y,position):

        '''building Pipe Constructor'''

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images\pipe.png')
        self.rect = self.image.get_rect()

        # position 1 means from top , -1 from bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = [x,y-pipe_gap//2]

        if position == -1:
            self.rect.topleft = [x,y+pipe_gap//2]

    # update pipe position (move it to left) 
    def update(self):
        '''This function to update pipe position'''
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()

# Restart Button Class
class Button():

    ''''Creating the bird class'''
    def __init__(self,x,y,image):

        '''building restart button Constructor'''

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    # draw restart button on the screen
    def draw_restart_button(self):

        '''This method to draw restart button on the screen'''

        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()
        # check if mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                action = True

        screen.blit(self.image,(self.rect.x,self.rect.y))

        return action

    # draw quit button on the screen
    def draw_quit_button(self):

        '''This method to draw quit button on the screen'''

        global run 

        # get mouse position
        pos = pygame.mouse.get_pos()
        # check if mouse is over the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                run = False

        screen.blit(self.image,(self.rect.x,self.rect.y))

# appending_high_score_function
def write_score(high_score):

    '''This function to append high_score in the file'''

    score_file = open('score.txt','w')
    score_file.write(f'{high_score}\n')
    score_file.close()

# reading_high_score_function
def read_score():

    '''This function to read high_score in the file'''

    score_file = open('score.txt','r')
    new = score_file.read()
    score_file.close()
    return int(new)

if os.path.exists('score.txt'):
    pass

else:
    write_score(0)


# instantiate an object from Bird
flappy = Bird(100,screen_height//2)
bird_group = pygame.sprite.Group()
bird_group.add(flappy)

pipe_group = pygame.sprite.Group()

# create restart button instance 
reset_button = Button(screen_width//2-200,screen_height//2-100,restart_button)
# create quit button instance 
quit_button = Button(screen_width//2+100,screen_height//2-100,exit_button)

run = True

while run: 

    # controll the speed of scrolling_ground_img 
    clock.tick(fps)

    # Show the background image on the Screen from position(0,0)
    screen.blit(bg,(0,0))

    # Show the bird object on the screen
    bird_group.draw(screen)

    # animate the bird wings
    bird_group.update()

    # Show the pipe object on the screen
    pipe_group.draw(screen)

    # Show and scrolling the ground image on the 
    # Screen from position(0,height of the bg image)
    screen.blit(ground_img,(ground_scroll,650))

    # Score check
    check_score(bird_group,pipe_group)

    # this function to draw score on the screen
    draw_text(str(score),font,color,screen_width//2-50,20)
    best = read_score()
    draw_text(f'Best {best}',font,color,screen_width-200,20)

    # collision between flappy_bird and pipe
    check_collision (bird_group,pipe_group,flappy)

    # check if bird has hit the ground
    hit_ground(flappy)

    # check for game_over and reset
    Game_Over()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN\
            and flying == False and game_over == False:

            flying = True 

    # To Continue showing each object on the screen
    pygame.display.update()


pygame.quit()
