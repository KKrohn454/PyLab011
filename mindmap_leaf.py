import os


class MindMapLeaf:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

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
        print(" "  * indent + str(self))

    def __str__(self):
        shape_representation = MindMapLeaf.get_shape_representation(self.shape)
        return shape_representation.format(self.name)

if __name__ == "__main__":
    # Step 5: Create a MindMapLeaf object and test the __str__ and display methods.
    leaf = MindMapLeaf("Jean-Luc Picard", "circle")
    print(leaf)  # Should display "((Jean-Luc Picard))"
    leaf.display(2)  # Should display "  ((Jean-Luc Picard))" with two spaces

    print("MindMapLeaf tests completed!")