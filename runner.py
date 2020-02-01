from computer import Computer
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
import pyglet
from pyglet.window import mouse

# my_computer = Computer()
# my_computer.load_program('test_code/fibo.joshcomp')
# my_computer.do_computer()


window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print(f'The left mouse button was pressed at x: {x}, y: {y}.')


@window.event
def on_draw():
    window.clear()
    label.draw()


pyglet.app.run()
