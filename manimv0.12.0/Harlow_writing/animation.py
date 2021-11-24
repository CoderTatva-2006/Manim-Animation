from os import write
from manim import *
import time

config.pixel_height = 1080 # 1080 is full hd

config.pixel_width = int(config.pixel_height * config.aspect_ratio)
config.frame_rate = 60 # 30fps and 60fps 

# config.frame_height = 0
# config.frame_width = config.frame_height * config.aspect_ratio

class scenes(Scene):

	def _render(self):
		self.render(preview=True)

	def construct(self):
		self.wait(1)
		welcome = Text("Hello Everyone!",font="Harlow Solid Plain",font_size=108)
		self.play(Write(welcome,run_time=3))
		self.wait(1)
		self.clear()
		with register_font("./harlowsolidplain.otf") as font:
			text = Text("Isn't this font beautiful?\n It's Harlow Solid.",font="Harlow Solid Plain",font_size=96)
		self.play(Write(text),run_time=5)
		fine_text = Text("Available at https://github.com/CoderTatva-2006/Harlow-Solid-Font",font_size=22)
		fine_text.shift([0,-3,0])
		self.play(Write(fine_text))
		self.wait(2)
		self.clear()
		self.add(fine_text)
		with register_font("./harlowsolidplain.otf") as font:
			text = Text("Want to see all the beautiful letters in action?",font="Harlow Solid Plain")
		self.play(Write(text))
		self.wait(2)
		self.clear()
		self.add(fine_text)
		with register_font("./harlowsolidplain.otf") as font:
			glyphs = Text("""A  B  C  D  F  G  H  I  J  K  L  M

N  O  P  Q  R  S  T  U  V  W  X  Y  Z

a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t 
u  v  w  x  y  z

	1 2 3 4 5 6 7 8 9 0""",font="Harlow Solid Plain")
		self.play(Write(glyphs),run_time=10)
		self.wait(5)
		self.clear()
		self.add(fine_text)
		self.play(Write(Text("\tThank You!",font="Harlow Solid Plain")),run_time=2)
		self.play(Write(Text("Credits : Tatva Agarwal").shift([0,-1,0])))
		self.wait(3)

		
if __name__ == '__main__':
	print(f"Starting Render at {time.ctime()}")
	start = time.time()
	scenes()._render()
	end = time.time()
	print(f"Render Completed in {end - start} seconds.")