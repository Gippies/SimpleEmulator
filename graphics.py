import pyglet

from settings import SCREEN_HEIGHT


class GraphicView:
    def __init__(self, title, sub_components=()):
        self.title = pyglet.text.Label(title,
                                       font_name='Times New Roman',
                                       font_size=12,
                                       x=10, y=SCREEN_HEIGHT - 10,
                                       anchor_x='left', anchor_y='top')
        self.sub_components = sub_components

    def was_clicked(self, x, y):
        return True

    def draw(self):
        for c in self.sub_components:
            c.draw()
        self.title.draw()


class GraphicComponent:
    def __init__(self, text, x, y, width=150, height=100):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.label = pyglet.text.Label(text,
                                       font_name='Times New Roman',
                                       font_size=12,
                                       x=self.x + (self.width // 2), y=self.y + (self.height // 2),
                                       anchor_x='center', anchor_y='center')

    def set_text(self, text):
        self.label.text = text

    def was_clicked(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    def draw(self):
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_LINE_LOOP,
                                     [0, 1, 2, 3, 0],
                                     ('v2i', (self.x, self.y,
                                              self.x + self.width, self.y,
                                              self.x + self.width, self.y + self.height,
                                              self.x, self.y + self.height))
                                     )
        self.label.draw()
