#!/usr/bin/python
# coding:utf-8

import random
import pygame
import sys
from pygame.math import Vector2


# create the class of fruit
# logic of Fruit: if eat fruit, the size of  snake increase
# use the vector2 to record the 2D data
class Fruit:
    def __init__(self):
        self.x = random.randint(0,cell_number)
        self.y = 10
        # create an x and y position
        # draw a square
        # create a 2D vector to store the information
        self.pos = pygame.math.Vector2(self.x, self.y)

    # create a rectangle
    def draw_fruit(self):
        # draw the rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        # if you want to use the image you import, then
        screen.blit(apple,fruit_rect)
        # pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

    # recreating a fruit in another place
    def randomize(self):
        self.x = random.randint(0,cell_number)
        self.y = 10
        self.pos = pygame.math.Vector2(self.x, self.y)

# create the class of snake
class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10),Vector2(6, 10),Vector2(7, 10)]
        self.direction = Vector2(-1,0)
        self.new_block = False

        self.head_up = pygame.image.load("粑卡粑卡.png").convert_alpha()
        self.head_down = pygame.image.load("粑卡粑卡.png").convert_alpha()
        self.head_right = pygame.image.load("粑卡粑卡侧脸.png").convert_alpha()
        self.head_left = pygame.image.load("粑卡粑卡侧脸.png").convert_alpha()

        self.tail_up = pygame.image.load("憨包正面.png").convert_alpha()
        self.tail_down = pygame.image.load("憨包正面.png").convert_alpha()
        self.tail_left = pygame.image.load("憨包_副本.png").convert_alpha()
        self.tail_right = pygame.image.load("憨包_副本.png").convert_alpha()

        self.body_vertical = pygame.image.load("憨包_副本.png").convert_alpha()
        self.body_horizontal = pygame.image.load("憨包_副本.png").convert_alpha()

        self.body_tr = pygame.image.load("憨包_副本.png").convert_alpha()
        self.body_tl = pygame.image.load("憨包_副本.png").convert_alpha()
        self.body_br = pygame.image.load("憨包_副本.png").convert_alpha()
        self.body_bl = pygame.image.load("憨包_副本.png").convert_alpha()

    def draw_snake(self):
        # pick the four of head/tail/body methods
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            # 1. we still need a rect for the positioning
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            # 2. what direction is the face heading
            if index == 0:
                screen.blit(self.head_right, block_rect)
                # 3.snake head direction is not updating
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                # case if go left or right
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                # case if go up or down
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_vertical, block_rect)
                # case of cornor
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)
                        # case of cornor
                    else:
                        if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                            screen.blit(self.body_tl,block_rect)
                        elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                            screen.blit(self.body_bl,block_rect)
                        elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                            screen.blit(self.body_tr,block_rect)
                        elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                            screen.blit(self.body_br,block_rect)

    # def draw_snake(self):
   #     for block in self.body:
   #         # create a rect
   #         x_pos = int(block.x * cell_size)
   #         y_pos = int(block.y * cell_size)
   #         block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
   #         # draw the rectangle
   #         pygame.draw.rect(screen,(183,111,122), block_rect)

    # Move the snake
    # update the head position

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

    def move_snake(self):
        # add a block if snake eat the fruit
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] +self.direction)
            self.body = body_copy[:]
            self.new_block = False
        # copy our entire list but only for the first two elements (so moved for one cell)
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] +self.direction)
            self.body = body_copy[:]

    # add blocks to the snake
    def add_block(self):
        self.new_block = True

    # reset the game
    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]


# Main Class
class Main:
    def __init__(self):
        # create a fruit object & snake object
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        # enable the fruit to be renewed
        self.check_collision()
        # update to check if failed
        self.check_fail()

    def draw_element(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        # see if snake's head element get the food
        if self.fruit.pos == self.snake.body[0]:
            # reposition of the fruit
            self.fruit.randomize()
            # add another block to the snake
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    # check if failed
    def check_fail(self):
        # check if snake is outside of the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
               self.game_over()

    # case for game over
    def game_over(self):
       # pygame.quit()
        # quit could only shut done part of the functions, but sys.exit() could shut down all
       # sys.exit()
        self.snake.reset()

# initialize the pygame package
pygame.init()

# set the height and width of the screen
## After we done this and run the program, we could see that a small window showed up but quickly disappeared
## In this case, this means our screen was build successfully, but it does not know how long to maintain the window
# screen = pygame.display.set_mode((1000, 800))  # set_mode(height, width)
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))

# different computers run different speed, and to make our game perform somewhat consistently,
# we need to create a clock object to set the maximum speed
clock = pygame.time.Clock()

# draw a fruit: import an image
apple = pygame.image.load('奥利给.png').convert_alpha() # convert alpha so that the system works better

SCREEN_UPDATE = pygame.USEREVENT
# the event will triggered every 150 ms
pygame.time.set_timer(SCREEN_UPDATE, 150)

# declare main object
main_game = Main()

# the loop to maintain the windows: basically put every details here
while True:
    # the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # quit could only shut done part of the functions, but sys.exit() could shut down all
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        # Critical: related the snake motion with the pressing button
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # check if our direction is in direct opposite direction (if not, then the program will shut down immediately)
                if main_game.snake.direction.y != 1:
                   main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                   main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                   main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                   main_game.snake.direction = Vector2(1, 0)


    # fill the screen with color for display surface
    # could use color object: screen.fill(pygame.Color('gold'))
    # or we could use
    screen.fill((135, 115, 70))
    # Main.fruit.draw_fruit()
   # Main.snake.draw_snake()
    main_game.draw_element()

    # draw all out elements (snake, fruit, background etc.) & update it for canvas to continue existing
    pygame.display.update()

    # the program would run no larger than 60 frame/s (); the loop less than 60 per second
    clock.tick(200)

end




# use this: x_pos += 1 ; we could get a basic animation by moving the test_surface gradually to a direction
# move the rectangle with test_rect.left += 1

# draw the rectangle to the surface
# pygame.draw.rect(screen, pygame.Color('red'), test_rect)


# put surface on display surface
# screen.blit(test_surface, (x_pos, y_pos))

# Rectangles: created by:
# 1, pygame.Rect(x,y,w,h) --> new rect
# 2, surface.get_rect(position) -> rect around surface
# test_rect = test_surface.get_rect(center = (200, 25))

# the position of the snake
# x_pos = 200
# y_pos = 250

# draw shape in the pygame
# surfaces (layer that can display graphics, only multiple, not displayed by default)
# 1, create a surface, import an image, write text, or create an empty space
# 2, display the surface, this could be the display or a regular surface
# display surface: the canvas the entire game is drawn one, there is only one, it is displayed by default
# test_surface = pygame.Surface((100, 200))  # need to be in double curly braces

# fill the test_surface with blue
# test_surface.fill(pygame.Color("blue"))



