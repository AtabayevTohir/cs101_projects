class OrderItem:
    def __init__(self,dish_name=str ,unit_price = float,portions = int):
        self.dish_name = dish_name
        self.unit_price = unit_price
        self.portions=  portions

    def __str__(self):
        return f"{self.dish_name}: {self.portions} portion(s) at ${self.unit_price}"
    
    def __repr__(self):
        return f"OrderItem('{self.dish_name}', {self.unit_price}, {self.portions})"

    def __add__(self,other):
        if isinstance(other,OrderItem):
            if self.dish_name == other.dish_name:
                total = self.portions + other.portions
                return OrderItem(self.dish_name, self.unit_price, total)
            return NotImplemented
        if isinstance(other, int):
            total = self.portions + other
            return OrderItem(self.dish_name, self.unit_price, total)
        
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, OrderItem):
            return self.dish_name == other.dish_name and self.unit_price == other.unit_price
        return NotImplemented
    
    def __bool__(self):
        return self.portions >0
    
item1 = OrderItem("Burger", 8.5, 2)
item2 = OrderItem("Burger", 8.5, 3)
item3 = OrderItem("Salad", 5.0, 0)

print(str(item1))
print(repr(item1))
print(item1 + item2)
print(item1 + 2)
print(item1 == item2)
print(bool(item1))
print(bool(item3))
            
