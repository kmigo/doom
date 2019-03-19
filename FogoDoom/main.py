# -*- coding: latin-1 -*-

#import libs
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import random
from time import sleep


fireColorsPalette  = [{ " r " : 7 , " g " : 7 , " b " : 7 }, { " r " : 31 , " g " : 7 , " b " : 7 }, { " r " : 47 , " g " : 15 , " b " : 7 },{ "r " : 71 , " g " : 15 , " b " : 7 }, { " r " : 87 , " g " : 23 , " b " : 7 }, { " r " : 103 , " g " : 31 , " b " : 7 }, { " r " :119 , "g " : 31 , " b " : 7 }, { " r " : 143 , " g " : 39 , " b " : 7 }, { " r " : 159 , " g " : 47 , " b " : 7 }, { " r " : 175 , " g " :63 , "b " : 7 }, { " r " : 191 , " g " : 71 , " b " : 7 }, { " r " : 199 , " g " : 71 , " b " : 7 }, { " r " : 223 , " g " : 79 , " b " :7 }, { "r " : 223 , " g " : 87 , " b " : 7 }, { " r " : 223 , " g " : 87 , " b " : 7 }, { " r " : 215 , " g " : 95 , " b " : 7 }, { " r " :215 , "g " : 95 , " b " : 7 }, { " r " : 215 , " g " : 103 , " b " : 15 }, { " r " : 207 , " g " : 111 , " b " : 15 }, { " r " : 207 , " g " :119 ," b " : 15 }, [207,127,15],[207,135,23],[199,133,23],[199,143,23],[199,151,31],[191,159,31],[191,159,31],[191,167,39],[197,167,39],[191,175,47],[183,175,47],[183,183,47],[183,183,55],[207,207,111], [223,223,159],[239,239,199],[255,255 ,255]]




class Fogo(BoxLayout):
	def __init__(self,**kwargs):
		super(Fogo,self).__init__(**kwargs)
		self.test=None
		Clock.schedule_interval(self.update,.1)
		self.fireWidth=33
		self.fireHeight=33
		self.areaPixel=self.fireWidth * self.fireHeight
		self.fireRandom=0
	
	def update(self,bt):
		if self.test == None:
			
			self.estrutura()
			
			self.test=False
		self.algoritmo()
		self.fireRender()
	
	def estrutura(self):
		self.ids.grid.cols=self.fireWidth
		for i in range(self.areaPixel):
			self.ids.grid.add_widget(Button(
			background_normal='',
			background_color=(1,1,1,1),
			color=(0,0,0,0),
			size_hint=(None,None),
			size=(7,7)
				))
			
		for item in range( self.fireWidth,self.areaPixel):
			
			self.ids.grid.children[item].text='0'
			
		for cada in range(self.fireWidth):
			self.ids.grid.children[cada].text='37'
		
	def algoritmo(self):
		self.fireRandom=random.randint(30,36)
		self.baseFire()
		for colum in range(self.fireWidth):
			for row in range(self.fireHeight):
				if row == 0:
					pass
				else:
					pixel = colum - (self.fireWidth * row)
					self.ids.lb.text=str(pixel)
					self.updatefirepixel(pixel)
	
	def updatefirepixel(self,pixel):
		pixelAnterior = pixel - self.fireHeight
		
		if pixelAnterior >= self.areaPixel:
			return 0
		
		decay = random.randint(0,5)
		pixelAnteriorInt=self.ids.grid.children[pixelAnterior]
		newIntenFire= int(pixelAnteriorInt.text)-decay
		
		if not newIntenFire >= 0:
			newIntenFire = 0
		
		self.ids.grid.children[pixel - decay].text=str(newIntenFire)
		
	
	
	def baseFire(self):
		for cada in range(self.fireWidth):
			self.ids.grid.children[cada].text=str(
			self.fireRandom)
	
	def fireRender(self):
		global fireColorsPalette
		lista=fireColorsPalette
		for pixel in range(self.areaPixel):
			if pixel >= self.areaPixel:
				pixel=self.areaPixel
			cor=self.RgbToRgba(lista[int(self.ids.grid.children[pixel].text)])
			self.ids.grid.children[pixel].background_color=cor
		
	
	def RgbToRgba(self,rgb=[]):
		res=[]
		if type(rgb) == list:
			for i in rgb:
				a=(i * 100 / 255) / 100.0
				res.append(a)
			res.append(1)
			return res
		else:
			lista=['r','g','b']
			for a in rgb.values():
				print a
				u=(a * 100 / 255) / 100.0
				res.append(u)
			res.append(1)
			return res

	
class FogoApp(App):
	
	def build(self):
		fogo=Fogo()
		
		return fogo


if __name__ == '__main__':
	FogoApp().run()
