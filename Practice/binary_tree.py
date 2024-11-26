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

    def find_parent(self, root, target):
        if not root:
            return None
        if root.left == target or root.right == target:
            return root

        left_parent = self.find_parent(root.left, target)
        if left_parent:
            return left_parent
        
        return self.find_parent(root.right)
    
    def find_direct_neighbors(self, root, target):
        neighbors = []

        if target.left:
            neighbors.append(target.left)
        if target.right:
            neighbors.append(target.right)

        parent = self.find_parent(root, target)
        if parent:
            neighbors.append(parent)

        return neighbors
    
    def find_k_nbors(self, target, k, res):
        if not target or k < 0:
            return []
        
        if k==0:
            res.append(target.val)
            return
        
        self.find_k_nbors(target.left, k-1, res)
        self.find_k_nbors(target.right, k-1, res)


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
        self.neighbor_color = (0, 255, 0)
        self.edge_color = (0, 255, 0)
        self.is_paused = False

    def setup_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Binary Tree Visualization")
        self.screen.fill((255, 255, 255))
        self.font = pygame.font.Font(None, 24)
        pygame.display.update()

    def draw_tree(self, node, x, y, x_offset, y_offset, visited=None, neighbors=None):
        if node:
            if node.left:
                pygame.draw.line(self.screen, self.edge_color, (x, y), (x - x_offset, y + y_offset), 2)
                self.draw_tree(node.left, x - x_offset, y + y_offset, x_offset // 2, y_offset, visited, neighbors)

            if node.right:
                pygame.draw.line(self.screen, self.edge_color, (x, y), (x + x_offset, y + y_offset), 2)
                self.draw_tree(node.right, x + x_offset, y + y_offset, x_offset // 2, y_offset, visited, neighbors)

            if visited and node in visited:
                color = self.visited_color 
            elif neighbors and node in neighbors:
                color = self.neighbor_color
            else:
                color = self.default_color 

            pygame.draw.circle(self.screen, color, (x, y), self.node_rad)
            node_val_text = self.font.render(str(node.val), True, (255, 255, 255))
            self.screen.blit(node_val_text, (x - self.node_rad // 2 + 3, y - self.node_rad // 2 + 2))
        pygame.display.update()

    def draw_instructions(self):
        instructions = [
            "Press 1 to show 'Inorder Traverse'",
            "Press 2 to show 'Preorder Traverse'",
            "Press 3 to show 'Reversed Inorder Traverse'",
            "Press 4 to show 'Postorder Traverse'",
            "Press n to show direct neighbors of node 5",
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

    def highlight_neighbors(self, neighbors):
        self.screen.fill((255, 255, 255))
        self.draw_tree(self.tree.root, self.width // 2, 50, 200, 70, None, neighbors)
        self.draw_instructions()
        pygame.display.update()
        time.sleep(1)

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
        
        if keys[pygame.K_n]:
            target = tree.root.left
            nbors = tree.find_direct_neighbors(tree.root, target)
            visualizer.highlight_neighbors(nbors)
            # visualizer.visualize_binary_tree()

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

    # getting direct neighbors
    target = tree.root.left
    print(f'\nDirect neighbors of node {target.val}')
    neighbors = tree.find_direct_neighbors(tree.root, target)
    print([node.val for node in neighbors])

    # get k distance from target neighbors
    k = 2
    res = []
    target = tree.root.left
    print(f'\nNeighbors {k} distance from node {target.val}')
    tree.find_k_nbors(target, 1, res)
    print(res)

start_term()
start_visual()
