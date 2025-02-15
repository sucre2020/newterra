from db.dbconnection import db
orders_collection = db['orders']

def create_order(user_id, items, total_price, status="Processing"):
    order_data = {
        "user_id": user_id,
        "items": items,
        "total_price": total_price,
        "status": status,
    }
    result = orders_collection.insert_one(order_data)
    return result.inserted_id

def get_user_orders(user_id):
    return list(orders_collection.find({"user_id": user_id}))

