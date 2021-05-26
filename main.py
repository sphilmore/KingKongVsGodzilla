import pygame
import pygame.event


FPS = 60
green = (0, 255, 0)
border = pygame.Rect(1200//2 -5, 0, 10, 600)
black = (0, 0, 0)
width, height = 1200, 600
vel = 5
bullet_vel = 7
max_bullets = 3
window = pygame.display.set_mode((width, height))
kong_image = pygame.image.load("images/gorilla.bmp")
godzilla_image = pygame.image.load("images/godzilla.bmp")
fire_ball_image = pygame.image.load("images/fire_ball.bmp")

image_width = 60
image_height = 48
pygame.display.set_caption("King Kong Vs Godzilla")

def draw_window(kong, godzilla):

    window.fill(green)
    pygame.draw.rect(window, black, border)
    window.blit(kong_image, (kong.x, kong.y))
    window.blit(godzilla_image, (godzilla.x, godzilla.y))
    pygame.display.update()

def godzilla_movement(keys_pressed, godzilla_rect):

        if keys_pressed[pygame.K_a] and godzilla_rect.x - vel > 0:  # Left
            godzilla_rect.x -= vel
        if keys_pressed[pygame.K_d] and godzilla_rect.x + vel + image_width < border.x:  # Right
            godzilla_rect.x += vel
        if keys_pressed[pygame.K_w] and godzilla_rect.y - vel > 0:  # Up
            godzilla_rect.y -= vel
        if keys_pressed[pygame.K_s] and godzilla_rect.y + vel + image_height < height:  # Down
            godzilla_rect.y += vel


def king_kong_movement(keys_pressed, king_kong_rect):

    if keys_pressed[pygame.K_LEFT] and king_kong_rect.x - vel > border.x + border.width:  # Left
        king_kong_rect.x -= vel
    if keys_pressed[pygame.K_RIGHT] and king_kong_rect.x + vel + image_width < width:  # Right
        king_kong_rect.x += vel
    if keys_pressed[pygame.K_UP] and king_kong_rect.y - vel >0:  # Up
        king_kong_rect.y -= vel
    if keys_pressed[pygame.K_DOWN] and king_kong_rect.y + vel + image_height < height:  # Down
        king_kong_rect.y += vel


def handle_bullets(godzilla_bullet, king_kong_bullet, godzilla_rect, king_kong_rect):
    for bullet in godzilla_bullet:
        bullet.x += bullet_vel
        if godzilla_rect.colliderect(bullet):

            godzilla_bullet.remove(bullet)

def main():
    """The main function of the game coded here"""

    king_kong_rect = pygame.Rect(800, 300, image_width, image_height)
    godzilla_rect = pygame.Rect(200,300, image_width, image_height )
    godzilla_bullet = []
    king_kong_bullet = []
    clock = pygame.time.Clock()
    run = True
    while run:
       clock.tick(FPS)
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False

           if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(godzilla_bullet) < max_bullets:
                 bullet = pygame.Rect(godzilla_rect.x + godzilla_rect.width, godzilla_rect.y + godzilla_rect.height/2-2, 10, 5)
                godzilla_bullet.append(bullet)

                if event.key == pygame.K_RCTRL and len(king_kong_bullet) < max_bullets:
                   bullet = pygame.Rect(king_kong_rect.x, king_kong_bullet.y + king_kong_rect.height / 2 - 2, 10, 5)
                   king_kong_bullet.append(bullet)

       keys_pressed = pygame.key.get_pressed()
       godzilla_movement(keys_pressed, godzilla_rect)
       king_kong_movement(keys_pressed, king_kong_rect)

       draw_window(king_kong_rect, godzilla_rect)



    pygame.quit()



if __name__ == '__main__':
    main()




