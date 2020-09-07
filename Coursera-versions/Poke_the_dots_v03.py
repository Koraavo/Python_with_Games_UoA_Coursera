# Poke the Dots v03
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
    pass

class Dot:
    pass

def create_window():
    window = Window('Poke the Dots', 500, 400)
    window.set_font_name('ariel')
    window.set_font_size(40)
    window.set_font_color('white')
    window.set_bg_color('black')
    return window

def main():
    window = create_window()
    game = create_game(window)
    play_game(game)
    window.close()

def create_dot(color, radius, center, speed, window):
    dot = Dot()
    dot.color = color
    dot.radius = radius
    dot.center = center
    dot.velocity = speed
    dot.window = window
    return dot

def create_game(window):
    game = Game()
    game.window = window
    game.frame_rate = 90
    game.clock = Clock()
    game.close_selected = False
    game.small_dot = create_dot('red', 20, [100, 50], [1, 2], window)
    game.big_dot = create_dot('blue', 40, [200, 100], [1, 2], window)
    randomize_dot(game.small_dot)
    randomize_dot(game.big_dot)
    game.score = 0
    return game

def draw_score(game):
    string = 'Score: ' + str(game.score)
    game.window.draw_string(string, 0, 0)

def draw_dot(dot):
    # Draw the dot on the window.
    # - window is the Window to draw in
    # - color_string is the str color of the dot
    # - center is the list of x int and y int coordinates of the
    # center of the dot
    # - radius is the int radius of the dot

    surface = dot.window.get_surface()
    color = Color(dot.color)
    draw_circle(surface, color, dot.center, dot.radius)

def draw_game(game):
    game.window.clear()
    draw_score(game)
    draw_dot(game.big_dot)
    draw_dot(game.small_dot)
    game.window.update()

def update_game(game):
    # move big dot
    move_dot(game.big_dot)

    # move small dot
    move_dot(game.small_dot)

    # control frame rate
    game.clock.tick(game.frame_rate)
    game.score = get_ticks()//1000

def play_game(game):

    while not game.close_selected:
        handle_events(game)
        draw_game(game)
        update_game(game)

def handle_events(game):
    event_list = get_events()
    for event in event_list:
        # handle one event
        if event.type == QUIT:
            game.close_selected = True
        elif event.type == MOUSEBUTTONUP:
            handle_mouse_button(game)
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                handle_mouse_button(game)
            if event.key == K_q:
                game.close_selected = True


def handle_mouse_button(game):
    randomize_dot(game.small_dot)
    randomize_dot(game.big_dot)

def randomize_dot(dot):
    size = [dot.window.get_width(), dot.window.get_height()]
    for index in range(0, 2):
        dot.center[index] = randint(dot.radius, size[index] - dot.radius)

def move_dot(dot):
    # Change the location and the velocity of the dot so it
    # remains on the surface by bouncing from its edges.
    # - window is the Window to move in
    # - center is the list of x int and y int coordinates
    # of the center of the dot
    # - radius is the int radius of the dot
    # - velocity is the list of horizontal int and vertical
    # int speeds of the dot

    size = [dot.window.get_width(), dot.window.get_height()]
    # for index in sequence 0-1
    for index in range(0, 2):
        dot.center[index] = dot.center[index] + dot.velocity[index]
        # update centre at index
        # add velocity at index to centre at index
        if (dot.center[index] + dot.radius >= size[index]) or (dot.center[index] <= dot.radius):
            dot.velocity[index] = - dot.velocity[index]
        # debugging to check what happens if it is the size of the index
        # since the value of coordinates [x,y] starts at 0, assigned 0 to check it as well
        #if (center[index] >= size[index]) or (center[index] <= 0):
            #velocity[index] = - velocity[index]

main()