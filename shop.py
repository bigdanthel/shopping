#Please assign your personal information to variables
name = "Joey"
surname = "Tribbiani"
age = 25
id_number = 1234567890
residence = "London"
health_insurance = True

#Write a sentence using the print function to describe yourself using the variables above in the correct data type
print(f"My name is {name} {surname}. I am {age} years old and I live in {residence}.")

#Create the item_list
item_list = ["Laptop", "Headset", "Second monitor", "Mousepad", "USB drive", "External drive"]

#Print the list
print(item_list)

#Use list slicing to divide the mandatory items
mandatory_item_list = item_list[0:3]

#Use list slicing to divide the optional items
optional_item_list = item_list[3:]

#Print both to the screen
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
  shopping_cart.append(item,quantity)
  item_list.remove(item)

#@title
#Define the "create_invoice" function
def create_invoice():
  total_price = 0
  for item, quantity in shopping_cart:
    price = price_sheet[item]
    tax = price * 0.18
    total = (tax + price) * quantity
    total_price += total
    print("item:", item, "/t", "price:", price, "/t", "quantity:", quantity, "/t", "tax:", tax, "/t", "total:", total, "/n" )
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
    print(f"You pay {total_amount}.")

#Call the "add_to_cart" function for each item

#Add first item to cart
add_to_cart("Laptop", 1)

#Add second item to cart


#Add third item to cart


#Add fourth item to cart


#Add fifth item to cart


#Add last item to cart


#Call the create "checkout" function to pay for all your items
checkout()