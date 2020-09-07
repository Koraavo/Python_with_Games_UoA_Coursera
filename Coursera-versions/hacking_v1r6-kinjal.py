# Hacking Version 6
# This is a graphical password guessing game that displays a
# list of potential computer passwords. The player is allowed
# up to 4 attempts to guess the password. Each time the user
# guesses incorrectly, the user is prompted to make a new guess.
# The game indicates whether the player successfully guessed
# the password or not.

from uagame import Window
from time import sleep

def main():
    location = [0, 0]
    window = create_window()
    string_height = window.get_font_height()
    attempts_left = 4
    display_header(window, attempts_left, location)
    password = display_password_list(window, location)
    guess = get_guesses(window, location, password, attempts_left)
    end_game(window, guess, password)


def create_window():
    # Create a window for the game, open it and return it
    window = Window('Hacking', 600, 500)
    window.set_font_name('couriernew')
    window.set_font_size(18)
    window.set_font_color('green')
    window.set_bg_color('black')
    return window

def display_line(window, string, location):
    # Display a string in the window and update the location
    # - window is the Window to display in
    # - string is the str to display
    # - location is a list containing the int x and int y coords
    # of where the string should be displayed and it should be
    # updated to one "line" below the top left corner of the
    # displayed string

    pause_time = 0.3
    window.draw_string(string, location[0], location[1])
    window.update()
    sleep(pause_time)
    location[1] = location[1] + window.get_font_height()


def display_header(window, attempts_left, location):
    # Display the game header
    # - window is the Window to display in
    # - location is a list containing the int x and y coords of
    # where the header should be displayed and it should be
    # updated for the next output
    # - attempts is the number of guesses allowed
    header = ['DEBUG MODE', str(attempts_left) + ' ATTEMPT(S) LEFT', '']
    for header_line in header:
        # display header line
        display_line(window, header_line, location)

def display_password_list(window, location):
    # Display the game passwords, update the location for the next
    # text and return the correct password
    # - window is the Window to display in
    # - location is a list containing the int x and y coords of
    # where the first password should be displayed and it should
    # be updated for the next output

    password_list = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS',
                     'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE',
                     'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING', '']
    for password in password_list:
        # display password line
        display_line(window, password, location)

    #   choose password
    return password_list[7]

def prompt_user(window, prompt, location):
    input = window.input_string(prompt, location[0], location[1])
    return input

def get_guesses(window, location, password, attempts_left):
    # Input multiple guesses by the player and provide feedback.
    # Return the player's final guess.
    # - window is the Window to display in
    # - password is the str correct password
    # - location is a list containing the int x and y coords of
    # where the first password prompt should be displayed
    # - attempts_left is the number of guesses left

    prompt = 'ENTER PASSWORD >'
    line_x = 0
    guess = prompt_user(window, prompt, location)

    while guess != password and attempts_left != 1:
        attempts_left = attempts_left - 1
        window.draw_string(str(attempts_left), line_x, window.get_font_height())

        check_warning(window, attempts_left, location)
        guess = prompt_user(window, prompt, location)
    return guess


def check_warning(window, attempts_left, location):
    # Check whether a lockout warning should be displayed and if so,
    # display it
    # - window is the Window to display in
    # - attempts_left is the number of guesses left

    if attempts_left == 1:
        # display warning
        # warning message
        warning = '*** LOCKOUT WARNING ***'
        x_warning = window.get_width() - window.get_string_width(warning)
        y_warning = window.get_height() - window.get_font_height()
        window.draw_string(warning, x_warning, y_warning)

    location[1] = location[1] + window.get_font_height()

def end_game(window, guess, password):
    # End the game by displaying the outcome and prompting for
    # an enter.
    # - window is the Window to display in
    # - guess is the player's guess str
    # - password is the correct password string
    # - pause_time is the number of seconds to pause after displaying
    # each result line

    window.clear()
    if guess == password:
        # create success
        outcome = [guess, '', 'EXITING DEBUG MODE', '', 'LOGIN SUCCESSFUL - WELCOME BACK', '']
        prompt = 'PRESS ENTER TO CONTINUE'
    else:
        # create failure
        outcome = [guess, '', 'LOGIN FAILURE - TERMINAL LOCKED', '', 'PLEASE CONTACT AN ADMINISTRATOR', '']
        prompt = 'PRESS ENTER TO EXIT'

    location = display_outcome(window, outcome)

    #   prompt for end
    x_space = window.get_width() - window.get_string_width(prompt)  # 600 - 253
    location[0] = x_space // 2
    prompt_user(window, prompt, location)

    #   close window
    window.close()

def display_outcome(window, outcome):
    # Display the outcome of the game: success or failure depending
    # on whether the guess equals the password or not. Return
    # the location of the line below the outcome.
    # - window is the Window to display in
    # - guess is the player's guess str
    # - password is the correct password string
    # - pause_time is the number of seconds to pause after displaying
    # each result line

    #      compute y coordinate
    outcome_height = (len(outcome) + 1) * window.get_font_height()  # string_height = 21
    y_space = window.get_height() - outcome_height  # (500 - 147(21*7))//2 = placement in y-axis for first one
    line_y = y_space // 2
    location = [0, line_y]

    for outcome_line in outcome:
        # display centered outcome line
        #    compute x coordinate
        x_space = window.get_width() - window.get_string_width(outcome_line)  # (600 - 341)//2 for all x axis
        location[0] = x_space // 2
        display_line(window, outcome_line, location)
    return location

main()