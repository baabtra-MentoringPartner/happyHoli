import pygame

# Initialize pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 800

# Set font and text
font = pygame.font.Font('Thalib.otf', 75)
text = "Happy Holi!"

# Set text position and speed
text_x = SCREEN_WIDTH
text_y = SCREEN_HEIGHT / 3
text_speed = -1

# Load decorations and images
background = pygame.image.load("holyBg_mobile.jpg")
# flowers = pygame.image.load("flowers.png")
# heart = pygame.image.load("heart.png")

# Set screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The festival of colors")

# Main loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add decorations to screen
    screen.blit(background, (0, 0))
    # screen.blit(flowers, (0, 0))
    # screen.blit(heart, (SCREEN_WIDTH - heart.get_width() - 20, SCREEN_HEIGHT - heart.get_height() - 20))

    # Add text to screen
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (text_x, text_y))

    # Update text position
    text_x += text_speed
    if text_x <= -text_surface.get_width():
        text_x = SCREEN_WIDTH

    # Update screen
    pygame.display.update()

# Quit pygame
pygame.quit()

