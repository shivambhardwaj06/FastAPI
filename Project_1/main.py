from fastapi import  FastAPI , Query 
from models import MenuItem,MenuResponse
from data import menu_items
from fastapi.exceptions import HTTPException
app= FastAPI(
    title="Chai Menu API",
    description="Read Only Menu API for Kiosk displays and mobile applications.",
    version="1.0.0",
)

@app.get("/")
def root():
    return {"message": "Welcome to the Chai Menu API!"}


@app.get("/menu",response_model=MenuResponse)
def get_menu(category:str | None = Query(None, description="Filter menu items by chai,snack or combo")):
    if category : 
        filtered = [item for item in menu_items if item["category"]==category.lower()]
        if not filtered :
            raise HTTPException(status_code=404, detail=f"No menu items found for the specified category : {category}")
        return MenuResponse(count = len(filtered), items= filtered)
    return MenuResponse(count=len(menu_items),items=menu_items)

@app.get("/menu/{item_id}",response_model=MenuItem)
def get_item(item_id:int):
    for item in menu_items:
        if item["id"] == item_id:
            return item
        raise HTTPException(status_code=404,detail=f"Menu item with id : {item_id} is not found")