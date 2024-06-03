class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder_traversal(root):
    def traverse(node):
        if node:
            yield from traverse(node.left)
            yield node.val
            yield from traverse(node.right)

    return list(traverse(root))

def preorder_traversal(root):
    def traverse(node):
        if node:
            yield node.val
            yield from traverse(node.left)
            yield from traverse(node.right)

    return list(traverse(root))


def reverse_order_traversal(root):
    def traverse(node):
        if node:
            yield from traverse(node.right)
            yield node.val
            yield from traverse(node.left)

    return list(traverse(root))

# Example usage:
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

preorder_values = preorder_traversal(root)
print(preorder_values)  # [4, 2, 1, 3, 5]
print("preorder [4, 2, 1, 3, 5]")

# Example usage:
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

inorder_values = inorder_traversal(root)
print("inorder_values : [1, 2, 3, 4, 5]")
print(inorder_values)  # [1, 2, 3, 4, 5]

reverse_order_values = reverse_order_traversal(root)
print("reverse_order_values : ")
print( reverse_order_values)  # [1, 2, 3, 4, 5]