# This project is a basic software for managing company inventory. In this case, the company is a shoe retailer
# The aim of this program is to show an understanding of various Python concepts with a main focus on Object Oriented Programming and classes

from tabulate import tabulate

# Class used for all products imported from text file
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        
        return self.cost

    def get_quantity(self):
        
        return self.quantity

    def __str__(self):
        
        return f'Country: {self.country}\nProduct Code: {self.code}\nProduct Name: {self.product}\nShoe Cost: {self.cost}\nQuantity: {self.quantity}\n'
    
    def __repr__(self):
        
        return f'Country: {self.country}\nProduct Code: {self.code}\nProduct Name: {self.product}\nShoe Cost: {self.cost}\nQuantity: {self.quantity}\n'


# This list will be used to store shoe objects.
shoe_list = []


# ==========Functions outside the class==============


# Defines update function which will update our text file from the object filled shoe_list
def update():

    with open('inventory.txt', 'w+') as new_data:
        new_data.write('Country,Code,Product,Cost,Quantity')
        for item in shoe_list:
            new_data.write(f'\n{item.country},{item.code},{item.product},{item.cost},{item.quantity}')


# Defines function which will read the data from the text file and add it to the 'shoe_list'
def read_shoes_data():

    while True:
        try:
            inventory_read = open('inventory.txt', 'r')
            data = inventory_read.readlines()
            for shoe_info in data:
                split_info = shoe_info.split(',')
                split_info[4] = split_info[4].strip('\n')
        
                if split_info[0] != 'Country':
                    converted_cost = float(split_info[3])
                    converted_quantity = int(split_info[4])
                    individual_shoe = Shoe(split_info[0], split_info[1], split_info[2], converted_cost, converted_quantity)
                    shoe_list.append(individual_shoe)
    
            inventory_read.close()
            break

        except FileNotFoundError:
            print('''The data file 'inventory.txt' does not exist. The program will not run without a
            data file. Make sure the data file is named 'inventory.txt' and try again.''')
            exit()


# This function will allow a user to add new shoe data. Creates new shoe object in 'shoe_list'
def capture_shoes():

    country_input = input("Enter the shoe's country of origin: ")
    code_input = input('Enter the product code: ')
    product_input = input('Enter the shoe name: ')
    cost_input = input('Enter the cost of the shoe: ')
    quantity_input = input('Enter the quantity available worldwide: ')
    new_shoe = Shoe(country_input, code_input, product_input, cost_input, quantity_input)
    shoe_list.append(new_shoe)
    update()


# Defines function to iterate over the shoes list and print the details of the shoes returned from the __str__ function
def view_all():

    tab_shoe_list = [['Country', 'Code', 'Product', 'Cost', 'Quantity']]
    for item in shoe_list:
        tab_shoe_list.append([item.country, item.code, item.product, item.cost, item.quantity])
    new_tab_shoe_list = tabulate(tab_shoe_list, headers = 'firstrow', tablefmt = 'grid')

    print(new_tab_shoe_list)


# Defines function to find lowest stock value product and choice of restocking
def re_stock():
    
    low_quant = shoe_list[0].quantity
    for shoe_info in shoe_list:
        if shoe_info.quantity < low_quant:
            low_quant = shoe_info.quantity
            temp_shoe_object = shoe_info
    print(f'{temp_shoe_object.product} has the lowest quantity with a value of {low_quant}')
    while True:

        edit_choice = input('Would you like to edit this quantity? Yes or no? ').lower()

        if edit_choice == 'yes':
            for shoe_info in shoe_list:
                if shoe_info.code == temp_shoe_object.code:
                    edit_quantity = int(input('By how much would you want to update the quantity? '))
                    shoe_info.quantity += edit_quantity
                    break
            break

        elif edit_choice == 'no':
            break
        else:
            print('You have entered an invalid option.')
            continue

    update()


# Function searches for a shoe from the list using shoe code
def search_shoe():

    shoe_code = input('Enter product code: ')
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            print(shoe)
        else:
            print('This is not a valid product code.')


# Calculate's total value for each item, prints in table.
def value_per_item():

    value_list = [['Product', 'Total Value']]
    for item in shoe_list:
        value_list.append([item.product, item.cost*item.quantity])
    new_value_list = tabulate(value_list, headers = 'firstrow', tablefmt = 'grid')
    print(new_value_list)
        

# Determines product with highest quantity, declares for sale
def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    high_quant = shoe_list[0].quantity
    for shoe_info in shoe_list:
        if shoe_info.quantity > high_quant:
            high_quant = shoe_info.quantity
            temp_shoe_object = shoe_info
    print(f'{temp_shoe_object.product} has a quantity of {temp_shoe_object.quantity}. It is now for sale.')


# ==========Main Menu=============

read_shoes_data()

while True:
    menu = input('''Select one of the following options below: 
    A - Add the data for a new type of shoe.
    B - View all the current stock data.
    C - Re-stock shoe with lowest quantity.
    D - View specific product.
    E - View total value of stock.
    F - Mark highest quantity product as for sale.
    G - Exit ''').lower()

    if menu == 'a':
        capture_shoes()
        continue

    elif menu == 'b':
        view_all()
        continue

    elif menu == 'c':
        re_stock()
        continue

    elif menu == 'd':
        search_shoe()
        continue

    elif menu == 'e':
        value_per_item()
        continue

    elif menu == 'f':
        highest_qty()
        continue

    elif menu == 'g':
        print('Goodbye.')
        exit()

    else:
        print('You have entered an invalid option. Try again.')
        continue


