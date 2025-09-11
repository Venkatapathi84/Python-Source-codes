# Define a Node of the binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Inorder traversal: Left -> Root -> Right
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

# Preorder traversal: Root -> Left -> Right
def preorder_traversal(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Postorder traversal: Left -> Right -> Root
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')

# Sample binary tree:
#         A
#        / \
#       B   C
#      / \   \
#     D   E   F

if __name__ == "__main__":
    # Create the tree nodes
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.right = Node('F')

    print("Inorder Traversal:")
    inorder_traversal(root)  # Output: D B E A C F

    print("\nPreorder Traversal:")
    preorder_traversal(root)  # Output: A B D E C F

    print("\nPostorder Traversal:")
    postorder_traversal(root)  # Output: D E B F C A
