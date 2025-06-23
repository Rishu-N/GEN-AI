from pydantic import BaseModel

class Item(BaseModel):
    name: str
    quantity: int
    price: float
    return_window: int = 14 
    replacement: bool = False
    
Items = [
    Item(name="iphone", quantity=2, price=500),
    Item(name="rolex", quantity=5, price=2000, return_window=60, replacement=True),
    Item(name="macbook", quantity=1, price=1200, return_window=30,replacement=True),
    Item(name="monitor", quantity=1, price=400, return_window=30),
    Item(name="ipad", quantity=3, price=800),
    Item(name="headphones", quantity=4, price=150, return_window=21, replacement=True),
    Item(name="smartwatch", quantity=2, price=350),
    Item(name="gaming_console", quantity=1, price=450, return_window=45),
    Item(name="camera", quantity=1, price=900, return_window=30, replacement=True),
    Item(name="keyboard", quantity=5, price=100, replacement=True),
    Item(name="mouse", quantity=7, price=50),
    Item(name="external_hard_drive", quantity=2, price=120, return_window=30, replacement=True),
]

def get_item(name):
    item_list = []
    for i in name:
        for item in Items:
            if item.name.lower() == i.lower():
                item_list.append(item)
    return item_list
