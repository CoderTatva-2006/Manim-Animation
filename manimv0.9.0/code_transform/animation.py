from manim import *
import time

config.pixel_height = 1080

config.pixel_width = int(config.pixel_height * config.aspect_ratio)
config.frame_rate = 60

# config.frame_height = 0
# config.frame_width = config.frame_height * config.aspect_ratio

class scenes(Scene):

	def _render(self):
		self.render(preview=True)

	def construct(self):
		
		code1 = """
# Python Program Showcasing list comprehensions
# Equivalent to set builder from in mathematical sets
# Task : print a list of squares from 0 to 10 

############ Normal Approach #############

list_of_squares = []

for num in range(11):
    list_of_squares.append(num**2)

print(list_of_squares) # [0,1,4,9,16,25,36,49,64,81,100]


"""
		code2 = """
# Python Program Showcasing list comprehensions
# Equivalent to set builder from in mathematical sets
# Task : print a list of squares from 0 to 10 

############ List comprehension ##########

list_of_squares = [ num**2 for num in range(11) ] 

print(list_of_squares) # [0,1,4,9,16,25,36,49,64,81,100]
"""

		code_block_1 = Code(
			code=code1, # maximum of 20 lines and 65 cols per line
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

		code_block_2 = Code(
			code=code2, # maximum of 20 lines and 65 cols per line
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

		self.play(Write(code_block_1),run_time=15)
		self.wait(5)
		self.play(
			Unwrite(
					VGroup(
					code_block_1.line_numbers,
					code_block_1.code
					)
				),
			run_time=15
			)
		self.wait(5)
		self.play(
			Transform(
				VGroup(
					code_block_1.code,
					code_block_1.background_mobject,
					# code_block_1.line_numbers
					),
				VGroup(
					code_block_2.code,
					code_block_2.background_mobject,
					# code_block_2.line_numbers
					)
				),
			run_time=15) 

		self.play(
				Transform(
					code_block_1.line_numbers,
					code_block_2.line_numbers
					),
				run_time=1
			)

		self.play(
				Write(
					VGroup(
					code_block_1.line_numbers,
					code_block_1.code
					)
				),
			run_time=15
			)

		self.wait(5)
		self.play(Unwrite(code_block_1),run_time=15)
		self.wait(5)
if __name__ == '__main__':
	print(f"Starting Render at {time.ctime()}")
	start = time.time()
	scenes()._render()
	end = time.time()
	print(f"Render Completed in {end - start} seconds.")