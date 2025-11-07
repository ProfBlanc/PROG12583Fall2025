def order_shirt(size, shirt_type, color, payment_type, delivery_details):
    # print("Size =", size)
    # print("Shirt Type=", shirt_type)
    
    # confirm/ensure that each variable is the expected data type
    # size, shirt_type, color, payment = str
    # delivery_details = dict with keys of street, city, province, postal & country
    # "Only accept" 2 values for size, type, color and payment type
    # Only accept delivery to Brampton
    pass




order_details = {
    "size": "large",
    "shirt_type": "long-sleeve",
    "color": "black",
    "payment_type": "debit",
    "delivery_details": {
        "street" : "7899 McLaughlin Road",
        "city": "Brampton",
        "province": "Ontario",
        "postal": "A1B 2C3",
        "country": "Canada"
    }
}

my_shirt1 = order_shirt(
    size=order_details["size"],
    shirt_type=order_details["shirt_type"],
    color=order_details["color"],
    payment_type=order_details["payment_type"],
    delivery_details=order_details["delivery_details"]
    )

my_shirt2 = order_shirt(**order_details)

