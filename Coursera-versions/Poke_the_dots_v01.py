# Poke the Dots v01
# The first version is supposed to open a window. with two dots
# when the player clicks close, the window is supposed to close
# the dots bounce when they touch the edges of the screen
# they start from the left corner and moves straight at a constant speed towards right

from uagame import Window
from pygame import QUIT, Color
from pygame.time import Clock
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle


def main():
    window = create_window()
    clock = Clock()
      # create small dot
    small_color = 'red'
    small_radius = 20
    small_center = [100, 50]
    small_velocity = [1, 2]

      # create big_dot
    big_color = 'blue'
    big_radius = 40
    big_center = [200, 100]
    big_velocity = [2, 1]

    play_game(window, small_color, small_center, small_radius, small_velocity, big_color, big_center, big_radius, big_velocity, clock)
    window.close()


def create_window():
    window = Window('Poke the Dots', 500, 400)
    window.set_bg_color('black')
    return window


def play_game(window, small_color, small_center, small_radius, small_velocity, big_color, big_center, big_radius, big_velocity, clock):
    close_selected = False

    while not close_selected:
        close_selected = handle_events()
        draw_game(window, big_color, big_center, big_radius, small_color, small_center, small_radius)
        update_game(window, big_center, big_radius, big_velocity, small_center, small_radius, small_velocity, clock)


def handle_events():
    closed = False
    event_list = get_events()
    for event in event_list:
        # handle one event
        if event.type == QUIT:
            closed = True

    return closed

def draw_game(window, big_color, big_center, big_radius, small_color, small_center, small_radius):
    # Draw all game objects.
    # - window is the Window to draw in
    # - small_color is the str color of the small dot
    # - small_center is the list of x int and y int coordinates
    # of the center of the small dot
    # - small_radius is the int radius of the small dot
    # - small_velocity is the list of horizontal int and vertical
    # int speeds of the small dot
    # - big_color is the str color of the big dot
    # - big_center is the list of x int and y int coordinates
    # of the center of the big dot
    # - big_radius is the int radius of the big dot
    # - big_velocity is the list of horizontal int and vertical
    # int speeds of the big dot

    window.clear()
    draw_dot(window, big_color, big_center, big_radius)
    draw_dot(window, small_color, small_center, small_radius)
    window.update()

def draw_dot(window, color_string, center, radius):
    # Draw the dot on the window.
    # - window is the Window to draw in
    # - color_string is the str color of the dot
    # - center is the list of x int and y int coordinates of the
    # center of the dot
    # - radius is the int radius of the dot

    surface = window.get_surface()
    color = Color(color_string)
    draw_circle(surface, color, center, radius)


def update_game(window, big_center, big_radius, big_velocity, small_center, small_radius, small_velocity, clock):
    # Update all game objects with state changes
    # that are not due to user events.
    # - window is the Window to move in
    # - small_center is the list of x int and y int coordinates
    # of the center of the small dot
    # - small_radius is the int radius of the small dot
    # - small_velocity is the list of horizontal int and vertical
    # int speeds of the small dot
    # - big_center is the list of x int and y int coordinates
    # of the center of the big dot
    # - big_radius is the int radius of the big dot
    # - big_velocity is the list of horizontal int and vertical
    # int speeds of the big dot
    # - clock is a Clock used to control game speed

    frame_rate = 90
    # move big dot
    move_dot(window, big_center, big_radius, big_velocity)
    # move small dot
    move_dot(window, small_center, small_radius, small_velocity)
    # control frame rate
    clock.tick(frame_rate)

def move_dot(window, center, radius, velocity):
    # Change the location and the velocity of the dot so it
    # remains on the surface by bouncing from its edges.
    # - window is the Window to move in
    # - center is the list of x int and y int coordinates
    # of the center of the dot
    # - radius is the int radius of the dot
    # - velocity is the list of horizontal int and vertical
    # int speeds of the dot

    size = [window.get_width(), window.get_height()]
    # for index in sequence 0-1
    for index in range(0, 2):
        center[index] = center[index] + velocity[index]
        # update centre at index
        # add velocity at index to centre at index
        if (center[index] + radius >= size[index]) or (center[index] <= radius):
            velocity[index] = - velocity[index]
        # debugging to check what happens if it is the size of the index
        # since the value of coordinates [x,y] starts at 0, assigned 0 to check it as well
        #if (center[index] >= size[index]) or (center[index] <= 0):
            #velocity[index] = - velocity[index]

main()
