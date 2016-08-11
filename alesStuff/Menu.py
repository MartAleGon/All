import random
Menu=["Pancakes", "Sausage", "Crepes", "Eggs", "French Toast", "Bacon", "Toast","Hashbrowns", "Waffles", "Fruit"]
price= ["$8.00", "$3.00", "$9.00", "$4.00", "$10.00", "$5.00", "$6.00", "$11.00", "$3.00", "$4.00"]
menu_length=len(Menu)
price_length=len (price)
user=print("What item number would you like to know about?")
men=random.randint(0, menu_length-1)
print ("Item number " + str(men) + "?")
print("That would be the " + Menu[men])
print ("That will cost " + price[men])
