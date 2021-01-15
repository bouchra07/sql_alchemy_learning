from category_hierarchy import CategoryHierarchy
from category import Category
from tariff import Tariff
from tariff_hierarchy import TariffHierarchy


t1 = TariffHierarchy()
tree=t1.get_ancestors(50)
print(tree)

anonymC = Tariff()

print(anonymC.getAncestorsByHsCode("0101.90.00"))
print(anonymC.getAncestorsById(15))

print(anonymC.getDescendantsByHsCode("0106"))
print(anonymC.getDescendantsById(139))


# c1 = CategoryHierarchy()
# tree = c1.get_ancestors("2405fd52-2d7a-4fab-b353-392ce5719995")
# print(tree)
#
#
#
# anonymC = Category()
#
# print(anonymC.getAncestorsByName("Meat and poultry2"))
# print(anonymC.getAncestorsById("2405fd52-2d7a-4fab-b353-392ce5719995"))




