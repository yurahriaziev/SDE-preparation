class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.random = None

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)

# n1.next = n2
# n2.next = n3

# n1.random = n3
# n2.random = None
# n3.random = n1

'''
Traversing a linked list
'''
# current = n1
# while current is not None:
#     print(f'Node value {current.value}')
#     print(f'Next node value {current.next.value if current.next else 'None'}')
#     print(f'Random node value {current.random.value if current.random else 'None'}\n')
#     current = current.next

'''
Interleaving a linked list
'''

# current = n1
# while current is not None:
#     new_node = Node(current.value)
#     new_node.next = current.next
#     current.next = new_node
#     print(f"Original Node: {current.value}")
#     print(f"Copied Node: {current.next.value}")
#     current = new_node.next


'''
Interleaving with random pointer
'''


# def print_list(head):
#     current = head
#     while current:
#         random_val = current.random.value if current.random else 'None'
#         next_val = current.next.value if current.next else 'None'
#         print(f'[Val: {current.value}, Next: {next_val}, Random: {random_val}]')
#         current = current.next
#     print("-" * 50)

# print('\nOriginal list')
# print_list(n1)
# current = n1
# while current:
#     new_node = Node(current.value)
#     new_node.next = current.next
#     current.next = new_node
#     current

#     current = new_node.next
#     print('List after interleaving')
#     print_list(n1)


'''
Storing random values for interleaved nodes
'''

# def display_linked_list(head):
#     result = []
#     current = head
#     while current:
#         next_val = current.next.val if current.next else "None"
#         random_val = current.random.val if current.random else "None"
        
#         result.append(f"[{current.val} | Next -> {next_val}, Random -> {random_val}]")
        
#         current = current.next
    
#     print(" -> ".join(result))


# current = n1
# while current:
#     new_node = Node(current.val)
#     new_node.next = current.next
#     current.next = new_node
#     current = new_node.next


# current = n1
# while current:
#     if current.random:
#         current.next.random = current.random.next
    
#     current = current.next.next

# original = n1
# copy = n1.next
# copy_head = copy
# while original:
#     original.next = original.next.next
#     if copy.next:
#         copy.next = copy.next.next

#     original = original.next
#     copy = copy.next

'''
Merging two sorted linked lists
'''
a1 = Node(1)
a2 = Node(2)
a3 = Node(4)
a1.next = a2
a2.next = a3

b1 = Node(1)
b2 = Node(3)
b3 = Node(4)
b1.next = b2
b2.next = b3

if a1.val <= b1.val:
    head = a1
    a1 = a1.next
else:
    head = b1
    b1 = b1.next

cur = head
while a1 and b1:
    if a1.val <= b1.val:
        cur.next = a1
        a1 = a1.next
    else:
        cur.next = b1
        b1 = b1.next
    cur = cur.next

if a1:
    cur.next = a1
if b1:
    cur.next = b1

