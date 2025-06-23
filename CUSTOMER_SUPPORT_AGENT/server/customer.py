from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    name: str
    
Customers = [
    Customer(id=1, name="Alice"),
    Customer(id=2, name="Bob"),
    Customer(id=3, name="Charlie"),
    Customer(id=4, name="Diana"),
    Customer(id=5, name="Ethan"),
    Customer(id=6, name="Fiona"),
    Customer(id=7, name="George"),
]
