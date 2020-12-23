# Sorting Algorithm Viz
# Suraj Khati, 2020
# rld10.mp3 download link: https://www.youtube.com/watch?v=Ig_MvAck8gg&t=191s
# Rename the file as 'rld10.mp3' and save it in the same directory as
# SortAlgoViz.py file.

import pygame, random

# To check if the music file exists
import os.path
from os import path

## ---- Variables ---- ##

# Colors

white = (255, 255, 255)
black = (0, 0, 0)
red   = (255, 0, 0)
green = (0, 255, 0)

# System Vars

method_list = ['BubbleSort',
               'SelectSort',
               'MergeSort',
               'InsertionSort']

method_index = 0

already_sorted = False

screen_width  = 1024
screen_height = 256
scale = 1
sort_speed = 5
draw_speed = 1

pause_music = False

run = False
clock = pygame.time.Clock()

# Program Vars
plot_color = [random.randint(0, 255),
              random.randint(0, 255),
              random.randint(0, 255)]
array = []

# Screen Vars
foreground = pygame.Surface((screen_width, screen_height))
final_screen = pygame.display.set_mode((screen_width * scale, screen_height * scale))

## ---- Variables ---- ##


## ---- Functions ---- ##
# ---- Utility Functions ---- #

def clear_console():
    print("\n" * 1024)

def update_caption():
    caption = "SortAlgoViz"
    caption += " | Algo: " + method_list[method_index]
    caption += " | Speed: " + str(sort_speed) + " ms"
    caption += " | Sorted: " + str(already_sorted)
    pygame.display.set_caption(caption)

def print_help():
    print("\n---- Sorting Algo Viz ----")
    print("Suraj Khati, 2020\n")

    print("To the uninitiated, keygen music is THE best music. This one's RLD10.\n")
    print("Speed (in ms): " + str(sort_speed))
    print("Array size (w, h): " + str(screen_width) + ", " + str(screen_height))
    print("Current Algorithm: " + method_list[method_index])
    
    print("\nHere is the list of keys you can press to control the program: \n")
    print("[m]     -> Play/Stop Music")
    print("[q]     -> Quit")
    print("[r]     -> Generate new array")
    print("[ENTER] -> Sort the array")
    print("[c]     -> Cycle through Sorting Algorithms")
    print("[UP]    -> Speed up")
    print("[DOWN]  -> Slow down")


def play_pause_music():
    global pause_music
    
    if pause_music == False:
        pause_music = True
        pygame.mixer.music.stop()
    else:
        pause_music = False
        pygame.mixer.music.rewind()
        pygame.mixer.music.play(-1)

def increase_speed():
    global sort_speed
    if sort_speed == 1:
        print("\nCan't go faster than that!")
        return
    sort_speed -= 1

    update_caption()    
    print("\nIncreased speed to: " + str(sort_speed))

def decrease_speed():
    global sort_speed
    if sort_speed == 50:
        print("\nSlower than that...not much useful.")
        return
    sort_speed += 1

    update_caption()
    print("\nDecreased speed to: " + str(sort_speed))

def draw_screen():
    final_screen.blit(pygame.transform.scale(foreground, final_screen.get_rect().size), (0, 0))
    pygame.display.update()

def randomize_plot_color():
    global plot_color
    plot_color = [random.randint(0, 255),
                  random.randint(50, 255),
                  random.randint(100, 255)]


def generate_array():

    global already_sorted
    
    array.clear()
    already_sorted = False
    update_caption()
    randomize_plot_color()
    for i in range(0, screen_width):
        array.append(random.randint(1, screen_height - 1))

def plot_array(flag):
    global plot_color
    foreground.fill(black)
    
    for i in range(0, screen_width):

        if flag == 1:
            # Draw Red for a moment

            pygame.draw.line(foreground,
            red,
            (i, screen_height), (i, screen_height - array[i] + 1), 1)
            foreground.set_at((i, screen_height - array[i]), white)

            # Delay a bit
            pygame.time.delay(draw_speed)
            draw_screen()

        if flag == 2:
            # Draw the actual color
            pygame.draw.line(foreground,
            green,
            # Position
            (i, screen_height), (i, screen_height - array[i] + 1), 1)
            foreground.set_at((i, screen_height - array[i]), white)
            draw_screen()

        # Draw the actual color
        pygame.draw.line(foreground,

        # Plot Color Luminiosity Gradient
        ((plot_color[0]) / (screen_width + 1) * (screen_width - i + 1),
         (plot_color[1]) / (screen_width + 1) * (screen_width - i + 1),
         (plot_color[2]) / (screen_width + 1) * (screen_width - i + 1)),
        
        # Position
        (i, screen_height), (i, screen_height - array[i] + 1), 1)
        foreground.set_at((i, screen_height - array[i]), white)
            
# ---- Utility Functions ---- #
# ---- Sorting Algorithms ---- #

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        plot_array(0)
        pygame.time.delay(sort_speed)
        draw_screen()

def selection_sort(array):
    for i in range(len(array)): 
          
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(array)): 
            if array[min_idx] > array[j]: 
                min_idx = j 
                  
        # Swap the found minimum element with  
        # the first element         
        array[i], array[min_idx] = array[min_idx], array[i]

        plot_array(0)
        pygame.time.delay(sort_speed)
        draw_screen()

def merge(a, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = a[l + i] 
    for i in range(0, n2): 
        R[i] = a[m + i + 1] 
 
    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        if L[i] > R[j]: 
            a[k] = R[j] 
            j += 1
        else: 
            a[k] = L[i] 
            i += 1
        k += 1
        plot_array(0)
        pygame.time.delay(sort_speed)
        draw_screen()

 
    while i < n1: 
        a[k] = L[i] 
        i += 1
        k += 1
        plot_array(0)
        pygame.time.delay(sort_speed)
        draw_screen()

 
    while j < n2: 
        a[k] = R[j] 
        j += 1
        k += 1
        plot_array(0)
        pygame.time.delay(sort_speed)
        draw_screen()

def merge_sort(array):
    a = array
    current_size = 1
     
    # Outer loop for traversing Each 
    # sub array of current_size 
    while current_size < len(a) - 1: 
         
        left = 0
        # Inner loop for merge call 
        # in a sub array 
        # Each complete Iteration sorts 
        # the iterating sub array 
        while left < len(a)-1: 
             
            # mid index = left index of 
            # sub array + current sub 
            # array size - 1 
            mid = min((left + current_size - 1),(len(a)-1))
             
            # (False result,True result) 
            # [Condition] Can use current_size 
            # if 2 * current_size < len(a)-1 
            # else len(a)-1 
            right = ((2 * current_size + left - 1, 
                    len(a) - 1)[2 * current_size 
                        + left - 1 > len(a)-1]) 
                             
            # Merge call for each sub array 
            merge(a, left, mid, right)
            left = left + current_size*2
             
        # Increasing sub array size by 
        # multiple of 2 
        current_size = 2 * current_size 
            
# ---- Sorting Algorithms ---- #
# ---- Sort-Helper Functions ---- #

def sort_array(array):
    global already_sorted

    if method_index == 0:       # Bubble Sort
        bubble_sort(array)
    elif method_index == 1:     # Selection Sort
        selection_sort(array)
    elif method_index == 2:     # Merge Sort
        merge_sort(array)
    else:
        print("Invalid method.")
        return
    already_sorted = True
    update_caption()
    plot_array(2)

def cycle_method():
    
    global method_list
    global method_index
    
    if (method_index == len(method_list) - 1):
        method_index = 0
    else:
        method_index += 1
    update_caption()
    print("\nAlgo " + str(method_index) + ": " + method_list[method_index])

# ---- Sort-Helper Functions ---- #
# ---- Main Function ---- #
        
def main():

    run = True

    # Initialize Pygame
    pygame.init()
    pygame.mixer.init()
    update_caption()

    # Start Music Initially
    if path.exists("rld10.mp3"):
        if pause_music == False:
            pygame.mixer.music.load("rld10.mp3")
            pygame.mixer.music.play(-1)
    else:
        print("You must have rld10.mp3 to play it.")

    # Init Program and draw first plot
    print_help()
    generate_array()
    plot_array(1)

    # Pygame Loop

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    print("\nBye!")
                    run = False
                elif event.key == pygame.K_ESCAPE:
                    clear_console()
                elif event.key == pygame.K_c:
                    cycle_method()
                elif event.key == pygame.K_h:
                    print_help()
                    
                elif event.key == pygame.K_r:
                    print("\nGenerating new array...")
                    generate_array()
                    plot_array(1)
                    
                elif event.key == pygame.K_RETURN:
                    if already_sorted == True:
                        print("Already sorted!")
                        continue
                    print("\nSorting...")
                    sort_array(array)
                    
                elif event.key == pygame.K_m:
                    if path.exists("rld10.mp3"):
                        play_pause_music()
                    else:
                        print("You must have rld10.mp3 to play it.")

                elif event.key == pygame.K_UP:
                    increase_speed()
                elif event.key == pygame.K_DOWN:
                    decrease_speed()

        draw_screen()
        clock.tick(60)

    pygame.quit()
# ---- Main Function ---- #
## ---- Functions ---- ##

main()
