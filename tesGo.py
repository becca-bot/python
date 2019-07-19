from pymongo import MongoClient
client = MongoClient(host = "localhost", port = 27017)
my_db = client["tesGo"]
my_collection = my_db["items"]

class items() : #attributes of items
    def __init__(self, _id, item_name, cost, stock):
        self._id = id
        self.item_name = item_name
        self.cost = cost
        self.stock = stock

def add_item(items): #this function will allow user to insert a new record within the database#
    _id = int(input("Add a item id. Please check full item list for next id number in sequence: "))
    item_name = input("Add a item name: ")
    cost = float(input("Add cost of item: "))
    stock = input("Add number of stock this item has: ")

    item = {"_id": _id, "item_name": item_name, "cost": cost, "stock": stock}
    new_item = my_collection.insert_one(item)
    print ("A new item has been inserted")

def search_all_items(items): #function that searchs for all items. Item name and id will be shown
    for item_searches in my_collection.find({},{"_id":1,"item_name":1}):
        print(item_searches) 

def specific_item(items): # function that searched for one item
    item_choice = input("what item do you want to find? ")
    myquery = {"item_name": item_choice}
    item_search = my_collection.find_one(myquery)

    if item_search is not None:
        print(item_search)
    else:
            print("Error 101: This item is cannot found")

def update_stock(items): #This function will update the stock of the item that the user inputs.
    item_query = input("what item do you want to find? ")
    stock_level = input("Input the new stock level: ")
    myquery = {"item_name": item_query}
    newvalue = {"$set" : { "stock": stock_level}}

    update_stock_query = my_collection.update_one(myquery, newvalue)
    print ("%d item found, %d item updated"
    %(update_stock_query.matched_count, update_stock_query.modified_count))

def update_cost(items): #This function will update the cost of a item that the user inputs
    item_cost_change_query = input("what item do you want to find? ")
    item_cost = input("Input the new item cost: ")
    newquery = {"item_name": item_cost_change_query}
    new_cost_value = {"$set" : { "cost": item_cost}}

    update_cost_query = my_collection.update_one(newquery, new_cost_value)
    print ("%d item found, %d item updated"
    %(update_cost_query.matched_count, update_cost_query.modified_count))

def remove_item(items): #This function will remove a item from the database
    item_remove_choice = input("What item would you like to remove from database? ")
    new_delete_query = {"item_name": item_remove_choice}
    delete_query = my_collection.delete_one(new_delete_query)
    
    print("\nDeleted %d item" %(delete_query.deleted_count))

def program_end():
        exit()

def new_query():
    print("Would you like to perform a new query? ")
    user_input = input("Yes or No: ")

    if user_input == "yes":
        program_start(items)

    elif user_input == "no":
        program_end()


def program_start(items):

    print("Hi welcome to TesGo's command line interface!\n")
    print ("We can do many different queries here.\nWhich option would you like to do? \n")

    list = ["Add a new item ",
    "Search for all items",
    "Search for one specific item",
    "Update stock of item",
    "Update cost of item",
    "Remove an item from the database"]

    for i in list:
        print(i)

    user_choice = input("Choose your option from the list above: ")
    if user_choice == "add a new item":
        add_item(items) 
        new_query()

    elif user_choice == "search for all items":
        search_all_items(items)
        new_query()

    elif user_choice == "search for one specific item":
        specific_item(items)
        new_query()

    elif user_choice == "update stock of item":
        update_stock(items)
        new_query()

    elif user_choice == "update cost of item":
        update_cost(items)
        new_query()

    elif user_choice == "remove an item from the database":
        remove_item(items)
        new_query()

    else:
        print("\nInvalid reponse given. Check spelling and try again\n")
        program_start(items)


program_start(items)

client.close()











