def craft_item(inventory, recipes, item_name):
    if item_name not in recipes:
        raise KeyError("Recipe unknown")
    
    for ingredient, required_qty in recipes[item_name].items():
        if ingredient not in inventory or inventory[ingredient] < required_qty:
            raise ValueError("Missing ingredients")
    for ingredient, required_qty in recipes[item_name].items():
        inventory[ingredient] -= required_qty
    return f"Crafted {item_name}"

def craft_batch(inventory, recipes, to_craft_list):
    result = []
    
    for item_name in to_craft_list:
        try:
            result.append(craft_item(inventory, recipes, item_name))
        except KeyError:
            print("Recipe unknown")
        except ValueError:
            print("Missing ingredients")
    
    return result

# Format: {Item: {Ingredient: Qty, Ingredient: Qty}}
recipes = {
    "Sword": {"Iron": 2, "Wood": 1},
    "Shield": {"Wood": 4}
}

# Current Inventory
inventory = {"Iron": 5, "Wood": 2, "Sword": 0}

queue = [
    "Sword",        # Valid. Consumes 2 Iron, 1 Wood. (Rem: 3 Iron, 1 Wood)
    "Shield",       # Error: Needs 4 Wood, have 1.
    "LaserGun",     # Error: Recipe unknown
    "Sword"         # Valid: Needs 1 Wood, have 1. Needs 2 Iron, have 3.
]
output = craft_batch(inventory, recipes, queue)
print(output)