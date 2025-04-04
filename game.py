import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

# Initialize pygame and set up font for displaying text
pygame.init()

font = pygame.font.Font('arial.ttf', 25)

# Enum to represent possible directions for the snake's movement    
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

# Named tuple to represent points (x, y) in the game grid
Point = namedtuple('Point', 'x, y')

# RGB color definitions for the game visuals
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  
YELLOW = (255, 255, 0)  
LIGHT_GREEN = (144, 238, 144)  
DARK_GREEN = (0, 128, 0) 
LIGHT_YELLOW = (255, 255, 102)
DARK_YELLOW = (204, 204, 0)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20
SPEED = 40

# Class to represent the Snake Game with AI functionality
class SnakeGameAI:
    def __init__(self, w=640, h=480):
        """
        Initialize the game environment.
        Args:
            w: Width of the game window.
            h: Height of the game window.
        """
        self.w = w  # Game window width
        self.h = h  # Game window height

        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')

        # Initialize the game clock for controlling frame rate
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        """
        Reset the game state to start a new session.
        """
        self.direction = Direction.RIGHT    # Default direction is right

        # Initialize snake with three blocks starting at the center of the screen
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]

        self.score = 0  # Reset score to zero
        self.food = None    # Food position will be set later
        self._place_food()  # Place food randomly on the grid
        self.frame_iteration = 0    # Track frames since last reset


    def _place_food(self):
        """
        Place food at a random position on the grid.
        Ensures food does not overlap with the snake's body.
        """
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = Point(x, y)

        # If food overlaps with snake's body, reposition it recursively
        if self.food in self.snake:
            self._place_food()


    def play_step(self, action):
        """
        Execute one step of gameplay based on the given action.
        
        Args:
            action: A list representing the move [straight, right turn, left turn].
        
        Returns:
            reward: Reward for the step (+10 for eating food, -10 for collision).
            game_over: Boolean indicating whether the game ended.
            score: Current score after this step.
        """
        self.frame_iteration += 1
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # 2. move
        self._move(action) # update the head
        self.snake.insert(0, self.head)
        
        # 3. check if game over
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score

        # 4. place new food or just move
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()
        
        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)
        # 6. return game over and score
        return reward, game_over, self.score


    def is_collision(self, pt=None):
        """
        Check if a point collides with boundaries or snake itself.
        
        Args:
            pt: Point to check collision for. Defaults to snake's head.
        
        Returns:
            Boolean indicating whether a collision occurred.
        """
        if pt is None:
            pt = self.head
        # hits boundary
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        # hits itself
        if pt in self.snake[1:]:
            return True

        return False


    def _update_ui(self):
        """
        Update the game's graphical user interface (UI).
        
        Draws background, snake body, food item, and score text.
        """
        self.display.fill(BLACK)

        for pt in self.snake:
            pygame.draw.rect(self.display, DARK_GREEN, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, LIGHT_GREEN, pygame.Rect(pt.x+4, pt.y+4, 12, 12))

        pygame.draw.rect(self.display, YELLOW, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()


    def _move(self, action):
        """
       Move snake's head based on action [straight/right/left].
       
       Args:
           action: A list representing movement direction [straight/right turn/left turn].
       """
        # [straight, right, left]
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx] # no change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx] # right turn r -> d -> l -> u
        else: # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx] # left turn r -> u -> l -> d

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)