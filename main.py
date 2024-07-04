from pygame import * 

init()

window_WIDTH, window_HEIGHT = 1000, 800 
CHAR_IMG = "char.png"
VOLVASOR_IMG = "volvasor.png"
GOAL_IMG = "hero.png"
FAIL_IMG = "fail_1.jpg"
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50, 117, 168)
GREEN = (54, 168, 50)
PURPLE = (141, 50, 168)
window = display.set_mode ((window_WIDTH, window_HEIGHT))
display.set_caption ("Proyecto Noda")



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
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(Character):

    def update(self):
        # guardar en un diccionario todas las teclas que pueden presioanrse 
        keys = key.get_pressed()

        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keys[K_d] and self.rect.x < window_WIDTH - self.widht:
            self.rect.x += self.speed
        
        elif keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed 
        
        elif keys[K_s] and self.rect.y < window_HEIGHT - self.height:
            self.rect.y += self.speed

class Enemy(Character):
    def __init__(self,char_image, x_cord, y_cord,char_width, char_height, speed):
        super().__init__(char_image, x_cord, y_cord, char_width, char_height, speed)
        self.move_right = True
        
    def update(self):
        if self.move_right:
            self.rect.x += self.speed
            if self.rect.x >= window_WIDTH - self.widht:
                self.move_right = False 
        else: # cuando self.move.right == false
            self.rect.x -= self.speed 
            if self.rect.x <= 0:
                self.move_right = True 
        
class Wall(sprite.Sprite):
    def __init__(self, color, x_cord, y_cord, wall_width, wall_height):
        super().__init__()
        self.color = color 
        self.width = wall_width
        self.height = wall_height
        
        #definimos una propiedad imagen, un rectangulo
        self.image = Surface([self.width, self.height])
        self.image.fill(self.color)#rellenamos de color el metodo fill
        #cada obejto debe almacenar la propiedad rect
        self.rect = self.image.get_rect()
        self.rect.x = x_cord
        self.rect.y = y_cord
    
    def draw_wall(self):
        draw.rect(window,self.color,self.rect)
#instancias 
pokemon = Player(CHAR_IMG, 100,100, 60, 60, 3)
volvasor = Enemy(VOLVASOR_IMG, 500 ,100,30,50, 5)
goal = Character(GOAL_IMG, 500, 400, 50, 50)
wall_1 = Wall(WHITE, 300, 100, 400, 20 )
wall_2 = Wall(GREEN, 45, 55,200, 20)
wall_3 = Wall(BLUE, 260, 55, 20, 200)
wall_4 = Wall(PURPLE, 458, 44, 66, 600)


clock = time.Clock() 

run = True
finish = False  
while run:

    # 3. MANEJO DE EVENTOS 
    for i in event.get():
        if i.type == QUIT: 
            run = False
    
    if not finish:
        window.fill(BLACK)
        pokemon.reset()
        pokemon.update()
        volvasor.reset()
        volvasor.update()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        goal.reset()

        #condiciones de derrota 
        if sprite.collide_rect(pokemon, volvasor) or sprite.collide_rect(pokemon, wall_1) or sprite.collide_rect(pokemon, wall_2) or sprite.collide_rect(pokemon, wall_3) or sprite.collide_rect(pokemon, wall_4): 
            print("OUCH")
            finish = True
            window.fill(BLACK)
            fail_img = transform.scale(image.load(FAIL_IMG), (1000, 800  ))
            window.blit(fail_img, (0,0)) 
        
        
    display.update()
    clock.tick(60)
quit()


        







