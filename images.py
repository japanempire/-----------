import pygame


WIDTH = 600
HEIGHT = 400
FPS = 60


game_sc = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Работа с изображениями')

clock = pygame.time.Clock()

car_up = pygame.image.load('images/car.bmp')
finish = pygame.image.load('images/finish.png')
sand = pygame.image.load('images/sand.jpg')

sand = pygame.transform.scale(sand, [640, 400])

car_up.set_colorkey([255, 255, 255])

car_right = pygame.transform.rotate(car_up, -90)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    game_sc.blit(sand, [0, 0])
    game_sc.blit(car_right, [0, 0])
    game_sc.blit(finish, [360, 300])


    pygame.display.flip()
    clock.tick(FPS)