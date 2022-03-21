# 8-1_3 Creating Modules
from ecommerce.shopping.sales import calc_tax, calc_shipping
from ecommerce.shopping import sales

calc_tax()
calc_shipping()
sales.calc_tax

# print(dir(sales))
print(sales.__name__)
print(sales.__file__)
