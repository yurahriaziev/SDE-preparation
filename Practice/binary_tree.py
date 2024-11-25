class BinaryTree:
    def __init__(self, root_val):
        self.root = Node(root_val)

    def inorder_trav(self, node):
        if node:
            self.inorder_trav(node.left)
            print(node.val, end=" ")
            self.inorder_trav(node.right)

    # adding a new node to the tree
    def insert(self, current, val):
        if val < current.val:
            if current.left:
                self.insert(current.left, val)
            else:
                # self.insert(current.right, val)
                current.left = Node(val)
        else:
            if current.right:
                self.insert(current.right, val)
            else:
                current.right = Node(val)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
Visualize binary tree with PyGame
'''

import pygame
import time

# visualize class
class VisualizeTree:
    def __init__(self, tree):
        self.tree = tree
        self.screen = None
        self.width = 800
        self.height = 600
        self.node_rad = 20
        self.font = None
        self.visited_color = (255, 0, 0)
        self.default_color = (0, 0, 255)
        self.edge_color = (0, 255, 0)
        self.is_paused = False

    def setup_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Binary Tree Visualization")
        self.screen.fill((255, 255, 255))
        self.font = pygame.font.Font(None, 24)
        pygame.display.update()

    def draw_tree(self, node, x, y, x_offset, y_offset, visited=None):
        if node:
            if node.left:
                pygame.draw.line(self.screen, self.edge_color, (x, y), (x-x_offset, y+y_offset), 2)
                self.draw_tree(node.left, x-x_offset, y+y_offset, x_offset//2, y_offset, visited)

            if node.right:
                pygame.draw.line(self.screen, self.edge_color, (x, y), (x+x_offset, y+y_offset), 2)
                self.draw_tree(node.right, x+x_offset, y+y_offset, x_offset//2, y_offset, visited)

            color = self.visited_color if node in visited else self.default_color
            pygame.draw.circle(self.screen, color, (x, y), self.node_rad)
            node_val_text = self.font.render(str(node.val), True, (0,0,0))
            self.screen.blit(node_val_text, (x - self.node_rad//2, y-self.node_rad//2))
        pygame.display.update()

    def draw_instructions(self):
        instructions = [
            "Press 1 to show 'Inorder Traverse'",
            "Press 2 to pause the traverse",
            "Press 'q' to quit",
        ]
        y_pos = self.height - len(instructions) * 30
        for instruction in instructions:
            text_surface = self.font.render(instruction, True, (0, 0, 0))
            self.screen.blit(text_surface, (20, y_pos))
            y_pos += 30
        pygame.display.update()

    def inorder_trav(self, node, visited):
        if node:
            self.inorder_trav(node.left, visited)

            visited.add(node)
            self.screen.fill((255, 255, 255))
            self.draw_tree(self.tree.root, self.width//2, 50, 200, 70, visited)
            self.draw_instructions()

            while self.is_paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_1]:
                        self.is_paused = False
                    elif keys[pygame.K_q]:
                        pygame.quit()
                        exit()
            
            time.sleep(0.5)

            self.inorder_trav(node.right, visited)
        
    def visualize_inorder_trav(self):
        visited = set()
        self.setup_pygame()
        self.inorder_trav(self.tree.root, visited)

tree = BinaryTree(10)
tree.insert(tree.root, 5)
tree.insert(tree.root, 15)
tree.insert(tree.root, 3)
tree.insert(tree.root, 7)
tree.insert(tree.root, 12)
tree.insert(tree.root, 18)
tree.insert(tree.root, 2)

def start():
    pygame.init()
    visualizer = VisualizeTree(tree)

    run = True
    traversing = True

    while run:
        if traversing:
            visualizer.visualize_inorder_trav()
            traversing = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            traversing = True

        if keys[pygame.K_2]:
            visualizer.is_paused = True

        if keys[pygame.K_q]:
            run = False

    pygame.quit()

start()
