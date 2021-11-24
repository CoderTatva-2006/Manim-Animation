from manim import *
import time
import random 

config.pixel_height = 1080

config.pixel_width = int(config.pixel_height * config.aspect_ratio)
config.frame_rate = 30

# config.frame_height = 0
# config.frame_width = config.frame_height * config.aspect_ratio

grid = [
		[str(x) for x in range(1,11)],
		[str(x) for x in range(11,21)],
		[str(x) for x in range(21,31)],
		[str(x) for x in range(31,41)],
		[str(x) for x in range(41,51)],
	]

class scenes(Scene):

	def _render(self):
		self.render(preview=True)

	def construct(self):
		table = Table(
					  grid,
					  include_outer_lines=True
					  ).scale(0.5)
		self.play(Create(table),run_time=5)
		for x in range(5):
			self.remove(table)
			random.shuffle(grid)
			table = Table(grid,include_outer_lines=True).scale(0.5)
			self.add(table)
			self.wait(0.1)	
		
		
		self.play(Uncreate(table),run_time=5)
		self.wait()
		

		
if __name__ == '__main__':
	print(f"Starting Render at {time.ctime()}")
	start = time.time()
	scenes()._render()
	end = time.time()
	print(f"Render Completed in {end - start} seconds.")