#Create the item_list
item_list = ["Laptop", "Headset", "Second monitor", "Mousepad", "USB drive", "External drive"]
print(item_list)

#Use list slicing to divide
mandatory_item_list = item_list[0:3]
optional_item_list = item_list[3:]

print(mandatory_item_list)
print(optional_item_list)

#Assign the spending limit value to a variable called limit
limit = 5000

#Create a dictionary that contains each item and its price
price_sheet = {
    "Laptop" : 1500,
    "Headset" : 100,
    "Second monitor" : 200,
    "Mousepad" : 50,
    "USB drive" : 70,
    "External drive" : 250
}
print(price_sheet)

#Initialize the cart list
shopping_cart = {}

#Define the "add_to_cart" function
def add_to_cart(item,quantity):
  shopping_cart.update({item: quantity})
  item_list.remove(item)

#Define the "create_invoice" function
def create_invoice():
  total_price = 0
  for item, quantity in shopping_cart.items():
    price = price_sheet[item]
    tax = price * 0.18
    total = (tax + price) * quantity
    total_price += total
    print("item:", item, "price:", price, "quantity:", quantity, "tax:", tax, "total:", total,)
  print("after tax added:" , total_price)
  return total_price

#Define the "checkout" function
def checkout():
  global limit
  total_amount = create_invoice()
  if limit == 0:
    print("You have no limit.")
  elif total_amount > limit:
    print("It exceeds limit.")
  else:
    limit -= total_amount
    print(f"You pay {total_amount}$")

#Call the "add_to_cart" function for each item

#Add first item to cart
add_to_cart("Laptop", 1)

checkout()
