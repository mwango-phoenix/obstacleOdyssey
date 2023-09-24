import pygame
import time
import sys
import random

pygame.init()

# defining colours
gray = (119, 118, 110)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

# define display dimensions
width = 800
height = 600

# game display set up
display = pygame.display.set_mode((width,
                                   height))
pygame.display.set_caption("car game")
clock = pygame.time.Clock()

# Load car image and background images
carImg = pygame.image.load('./assets/car1.png')
backgr = pygame.image.load("./assets/background.jpg")
strip = pygame.image.load("./assets/strip.png")
instruction_background = pygame.image.load("./assets/instr.jpg")

# Set car height and initialize pause state
car_height = 118
car_width = 235
pause = False


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Function to create a button with specified parameters
# msg: The text to be displayed
# x, y: top-left corner of the button
# w, h: The width and height of the button
# ic: inactive colour
# ac: hover colour
# action: The action to be performed when the button is clicked


def button(msg, x, y, w, h, ic, ac, action=None):
    # Get the current mouse position
    mouse = pygame.mouse.get_pos()
    # Get the current state of mouse buttons
    click = pygame.mouse.get_pressed()

    # Check if mouse is within the button's boundaries
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        # Draw button with active color
        pygame.draw.rect(display, ac, (x, y, w, h))
        # Check if left mouse button is clicked
        # and action is specified
        if click[0] == 1 and action != None:
            # If action is "play", call the countdown()
            if action == "play":
                countdown()
             # If action is "quit", quit the game
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()

            elif action == "intro":
                intro()
            # If action is "menu", call the intro_loop() function
            elif action == "menu":
                intro_loop()
            # If action is "pause", call the paused() function
            elif action == "pause":
                paused()
            elif action == "unpause":
             # If action is "unpause", call the unpaused() function
                unpaused()

    else:
        # Draw button with inactive color
        pygame.draw.rect(display, ic, (x, y, w, h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    display.blit(textSurf, textRect)


def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        # Display background image
        intro_background = pygame.image.load("./assets/intro.jpg")
        display.blit(intro_background,
                     (0, 0))

        # Render and display "Race Car" text
        carText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Car Sim", carText)
        TextRect.center = (400, 100)
        display.blit(TextSurf, TextRect)

        # Render and display "START" button
        button("START", 150, 520, 100, 50, green, bright_green, "play")

        # Render and display "QUIT" button
        button("QUIT", 550, 520, 100, 50, red,
               bright_red, "quit")

        # Render and display "INSTRUCTION" button
        button("INSTRUCTION", 300, 520, 200,
               50, blue, bright_blue, "intro")

        pygame.display.update()
        clock.tick(50)


def intro():
    introduction = True
    while introduction:
        # Get events from queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  # Quit the game
                sys.exit()
        # Draw the instruction background
        display.blit(instruction_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)

        # Render and draw the instruction text
        textSurf, textRect = text_objects(
            "Dodge the incoming objects", smalltext)
        textRect.center = ((350), (200))
        TextSurf, TextRect = text_objects("INSTRUCTION", largetext)
        TextRect.center = ((400), (100))
        display.blit(TextSurf, TextRect)
        display.blit(textSurf, textRect)

        # Render and draw the control instructions
        stextSurf, stextRect = text_objects(
            "ARROW UP : Move Up", smalltext)
        stextRect.center = ((150), (400))
        hTextSurf, hTextRect = text_objects(
            "ARROW DOWN : Move Down", smalltext)
        hTextRect.center = ((150), (450))
        ptextSurf, ptextRect = text_objects("P : PAUSE  ", smalltext)
        ptextRect.center = ((150), (350))
        sTextSurf, sTextRect = text_objects("CONTROLS", mediumtext)
        sTextRect.center = ((350), (300))
        display.blit(sTextSurf, sTextRect)
        display.blit(stextSurf, stextRect)
        display.blit(hTextSurf, hTextRect)
        display.blit(ptextSurf, ptextRect)

        # Render and draw the 'BACK' button
        button("BACK", 600, 450, 100, 50, blue,
               bright_blue, "menu")

        pygame.display.update()  # Update the display
        clock.tick(30)  # Limit frame rate to 30 FPS


def paused():
    global pause

    # Loop for handling events during pause state
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        display.blit(instruction_background,
                     (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf',
                                     115)
        TextSurf, TextRect = text_objects("PAUSED",
                                          largetext)
        TextRect.center = (
            (width/2),
            (height/2))
        display.blit(TextSurf, TextRect)
        # Create buttons for continue, restart, and main menu
        button("CONTINUE", 150,
               450, 150, 50,
               green, bright_green, "unpause")
        button("RESTART", 350,
               450, 150, 50,
               blue, bright_blue, "play")
        button("MAIN MENU", 550,
               450, 200, 50,
               red, bright_red, "menu")
        pygame.display.update()
        clock.tick(30)


def unpaused():
    global pause
    pause = False


def countdown_background():
    # Import the necessary modules and set up the game display
    # Initialize the font for displaying text
    font = pygame.font.SysFont(None, 25)
    # Set the initial positions for the game objects
    x = (width*0.10)
    y = (height*0.4)
    # Draw the background images on the game display
    display.blit(backgr, (0, 0))
    display.blit(backgr, (backgr.get_rect().width, 0))
    display.blit(backgr, (backgr.get_rect().width*2, 0))
    display.blit(backgr, (0, 400))
    display.blit(backgr, (backgr.get_rect().width, 400))
    display.blit(backgr, (backgr.get_rect().width*2, 400))
    # Draw the side strips on the  display
    display.blit(strip, (0, 100))
    # Draw the car on the  display
    display.blit(carImg, (x, y))
    # Draw the "PAUSE" button on the game display
    button("PAUSE", 650, 0, 150, 50, blue, bright_blue, "pause")


def countdown():
    # Initialize a boolean variable to indicate if countdown is i
    # n progress
    countdown = True
    # Continue looping until countdown is complete
    while countdown:
        # Check for events in the pygame event queue
        for event in pygame.event.get():
            # If user closes the game window
            if event.type == pygame.QUIT:
                pygame.quit()  # Quit pygame
                quit()  # Quit the game
                sys.exit()  # Exit the program
        # Fill the game display with a gray color
        display.fill(gray)
        # Call a function to display the countdown background
        countdown_background()

        # Display "3" in large font at the center of the screen
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("3", largetext)
        TextRect.center = ((width/2), (height/2))
        display.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)  # Delay for 1 second

        display.fill(gray)
        countdown_background()

        # Display "2" in large font at the center of the screen
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("2", largetext)
        TextRect.center = ((width/2), (height/2))
        display.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)  # Delay for 1 second

        display.fill(gray)
        countdown_background()

        # Display "1" in large font at the center of the screen
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("1", largetext)
        TextRect.center = ((width/2), (height/2))
        display.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)  # Delay for 1 second

        display.fill(gray)
        countdown_background()

        # Display "GO!!!" in large font at the center of the screen
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("GO!!!", largetext)
        TextRect.center = ((width/2), (height/2))
        display.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)  # Delay for 1 second
        # Call the game loop function after the countdown is complete
        game_loop()

# Loading the obstacles


def obstacle(startx, starty, obs):
    if obs == 0:
        pic = pygame.image.load("./assets/obs.png")
    elif obs == 1:
        pic = pygame.image.load("./assets/obs.png")
    elif obs == 2:
        pic = pygame.image.load("./assets/obs2.png")
    elif obs == 3:
        pic = pygame.image.load("./assets/obs4.png")
    elif obs == 4:
        pic = pygame.image.load("./assets/obs5.png")
    elif obs == 5:
        pic = pygame.image.load("./assets/obs6.png")
    elif obs == 6:
        pic = pygame.image.load("./assets/obs7.png")
    display.blit(pic, (startx, starty))


def score_system(passed, score):
    # Create a font object with size 25
    font = pygame.font.SysFont(None, 25)
    # Render the "Passed" text with passed parameter
    # and color black
    text = font.render("Passed: "+str(passed), True, black)
    # Render the "Score" text with score parameter and color red
    score = font.render("Score: "+str(score), True, red)
    # Draw the "Passed" text on the game display at (0, 50) coordinates
    display.blit(text, (0, 50))
    # Draw the "Score" text on the game display at (0, 30) coordinates
    display.blit(score, (0, 30))


def message_display(text):
    # Create a font object with size 80
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    # Render the given text with the created font
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((width/2), (height/2))
    # Draw the rendered text on the game display at the center of the
    # screen
    display.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("YOU CRASHED")


def car(x, y):
    display.blit(carImg, (x, y))


def game_loop():
    global pause
    x = (width*0.10)
    y = (height*0.4)
    obstacle_speed = 9
    obs = 0
    y_change = 0  # Initialize y_change to 0
    obs_startx = 1200
    obs_starty = random.randrange(height - 480, 480)
    obs_height = 110
    passed = 0
    level = 0
    score = 0
    y2 = 7
    fps = 120

    # flag to indicate that the player has been crashed
    bumped = False
    # Set initial relative x-positions for the background and street
    rel_x_bg = 0
    rel_x_strip = 0

    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0


        # Update player's car position
        y += y_change

        # Set pause flag to True
        pause = True

        # Update background position
        background_speed = 5
        rel_x_bg -= background_speed
        rel_x_strip -= background_speed * 2  # Adjust the strip's scrolling speed

        # Check if the background and strip have scrolled completely to the left
        if rel_x_bg < -backgr.get_rect().width:
            rel_x_bg = 0  # Reset the relative x-position to create a seamless loop
        if rel_x_strip < -strip.get_rect().width:
            rel_x_strip = 0  # Reset the relative x-position for the strip

        # Draw the background at the current relative x-position
        display.blit(backgr, (rel_x_bg, 0))

        # Draw a second copy of the background to create the seamless scrolling effect
        display.blit(backgr, (rel_x_bg + backgr.get_rect().width, 0))

        # Draw the street at the current relative x-position
        display.blit(strip, (rel_x_strip, 100))

        # Draw a second copy of the street
        display.blit(strip, (rel_x_strip + strip.get_rect().width, 100))


        # Update obstacle positions and display them
        y2 += obstacle_speed
        obs_startx += obstacle_speed / 4

        # Call the obstacle function with the correct parameters
        obstacle(obs_startx, obs_starty, obs)

        obs_startx -= obstacle_speed

        # Update player's car position and display it
        car(x, y)

        # Update score system and display score
        score_system(passed, score)

        # Check for collision with screen edges and call crash() function if collision occurs
        if y > 490 - car_height or y < 100:
            crash()
        if y > height - (car_height+ 110):
            crash()
        if y < 100:
            crash()

        # Update obstacle positions and display them
        if obs_startx < 0:
            obs_starty = random.randrange(height - 480, 480)
            obs_startx = width
            obs = random.randrange(0, 7)
            passed += 1
            score = passed * 10

            # Check for level up and update obstacle speed, display level text, and pause for 3 seconds
            if int(passed) % 10 == 0:
                level += 1
                obstacle_speed += 2
                largetext = pygame.font.Font('freesansbold.ttf', 80)
                (textsurf, textrect) = text_objects('LEVEL' + str(level), largetext)
                textrect.center = (width / 2, height / 2)
                display.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        # Check for collision with obstacles and call crash() function if collision occurs
        if x+car_width > obs_startx:
            if y > obs_starty and y < obs_starty + obs_height or y + car_height > obs_starty and y + car_height < obs_starty + car_height:
                crash()
                print(str(y) + ": " + str(obs_starty))

        # Draw pause button
        button('Pause', 650, 0, 150, 50, blue, bright_blue, 'pause')

        # Update game display and set frames per second to 60
        pygame.display.update()
        clock.tick(60)


intro_loop()
game_loop()
pygame.quit()
quit()
