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

##  a = Tree(3, None, None)
##  a.show()
##  '(3  .   . )'
##  a.left = Tree (1, None, None)
##  a.show()
##  '(3 (1  .   . )  . )'
##  a.left.right = Tree(2, None, None)
##  a.show()
##  '(3 (1  .  (2  .   . ))  . )'

    
