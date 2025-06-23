from fastapi import FastAPI, HTTPException, Query, Body
from typing import List, Optional
import item,customer,purchase

app = FastAPI()

class DataStore:
    customers = customer.Customers
    purchases = purchase.Purchases

@app.get("/customers/search")
def search_customers(name: Optional[str] = Query(None, min_length=1)):
    if name:
        matches = [c for c in DataStore.customers if name.lower() in c.name.lower()]
        print(name)
    else:
        matches = customer.Customers
    return matches

@app.get("/purchases")
def get_purchases(id: Optional[int] = Query()):
    if id:
        matches = [p for p in DataStore.purchases if id == p.customer_id]
    else:
        matches = []
    return matches

@app.get("/returns")
def get_purchases(id: Optional[int] = Query()):
    if id:
        matches = [p for p in DataStore.purchases if id == p.purchase_id]
    else:
        matches = []
    return matches

@app.post("/purchase/{purchase_id}/return")
def return_item(
    purchase_id: int,
    item_name: str = Body(..., embed=True),
    action: str = Body(..., embed=True)  
):
    purchase_obj = next((p for p in DataStore.purchases if p.purchase_id == purchase_id), None)
    if not purchase_obj:
        raise HTTPException(status_code=404, detail="Purchase not found")
    result = purchase_obj.process_return(item_name, action)
    if "processed" in result:
        return {"status": "success", "message": result}
    else:
        return {"status": "failed", "message": result}
