class BstNode:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else: # self.key > key
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


import random

b = BstNode(50)
for _ in range(10):
    number = random.randint(0, 100)
    print("Inserting", number)
    b.insert(number)
    b.display()
    print("\n------\n")

# Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
# Type "help", "copyright", "credits" or "license()" for more information.
# 
# ================= RESTART: /Users/dgerman/Desktop/lecture-06.py ================
# Inserting 45
#   50
#  /  
# 45  
# 
# ------
# 
# Inserting 90
#   50_ 
#  /   \
# 45  90
# 
# ------
# 
# Inserting 77
#   50___ 
#  /     \
# 45    90
#      /  
#     77  
# 
# ------
# 
# Inserting 41
#     50___ 
#    /     \
#   45    90
#  /     /  
# 41    77  
# 
# ------
# 
# Inserting 93
#     50___   
#    /     \  
#   45    90_ 
#  /     /   \
# 41    77  93
# 
# ------
# 
# Inserting 44
#       50___   
#      /     \  
#   __45    90_ 
#  /       /   \
# 41_     77  93
#    \          
#   44          
# 
# ------
# 
# Inserting 19
#         50___   
#        /     \  
#     __45    90_ 
#    /       /   \
#   41_     77  93
#  /   \          
# 19  44          
# 
# ------
# 
# Inserting 48
#         __50___   
#        /       \  
#     __45_     90_ 
#    /     \   /   \
#   41_   48  77  93
#  /   \            
# 19  44            
# 
# ------
# 
# Inserting 5
#          __50___   
#         /       \  
#      __45_     90_ 
#     /     \   /   \
#    41_   48  77  93
#   /   \            
#  19  44            
# /                  
# 5                  
# 
# ------
# 
# Inserting 90
#          __50___   
#         /       \  
#      __45_     90_ 
#     /     \   /   \
#    41_   48  77  93
#   /   \            
#  19  44            
# /                  
# 5                  
# 
# ------
# 

