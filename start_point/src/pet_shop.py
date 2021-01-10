# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount #This function is used for both add_or_remove_cash_add and add_or_remove_cash_remove tests


def  get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] += amount


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    found_pet = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_pet.append(pet)
    return found_pet #This function is used for both all_pets_by_breed_found and all_pets_by_breed_not_found tests.


def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
    return None #This function is used for both find_pet_by_name_returns_pet and find_pet_by_name_returns_None tests.



# def remove_pet_by_name(pet_shop, pet_name):
#     for pet in pet_shop["pets"]:
#         if pet["name"] == pet_name:
#             pet_shop["pets"].remove(pet)  One version of the function remove_pet_by_name that passes the test.

def remove_pet_by_name(pet_shop, pet_name):
    pet = find_pet_by_name(pet_shop, pet_name)
    pet_shop["pets"].remove(pet)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, amount):
    new_value = get_customer_cash(customer) - amount
    customer["cash"] = new_value

def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)



def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return customer