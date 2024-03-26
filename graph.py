import pygame
import random
import math

# Define constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
DOT_RADIUS = 3
MIN_DISTANCE = 200

# Define colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Function to calculate distance between two points
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Function to draw a line between two points
def draw_line(screen, p1, p2):
    pygame.draw.line(screen, BLACK, p1, p2, 1)

# Function to generate random dots
def generate_dots(num_dots):
    dots = []
    for _ in range(num_dots):
        dots.append((random.randint(50, WINDOW_WIDTH - 50), random.randint(50, WINDOW_HEIGHT - 50)))
    return dots

# Function to connect nearby dots
def connect_dots(screen, dots):
    for i, dot1 in enumerate(dots):
        for dot2 in dots[i+1:]:
            if distance(dot1, dot2) <= MIN_DISTANCE:
                draw_line(screen, dot1, dot2)

# Main function
def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Graph Animation")
    clock = pygame.time.Clock()

    # Generate random dots
    dots = generate_dots(20)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((255, 255, 255))

        # Connect nearby dots
        connect_dots(screen, dots)

        # Draw dots
        for dot in dots:
            pygame.draw.circle(screen, BLUE, dot, DOT_RADIUS)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
