import pygame
import pygame.locals
from pygame import mixer
from settings import Settings
from moviepy.editor import VideoFileClip
import os
import sys

class Main:

    def __init__(self):

        pygame.init()
        mixer.init()
        self.load_screen = False
        self.size = (1000,800)
        self.window = pygame.display.set_mode((self.size))
        self.fps = 60
        self.nav_mus = mixer.Sound(r"data/music/navigation.wav")
        self.intro = pygame.image.load(r"data/images/template.png")
        self.played = False
        self.load_settings = False
        pygame.display.set_caption("Your game name")
        self.clock = pygame.time.Clock()
        video = VideoFileClip(r'data/videos/intro.mp4')
        video.preview()
        self.colors = {
        "white" : (255,255,255),
        "red" : (255,0,0),
        "black" : (0,0,0),
        "blue" : (0,0,255),
        "green" : (0,255,0),
        "test" : (100,60,40),
        "bg" : (0,215,215)
        }

        self.locations = [
            (20,500,200,570),
            (20,590,200,660),
            (20,680,200,750)              
        ]

        self.append_rect()
        self.btn_clr = [
            self.colors["test"],
            self.colors["test"],
            self.colors["test"]
        ]

        self.cpy = self.btn_clr.copy()

        self.game_loop()

    def text(self,Text,color,x,y,s):
        font = pygame.font.Font(r"data\fonts\Debrosee-ALPnL.ttf",s)
        Txt = font.render(Text,True,self.colors[color])
        self.window.blit(Txt,(x,y))

    def append_rect(self):
        self.rects = {
        "play_Rect" : pygame.Rect(20,500,180,70),
        "settings_Rect" : pygame.Rect(20,590,180,70),
        "exit_Rect" : pygame.Rect(20,680,180,70)
        }
        self.len = len(self.rects)

    def chng_clr(self,locs,color1,color2,para = None):
        if not para:
            if self.pos_x > locs[0] and self.pos_x < locs[2]:
                if self.pos_y > locs[1] and self.pos_y < locs[3]:
                    color1 = color2
        elif para:
            if self.pos_x > 20 and self.pos_x < locs[2]:
                if self.pos_y > locs[1] and self.pos_y < locs[3]:
                    return True

    def check_mouse_pos(self):
        if self.chng_clr(self.locations[0],None,None,para=True):
            self.btn_clr[0] = (205,0,255)
            self.mus_play()

        elif self.chng_clr(self.locations[1],None,None,para=True):
            self.btn_clr[1] = (205,0,255)
            self.mus_play()

        elif self.chng_clr(self.locations[2],None,None,para=True):
            self.btn_clr[2] = (205,0,255)
            self.mus_play()

        else:
            self.btn_clr = self.cpy.copy()
            self.played = False
    def draw_rects(self):
        pygame.draw.rect(self.window,self.btn_clr[0],self.rects["play_Rect"])
        pygame.draw.rect(self.window,self.btn_clr[1],self.rects["settings_Rect"])
        pygame.draw.rect(self.window,self.btn_clr[2],self.rects["exit_Rect"])
        
    def blit_texts(self):
        self.text("PLAY","white",75,520,34)
        self.text("SETTINGS","white",50,609,34)
        self.text("EXIT","white",75,699,34)
        
    def mus_play(self):
        if not self.played:
            self.nav_mus.play()
            self.played = True

    def game_loop(self):
        while True:
            self.pos_x , self.pos_y = pygame.mouse.get_pos()
            self.window.fill(self.colors["bg"])
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif self.event.type == pygame.MOUSEBUTTONDOWN:
                    if self.pos_x > 20 and self.pos_x < 220:
                        if self.pos_y > 680 and self.pos_y < 750:
                            pygame.quit()
                            sys.exit()
                    if self.pos_x > 20 and self.pos_x < 220:
                        if self.pos_y > 500 and self.pos_y < 570:
                            self.load_screen = True
                            break
                    if self.pos_x >20 and self.pos_x<200:
                        if self.pos_y > 590 and self.pos_y < 660:
                            self.load_settings = True
            if self.load_screen:
                VideoFileClip(r'data/videos/loading.mp4').preview()
                self.load_screen = False
                os.system('main.py')
                #load_main

            elif self.load_settings:
                break
            self.clock.tick(self.fps)
            self.check_mouse_pos()
            self.draw_rects()
            self.blit_texts()
            pygame.display.update()

main = Main()

if main.load_settings:
    settings = Settings(main)