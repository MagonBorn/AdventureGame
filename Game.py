# ---------- Classes ---------- #
class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece # Holds story text as string.
        self.choices = [] # List of child node references for current node.

    # Method to add a child node to a parents list of referenced nodes
    def add_child(self, node):
        self.choices.append(node) # add argument node to the invoked nodes choices list.

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
print(story_root.story_piece)
print(story_root.choices[0].story_piece)
print(story_root.choices[1].story_piece)