from computer import Computer
from graphics import GraphicComponent
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
import pyglet
from pyglet.window import mouse

# my_computer = Computer()
# my_computer.load_program('test_code/fibo.joshcomp')
# my_computer.do_computer()


window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
test_component = GraphicComponent('Test', SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print(f'The left mouse button was pressed at x: {x}, y: {y}.')
        test_component.set_text(str(x))
        print(str(test_component.was_clicked(x, y)))


@window.event
def on_draw():
    window.clear()
    test_component.draw()


pyglet.app.run()
