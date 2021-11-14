from manim import *
import time

config.pixel_height = 1080

config.pixel_width = int(config.pixel_height * config.aspect_ratio)
config.frame_rate = 30

# config.frame_height = 0
# config.frame_width = config.frame_height * config.aspect_ratio

class scenes(Scene):

	def _render(self):
		self.render(preview=True)

	def construct(self):
		pass


		
if __name__ == '__main__':
	print(f"Starting Render at {time.ctime()}")
	start = time.time()
	scenes()._render()
	end = time.time()
	print(f"Render Completed in {end - start} seconds.")