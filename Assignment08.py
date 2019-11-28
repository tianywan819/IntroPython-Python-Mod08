# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# <Your Name>,<Today's Date>,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <TWang>,<27 Nov 2019>,Modified code to complete assignment 8
    """
    pass

    # TODO: Add Code to the Product class
    # Fields
    productname = ""
    productprice = ""

    # -- Constructor --
    def __init__(self, product_name: str, product_price: float):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # Product name

    @property  # DON'T USE NAME for this directive!
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name)  #

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    # Method
    def __str__(self):
        return self.__product_name.strip() + " "+ self.__product_price.strip()

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <TWang>,<27 Nov 2019>,Modified code to complete assignment 8
    """
    pass

    # TODO: Add Code to process data from a file
    def read_data_from_file(file_name):
        objFile = open(file_name, "r")
        for lines in objFile:
            lstOfProductObjects.append(lines)
        objFile.close()
        return lstOfProductObjects

    # TODO: Add Code to process data to a file
    def save_data_to_file(file_name, list_of_product_objects):
        if ("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):  # Double-check with user
            objFile = open(file_name, "w")
            for row in lstOfProductObjects:
                objFile.write(str(row) + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        return list_of_product_objects



# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """ Input and Output Presentation """
    pass

    # TODO: Add code to show menu to user
    @staticmethod
    def OutputMenuItems():
        print('''
                Menu of Options
                1) Show current data
                2) Add a product
                3) Save and exit program
                ''')
        print()
    # TODO: Add code to get user's choice
    def InputMenuChoice(self):
        self.choice = choice

    # TODO: Add code to show the current data from the file to user
    def LoadCurrentData():
        print("The current product are: ")
        for row in lstOfProductObjects:
            print(str(row))
        print("*********************")


    # TODO: Add code to get product data from user
    def getData():
        product_name = input("Enter product name - ")
        product_price = input("Enter product price - ")
        obj = Product(product_name,product_price)
        lstOfProductObjects.append(obj)
        print("**********************") # Added for look
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
# Show user current data in the list of product objects
# Let user add data to the list of product objects
# let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
while (True):
    IO.OutputMenuItems()  # Shows menu
    FileProcessor.read_data_from_file(strFileName)
    try:
        Input = int(input("Which option would you like to perform? [1 to 3] - "))  # Get menu option
        if input in range(1, 3):
            break
    except ValueError as e:
        print("Not a valid integer. Please Enter again.")
        print("Built-in python error info:")
        print(e, e.__doc__, type(e), sep='\n')

    # Step 3 - Process user's menu choice
    # Step 3.1 Show current data
    if (Input == 1):
        IO.LoadCurrentData()
        continue  # to show the menu
    elif (Input == 2):
       IO.getData()
       continue  # to show the menu
    elif (Input == 3):
       FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
       break  # and Exit
    else:
        print("Not a valid option")
