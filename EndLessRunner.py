
from curses import start_color
from random import randint
from time import sleep
import pygame
from sys import exit

import pygments 

#score system counting

def score_count () :
    global timer_count 
    timer_count = int(pygame.time.get_ticks()/500) - start_time
    score_surf = score.render(f"score : {timer_count}", True, "white")
    score_surf_rect = score_surf.get_rect(topleft = (0,0))
    screen.blit(score_surf,score_surf_rect)
    return score_surf

def bostacle_movement(enemy_list):
    if enemy_list :
        for enemy_rect in enemy_list :
            enemy_rect.x -= 5
            if enemy_rect.y == 250 : screen.blit(enemy,enemy_rect)
            else : screen.blit(fly_enemy,enemy_rect)
        enemy_list = [obs for obs in enemy_list if obs.x > -100]

        return enemy_list 
    else :
        return []  

def enemy_collision(main_player , enemy_rect_list) :
    if enemy_rect_list :       
        for enemy_rect in enemy_rect_list :
            if main_player.collidepoint(enemy_rect.bottomright) :
                return False
    return True

def main_player_animation() :
    global main_surf , main_index
    if main_surf_rect.bottom < 330 :
        main_surf = main_jump_resize
    else :
        main_index += 0.1
        if main_index > len(main_animation) : main_index = 0
        main_surf = main_animation[int(main_index)]



pygame.init()
screen = pygame.display.set_mode((800,400),pygame.RESIZABLE)
start_time = 0



#title of the screen
pygame.display.set_caption('Runner')
#change the icon of the game
game_icon = pygame.image.load('desktop102.ico').convert_alpha()
pygame.display.set_icon(game_icon)
#set a fixed framerate
clock = pygame.time.Clock()
#font object 
score = pygame.font.Font('Roboto-Thin.ttf',30)
restart = pygame.font.Font('Roboto-Thin.ttf',40)
#create sound
bg_sound = pygame.mixer.Sound('bg_sound.mp3')

#create normal surface 
sky = pygame.image.load('environment/sky.png').convert_alpha() 
sky_resize = pygame.transform.scale(sky, (800,300))

land = pygame.image.load('environment/land.png').convert_alpha()
land_resize = pygame.transform.scale(land, (800,400))

score_text = score.render(f'Score :',True,'white')
restart_text = restart.render('press Space to start ', True, '#ffffff')
game_name = restart.render("Pixel Runner" , True , '#ffffff')
#main character animation
main_surf1 = pygame.image.load("player_animation/st1.png").convert_alpha()
main_surf1_resize = pygame.transform.scale(main_surf1, (100,100))
main_surf2 = pygame.image.load("player_animation/st2.png").convert_alpha()
main_surf2_resize = pygame.transform.scale(main_surf2, (100,100))
main_surf3 = pygame.image.load("player_animation/st3.png").convert_alpha()
main_surf3_resize = pygame.transform.scale(main_surf3, (100,100))
main_surf4 = pygame.image.load("player_animation/st4.png").convert_alpha()
main_surf4_resize = pygame.transform.scale(main_surf4, (100,100))
main_surf5 = pygame.image.load("player_animation/st5.png").convert_alpha()
main_surf5_resize = pygame.transform.scale(main_surf5, (100,100))
main_animation = [main_surf1_resize, main_surf2_resize, main_surf3_resize, main_surf4_resize, main_surf5_resize]
main_index = 0
main_jump = pygame.image.load("jump.png").convert_alpha()
main_jump_resize = pygame.transform.scale(main_jump, (50,50))
main_surf = main_animation[main_index]

main_gravity = 0
bg_sound = pygame.mixer.Sound('bg_sound.mp3')
bg_sound.set_volume(.2)
jump_sound = pygame.mixer.Sound('jump_2.wav')

#land_enemy

enemy1 = pygame.image.load('land_enemy_animation/en1.png').convert_alpha()
enemy1_resize = pygame.transform.scale(enemy1, (60,60))
enemy2 = pygame.image.load('land_enemy_animation/en2.png').convert_alpha()
enemy2_resize = pygame.transform.scale(enemy2, (60,60))
enemy3 = pygame.image.load('land_enemy_animation/en3.png').convert_alpha()
enemy3_resize = pygame.transform.scale(enemy3, (60,60))
enemy4 = pygame.image.load('land_enemy_animation/en4.png').convert_alpha()
enemy4_resize = pygame.transform.scale(enemy4, (60,60))
enemy5 = pygame.image.load('land_enemy_animation/en5.png').convert_alpha()
enemy5_resize = pygame.transform.scale(enemy5, (60,60))
land_enemy_animation = [enemy1_resize, enemy2_resize, enemy3_resize, enemy4_resize, enemy5_resize]
land_enemy_index = 0
enemy = land_enemy_animation[land_enemy_index]

enemy_motion_2 = 570
#fly_enemy

fly_enemy1 = pygame.image.load('fly_enemy_animation/fly1.png')
fly_enemy1_resize = pygame.transform.scale(fly_enemy1, (60,60))
fly_enemy2 = pygame.image.load('fly_enemy_animation/fly2.png')
fly_enemy2_resize = pygame.transform.scale(fly_enemy2, (60,60))
fly_enemy3 = pygame.image.load('fly_enemy_animation/fly3.png')
fly_enemy3_resize = pygame.transform.scale(fly_enemy3, (60,60))
fly_enemy4 = pygame.image.load('fly_enemy_animation/fly4.png')
fly_enemy4_resize = pygame.transform.scale(fly_enemy4, (60,60))
fly_enemy5 = pygame.image.load('fly_enemy_animation/fly5.png')
fly_enemy5_resize = pygame.transform.scale(fly_enemy5, (60,60))
fly_enemy_animation = [fly_enemy1_resize, fly_enemy2_resize, fly_enemy3_resize, fly_enemy4_resize, fly_enemy5_resize]
fly_enemy_index = 0
fly_enemy = fly_enemy_animation[fly_enemy_index]


# rectangle area
main_surf_rect = main_surf.get_rect(topleft = (30,300))
score_rect = score_text.get_rect(midtop = (400,0))
restart_text_rect = restart_text.get_rect(center = (400,330))
game_name_rect = game_name.get_rect(center = (400, 50))


#timer UserEvent 
obstical_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstical_timer,1500)

#land_enemy_timer
enemy_timer = pygame.USEREVENT + 2
pygame.time.set_timer(enemy_timer, 300)

#fly_enemy_timer
fly_enemy_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_enemy_timer, 50)

game_active = True
timer_count = 0
enemy_rect_list = []

while True : 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
        if game_active :
            if event.type == pygame.MOUSEBUTTONUP :
                if main_surf_rect.collidepoint(event.pos) :
                    main_gravity = -20

            

            if event.type == obstical_timer :
                print(enemy_rect_list)
                if randint(0,2):
                    enemy_rect_list.append(enemy.get_rect(topleft = (randint(900,1100),250)))
                else : 
                    enemy_rect_list.append(fly_enemy.get_rect(topleft = (randint(900,1100),160)))
            
            if event.type == enemy_timer :
                if land_enemy_index == 0 : land_enemy_index = 1
                elif land_enemy_index == 1 : land_enemy_index = 2
                elif land_enemy_index == 2 : land_enemy_index = 3
                elif land_enemy_index == 3 : land_enemy_index = 4
                else : land_enemy_index = 0
                enemy = land_enemy_animation[land_enemy_index] 

            if event.type == fly_enemy_timer :
                if fly_enemy_index == 0 : fly_enemy_index = 1
                elif fly_enemy_index == 1 : fly_enemy_index = 2
                elif fly_enemy_index == 2 : fly_enemy_index = 3
                elif fly_enemy_index == 3 : fly_enemy_index = 4
                else : fly_enemy_index = 0
                fly_enemy = fly_enemy_animation[fly_enemy_index] 
            

            

            if event.type == pygame.KEYDOWN  :
                if event.key == pygame.K_SPACE :
                    if  main_surf_rect.bottom == 330 :
                        main_gravity = -20
                        #here play the jump sound
                        jump_sound.play()
        else :
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    game_active = True

    
    if game_active :
        

        bg_sound.play() 
        #but normal surface on the one and only display surface 
        screen.blit(sky_resize,(0,0))
        screen.blit(land_resize,(0,30))
        #pygame.draw.rect(screen,'#ff4488',score_rect,0,10)
        main_player_animation()
        #screen.blit(score_text,score_rect)
        screen.blit(main_surf, main_surf_rect)
        main_gravity += 1
        main_surf_rect.y += main_gravity
        if main_surf_rect.bottom >= 330 : main_surf_rect.bottom = 330
        
        
        score_1 = score_count ()

        #obstacle function call
        enemy_rect_list = bostacle_movement (enemy_rect_list)
        game_active = enemy_collision(main_surf_rect , enemy_rect_list)
    else :
        bg_sound.stop()
        sleep(1)
        screen.fill("#000000")
        screen.blit(game_name,game_name_rect)
        screen.blit(pygame.transform.rotozoom(main_jump_resize,0,1.5), (230,140))
        screen.blit(pygame.transform.rotozoom(enemy,0,1.8),(480,175))
        screen.blit(restart_text,restart_text_rect)
        start_time = int(pygame.time.get_ticks()/500)
        if timer_count != 0 : screen.blit(score_1,(335,190))
        enemy_rect_list.clear()
        main_surf_rect.topleft=(30,230)
        main_gravity = 0
            

    pygame.display.update()
    clock.tick(60)