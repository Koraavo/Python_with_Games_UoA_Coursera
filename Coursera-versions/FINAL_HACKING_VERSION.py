# Hacking Version 7
# This is a graphical password guessing game that displays a
# list of potential computer passwords. The player is allowed
# up to 4 attempts to guess the password. Each time the user
# guesses incorrectly, the user is prompted to make a new guess.
# The game indicates whether the player successfully guessed
# the password or not.

from uagame import Window
from time import sleep
from random import randint, choice

def main():
    location = [0, 0]
    window = create_window()
    attempts = 4
    display_header(window, location, attempts)
    password = display_password_list(window, location)
    guess = get_guesses(window, password, location, attempts)
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


def display_header(window, location, attempts):
    # Display the game header
    # - window is the Window to display in
    # - location is a list containing the int x and y coords of
    # where the header should be displayed and it should be
    # updated for the next output
    # - attempts is the number of guesses allowed
    header = ['DEBUG MODE', str(attempts) + ' ATTEMPT(S) LEFT', '']
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
                     'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING']
    embedded_size = 13

    for password in password_list:
        # display password line
        password_line = embed_password(password, embedded_size)
        display_line(window, password_line, location)

    #display blank line
    display_line(window, '', location)

    #   choose password
    return password_list[7]

def embed_password(password, size):
    # Return a fixed length with the password embedded (13)
    # somewhere in the string and padded with symbol characters
    # - password is the str to pad
    # -size is the int number of characters padded
    # computer random split index

    fill = '!@#$%^*()-+=~[]{}'
    embedding = ''
    password_size = len(password)
    split_index = randint(0, size - password_size)

    # Before password
    for index in range(0, split_index):
        embedding = embedding + choice(fill)

    # with password
    embedding = embedding + password

    # After password
    for index in range(split_index+password_size, size):
        embedding = embedding + choice(fill)

    return embedding


def prompt_user(window, prompt, location):
    # Display a prompt, input a string that the user types and
    # return the string
    # - window is the Window to display in
    # - prompt is the str to display
    # - location is a list containing the int x and int y coords
    # of where the prompt should be displayed and it should be
    # updated to one "line" below the top left corner of the
    # displayed prompt

    input = window.input_string(prompt, location[0], location[1])
    location[1] = location[1] + window.get_font_height()
    return input

def get_guesses(window, password, location, attempts_left):
    # Input multiple guesses by the player and provide feedback.
    # Return the player's final guess.
    # - window is the Window to display in
    # - password is the str correct password
    # - location is a list containing the int x and y coords of
    # where the first password prompt should be displayed
    # - attempts is the number of guesses left

    prompt = 'ENTER PASSWORD >'
    line_x = 0
    guess = prompt_user(window, prompt, location)
    x_result = window.get_width()//2
    y_result = 0
    feedback_location = [x_result, y_result]

    while guess != password and attempts_left != 1:
        attempts_left = attempts_left - 1
        window.draw_string(str(attempts_left), line_x, window.get_font_height())
        display_hint(window, password, guess, feedback_location)
        check_warning(window, attempts_left, location)
        guess = prompt_user(window, prompt, location)
    return guess

def display_hint(window, password, guess, location):
    # Display the guess and the number of correct letters
    # in the guess
    # - window is the Window to display in
    # - password is the str correct password
    # - guess is the str the player entered
    # - location is a list containing the int x and y

    index = 0
    for i in range(len(password)):
        if password[i] == guess[i]:
            index = index+1
    incorrect_message = guess + ' INCORRECT'
    display_line(window, incorrect_message, location)
    result = f'{index}/{len(password)} IN MATCHING POSITIONS'
    display_line(window, result, location)


def check_warning(window, attempts, location):
    # Check whether a lockout warning should be displayed and if so,
    # display it
    # - window is the Window to display in
    # - attempts is the number of guesses left

    if attempts == 1:
        # display warning
        # warning message
        warning = '*** LOCKOUT WARNING ***'
        x_warning = window.get_width() - window.get_string_width(warning)
        y_warning = window.get_height() - window.get_font_height()
        window.draw_string(warning, x_warning, y_warning)


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