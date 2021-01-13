from treelib import Node, Tree

tree = Tree()

tree.create_node("Moulay Ali Cherif", 1)
tree.create_node("Mohammed I", 2, parent=1)
tree.create_node("Ismail", 3, parent=1)
tree.create_node("Rachid", 4, parent=1)
tree.create_node("Ahmed",5, parent=3)
tree.create_node("Abdul Malek", 6 , parent=3)
tree.create_node("Zin al-Abidin", 7 , parent=4)


tree.show()

print(','.join([tree[node].tag for node in tree.expand_tree(mode=Tree.WIDTH)]))
