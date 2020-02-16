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

    # Override this to do stuff
    def on_click(self):
        pass

    def draw(self):
        self.title.draw()
        for c in self.sub_components:
            c.draw()


class GraphicComponent:
    def __init__(self, text, x, y, width=150, height=100, sub_components=()):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.label = pyglet.text.Label(text,
                                       font_name='Times New Roman',
                                       font_size=12,
                                       x=self.x + (self.width // 2), y=self.y + self.height - 10,
                                       anchor_x='center', anchor_y='center')
        self.sub_components = sub_components

    def set_text(self, text):
        self.label.text = text

    # Override this to do stuff
    def on_click(self):
        pass

    def draw(self):
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_LINE_LOOP,
                                     [0, 1, 2, 3, 0],
                                     ('v2i', (self.x, self.y,
                                              self.x + self.width, self.y,
                                              self.x + self.width, self.y + self.height,
                                              self.x, self.y + self.height))
                                     )
        self.label.draw()
        for c in self.sub_components:
            c.draw()


class GraphicComponentWithValues(GraphicComponent):
    def __init__(self, text, values, x, y, width=150, height=100, sub_components=()):
        super().__init__(text, x, y, width, height, sub_components)
        self.value_labels = []
        height_to_place = 30
        for v in values:
            self.value_labels.append(pyglet.text.Label(v,
                                           font_name='Times New Roman',
                                           font_size=12,
                                           x=self.x + (self.width // 2), y=self.y + self.height - height_to_place,
                                           anchor_x='center', anchor_y='center'))
            height_to_place += 20

    # Override this to include something to append.
    # E.g. Counter: {text}
    def update_value_label_text(self):
        pass

    def draw(self):
        super().draw()
        for v in self.value_labels:
            v.draw()
