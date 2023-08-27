#Sachi Bharwada 
#January 17th 2020
#A zelda like game where the chracter is fighting an enemy and defeat it in order to win the game

import pygame
import sys
import math
import pygame.transform 

pygame.init()

#these constants store how big the screen size is
WIDTH = 790
HEIGHT = 560

#this creates the graphics window 
game_window = pygame.display.set_mode((WIDTH, HEIGHT))

#colour constants
TEXT_COLOUR = (0, 0, 0)
TEXT2_COLOUR =(255, 255, 255)
WIN_COLOUR = (19, 11, 250)
LOSE_COLOUR = (240,10, 10)

#load the background image file
background_image = pygame.image.load("zeldabackground.png")
#blit the background to show on the game window
game_window.blit(background_image, (0, 0))

#load the sword image files
sword_up = pygame.image.load("swordback.png")
sword_down = pygame.image.load("swordfront.png")
sword_left = pygame.image.load("swordleft.png")
sword_right = pygame.image.load("swordright.png")

#attack variable set to determine whether character is attacking or not 
attack = False

#make variables for the sword's directions
sword_direction = 0
sword_direction_up = 0
sword_direction_down = 1
sword_direction_left = 2
sword_direction_right = 3

#load the character/player image files
character_front_image = pygame.image.load("zeldaback.png")
character_back_image = pygame.image.load("zeldafront.png")
character_left_image = pygame.image.load("zeldaleft.png")
character_right_image = pygame.image.load("zeldaright.png")
#set a variable to equal to one of the files
character_image = character_front_image

#load the dragon/enemy image file
dragon_image = pygame.image.load("zelda_dragon.png")

#make variables for the dragon's data
dragon_x = 370
dragon_y = 10
#store the dragon's health variable
dragon_health = 10
 
#load the fireball image file
fireball = pygame.image.load("fireball.png")

# New desired size
new_character_width = 35 
new_character_height = 35  
new_sword_width = 30
new_sword_height = 30
new_dragon_width = 100
new_dragon_height = 130
new_fireball_width = 30
new_fireball_height = 30

# Resize the images
character_front_image = pygame.transform.scale(character_front_image, (new_character_width, new_character_height))
character_back_image = pygame.transform.scale(character_back_image, (new_character_width, new_character_height))
character_left_image = pygame.transform.scale(character_left_image, (new_character_width, new_character_height))
character_right_image = pygame.transform.scale(character_right_image, (new_character_width, new_character_height))
sword_up = pygame.transform.scale(sword_up, (new_sword_width, new_sword_height))
sword_down = pygame.transform.scale(sword_down, (new_sword_width, new_sword_height))
sword_left = pygame.transform.scale(sword_left, (new_sword_width, new_sword_height))
sword_right = pygame.transform.scale(sword_right, (new_sword_width, new_sword_height))
dragon_image = pygame.transform.scale(dragon_image, (new_dragon_width, new_dragon_height))
fireball = pygame.transform.scale(fireball, (new_fireball_width, new_fireball_height))

#collison detection rectangle for the dragon
dragon_rect = dragon_image.get_rect()
#dragon's rectangle width and height variables
dragonW = dragon_rect.width
dragonH = dragon_rect.height

#rectangle for the sword left image 
sword_left_rect = sword_left.get_rect()
sword_leftW = sword_left_rect.width
sword_leftH = sword_left_rect.height

#rectangle for the sword right image 
sword_right_rect = sword_right.get_rect()
sword_rightW = sword_right_rect.width
sword_rightH = sword_right_rect.height

#rectangle for the sword up image 
sword_up_rect = sword_up.get_rect()
sword_upW = sword_up_rect.width
sword_upH = sword_up_rect.height

#rectangle for the sword down image
sword_down_rect = sword_down.get_rect()
sword_downW = sword_down_rect.width
sword_downH = sword_down_rect.height

#set game_loop to True for user to play game
game_loop = True

while game_loop:
    #make character direction variables 
    character_direction = 0
    character_up = 0
    character_down = 1
    character_left = 2
    character_right = 3
    #store the character's data
    character_x = 350
    character_y = 500
    character_x_speed = 4
    character_y_speed = 4
    #store the character's health
    character_health = 50

    #store the dragon's data
    dragon_x = 370
    dragon_y = 10
    #store the dragon's health
    dragon_health = 10

    #fireball data
    fireball_x_speed = 0
    fireball_y_speed = 0
    fireball_x = 0
    fireball_y = 0
    fireball_rise = 0
    fireball_run = 0
    fireball_hypotenuse = 0
    is_fired = False
    FIREBALL_SPEED = 6

    is_playing = False


    while True:
        #write and display instructions on screen
        font = pygame.font.SysFont("garamond", 24)
        instructions_graphics = font.render("Hello player! Welcome to the Zelda boss game!", True, TEXT_COLOUR)
        game_window.blit(instructions_graphics,(160, 240))
        instructions_graphics_2 = font.render("Use the WASD keys to move the player.", True, TEXT_COLOUR)
        game_window.blit(instructions_graphics_2,(160, 270))
        instructions_graphics_3 = font.render("Use the arrow keys to pull out your sword and attack.", True, TEXT_COLOUR)
        game_window.blit(instructions_graphics_3,(160, 300))
        instructions_graphics_4 = font.render("Press the space bar to continue to the game", True, TEXT_COLOUR)
        game_window.blit(instructions_graphics_4, (160, 330))
        #get user input
        pygame.event.get()
        #get keys that are pressed
        keys = pygame.key.get_pressed()
        #check if user presses space key, if so the user can begin playing game
        if keys[pygame.K_SPACE]:
            is_playing = True
            break
        #redraws all the graphics
        pygame.display.update()
        

    while is_playing:
        #get the rectangle of the character's image 
        character_image_rect = character_image.get_rect()
        character_imageW = character_image_rect.width
        character_imageH = character_image_rect.height
        
        #DO COLLISION DETECTION
        #create the bounding box for the character INSIDE the loop since it's moving
        #and need the current(x,y) location 
        character_image_rect = pygame.Rect( character_x, character_y,  character_imageW, character_imageH)

        #create the bounding boxes for the sword images INSIDE the loop since it's moving
        #and need the current(x,y) location 
        sword_left_rect  = pygame.Rect(character_x - 27, character_y + 7, sword_leftW, sword_leftH)
        sword_right_rect  = pygame.Rect(character_x + 23, character_y + 13, sword_leftW, sword_leftH)
        sword_up_rect  = pygame.Rect(character_x + 6, character_y - 30, sword_leftW, sword_leftH)
        sword_down_rect  = pygame.Rect(character_x + 6, character_y + 25, sword_leftW, sword_leftH)

        #create box for dragon image
        dragon_rect = pygame.Rect(dragon_x, dragon_y, dragonW, dragonH)

        #get the user input
        pygame.event.get()
        #get the list of all keys that were pressed
        keys = pygame.key.get_pressed()
        #figure out exactly which keys were pressed
        #character can move right when the D key is pressed
        if keys[pygame.K_d]:
            character_x = character_x + character_x_speed
            character_direction = character_right
            #no attack is made 
            attack = False
        #charcter can move left when A key is pressed
        if keys[pygame.K_a]:
            character_x = character_x - character_x_speed
            character_direction = character_left
            #no attack is made 
            attack = False
        #charcter can move up when W key is pressed
        if keys[pygame.K_w]:
            character_y = character_y - character_y_speed
            character_direction = character_up
            #no attack is made 
            attack = False
        #charcter can move down when S key is pressed
        if keys[pygame.K_s]:
            character_y = character_y + character_y_speed
            character_direction = character_down
            #no attack is made 
            attack = False
        #sword is pulled out to the right when right arrow key is pressed
        if keys[pygame.K_RIGHT]:
            character_direction = character_right
            #attack is made and sword is present
            attack = True
            if sword_right_rect.colliderect(dragon_rect):
                # subtract 1 from dragon health variable after attack
                dragon_health = dragon_health - 1
        #sword is pulled out to the left when left arrow key is pressed
        if keys[pygame.K_LEFT]:
            character_direction = character_left
            #attack is made and sword is present
            attack = True
            if sword_left_rect.colliderect(dragon_rect):
                # subtract 1 from dragon health variable after attack
                dragon_health = dragon_health - 1
        #sword is pulled out in front when up arrow key is pressed
        if keys[pygame.K_UP]:
            character_direction = character_up
            #attack is made and sword is present
            attack = True
            if sword_up_rect.colliderect(dragon_rect):
                # subtract 1 from dragon health variable after attack
                dragon_health = dragon_health - 1
        #sword is pulled out in back when down arrow key is pressed
        if keys[pygame.K_DOWN]:
            character_direction = character_down
            #attack is made and sword is present
            attack = True
            if sword_down_rect.colliderect(dragon_rect):
                # subtract 1 from dragon health variable after attack
                dragon_health = dragon_health - 1
        #character can exit the game when the escape key is pressed
        if keys [pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        #write the dragon's health on screen
        dragon_health_text = font.render("dragon health =" + str(dragon_health), True, TEXT2_COLOUR)

        #write the character's health on screen
        character_health_text = font.render("character health =" + str(character_health), True, TEXT2_COLOUR)
        
        #set the chracter direction to the given image 
        #make the character image variable set to all images 
        if character_direction == character_right:
            character_image = character_right_image
        elif character_direction == character_left:
            character_image = character_left_image
        elif character_direction == character_up:
            character_image = character_front_image
        elif character_direction == character_down:
            character_image = character_back_image
        
        #if the user is defeated by the dragon the game ends 
        if character_health == 0:
            break
        #if the user defeats the dragon the game ends
        if dragon_health == 0:
            break 
        
        #check if is_fired is false
        if is_fired == False:
       #if no fireball is on the screen set the fireball x and y values equal to the enemy's
            fireball_x = dragon_x
            fireball_y = dragon_y
            #the rise (vertical distance between character and dragon) for the fireball used for slope
            fireball_rise = character_y - dragon_y
            #run(horizontal distance between character and dragon) for slope
            fireball_run = character_x - dragon_x
            #use the Pythagorean theorem to fetrmine hypotenuse
            fireball_hypotenuse = math.sqrt(fireball_rise*fireball_rise + fireball_run*fireball_run)
            #fireball is ready to be fired, so is fired is True
            is_fired = True
            #calculate the fireball speed for x and y
            fireball_x_speed = (fireball_run/fireball_hypotenuse) * FIREBALL_SPEED
            fireball_y_speed = (fireball_rise/fireball_hypotenuse) * FIREBALL_SPEED
        #check to see if a fireball is fired
        if is_fired == True:
            #move the fireball diagonally
            fireball_x = fireball_x + fireball_x_speed 
            fireball_y = fireball_y + fireball_y_speed
            #if the fireball goes off the screen, fire it again
            if fireball_x < 0 or fireball_x > WIDTH or fireball_y < 0 or fireball_y > HEIGHT:
                is_fired = False
        #fireball rectangle
        fireball_rect = fireball.get_rect()
        fireballW = fireball_rect.width
        fireballH = fireball_rect.height
        #create bounding box for fireball
        fireball_rect = pygame.Rect(fireball_x, fireball_y, fireballW, fireballH) 
        #if fireball collides with character the character's health is subtraced by one
        if fireball_rect.colliderect(character_image_rect):
            character_health = character_health - 1
            #refire the fireball after collsion
            is_fired = False


        #set the character boundries
        #check if the character is going off the screen, so if the x value is less than 0
        if character_x < 0: 
            #set the x value to 0, so that it stops
            character_x = 0
        #the character can move left and right to the end of the screen
        elif character_x + character_imageW > (WIDTH):
            character_x = WIDTH - character_imageW
        #check if the character is going off the screen, so if the y value is less than 0
        elif character_y < 0:
            #set the y value to 0, so that it stops
            character_y = 0
        #the character can move up and down to the end of the screen
        elif character_y + character_imageH > (HEIGHT):
            character_y = HEIGHT - character_imageH
        
        #display the background image on screen
        game_window.blit(background_image, (0, 0))
        #display the dragon image on screen
        game_window.blit(dragon_image, (dragon_x, dragon_y))
        #display the fireball image on screen
        game_window.blit(fireball, (fireball_x, fireball_y))
        #display the character image on screen
        game_window.blit(character_image, (character_x, character_y))
        #display the dragon's health on screen
        game_window.blit(dragon_health_text,(20, 300))
        #display the character's health on screen 
        game_window.blit(character_health_text, (20, 350))
        
        #only pull right sword when the attack is True and character direction is right
        if character_direction == character_right and attack == True:
                game_window.blit(sword_right, (character_x + 23, character_y + 13))
        #only pull left sword when the attack is True and character direction is left
        elif character_direction == character_left and attack == True:
                game_window.blit(sword_left, (character_x - 27, character_y + 7))
        #only pull up sword when the attack is True and character direction is up
        elif character_direction == character_up and attack == True:
                game_window.blit(sword_up, (character_x + 6, character_y - 30))
        #only pull down sword when the attack is True and character direction is down
        elif character_direction == character_down and attack == True:
                game_window.blit(sword_down, (character_x + 6, character_y + 25))
        #redraws all the graphics
        pygame.display.update()

    while True:
        #if character is defeated 
        if character_health == 0:
            #screen will be background image
            game_window.blit(background_image, (0,0))
            #write a you lose message
            lose_font = pygame.font.SysFont("Courier New Bold ", 30)
            game_lost_text = lose_font.render("You have been burnt too much, you have lost.", True, LOSE_COLOUR)
            game_lost_text2 = lose_font.render("Press ENTER to restart or ESCAPE to exit.", True, LOSE_COLOUR)
            #display the lose message on screen
            game_window.blit(game_lost_text,(180, 250))
            game_window.blit(game_lost_text2,(180, 280))
            #get the user input
            pygame.event.get()
            #get the list of all keys that were pressed
            keys = pygame.key.get_pressed()
            #game loop is False so the game has stopped
            game_loop = False
            #if the user presses the RETURN key they can restart the game
            if keys [pygame.K_RETURN]:
                game_loop = True
                game_window.blit(background_image, (0,0))
                break
            #redraws all the graphics
            pygame.display.update()
            #if the user presses ESCAPE key they can exit the game
            if keys [pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

        #if character defeats the dragon
        if dragon_health == 0:
            #screen will be background image
           game_window.blit(background_image, (0,0))
            #write a you win message
           win_font = pygame.font.SysFont("Courier New Bold ", 30)
           game_won_text = win_font.render("You have defeated the dragon, you have won!", True, WIN_COLOUR)
           game_won_text2 = win_font.render("Press ENTER to restart or ESCAPE to exit.", True, WIN_COLOUR)
            #display the lose message on screen
           game_window.blit(game_won_text,(180, 250))
           game_window.blit(game_won_text2,(180, 280))
            #get the user input
           pygame.event.get()
            #get the list of all keys that were pressed
           keys = pygame.key.get_pressed()
            #game loop is False so the game has stopped
           game_loop = False
            #if the user presses the RETURN key they can restart the game
           if keys [pygame.K_RETURN]:
               game_loop = True
               game_window.blit(background_image, (0,0))
               break
            #redraws all the graphics
           pygame.display.update()
            #if the user presses ESCAPE key they can exit the game
           if keys [pygame.K_ESCAPE]:
               pygame.quit()
               sys.exit()
