#!/usr/bin/env python3

import sys

import pygame
from settings import Settings

def drawStuff(background):
	pygame.draw.line(background, (255, 0, 0), (100,300), (1100, 300))
	
def run_game():
	#定义运行函数并初始化屏幕对象
	pygame.init()#初始化
	ai_settings = Settings()#实例化对象
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))#调用对象的参数
	pygame.display.set_caption("Invasion")#标题
	
	
	while True:#主循环
		# 观察输入指令
		for event in pygame.event.get():#退出循环
			if event.type == pygame.QUIT:
				sys.exit()
				
		screen.fill(ai_settings.bg_color)#1重绘屏幕
				
		pygame.display.flip()#2使屏幕可见
		
run_game()