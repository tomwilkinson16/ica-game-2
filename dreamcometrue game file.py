#Tom Wilkinson
#Game 2 - Dream Come True
#14/04/2021


#Importing from Pygame and Folders
from imagesnsounds import *
from pygame.locals import *
from world_data import *
from gamestuff import *

'''This is the starting screen when entering the game'''
def game_intro():
    intro = True
    start_button = Button(420 , SCREEN_HEIGHT -350, start_img)
    rules_button = Button (420 , SCREEN_HEIGHT -250, rules_img)

    while intro:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
        # checking to see if the player closes the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                # if the player quits the running while loop is set false 
                
           
        WINDOW.fill(WHITE)
        WINDOW.blit(background,(0,0))
        draw_text('Dream Come True?', fontbig, WHITE, 250, 7) # Display FPS
        if start_button.draw():
            Game()
        if rules_button.draw():
            Rules()
        pygame.display.update()


'''The pause function is there to stop the game in its tracks'''
def Pause():
    paused = True
    restart_button = Button(400, 300, restart_img)
    quit_button = Button(700,  300, quit_img)
    resume_button = Button(100, 300, resume_img)
    while paused:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            # checking to see if the player closes the window 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
                               
        WINDOW.fill(WHITE)
        WINDOW.blit(background,(0,0))
        draw_text('Dream Come True?', fontbig, WHITE, 250, 7) # Display game title
        if resume_button.draw():
            paused = False
        if restart_button.draw():
            Game()
        if quit_button.draw():
            game_intro()
        pygame.display.update()



'''The rules will be displayed if the player presses the rules button'''
def Rules():
    intro = True
    while intro:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
        # checking to see if the player closes the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        WINDOW.fill(WHITE)
        WINDOW.blit(background,(0,0))
        draw_text('Dream Come True?', fontbig, WHITE, 250, 7) # display game title
        draw_text('Press W to initialise JETPACK', font, WHITE, 75, 125) # Display FPS
        draw_text('CAUTION: Keep an eye on your jetpack fuel which will deplete when', font, WHITE, 75, 175) # Display FPS
        draw_text('in use. Your jetpack fuel will recharge when landing on a platform.', font, WHITE, 75, 200) # Display FPS
        draw_text('Press D to move RIGHT and Press A to move LEFT', font, WHITE, 75, 250) # Display FPS
        draw_text('You have 60 seconds:', font, WHITE, 75, 300) # Display FPS
        draw_text('Collect as many points as possible by killing aliens and eating', font, WHITE, 75, 325) # Display FPS
        draw_text('doughnuts before your time runs out.', font, WHITE, 75, 350) # Display FPS
        draw_text('SURVIVE!!', fontbig, WHITE, 345, 450) # Display FPS15       
        back_button = Button (SCREEN_WIDTH - 165, SCREEN_HEIGHT -50, back_img)

        if back_button.draw():
            game_intro()
        pygame.display.update()

'''This is the Main Game and inside is the game loop'''
def Game():
    #game variables
    tile_size = 50
    countdown = 60
    last_count = pygame.time.get_ticks()


    #sprite groups
    player_sprite = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    alien_group = pygame.sprite.Group()
    spike_group = pygame.sprite.Group()
    snack_group = pygame.sprite.Group()

    class World ():
            def __init__(self, data):
                #load the img
                pygame.sprite.Sprite.__init__(self)
                self.tile_list = []
                tile_size = 50
                platform = pygame.image.load('png/Tiles/platform2.png')
                barrel = pygame.image.load('png/Objects/Barrel (2).png')
                alien = pygame.image.load ('img/newalien.png')
                alien = alien.set_colorkey(BLACK)
                row_count = 0 
                for row in data:
                    col_count = 0
                    for tile in row:
                        if tile == 1:
                            image = pygame.transform.scale(platform, (tile_size , tile_size//2))
                            image_rect = image.get_rect()
                            image_rect.x = col_count * tile_size
                            image_rect.y = row_count * tile_size
                            tile = (image, image_rect)
                            self.tile_list.append(tile)
                        if tile == 2:
                            spike = Spike(col_count * tile_size, row_count * tile_size + (tile_size//2))
                            spike_group.add(spike)
                        if tile == 3:
                            snack = Snack(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                            snack_group.add(snack)
                        if tile == 4:
                            alien = Enemy(col_count * tile_size, row_count * tile_size -13)  #to get them to sit on the tile)
                            alien_group.add(alien)

                        col_count += 1
                    row_count += 1

            def draw(self):
                for tile in self.tile_list:
                    WINDOW.blit(tile[0], tile [1])

                    #draws rectangles around objects
                    #pygame.draw.rect(WINDOW, (WHITE), tile [1], 2)
            #tile movement
            def update(self):
                if player.direction == 1 and player.moving == True:
                    for tile in self.tile_list:
                        tile[1].x -= 2
                if player.direction == -1 and player.moving == True:
                    for tile in self.tile_list:
                        tile[1].x += 2
                        

    
    class Snack(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('img/snack.png')
            self.image = pygame.transform.scale(img, (tile_size//2, tile_size //2))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
        
        def update(self):
            if pygame.sprite.collide_rect(self, player):
                player.score +=5
                self.kill()
            if player.direction == 1 and player.moving == True:
                self.rect.x -=2
            if player.direction == -1 and player.moving == True:
                self.rect.x +=2




    class brad (pygame.sprite.Sprite):
        def __init__(self, x ,y):
            pygame.sprite.Sprite.__init__(self)
            self.images_right = []
            self.images_left = []
            self.jump = 0
            self.airbourne = False
            self.index = 0
            self.counter = 0
            for num in range (1,13):
                img_right = pygame.image.load(f'img/hero{num}.png')
                img_right = pygame.transform.scale(img_right,(40, 40))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
            self.img_upright = pygame.image.load('img/herof1.png')
            self.img_upright = pygame.transform.scale(self.img_upright,(40, 40))
            self.img_upleft = pygame.transform.flip(self.img_upright, True, False)
            self.image = self.images_right[0]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            pygame.draw.rect(WINDOW, (WHITE), self.rect, 2)
            self.direction = 1
            self.shoot_cooldown = 0
            self.vel_x = 0
            self.vel_y = 0
            self.jetpack = 120
            self.health = 100
            self.max_health = self.health
            self.alive = True
            self.probed = False
            self.touched = 0
            self.moving = False
            self.score = 0


        def shoot(self):
            #draws the bullets in front of brad
            if self.shoot_cooldown ==0:
                self.shoot_cooldown = 15
                bullet = Bullets(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction) #self.rect.top +23)
                bullets.add(bullet)
                

        def update (self):
            dx =0
            dy =0
            walk_cooldown = 2
            if self.shoot_cooldown > 0:
                self.shoot_cooldown -= 1
            
            '''This is the Player Movement'''
            key = pygame.key.get_pressed()
            if key[pygame.K_a] and self.rect.x > 1:
                dx -= 0.
                self.counter += 1
                self.direction = -1
                self.moving = True
                
            if key[pygame.K_d]:# and self.rect.x <(SCREEN_WIDTH - self.rect.width):
                dx += 1
                self.counter += 1
                self.direction = 1
                self.moving = True
            if key[pygame.K_w]  and self.jetpack > 0:
                dy -= self.vel_y+2
                self.jetpack -= 1
                self.airbourne = True
            if key[pygame.K_d] == False and key[pygame.K_a] == False:
                self.counter = 0
                self.index = 0
                self.moving = False
            if key[pygame.K_w] == False:
                self.airbourne = False
                if self.direction ==1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]
                if self.jump ==1:
                    self.image = self.images_up[self.airbourne]

            '''This is animating the player'''   
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction ==1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            if self.airbourne:
                if self.direction == 1:
                    self.image = self.img_upright
                else:
                    self.image = self.img_upleft
            
            
            '''This is how the Jetpack works'''
            self.vel_y += 1
            if self.vel_y > 4:
                self.vel_y -= 1
            dy += self.vel_y
    
            '''This is where we check for ALL collisions'''
            for tile in world.tile_list:
                # check for collision in x direction for platforms
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                           
                #check for collision  on platforms in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below ground (Jumping) JAMES edit
                    if self.vel_y < 0:
                        dy = tile[1].bottom
                    #check if above ground (Falling)
                    if self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                    dy = 0 
                    self.vel_y = 0
                    

                    if self.rect.bottom == tile[1].top and (self.rect.x >= tile[1].x or self.rect.x + self.rect.width >= tile[1].x + tile[1].width):
                        self.jetpack = 120
        

            '''Checks to see if bullets have hit the enemy'''
            enemydead = 0
            hits = pygame.sprite.groupcollide(alien_group, bullets, False, True)
            for hit in hits:
                hit.alienhealth -=1
                if hit.alienhealth == 0:
                    enemydead +=1 
                    hit.kill()
                    player.score +=1
                    aliendead_fx.play()

            '''Checks to see if Player COLLIDES with Enemy'''
            if not player.probed:
                hits = pygame.sprite.groupcollide(player_sprite, alien_group, False, False)
                for hit in hits:
                    player.probed = True
                    player.health -= 25

            if player.probed:
                player.touched +=1
                if player.touched == 60:
                    player.probed = False
                    player.touched = 0
                    
        
            '''Checks for COLLISIONS with Spikes'''
            hits = pygame.sprite.groupcollide(player_sprite, spike_group, False, False)
            if hits:
                player.health = 0

            '''Update players co-ords'''
            self.rect.x += dx
            self.rect.y += dy

                

        #Draws rectangle around player
            #pygame.draw.rect(WINDOW, (255,255,255), self.rect, 2)


    
                

                
    '''This is the Enemy class'''
    class Enemy(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('img/newalien.png')
            self.image = pygame.transform.flip(self.image, True, False) 
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.aliendirection = 1
            self.alienmovecount = 0
            self.alienhealth = 3
            self.alive = True
            self.idling = False
            self.idle_count = 0



        def update (self):
            if player.direction == 1 and player.moving == True:
                self.rect.x -=2
            if player.direction == -1 and player.moving == True:
                self.rect.x +=2
            else:
                if self.alive and player.alive:
                    if random.randint(1,200) == 1:
                        self.idling = True
                        self.idle_count = 100
                    if self.idling == False:
                        self.rect.x += self.aliendirection
                        self.alienmovecount += 1
                        if (self.alienmovecount) == 62:
                            self.aliendirection *= -1
                            self.alienmovecount *= -1
                            if self.rect.left >= 62:
                                self.image = pygame.transform.flip(self.image, True, False)
                                self.image.set_colorkey(WHITE)

                    else:
                        self.idle_count -= 1
                        if self.idle_count <= 0:
                            self.idling = False


    '''This is the class which sits at the bottom of the game, if you touch them, you DIE!!'''
    class Spike (pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            spike = pygame.image.load('png/Tiles/Spike.png')
            self.image = pygame.transform.scale (spike, (tile_size, tile_size//2))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    '''This is a healthbar class'''
    class HealthBar():
        def __init__(self, x, y, health, max_health):
            self.x = x
            self.y = y
            self.health = health
            self.max_health = max_health

        def draw(self, health):
            self.health = health
            ratio = self.health / self.max_health
            pygame.draw.rect(WINDOW, WHITE, (self.x -2, self.y -2, 154, 24))
            pygame.draw.rect(WINDOW, RED, (self.x, self.y, 150, 20))
            pygame.draw.rect(WINDOW, GREEN, (self.x, self.y, 150 * ratio, 20))
            


    '''This is the Bullets class'''
    class Bullets(pygame.sprite.Sprite):
        def __init__(self, x, y, direction):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((10, 5))
            self.image.fill (YELLOW)
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.right = x
            self.vel = 20
            self.direction = direction
            
        def update (self):
            if self.direction == 1:
                self.rect.x += self.vel
            else:
                self.rect.x -= self.vel

            
            #bullet dies if moved off screen
            if self.rect.right < -20 or self.rect.left > SCREEN_WIDTH +5:
                self.kill()
            
                

    '''Pregame variables'''
    player = brad(0, 460)
    health_bar = HealthBar (450, 10, player.health, player.health)
    player_sprite.add(player)
    world = World(world_data)

    ''' This is the Main Loop '''
    live = True
    while live:
        
        CLOCK.tick(FPS)
        WINDOW.blit(background,(0,0))
        world.draw()
        health_bar.draw(player.health)
        fps = update_fps()


        if player.health <= 0:
            if player.rect.y > 1:
                player.rect.y -=5
            game_over(player.rect.x, player.rect.y)

        if countdown > 0:
            draw_text(f'Time Left: {countdown}', font, WHITE, 10, 50) #show time left      
            count_timer = pygame.time.get_ticks()
            if count_timer - last_count >1000:
                countdown -= 1
                last_count = count_timer
                if countdown == 0:
                    player.health = 0
                    if player.rect.y > 1:
                        player.rect.y -=5
                    game_over(player.rect.x, player.rect.y)


        '''Drawing all the sprite groups onto the window'''
        player_sprite.draw(WINDOW)
        bullets.draw(WINDOW)    
        spike_group.draw(WINDOW) # SPIKES AT BOTTOM OF SCREEN   
        alien_group.draw(WINDOW)  # ENEMIES
        snack_group.draw(WINDOW)

        '''Drawing from the function above are here!'''
        draw_text(f'Health: ', font, WHITE, 350, 7) #show health
        draw_text(f'Jetpack Fuel: {player.jetpack}', font, WHITE, 750, 7) #show jetpack            
        draw_text(f'FPS: {fps}', font, WHITE, 10, 7) # Display FPS
        draw_text(f'Score: {player.score}', font, WHITE, 750, 50) #show health
    
        '''Updating the groups for for displaying changes'''
        player.update()
        alien_group.update()
        bullets.update()
        world.update()
        snack_group.update()
        pygame.display.update()

        '''Events in the game I.E, user inputs'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                live = False  
                pygame.quit()
            if event.type == pygame.KEYDOWN:    
                if event.key == K_ESCAPE:
                    Pause()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.shoot_cooldown == 0:
                    shoot_fx.play()
                    player.shoot()


'''This function displays when the player dies or runs out of time!'''
def game_over(player_x, player_y):
    ghost_x = player_x
    ghost_y = player_y
    game_over = True
    gameover_fx.play()
    

    restart_button = Button(SCREEN_WIDTH /2 -109 , SCREEN_HEIGHT -400, restart_img)
    quit_button = Button(SCREEN_WIDTH /2 -111 , SCREEN_HEIGHT -300, quit_img)
    

    while game_over:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            # checking to see if the player closes the window 
            if event.type == pygame.QUIT:
                pygame.quit()
                # if the player quits the running while loop is set false 
                game_over = False

        WINDOW.fill(BLACK)
        WINDOW.blit(background,(0,0))
        WINDOW.blit(dead_image, (ghost_x, ghost_y))
        
        
        if quit_button.draw():
            game_intro()
        if restart_button.draw():
            Game()
        ghost_y -= 1
        pygame.display.update()

game_intro()
Game()



'''
fix self vel and world vel so that the player stays central


if player x == alien x 
then alien throws something at player

'''
