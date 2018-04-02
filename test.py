import pygame
import math
from settings import Settings
from pygame.sprite import Sprite
from pygame.sprite import Group
from train import Train
import game_functions as gf
pygame.init()

def drawLine(background):
	pygame.draw.line(background,(255,0,0),(100,300),(1100,300),3)
	pygame.draw.line(background,(255,0,0),(100,400),(1100,400),3)
	pygame.draw.line(background,(255,0,0),(250,300),(300,200),3)
	pygame.draw.line(background,(255,0,0),(300,200),(900,200),3)
	pygame.draw.line(background,(255,0,0),(900,200),(950,300),3)
	
def main():
	ai_settings=Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))	#界面
	pygame.display.set_caption("Track_Line")	#命名
	
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((ai_settings.bg_color))#背景板参数
	
	drawLine(background)
	train=Train(background)
	trains=Group()#把列车变成组
	
	clock = pygame.time.Clock()
	keepGoing = True
	while keepGoing:
		clock.tick(30)
		gf.check_events()#事件响应模块
		##train.move_contrail()
		gf.update_screen()#绘制模块
		
main()