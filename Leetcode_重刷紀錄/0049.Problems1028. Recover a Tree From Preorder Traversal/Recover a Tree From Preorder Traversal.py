# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, S: str) -> Optional[TreeNode]:
        nodes = []
        i, n = 0, len(S)
        while i < n:
            depth = 0
            while i < n and S[i] == '-':
                depth += 1
                i += 1
            
            val = 0
            while i < n and S[i].isdigit():
                val = val * 10 + int(S[i])
                i += 1
            
            nodes.append((depth, val))
        
        if not nodes:
            return None
        
        root = TreeNode(nodes[0][1])  
        stack = [root]
        
        for idx in range(1, len(nodes)):
            depth, val = nodes[idx]
            node = TreeNode(val)
            
            while len(stack) > depth:
                stack.pop()
            
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            
            stack.append(node)
        
        return root
