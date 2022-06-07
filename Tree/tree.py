class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None 

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        spaces = '    ' * (self.get_level() + 1)
        prifix = spaces + "|___"

        if self.children:
            for child in self.children:
                print(prifix, end="")
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent
        return level

def built_product():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")

    MacBook = TreeNode("MacBook")
    asus = TreeNode("Asus")
    hp = TreeNode("HP")
    
    laptop.addChild(MacBook)
    laptop.addChild(asus)
    laptop.addChild(hp)

    phone = TreeNode("Phone")

    iphone = TreeNode("Iphone")
    samsung = TreeNode("Samsung")
    nokia = TreeNode("Nokia")

    phone.addChild(iphone)
    phone.addChild(samsung)
    phone.addChild(nokia)

    root.addChild(laptop)
    root.addChild(phone)
    
    return root

if __name__ == '__main__':
    root = built_product()
    root.print_tree()
