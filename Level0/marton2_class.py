# %% Question 1
def hanoi_n(n, _from, to, via):
    if n == 1:
        print(f'{_from} to {to}')

    hanoi_n(n-1, _from, via, to)
    print(f'{_from} to {to}')
    hanoi_n(n-1, via, to, _from)

def hanoi_BH_a(n):
    hanoi_n(n, 0, 2, 1)
    hanoi_n(n, 3,0,1)
    hanoi_n(n, 2,3,1)

def hanoi_BH_b(n):
    hanoi_n(n-1,0,1,2)
    hanoi_n(1,0,2,None)
    hanoi_n(n,3,0,2)
    hanoi_n(1,2,3,None)
    hanoi_n(n-1,1,3,2)


# %% Question 2
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next: 'Node' = None

def num_to_list(a):
    if a <= 0:
        return None

    node = Node(a % 10)
    node.next = num_to_list(a // 10)
    return node

def compare_linked_lists(node1, node2):
    if not node1 and not node2:
        return 0

    if node1 and not node2:
        return 1

    if not node1 and node2:
        return -1

    result_tail = compare_linked_lists(node1.next, node2.next)
    if result_tail == 0:
        if node1.value > node2.value:
            return 1
        elif node1.value < node2.value:
            return -1
        else:
            return 0

    return result_tail

def bubble_sort_lists(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if compare_linked_lists(lst[j], lst[j+1]) == 1:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp


def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print("None")

# %% Question 3
def climb_combinations(n):
    pass

def tomer_climb_combinations(n, steps):
    pass

# %% Question 4
from dataclasses import dataclass

@dataclass
class Node:
    value: str
    next: 'Node' = None

def s_push(s, node):
    if not s:
        return node

    if not node:
        return s

    node.next = s
    return node

def s_top(s):
    return s

def s_pop(s):
    if not s:
        return None, None

    new_s = s.next
    s.next = None
    return new_s, s


def isValid(parentheses):
    #[[}]()
    s = None
    d = {')':'(','}':'{',']':'['}

    for c in parentheses:
        if c in ['(','{','[']:
            s = s_push(s, c)
        else:
            if not s:
                return False
            else:
                s , popped = s_pop(s)
                if popped.value != d[c]:
                    return False
    return True


# %% Question 5
from dataclasses import dataclass


@dataclass
class Node:
    number: int
    next: 'Node' = None


def newSum(list1, list2):
    pass

# %% Question 6
def subsets(nums):
    ans, sol = [] , []
    backtrack(nums,len(nums),0,ans,sol)
    return ans

def backtrack(nums,n,i,ans,sol):
    if i == n:
        ans.append(sol[:])
        return

    #Don't pick nums[i]
    backtrack(nums,n,i+1,ans,sol)

    #pick nums[i]
    sol.append(nums[i])
    backtrack(nums,n,i+1,ans,sol)
    sol.pop()


# %% Question 7
def getA_sum(A):
    pass


def subarray_sum(A_sum, pos1, pos2):
    pass


def find_max_sum(A_sum, m, n):
    pass


[4,0] #log(n)
[100,120,0,1,2,3,4,5,6,7,9]

def search_a(nums):
    left , right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return left


def search_b(nums,target):
    index = search_a(nums)

    result1 = binary_search(nums,0,index,target)
    result2 = binary_search(nums,index,len(nums)-1,target)

    if result1 != -1:
        return result1

    return result2


def binary_search(nums,left,right, target):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


import pygame
import math
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Angry Birds Clone")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
GREEN = (34, 139, 34)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

# Bird settings
bird_radius = 15
initial_bird_x, initial_bird_y = 150, 350
birds = [(initial_bird_x, initial_bird_y, [0, 0], False)]  # List of birds
launching = False
mouse_pos = (0, 0)

# Obstacles
obstacles = [(500, HEIGHT - 80, 40, 80), (550, HEIGHT - 60, 40, 60)]

def draw_bird(pos):
    pygame.draw.circle(screen, RED, pos, bird_radius)

def draw_sling():
    pygame.draw.rect(screen, BROWN, (130, 330, 40, 100))

def draw_ground():
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - 20, WIDTH, 20))

def draw_target():
    pygame.draw.circle(screen, BLUE, (650, HEIGHT - 35), 20)

def draw_aim_line():
    if launching:
        pygame.draw.line(screen, BLACK, (birds[0][0], birds[0][1]), mouse_pos, 2)

def draw_reset_button():
    pygame.draw.rect(screen, BLACK, (WIDTH - 120, 20, 100, 40))
    font = pygame.font.Font(None, 30)
    text = font.render("Reset", True, WHITE)
    screen.blit(text, (WIDTH - 100, 30))

def draw_obstacles():
    for x, y, w, h in obstacles:
        pygame.draw.rect(screen, GRAY, (x, y, w, h))

def apply_physics():
    global birds
    new_birds = []
    for x, y, speed, launched in birds:
        if launched:
            x += speed[0]
            y += speed[1]
            speed[1] += 0.5  # Gravity effect

            # Collision with ground
            if y >= HEIGHT - 20 - bird_radius:
                y = HEIGHT - 20 - bird_radius
                speed[1] = -speed[1] * 0.5  # Bounce effect
                speed[0] *= 0.8  # Reduce horizontal speed
                if abs(speed[1]) < 1:
                    launched = False

        new_birds.append((x, y, speed, launched))
    birds = new_birds

def check_collision():
    global birds
    for i in range(len(birds)):
        x, y, speed, launched = birds[i]
        if math.hypot(x - 650, y - (HEIGHT - 35)) < bird_radius + 20:
            print("Target hit!")
            launched = False
        for ox, oy, ow, oh in obstacles:
            if ox < x < ox + ow and oy < y < oy + oh:
                speed[0] = -speed[0] * 0.5
                speed[1] = -speed[1] * 0.5
                launched = False
        birds[i] = (x, y, speed, launched)

def reset_game():
    global birds
    birds = [(initial_bird_x, initial_bird_y, [0, 0], False)]

def main():
    global birds, launching, mouse_pos
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)
        draw_sling()
        draw_ground()
        draw_target()
        draw_obstacles()
        for bird in birds:
            draw_bird((bird[0], bird[1]))
        draw_aim_line()
        draw_reset_button()
        apply_physics()
        check_collision()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION and launching:
                mouse_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if math.hypot(event.pos[0] - birds[0][0], event.pos[1] - birds[0][1]) < bird_radius:
                    launching = True
                    mouse_pos = event.pos
                elif WIDTH - 120 <= event.pos[0] <= WIDTH - 20 and 20 <= event.pos[1] <= 60:
                    reset_game()
            elif event.type == pygame.MOUSEBUTTONUP and launching:
                dx = birds[0][0] - event.pos[0]
                dy = birds[0][1] - event.pos[1]
                birds[0] = (birds[0][0], birds[0][1], [dx * 0.2, dy * 0.2], True)
                launching = False
                if len(birds) < 3:
                    birds.append((initial_bird_x, initial_bird_y, [0, 0], False))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
