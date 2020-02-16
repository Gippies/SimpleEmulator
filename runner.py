from computer import Computer, Program
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
import pyglet
from pyglet.window import mouse

my_computer = Computer()
my_computer.load_program(Program('test_code/fibo.joshcomp'))


window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT)


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        my_computer.on_click()


@window.event
def on_draw():
    window.clear()
    my_computer.draw()


pyglet.app.run()
