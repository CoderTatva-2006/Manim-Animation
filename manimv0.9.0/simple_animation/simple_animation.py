from manim import *
import os
import time
import manim

class scenes(Scene):
	def construct(self):
		
		circle = Circle(radius=1 , color = BLUE)
		circle.set_fill(BLUE,opacity=0.5)
		circle.shift([-2,0,0])
		line = Line([1,0,0],[3,0,0])
		line2 = Line([-3,0,0],[-1,0,0])
		line3 = line.copy()

		text = Text("Electronics & Semiconductors")
		text.shift([0,-2,0])

		self.play(Create(circle))
		self.play(Create(line))
		self.play(Transform(line,line2))
		self.remove(line)
		self.play(Rotate(line2,PI))
		self.wait(0.5)
		self.play(Rotate(line2,-PI))
		self.play(Transform(line2,line3))
		self.remove(line2)
		self.play(Rotate(line3,PI/2))
		line3.set_color(PINK)
		self.wait(1)
		group1 = VGroup(circle,line3)
		group2 = group1.copy().flip()
		self.play(Transform(group1,group2))
		self.play(Write(text))
		self.wait(2)


		
if __name__ == '__main__':
	print(f"Starting Render at {time.ctime()}")
	start = time.time()
	os.system("python3 -m manim -pqh simple_animation.py scenes")
	end = time.time()
	print(f"Render Completed in {end - start} seconds.")