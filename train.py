import pygame
import Sprite from pygame.sprite

class Train(Sprite):
	def super().__init__(self,number,ai_settings,lenth,screen):
		self.lenth=lenth
		self.number=number
		self.screen=screen
		self.rect = pygame.Rect(0, 0, ai_settings.train_width,ai_settings.train_height)
		#车辆产生
		carriage=[]
		for i in range(int(self.lenth)):
			carriage.append(Rect(100-i,300,1,ai_settings.train_height))#为列表添加车体
		
	def move_contrail(self,headstock_xvel,headstock_yvel):
		#定义每一帧的动作
		headstock=Rect(headstock_xvel, headstock_yvel,1,ai_settings.train_height)#车头位置的确定
		carriage_new=[]
		for i in range(int(self.lenth)-1):
			carriage_new.append(carriage[i])
		carriage_new.insert(0,headstock)
		carriage=carriage_new
		
	def draw_train(self):
		pygame.draw.rect(self.screen, self.color, self.rect)