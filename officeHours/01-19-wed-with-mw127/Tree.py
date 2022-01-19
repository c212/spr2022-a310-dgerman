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

def main():
    a = Tree(3, None, None)
    print(largestIn(a)) # 3
    a .right = Tree(5, None, None)
    print(largestIn(a)) # 5

if __name__=="__main__":
    main()
