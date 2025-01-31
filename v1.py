import math
import random
import pgzrun


#hero stats 
hero = Actor('hero_stand')
hero.x = 100
hero.y = 680
gravity = 5
score = 0
     
#enemies stats
enemy_1 = Actor('enemy_1_stand')
enemy_1.x = 100
enemy_1.y = 500

list_gem = []

WIDTH = 1280
HEIGHT = 720

#map generation 
tile_1 = Actor('tile_0161_ex_2',(320,704))
tile_2 = Actor('tile_0161_ex_2',(960,704))
tile_3 = Actor('tile_0161_ex')
list_coord = []
list_plataforms = []
valid_plataforms = [i for i in range(-320,321,1)]
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
    gem = Actor('tile_0062', (i[0] + + random.choice(valid_plataforms),i[1]- 16))
    list_plataforms.append(plataform)
    list_gem.append(gem)
            


def draw():   
    global list_plataforms
    screen.clear()
    
#characters
    hero.draw()
    enemy_1.draw()
    
    
#map
    tile_1.draw()
    tile_2.draw()
    for tile in list_plataforms:
        tile.draw()
    
    for gem in list_gem:
        gem.draw()
    



def update():
    global gravity
    global list_plataforms
    global score
    global list_gem


#limiters 
    if hero.x >= WIDTH:
        hero.x = 1230
        
    if hero.x <= 0:
        hero.x = 50
        
    if hero.y <= 0:
        hero.y = 670
        enemy_1.x = random.randint(10,1250)
        enemy_1.y = random.randint(10,680)
        random_platafoms()

        
#movements
    hero.y += gravity
    for tile in list_plataforms:
        if (keyboard.up and hero.colliderect(tile)) or (keyboard.up and hero.colliderect(tile_1)) or (keyboard.up and hero.colliderect(tile_2)):
            gravity = 3
            hero.y -= 100
            clock.schedule(set_stop, 0.3)
    for tile in list_plataforms:
        if hero.colliderect(tile):
            hero.y = tile.y - 32
            
    if hero.colliderect(tile_2):
        hero.y = tile_2.y - 32
        
    if hero.colliderect(tile_1):
        hero.y = tile_1.y - 32
        
    if keyboard.right:
        hero.image = 'hero_running_right'   
        hero.x = hero.x + 8
        clock.schedule(set_stop, 0.3)
        
    if keyboard.left:
        hero.image = 'hero_running_left'
        hero.x = hero.x - 8
        clock.schedule(set_stop, 0.3)
        
    
#collisions
    if hero.colliderect(enemy_1):
        hero.image = 'hero_falling'
    for gem in list_gem:
        if hero.colliderect(gem):
            gem.x = 3000
            gem.y = 3000
            score += 1
        



def set_stop():
    hero.image = 'hero_stand'

def random_platafoms():
    valid_plataforms = [i for i in range(-320,321,1)]
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
        

