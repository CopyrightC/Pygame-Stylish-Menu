import pygame,sys
from threading import Thread
pygame.init()

class Settings:
    def __init__(self,main):
        self.main = main
        self.back_Rect = pygame.Rect(7,7,60,60)
        self.back = pygame.image.load(r'data/images/back.png')
        self.back = pygame.transform.scale(self.back,(64,64))
        self.running = True
        while self.running:
            self.pos_x , self.pos_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.pos_x > 7 and self.pos_x < 71:
                        if self.pos_y > 7 and self.pos_y < 71:
                            main.load_screen = False
                            main.load_settings = False
                            main.append_rect()
                            main.game_loop()                
            main.text("Settings","black",410,10,50)
            main.window.blit(self.back,(7,7))
            pygame.display.update()
            main.clock.tick(main.fps)