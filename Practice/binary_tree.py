class BinaryTree:
    def __init__(self, root_val):
        self.root = Node(root_val)

    def inorder_trav(self, node):
        if node:
            self.inorder_trav(node.left)
            print(node.val, end=" ")
            self.inorder_trav(node.right)
    
    def preorder_trav(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder_trav(node.left)
            self.preorder_trav(node.right)

    def rev_inorder_trav(self, node):
        if node:
            self.rev_inorder_trav(node.right)
            print(node.val, end=' ')
            self.rev_inorder_trav(node.left)

    def postorder_trav(self, node):
        if node:
            self.postorder_trav(node.left)
            self.postorder_trav(node.right)
            print(node.val, end=' ')

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
            if visited:
                color = self.visited_color if node in visited else self.default_color
            else:
                color = self.default_color
            pygame.draw.circle(self.screen, color, (x, y), self.node_rad)
            node_val_text = self.font.render(str(node.val), True, (255,255,255))
            self.screen.blit(node_val_text, (x - self.node_rad//2+3, y-self.node_rad//2+2))
        pygame.display.update()

    def draw_instructions(self):
        instructions = [
            "Press 1 to show 'Inorder Traverse'",
            "Press 2 to show 'Preorder Traverse'",
            "Press 3 to show 'Reversed Inorder Traverse'",
            "Press 4 to show 'Postorder Traverse'",
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

            visited.add(node)
            self.screen.fill((255, 255, 255))
            self.draw_tree(self.tree.root, self.width//2, 50, 200, 70, visited)
            self.draw_instructions()
            
            time.sleep(0.5)

            self.inorder_trav(node.right, visited)
        
    def preorder_trav(self, node, visited):
        if node:
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

            visited.add(node)
            self.screen.fill((255, 255, 255))
            self.draw_tree(self.tree.root, self.width//2, 50, 200, 70, visited)
            self.draw_instructions()
            time.sleep(0.8)

            self.preorder_trav(node.left, visited)
            self.preorder_trav(node.right, visited)
    
    def rev_inorder_trav(self, node, visited):
        if node:
            self.rev_inorder_trav(node.right, visited)
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

            visited.add(node)
            self.screen.fill((255, 255, 255))
            self.draw_tree(self.tree.root, self.width//2, 50, 200, 70, visited)
            self.draw_instructions()
            time.sleep(0.8)
            self.rev_inorder_trav(node.left, visited)

    def postorder_trav(self, node, visited):
        if node:
            self.postorder_trav(node.left, visited)
            self.postorder_trav(node.right, visited)

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

            visited.add(node)
            self.screen.fill((255, 255, 255))
            self.draw_tree(self.tree.root, self.width//2, 50, 200, 70, visited)
            self.draw_instructions()
            time.sleep(0.8)



    def visualize_binary_tree(self):
        self.setup_pygame()
        self.screen.fill((255, 255, 255))
        self.draw_tree(self.tree.root, self.width // 2, 50, 200, 70, None)
        self.draw_instructions()

    def visualize_inorder_trav(self):
        visited = set()
        self.setup_pygame()
        self.inorder_trav(self.tree.root, visited)

    def visualize_preorder_trav(self):
        visited = set()
        self.setup_pygame()
        self.preorder_trav(self.tree.root, visited)

    def visualize_revinorder_trav(self):
        visited = set()
        self.setup_pygame()
        self.rev_inorder_trav(self.tree.root, visited)

    def visualize_postorder_trav(self):
        visited = set()
        self.setup_pygame()
        self.postorder_trav(self.tree.root, visited)

tree = BinaryTree(10)
tree.insert(tree.root, 5)
tree.insert(tree.root, 15)
tree.insert(tree.root, 3)
tree.insert(tree.root, 7)
tree.insert(tree.root, 12)
tree.insert(tree.root, 13)
tree.insert(tree.root, 11)
tree.insert(tree.root, 9)
tree.insert(tree.root, 18)
tree.insert(tree.root, 2)

def start_visual():
    pygame.init()
    visualizer = VisualizeTree(tree)

    run = True
    traversing = True

    visualizer.visualize_binary_tree()
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            visualizer.visualize_inorder_trav()
            time.sleep(0.5)
            visualizer.visualize_binary_tree()

        if keys[pygame.K_2]:
            visualizer.visualize_preorder_trav()
            time.sleep(0.5)
            visualizer.visualize_binary_tree()

        if keys[pygame.K_3]:
            visualizer.visualize_revinorder_trav()
            time.sleep(0.5)
            visualizer.visualize_binary_tree()

        if keys[pygame.K_4]:
            visualizer.visualize_postorder_trav()
            time.sleep(0.5)
            visualizer.visualize_binary_tree()

        if keys[pygame.K_q]:
            run = False

    pygame.quit()


def start_term():
    print('\nInorder Traverse')
    tree.inorder_trav(tree.root)
    print('\nPreorder Traverse')
    tree.preorder_trav(tree.root)
    print('\nReverse Inorder Traverse')
    tree.rev_inorder_trav(tree.root)
    print('\nPostorder Traverse')
    tree.postorder_trav(tree.root)

# start_term()
start_visual()
