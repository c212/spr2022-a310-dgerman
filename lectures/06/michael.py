def largestIn(tree):
    if tree.right == None:
        return tree.value
    else:
        return largestIn(tree.right)

class Tree:
    def __init__(self, value, left, right):
        (self.value, self.left, self.right) = (value, left, right)
    def show(self):
        if self.left == None:
            left = " . "
        else:
            left = self.left.show()
        if self.right == None:
            right = " . "
        else:
            right = self.right.show()
        # return "(" + left + " " + str(self.value) + " " + right + ")"
        return "(" + str(self.value) + " " + left + " " + right + ")"
    def remove(self, value):
        if self.value == value:
            if self.left == None:
                return self.right
            else:
                a = largestIn(self.left)
                return Tree(a, self.left.remove(a), self.right)
        elif self.value > value: # I assume the value can be found in 
            return Tree(self.value, self.left.remove(value), self.right)
        else: # if the value does not exist the code needs to protect itself against that 
            return Tree(self.value, self.left, self.right.remove(value))


def main():
    a = Tree(3, None, None)
    a.right = Tree(5, None, None)
    a.right.left = Tree(4, None, None)
    print(a.show()) # (3 . (5 (4 . .) .))
    b = a.remove(5)
    print("Remove 5 the tree becomes: " + b.show())

if __name__=="__main__":
    main()

# Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
# Type "help", "copyright", "credits" or "license()" for more information.
# 
# ==================================== RESTART: /Users/dgerman/Desktop/michael.py ====================================
# (3  .  (5 (4  .   . )  . ))
# Remove 5 the tree becomes: (3  .  (4  .   . ))
