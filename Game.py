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

# Choice_a A1 Treenode
choice_a1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_a.add_child(choice_a1) # Add choice_a1 to the choice_a TreeNodes list of choices

# Choice_a A2 TreeNode
choice_a2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.
 
YOU REMAIN LOST.
""")
choice_a.add_child(choice_a2) # Add choice_a2 to the choice_a TreeNodes list of choices

# Choice_b B1 TreeNode
choice_b1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.
 
YOU REMAIN LOST.
""")
choice_b.add_child(choice_b1) # Add choice_b1 to the choice_b TreeNodes list of choices

# Choice_b B2 TreeNode
choice_b2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.
 
YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_b.add_child(choice_b2) # Add choice_b2 to the choice_b TreeNodes list of choices

# ---------- Testing Area ---------- #
print("Once Upon A Time....")
story_root.traverse()