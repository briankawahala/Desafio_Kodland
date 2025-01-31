import math
import random
import pgzrun
from pgzhelper import *


#hero variables 
hero = Actor('hero_stand')

hero.x = 100
hero.y = 680
invincibility = True
     
#enemies variables
enemy_1 = Actor('enemy_1_stand')
enemy_1.images = ['enemy_1_stand','enemy_1_moving','enemy_1_moving_right', 'enemy_1_moving_left']
enemy_1.x = 100
enemy_1.y = 500
movement_enemy_1 = True

enemy_2 = Actor('enemy_2_stand')
enemy_2.images = ['enemy_2_stand','enemy_2_moving','enemy_2_moving_right', 'enemy_2_moving_left']
enemy_2.x = 200
enemy_2.y = 660
movement_enemy_2 = True

#game variables
music.play('music')
gravity = 2
jump = 0
background_music = True
score = 0
list_gem = []
game_start = True

box_start_menu = Actor('start_menu', (640,220))
box_start_music = Actor('music_menu', (640,320))
box_start_exit = Actor('exit_menu', (640,420))
game_over = False


WIDTH = 1280
HEIGHT = 720


#map variables 
tile_1 = Actor('tile_0161_ex_2',(320,704))
tile_2 = Actor('tile_0161_ex_2',(960,704))
tile_3 = Actor('tile_0161_ex')
list_coord = []
list_plataforms = []
valid_plataforms = [i for i in range(-320,321,320)]
first_plataform = [i for i in range(160,1121,1)]
tile_3.x = random.choice(first_plataform)
tile_3.y = 630  
list_coord.append((tile_3.x, tile_3.y ))
i = 1 
while True:
    if i == 7:
        break 
    tile_3.x = int(tile_3.x + random.choice(valid_plataforms))
    while tile_3.x <= 0 or tile_3.x >= WIDTH:
        tile_3.x = int(tile_3.x + random.choice(valid_plataforms))
        
    tile_3.y = int(630 - i*100)
    list_coord.append((tile_3.x, tile_3.y ))
    i += 1
for i in list_coord:
    plataform = Actor('hxg76-c9cfm', (i[0],i[1]))
    gem = Actor('tile_0062', (i[0] + random.choice(valid_plataforms),i[1]- 16))
    list_plataforms.append(plataform)
    list_gem.append(gem)
     
     
            
def update():
    global game_over, game_start, list_gem, list_plataforms, gravity, jump, background_music, score, movement_enemy_1, invincibility
    
#limiters 
    if hero.x >= WIDTH:
        hero.x = 1230
        
    if hero.x <= 0:
        hero.x = 50
        
    if hero.y >= 680:
        jump = 0
        hero.y = 680
        
    if hero.y <= 0:
        score += 5
        hero.y = 680
        enemy_1.x = random.randint(10,1250)
        enemy_1.y = 500
        coordx_enemy_1 = enemy_1.x
        random_platafoms()

        
#movements
    hero.y += gravity
    for tile in list_plataforms:
        if (keyboard.up and hero.colliderect(tile)) or (keyboard.up and hero.colliderect(tile_1)) or (keyboard.up and hero.colliderect(tile_2)):
            gravity = 3
            hero.y -= 100
            #clock.schedule(set_stop, 0.3)
    for tile in list_plataforms:
        if hero.colliderect(tile):
            hero.y = tile.y - 32
            
    if hero.colliderect(tile_2):
        hero.y = tile_2.y - 32
        
    if hero.colliderect(tile_1):
        hero.y = tile_1.y - 32
    
    if keyboard.right:
        hero.images = ['hero_running_right_1', 'hero_running_right_1', 'hero_running_right_1']
        hero.animate()
        hero.angle = 0
        hero.flip_y = False
        hero.move_forward(8)
        clock.schedule(set_stop, 0.3)
        
    if keyboard.left:
        hero.images = ['hero_running_right_1', 'hero_running_right_1', 'hero_running_right_1']
        hero.next_image()
        hero.angle = 180
        hero.flip_y = True
        hero.move_forward(8)
        clock.schedule(set_stop, 0.3)
        
#enemy movement
    enemy_1.animate()
    enemy_1_move_()
        
    enemy_2.animate()
    enemy_2_movement()
        
#collisions
    if invincibility == False:
        if hero.colliderect(enemy_1):
            hero.image = 'hero_falling'
            game_over = True
        if hero.colliderect(enemy_2):
            hero.image = 'hero_falling'
            game_over = True
        for gem in list_gem:
            if hero.colliderect(gem):
                if background_music == True:
                    sounds.gem.play()
                gem.x = 3000
                gem.y = 3000
                score += 1



def draw():
    global invincibility
    if game_over:
        screen.fill((128, 0, 0))
        screen.draw.text ('Game Over', centerx = 640, centery = 320, color = ('black'), fontsize = 80)
        box_start_exit.x = 640
        box_start_exit.y = 400
        box_start_exit.draw()
        music.stop()
        
    else:
        if game_start:
            screen.fill((128, 0, 0))
            box_start_menu.draw()
            box_start_music.draw()
            box_start_exit.draw()
        else:
            invincibility = False
            box_start_menu.x = 3000
            box_start_menu.y = 3000
            box_start_music.x = 3000
            box_start_music.y = 3000
            box_start_exit.x = 3000
            box_start_exit.y = 3000
            
            
            
            screen.clear()
            screen.draw.text('Score ' + str(score), (15,10), color = (255, 255, 255), fontsize = 15)
            hero.draw()
            enemy_1.draw()
            enemy_2.draw()
    #map
            tile_1.draw()
            tile_2.draw()
            for tile in list_plataforms:
                tile.draw()
                
            for gem in list_gem:
                gem.draw()



def set_stop():
    hero.image = 'hero_stand'

def on_mouse_down(pos, button):
    global background_music, game_start
    if button == mouse.LEFT and box_start_menu.collidepoint(pos):
        game_start = False
    if button == mouse.LEFT and box_start_music.collidepoint(pos):
        if background_music == True:
            music.stop()
            background_music = False
            
        else:
            background_music = True
            music.play('music')
    if button == mouse.LEFT and box_start_exit.collidepoint(pos):
            exit()

def random_platafoms():
    valid_plataforms = [i for i in range(-320,321,320)]
    first_plataform = [i for i in range(160,1121,1)]
    list_plataforms[0].x = int(random.choice(first_plataform))
    list_plataforms[0].Y = 630
    i = 1
    while True:
        if i == 7:
            break 
        list_plataforms[i].x = int(list_plataforms[i-1].x + random.choice(valid_plataforms))
        while list_plataforms[i].x <= 0 or list_plataforms[i].x >= WIDTH:
            list_plataforms[i].x = int(list_plataforms[i-1].x + random.choice(valid_plataforms))
        list_plataforms[i].y = int(630 - i*100)
        list_gem[i].x = list_plataforms[i].x + random.choice(valid_plataforms)
        list_gem[i].y = list_plataforms[i].y - 16
        i += 1

def enemy_1_move_():
    global movement_enemy_1
    if enemy_1.y > 100 and movement_enemy_1:
        enemy_1.y -= 5
    elif enemy_1.y == 100:
        movement_enemy_1 = False
        enemy_1.y += 5
    elif enemy_1.y <500 and not movement_enemy_1:
        enemy_1.y += 5
    elif enemy_1.y == 500:
        movement_enemy_1 = True
        enemy_1.y -= 5
    

def enemy_2_movement():
    global movement_enemy_2
    if enemy_2.x < 1280 and movement_enemy_2:
        enemy_2.x += 2
        
    elif enemy_2.x == 1280:
        enemy_2.x -= 2
        movement_enemy_2 = False
        
    elif enemy_2.x > 0 and not movement_enemy_2:
        enemy_2.x -= 2
        
    elif enemy_2.x == 0:
        enemy_2.x -= 2
        movement_enemy_2 = True
