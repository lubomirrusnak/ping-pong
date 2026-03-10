from pygame import *


init()
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
   

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

            if keys[K_s] and self.rect.y < win_height - self.rect.height - 5:
                self.rect.y += self.speed
        
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height - 5:
            self.rect.y += self.speed


left_padle = Player( 30, 200, 50, 150, 4)
right_padle = Player( 520, 200, 50, 150, 4)

clock = time.Clock()
run = True 

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill((200, 255, 255))

    left_padle.update_l()
    right_padle.update_r()

    left_padle.draw()
    right_padle.draw()

    display.update()
    clock.tick(60)

quit()


        
