from category import Category
from category_hierarchy import CategoryHierarchy
from category import Category

c1 = CategoryHierarchy()
tree = c1.get_ancestors("2405fd52-2d7a-4fab-b353-392ce5719995")
print(tree)



anonymC = Category()

print(anonymC.getAncestorsByName("Meat and poultry2"))
print(anonymC.getAncestorsById("2405fd52-2d7a-4fab-b353-392ce5719995"))




