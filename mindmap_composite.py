import os


class MindMapComposite:

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    @staticmethod
    def get_shape_representation(key:str):
        shapes = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}",
            "bang": ")){}(("
        }
        return shapes.get(key, "{}")

    def display(self, indent=0):
        if indent == 0:
            print('mindmap' + os.linesep + '  root', end='')
            indent += 2
        print(" "  * indent + str(self))
        for child in self.children:
            child.display(indent + 2)


    def __str__(self):
        shape_representation = MindMapComposite.get_shape_representation(self.shape)
        return shape_representation.format(self.name)

if __name__ == "__main__":
    from mindmap_leaf import MindMapLeaf

    # Step 6: Create MindMapComposite and MindMapLeaf objects to test
    root = MindMapComposite("Root", "circle")
    leaf1 = MindMapLeaf("Child 1", "bang")
    leaf2 = MindMapLeaf("Child 2", "cloud")
    root.add(leaf1)
    root.add(leaf2)

    print(str(root))  # Should display "((Root))"
    root.display()  # Should display root and its children

    print("MindMapComposite tests completed!")