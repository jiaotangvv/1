import sys
import pygame

def check_events():
	for event in pygame.event.get():	#事件监听
		if event.type == pygame.QUIT:
			keepGoing = False
		elif event.type == pygame.MOUSEBUTTONUP:	#记录鼠标点击位置
			print(pygame.mouse.get_pos())
			
def update_screen(ai_settings, background, train):
	screen.blit(background, (0, 0))
	train.draw_train()
	pygame.display.flip()
	