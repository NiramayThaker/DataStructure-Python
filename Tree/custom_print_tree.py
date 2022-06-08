class TreeNode:
    def __init__(self, name, designation) -> None:
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None 

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, to_print):
        if to_print.lower() == "name":
            print(self.name)
        elif to_print.lower() == "designation":
            print(self.designation)
        elif to_print == "*":
            print(f"{self.name} ({self.designation})")
        else:
            print("Invalid data retrival permission ..!!")
            return

        spaces = '    ' * (self.get_level() + 1)
        prifix = spaces + "|___"

        if self.children:
            for child in self.children:
                print(prifix, end="")
                child.print_tree(to_print)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent
        return level

def built_product():
    CEO = TreeNode("Nilupul", "CEO")

    CTO = TreeNode("Chinmay", "CTO")
    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    cloud_manager = TreeNode("Dhaval", "Cloud Manager")
    app_mag = TreeNode("Abhijit", "App Manager")
    app_head = TreeNode("Amir", "Application Head")
    hr_head = TreeNode("Gels", "HR Head")
    rec_mag = TreeNode("Peter", "Recruitment Manager")
    policy_manager = TreeNode("Waqas", "Policy Manager")

    CTO.addChild(infra_head)
    
    infra_head.addChild(cloud_manager)
    infra_head.addChild(app_mag)

    CTO.addChild(app_head)

    hr_head.addChild(rec_mag)
    hr_head.addChild(policy_manager)

    CEO.addChild(CTO)
    CEO.addChild(hr_head)
    
    return CEO


if __name__ == '__main__':
    root = built_product()
    root.print_tree("*")  # Print both name and designation 
    # root.print_tree("Name")  # Print Name
    # root.print_tree("designation") # Print designation 

    print()
