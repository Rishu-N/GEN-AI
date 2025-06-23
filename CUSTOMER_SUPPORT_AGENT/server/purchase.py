from pydantic import BaseModel
from typing import List
from datetime import date, timedelta
import item

class Purchase(BaseModel):
    customer_id: int
    purchase_id: int
    items: List[item.Item]
    purchase_date: date
    shipping_status: List[str]
    
    def is_item_returnable(self, item_name: str, current_date: date = date.today()) -> bool:
        for purchased_item in self.items:
            if purchased_item.name.lower() == item_name.lower():
                return_deadline = self.purchase_date + timedelta(days=purchased_item.return_window)
                print(f"Checking return for {item_name}: Purchase Date: {self.purchase_date}, Return Deadline: {return_deadline}, Current Date: {current_date}")
                return current_date <= return_deadline
        return False

    def process_return(self, item_name: str, action: str) -> str:
        for idx, purchased_item in enumerate(self.items):
            if purchased_item.name.lower() == item_name.lower():
                if action not in ("refund", "replace"):
                    return "Invalid action. Must be 'refund' or 'replace'."
                if not self.is_item_returnable(item_name):
                    return "invalid action"
                if action == "replace" and not purchased_item.replacement:
                    return "invalid action"
                self.shipping_status[idx] = "Refunded" if action == "refund" else "Replaced"
                return f"{action.capitalize()} processed for {item_name}."
        return f"Item {item_name} not found in this purchase."

Purchases = [
    Purchase(purchase_id=1, customer_id=1, items=item.get_item(["iphone", "rolex"]), purchase_date=date(2025, 3, 14), shipping_status=["Delivered", "Delivered"]),
    Purchase(purchase_id=2, customer_id=2, items=item.get_item(["macbook", "monitor"]), purchase_date=date(2025, 5, 6), shipping_status=["Shipped", "Shipped"]),
    Purchase(purchase_id=3, customer_id=1, items=item.get_item(["monitor"]), purchase_date=date(2025, 5, 10), shipping_status=["Shipped"]),
    Purchase(purchase_id=4, customer_id=3, items=item.get_item(["iphone", "macbook", "monitor"]), purchase_date=date(2025, 5, 23), shipping_status=["Processing", "Processing", "Processing"]),
    Purchase(purchase_id=5, customer_id=4, items=item.get_item(["ipad", "headphones"]), purchase_date=date(2025, 3, 29), shipping_status=["Delivered", "Delivered"]),
    Purchase(purchase_id=6, customer_id=5, items=item.get_item(["smartwatch"]), purchase_date=date(2025, 4, 2), shipping_status=["Delivered"]),
    Purchase(purchase_id=7, customer_id=6, items=item.get_item(["gaming_console", "camera"]), purchase_date=date(2025, 5, 19), shipping_status=["Shipped", "Shipped"]),
    Purchase(purchase_id=8, customer_id=7, items=item.get_item(["keyboard", "mouse"]), purchase_date=date(2025, 4, 25), shipping_status=["Delivered", "Delivered"]),
    Purchase(purchase_id=9, customer_id=1, items=item.get_item(["external_hard_drive"]), purchase_date=date(2025, 3, 22), shipping_status=["Delivered"]),
    Purchase(purchase_id=10, customer_id=2, items=item.get_item(["iphone", "monitor"]), purchase_date=date(2025, 3, 16), shipping_status=["Delivered", "Delivered"]),
    Purchase(purchase_id=11, customer_id=3, items=item.get_item(["rolex", "ipad"]), purchase_date=date(2025, 5, 11), shipping_status=["Shipped", "Shipped"]),
    Purchase(purchase_id=12, customer_id=4, items=item.get_item(["macbook"]), purchase_date=date(2025, 5, 8), shipping_status=["Shipped"]),
    Purchase(purchase_id=13, customer_id=5, items=item.get_item(["monitor", "headphones"]), purchase_date=date(2025, 3, 31), shipping_status=["Delivered", "Delivered"]),
    Purchase(purchase_id=14, customer_id=6, items=item.get_item(["smartwatch", "gaming_console"]), purchase_date=date(2025, 5, 1), shipping_status=["Shipped", "Shipped"]),
    Purchase(purchase_id=15, customer_id=7, items=item.get_item(["camera", "keyboard"]), purchase_date=date(2025, 4, 17), shipping_status=["Delivered", "Delivered"]),
    Purchase(purchase_id=16, customer_id=1, items=item.get_item(["mouse", "external_hard_drive"]), purchase_date=date(2025, 3, 9), shipping_status=["Delivered", "Delivered"]),
    Purchase(purchase_id=17, customer_id=2, items=item.get_item(["iphone", "rolex"]), purchase_date=date(2025, 4, 26), shipping_status=["Delivered", "Delivered"]),
    Purchase(purchase_id=18, customer_id=3, items=item.get_item(["macbook", "monitor"]), purchase_date=date(2025, 5, 28), shipping_status=["Processing", "Processing"]),
    Purchase(purchase_id=19, customer_id=4, items=item.get_item(["monitor"]), purchase_date=date(2025, 3, 4), shipping_status=["Delivered"]),
    Purchase(purchase_id=20, customer_id=5, items=item.get_item(["iphone", "macbook", "monitor"]), purchase_date=date(2025, 4, 14), shipping_status=["Delivered", "Delivered", "Delivered"]),
    Purchase(purchase_id=21, customer_id=6, items=item.get_item(["ipad", "headphones", "mouse"]), purchase_date=date(2025, 5, 13), shipping_status=["Shipped", "Shipped", "Shipped"]),
    Purchase(purchase_id=22, customer_id=7, items=item.get_item(["smartwatch", "camera"]), purchase_date=date(2025, 3, 18), shipping_status=["Delivered", "Delivered"]),
    Purchase(purchase_id=23, customer_id=1, items=item.get_item(["keyboard", "monitor"]), purchase_date=date(2025, 5, 21), shipping_status=["Processing", "Processing"]),
    Purchase(purchase_id=24, customer_id=2, items=item.get_item(["gaming_console"]), purchase_date=date(2025, 4, 20), shipping_status=["Delivered"]),
    Purchase(purchase_id=25, customer_id=3, items=item.get_item(["rolex", "external_hard_drive"]), purchase_date=date(2025, 3, 27), shipping_status=["Delivered", "Delivered"]),
]
