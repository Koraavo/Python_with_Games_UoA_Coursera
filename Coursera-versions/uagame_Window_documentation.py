# This module provides support for simple graphical games.

class Window:
    # A Window represents a display window with a title bar,
    # close box and interior drawing surface.

    Window(title, width, height):
    # Create and open a window to draw in.
    # - title is the str title of the window
    # - width is the int pixel width of the window
    # - height is the int pixel height of the window

    close():
    # Close the window

    set_font_name(name):
    # Set the name of the window font used to draw strings
    # - name is the str name of the font

    set_font_size(point_size):
    # Set the point size of the window font used to draw strings
    # - point_size is the int point size of the font

    set_font_color(color_string):
    # Set the font color used to draw in the window
    # - color_string is the str name of the font color

    set_bg_color(color_string):
    # Set the background color used to draw in the window
    # - color_string is the str name of the background color

    get_font_color():
    # Return a str that represents the current window
    # font color

    get_bg_color():
    # Return a str that represents the current window
    # background color

    get_width():
    # Return the int pixel width of the window's drawable
    # interior surface

    get_height(self):
    # Return the int pixel height of the window's drawable
    # interior surface

    clear():
    # Erase the window contents

    get_font_height():
    # Return the int pixel height of the current font.

    get_surface():
    # Return the Pygame.Surface object that represents the
    # interior drawing surface of the window

    draw_string(string, x, y):
    # Draw a string in the window using the current font and
    # colors
    # - string is the str object to draw
    # - x is the int x coord of the upper left corner of the
    #   string in the window
    # - y is the int y coord of the upper left corner of the
    #   string in the window

    input_string(prompt, x, y):
    # Draw a prompt string in the window using the current font
    # and colors. Check keys pressed by the user until an enter
    # key is pressed and return the sequence of key presses as a
    # str object.
    # - prompt is the str to display
    # - x is the int x coord of the upper left corner of the
    #   string in the window
    # - y is the int y coord of the upper left corner of the
    #   string in the window

    get_string_width(string):
    # Return the int pixel width of the string using the current
    # font.
    # - string is the str object

    update():
    # Update the window by copying all drawn objects from the
    # frame buffer to the display.
