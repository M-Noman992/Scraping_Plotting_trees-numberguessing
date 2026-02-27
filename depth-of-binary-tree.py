class TreeNode:
    def __init__(self, value=0, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def findMaximumDepth(root_node: TreeNode) -> int:
    if not root_node:
        return 0
        
    left_subtree_depth = findMaximumDepth(root_node.left_child)
    right_subtree_depth = findMaximumDepth(root_node.right_child)
    
    return max(left_subtree_depth, right_subtree_depth) + 1

if __name__ == "__main__":
    root_node = TreeNode(1)
    root_node.left_child = TreeNode(2)
    root_node.right_child = TreeNode(3)
    root_node.left_child.left_child = TreeNode(4)
    root_node.left_child.right_child = TreeNode(5)
    root_node.left_child.left_child.left_child = TreeNode(6)
    
    tree_depth = findMaximumDepth(root_node)
    print("Maximum Depth of the Binary Tree:", tree_depth)