class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def calculate_sum(root, s, res):
    if root is None:
        return (s, res)
    s = s*10 + root.value
    if root.left == None and root.right == None:
        res += s
    else:
        s, res = calculate_sum(root.left, s, res)
        s, res = calculate_sum(root.right, s, res)
    return ((s - root.value)//10, res)

def find_sum(root):
    print(calculate_sum(root, 0, 0)[1])

def construct_tree():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    find_sum(root)
    
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    find_sum(root)
    
if __name__ == '__main__':
    construct_tree()