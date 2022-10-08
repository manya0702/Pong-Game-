'''1. IMPORT MODULES'''

import pygame,sys,random

''' BALL ANIMATION FUNCTION'''

def ball_animation():
    global ball_speed_x, ball_speed_y,player_score,opponent_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score+=1
        ball_restart()

    if ball.right >= screen_width:
        opponent_score+=1
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

''' PLAYER ANIMATION FUNCTION'''

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom =  screen_height 
        

''' OPPONENT ANIMATION FUNCTION'''

def opponent_animation():

    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom =  screen_height


''' BALL RESTART FUNCTION'''

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center =  (screen_width/2, screen_height/2)
   
    ball_speed_y *= random.choice((-1,1))
    ball_speed_x *= random.choice((-1,1))


''' 2. INITIALISE PYGAME'''

pygame.init()
clock = pygame.time.Clock()


'''3. CREATING A SCREEN OBJECT '''

screen_width = 1200 
screen_height = 900 

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

'''4. CREATING THE GAME COMPONENTS'''

ball = pygame.Rect(screen_width/2 -15, screen_height/2 - 15, 30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70,10,140)


'''5. COLOR INITIALISATION'''

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

'''9. INITIALISING SPEED VARIABLES'''

ball_speed_x = 5 * random.choice((-1,1))
ball_speed_y = 5 * random.choice((-1,1))
player_speed = 0
opponent_speed = 7

''' 11. INITIALISING SCORE VARIABLES AND FONT '''

player_score = 0
opponent_score = 0
game_font  =  pygame.font.Font("freesans.ttf",32)

''' 6. RUNNING A LOOP '''

while True:  # updates the game
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit() 

        ''' 8. ADDING ANIMATION TO THE RECTANGLES'''

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN: 
                player_speed += 7
            if event.key == pygame.K_UP: 
                player_speed -= 7

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN: 
                player_speed -= 7

        '''10. ANIMATION FUNCTIONS'''

    ball_animation()
    player_animation()
    opponent_animation()
        
# 7. DRAWING OBJECTS 

    screen.fill(bg_color) 
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball) 
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height)) 

# 12. TEXT RENDERING 

    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text,(620,440)) 

    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text,(560,440)) 

# 6. DISPLAYING ALL THE LOOP COMPONENTS 

    pygame.display.flip() 
    clock.tick(60)  
