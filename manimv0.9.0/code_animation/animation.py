from manim import *
import os
import time

class scenes(Scene):
	def construct(self):
		
		rendered_code = Code(
			"code.py", # maximum of 20 lines and 65 cols per line
			tab_width=4, # above at default scale of 0.5 
			background_stroke_width=1,
			background_stroke_color=WHITE,
			insert_line_no=True,
			style="monokai",
			background="window",
			language="Python",
			font="Monospace",
			#scale_factor=0.3
		)
		# rendered_code = Code("animation.py", tab_width=4, background="window",
							# language="Python", font="Monospace" , style="monokai")
							
		self.play(Create(rendered_code),run_time=20)
		# self.add(rendered_code)


		
if __name__ == '__main__':
	print(f"Starting Render at {time.ctime()}")
	start = time.time()
	os.system(f"python3 -m manim -pql {os.path.basename(__file__)} scenes")
	end = time.time()
	print(f"Render Completed in {end - start} seconds.")