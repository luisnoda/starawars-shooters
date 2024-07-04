from pygame import * 
from random import randint 

init()



#1 ESTABLECER EL MAIN SCREEN 
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800 
X_CORD, Y_CORD = (SCREEN_WIDTH - 100)// 2, (SCREEN_HEIGHT - 100)// 2
BACKGROUND_IMG  = "fondoespacial.jpg"
PLAYER_IMG = "falco.png"
ENEMY_IMG = "tie.png" 
GAME_OVER = "gameover2.jpg"
BULLET_IMG = "bala2.png"
WIN_IMG = "victoria.jpg"
BACKGROUND_SOUND = "musica.mp3"
FIRE_SOUND = "sonidobala.mp3"
BLACK = (0,0,0)
YELLOW = (227, 252, 3)
WHITE = (255,255,255)
BLUE = (50, 117, 168)
GREEN = (54, 168, 50)
PURPLE = (141, 50, 168)

#FUNCIONALIDADES 
score = 0
misses = 0

#INICIALIZAR EL MODULO DE FUENTES 
font.init()
font_1 = font.Font(None, 40)

#inicializar modulo de sonido
mixer.init()
#CARGAR MUSICA DE FONDO
mixer.music.load(BACKGROUND_SOUND)
#REPRODUCIR MUSICA DE FONDO
mixer.music.play()

fire_sound = mixer.Sound(FIRE_SOUND)





#ventana principal
screen = display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption ("Tirador")
background = transform.scale(image.load(BACKGROUND_IMG),(SCREEN_WIDTH, SCREEN_HEIGHT))

#definicion de clases 
class Character(sprite.Sprite):
    def __init__(self, char_image, x_cord, y_cord,char_width, char_height, speed=0):
        super().__init__() 
        self.widht = char_width
        self.height = char_height
        self.image = transform.scale(image.load(char_image),(self.widht, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x_cord
        self.rect.y = y_cord
        self.speed = speed

    def reset(self):
        screen.blit(self.image,(self.rect.x, self.rect.y))

class Player(Character):

    def update(self):
        # guardar en un diccionario todas las teclas que pueden presioanrse 
        keys = key.get_pressed()

        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keys[K_d] and self.rect.x < SCREEN_WIDTH - self.widht:
            self.rect.x += self.speed
    
    def fire(self):
        #CREAR BALAS
        print("pew pew")
        fire_sound.play()
        bullet = Bullet(BULLET_IMG, self.rect.centerx, self.rect.top, 30, 30, 10 )
        bullets.add(bullet)
        

class Enemy(Character):
    def update(self):
        global misses
        self.rect.y += self.speed 

        if self.rect.y >= SCREEN_HEIGHT:
            print(misses)   
            self.rect.y = 0 - self.height
            self.rect.x = randint(0, SCREEN_WIDTH - self.widht)
            self.speed = randint(1, 6)
            misses += 1

class Bullet(Character):
    def update(self):
        self.rect.y -= self.speed

        if self.rect.y  < 0: 
            self.kill()

    


#intancias de clases objetos
player = Player(PLAYER_IMG, 470, 720, 60, 80, 5)
monsters = sprite.Group() # creando un grupo de objetos enemigos

for i in range(1, 6):
#creando una instancia de la clase enemy
    monster = Enemy(ENEMY_IMG, randint(0,SCREEN_WIDTH - 60), 0, 50, 50, randint(1, 6))
# añadiendo un enemigo creado al grupo Monster
    monsters.add(monster)

bullets = sprite.Group() #creamos un grupo de objeto de bullets

#ciclo de juego 
run = True
finish = False 
clock = time.Clock()
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
                
                

    if not finish:


        screen.fill(BLACK)

        screen.blit(background,(0,0))
        score_text = font_1.render(f"SCORE: {score}", True, YELLOW )
        
        screen.blit (score_text,(SCREEN_WIDTH //25, SCREEN_HEIGHT //25))
        player.reset()
        player.update()
        monsters.draw(screen)
        monsters.update()
        bullets.draw(screen)
        bullets.update()
        
        #colisiones 
        collides = sprite.groupcollide(monsters, bullets, True, True)

        for collide in collides:
            score += 1
            monster = Enemy(ENEMY_IMG, randint(0,SCREEN_WIDTH - 60), 0, 50, 50, randint(1, 6))
            monsters.add(monster)
        
        #condiciones de derrota 
        if misses == 10 or sprite.spritecollide(player, monsters, False): 
            finish = True
            screen.fill(BLACK)
            GAME_OVER = transform.scale(image.load(GAME_OVER), (1000,800))
            screen.blit(GAME_OVER, (0,0)) 
        
        if score == 5:
            finish = True
            screen.fill(BLACK)
            WIN_IMG = transform.scale(image.load(WIN_IMG), (1000,800))
            screen.blit(WIN_IMG, (0,0))
            

        
        #enemy.reset()
        #enemy.update()
    
    display.update()
    clock.tick(60)



quit()



        







