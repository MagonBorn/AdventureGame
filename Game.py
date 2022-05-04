# ---------- Classes ---------- #
class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece # Holds story text as string.
        self.choices = [] # List of child node references for current node.

    # Method to add a child node to a parents list of referenced nodes
    def add_child(self, node):
        self.choices.append(node) # add argument node to the invoked nodes choices list.

    # Method to traverse the Tree and progress the story from the root node
    def traverse(self):
        story_node = self # The TreeNode Object the method is invoked on, is assigned to a variable
        print(story_node.story_piece)
        while story_node.choices: # while the current story_node has elements in its choices list
            choice = input("Enter 1 or 2 to continue the story: ") # Get users decision and save it to variable
            if choice not in ["1", "2"]: # Check user input is 1 or 2
                print("Please enter a valid option: 1 or 2")
            else:
                chosen_index = int(choice)-1 # parse user input to be an int and subtract one so it can be used for index selction
                chosen_child = story_node.choices[chosen_index] # save selected tree node to a variable using parsed chosen index
                print(chosen_child.story_piece) # print tree node story_piece
                story_node = chosen_child # set story_node to the user selected node and continue loop until we reach a node with no elements in its choices list

# ---------- Tree Nodes ---------- #
# Root TreeNode
story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")

# Root Choice A TreeNode
choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")
story_root.add_child(choice_a) # Add choice_a to the story_root TreeNodes list of choices

# Root Choice B TreeNode
choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")
story_root.add_child(choice_b) # Add choice_b to the story_root TreeNodes list of choices

# ---------- Testing Area ---------- #
print("Once Upon A Time....")
story_root.traverse()