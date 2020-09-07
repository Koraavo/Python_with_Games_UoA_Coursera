# Poke the Dots v04
# The first version is supposed to open a window. with two dots
# when the player clicks close, the window is supposed to close
# the dots bounce when they touch the edges of the screen
# they start from the left corner and moves straight at a constant speed towards right

from uagame import Window
from pygame import QUIT, Color, MOUSEBUTTONUP, KEYDOWN, K_SPACE, K_q
from pygame.time import Clock, get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle
from random import randint


class Game:
    def __init__(self):
        self._window = Window('Poke the Dots', 500, 400)
        self._adjust_window()
        self._frame_rate = 90
        self._clock = Clock()
        self._close_selected = False
        self._small_dot = Dot('red', 20, [100, 50], [1, 2], self._window)
        self._big_dot = Dot('blue', 40, [200, 100], [1, 2], self._window)
        self._small_dot.randomize_dot()
        self._big_dot.randomize_dot()
        self._score = 0

    def _adjust_window(self):
        self._window.set_font_name('ariel')
        self._window.set_font_size(40)
        self._window.set_font_color('white')
        self._window.set_bg_color('black')

    def play(self):
        while not self._close_selected:
            self.handle_events()
            self.draw_game()
            self.update_game()

    def handle_events(self):
        event_list = get_events()
        for event in event_list:
            self.handle_one_event(event)
            # handle one event

    def handle_one_event(self, event):
        if event.type == QUIT:
            self._close_selected = True
        elif event.type == MOUSEBUTTONUP:
            self.handle_mouse_button(event)
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                self.handle_mouse_button(event)
            if event.key == K_q:
                self._close_selected = True

    def handle_mouse_button(self, event):
        self._small_dot.randomize_dot()
        self._big_dot.randomize_dot()

    def draw_game(self):
        self._window.clear()
        self.draw_score()
        self._big_dot.draw() # this can also be game.big_dot.draw()
        self._small_dot.draw()
        self._window.update()

    def update_game(self):
        # move big dot
        self._big_dot.move_dot()

        # move small dot
        self._small_dot.move_dot()

        # control frame rate
        self._clock.tick(self._frame_rate)
        self._score = get_ticks() // 1000

    def draw_score(self):
        string = 'Score: ' + str(self._score)
        self._window.draw_string(string, 0, 0)


class Dot:
    def __init__(self, color, radius, center, speed, window):
        self._color = color
        self._center = center
        self._radius = radius
        self._velocity = speed
        self._window = window

    def draw(self):
        surface = self._window.get_surface()
        color = Color(self._color)
        draw_circle(surface, color, self._center, self._radius)

    def randomize_dot(self):
        size = [self._window.get_width(), self._window.get_height()]
        for index in range(0, 2):
            self._center[index] = randint(self._radius, size[index] - self._radius)

    def move_dot(self):
        # Change the location and the velocity of the dot so it
        # remains on the surface by bouncing from its edges.
        # - window is the Window to move in
        # - center is the list of x int and y int coordinates
        # of the center of the dot
        # - radius is the int radius of the dot
        # - velocity is the list of horizontal int and vertical
        # int speeds of the dot

        size = [self._window.get_width(), self._window.get_height()]
        # for index in sequence 0-1
        for index in range(0, 2):
            self._center[index] = self._center[index] + self._velocity[index]
            # update centre at index
            # add velocity at index to centre at index
            if (self._center[index] + self._radius >= size[index]) or (self._center[index] <= self._radius):
                self._velocity[index] = - self._velocity[index]
            # debugging to check what happens if it is the size of the index
            # since the value of coordinates [x,y] starts at 0, assigned 0 to check it as well
            # if (center[index] >= size[index]) or (center[index] <= 0):
            # velocity[index] = - velocity[index]


def main():
    game = Game()
    game.play()

main()
