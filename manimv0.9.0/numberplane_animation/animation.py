from manim import *
import os
import time

class scenes(Scene):
	def construct(self):
		
		grid = NumberPlane()
		
		dot_orig = Dot(ORIGIN)

		dot_vector = Dot([5,2,0])

		arr = Arrow(dot_orig,dot_vector,buff=0)
		brace = BraceBetweenPoints(ORIGIN,[5,2,0])

		self.play(Create(grid))
		self.play(Create(dot_orig))
		self.play(Create(dot_vector))
		self.play(Create(arr))
		self.play(Create(brace))		


		
if __name__ == '__main__':
	print(f"Starting Render at {time.ctime()}")
	start = time.time()
	os.system(f"python3 -m manim -pql {os.path.basename(__file__)} scenes")
	end = time.time()
	print(f"Render Completed in {end - start} seconds.")