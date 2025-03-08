# Trees and Dictionaries: Part 1 (Trees/bTree) - Donna Bui - 3/25/2023 - Professor Henry Estrada's COMSC 078
# This program will print the contents, label, branches, and number of leaves in a tree created using nested expressions.

# Source code from textbook
def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
    
def is_leaf(tree):
    return not branches(tree)

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)
    
    
# Driver method    
def main():
    t = tree(4, [ tree(2, [tree(1),tree(3)]) , tree(6, [tree(5)]) ] ) 
    print("Contents of tree:", t)
    print("Label:", label(t))
    print("Branches:", branches(t))
    print("Leaves:", count_leaves(t))
    
main()

""" Visualizing the tree:
 t = tree(4, # Label
             [ # Bracket containing branches
                 tree(2, # Branch
                      [tree(1), tree(3)] # Leaves
                 ) # End of branch
            , 
                tree(6, # Branch
                     [tree(5)] # Leaf
                ) # End of branch
             ] # Close bracket containing branches
        ) # Close tree
"""
