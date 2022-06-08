class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None 

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level):
        if self.get_level() > level:
            return 

        spaces = '    ' * (self.get_level() + 1)
        prifix = spaces + "|___"

        print(prifix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent
        return level

def built_product():
    Global = TreeNode("Global")

    INDIA = TreeNode("India")
    
    guj = TreeNode("Gujarat")
    ahme = TreeNode("Ahmedabad")
    baroda = TreeNode("Baroda")

    karnataka = TreeNode("Karnataka")
    bangluru = TreeNode("Bangluru")
    Mysore = TreeNode("Mysore")

    USA = TreeNode("USA")

    new_jersey = TreeNode("New Jersey")
    princeton = TreeNode("Princeton")
    Trenton = TreeNode("Trenton")

    california = TreeNode("California")
    san_franc = TreeNode("San Francisco")
    mountain_view = TreeNode("Mountain View")
    palo_alto = TreeNode("Palo Alto")

    california.addChild(san_franc)
    california.addChild(mountain_view)
    california.addChild(palo_alto)

    new_jersey.addChild(princeton)
    new_jersey.addChild(Trenton)

    USA.addChild(new_jersey)
    USA.addChild(california)

    karnataka.addChild(bangluru)
    karnataka.addChild(Mysore)

    guj.addChild(ahme)
    guj.addChild(baroda)

    INDIA.addChild(guj)
    INDIA.addChild(karnataka)

    Global.addChild(INDIA)
    Global.addChild(USA)

    return Global


if __name__ == '__main__':
    root = built_product()
    root.print_tree(2)

    print()
