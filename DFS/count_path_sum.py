class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def calculate_sum(root, s):
    if root is None:
        return 0
    if root.left == None and root.right == None and root.value == s:
        return 1
    left_c = calculate_sum(root.left, s - root.value)
    right_c = calculate_sum(root.right, s - root.value)
    return left_c + right_c

def find(root, s):
    print(calculate_sum(root, s))

def construct_tree():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)
    find(root, 12)
    
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    find(root, 23)
    
if __name__ == '__main__':
    construct_tree()