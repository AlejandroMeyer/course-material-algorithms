class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()

class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()

class NumNode:
    def __init__(self, num):
        self.num = num

    def eval(self):
        return self.num
    
def ast():
    # Building the AST
    expr = PlusNode(TimesNode(PlusNode(NumNode(5), NumNode(4)), NumNode(6)), NumNode(3))

    # Evaluating the AST
    result = expr.eval()
    print(result)  # Output: 57

ast()