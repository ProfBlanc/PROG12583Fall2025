def order_shirt(size, shirt_type, color, payment_type, delivery_details):
    # print("Size =", size)
    # print("Shirt Type=", shirt_type)
    
    # confirm/ensure that each variable is the expected data type
    # size, shirt_type, color, payment = str
    # delivery_details = dict with keys of street, city, province, postal & country
    # "Only accept" 2 values for size, type, color and payment type
    # Only accept delivery to Brampton
    if isinstance(size, str) and isinstance(shirt_type, str) \
    and isinstance(color, str) and isinstance(payment_type, str) \
    and isinstance(delivery_details, dict) and "street" in delivery_details \
    and "country" in delivery_details and "postal" in delivery_details \
    and "city" in delivery_details and "province" in delivery_details \
    and size.lower() in "medium,large".split(",") \
    and shirt_type.lower() in "t-shirt,long-sleeve".split(",") \
    and color.lower() in "black,white".split(",") \
    and payment_type.lower() in "debit,cash".split(",") \
    and delivery_details['city'].lower() == "brampton":
        return f"A {size} {color} {shirt_type} shirt was ordered to {delivery_details['city']} and was paid using {payment_type}"
    
    return "Invalid values passed"

# We will be back at 9:27


def count_all_odd_digits(num):
    converted = str(num)
    odd_digits_sum = 0
    if isinstance(num, int) and len(converted) >= 5:
        for digit in converted:
            digit_value = int(digit)
            if digit_value % 2 == 1:
                odd_digits_sum += digit_value
        return odd_digits_sum


def sentance_details(text):
    punctuation = [" ", "?", ","]
    fields = "num_spaces,num_qestion_marks,num_commas,words".split(",")
    details = dict()
    details[fields[0]] = 0
    details[fields[1]] = 0
    details[fields[2]] = 0
    details[fields[3]] = list()
    
    if isinstance(text, str):
        for p in range(len(punctuation)):
            details[fields[p]] = text.count(punctuation[p])
            
        details[fields[3]] = text.split(" ")
        
        for index in range(len(details[fields[3]])):
            word = details[fields[3]][index]
            
            for p in punctuation:
                if word.endswith(p):
                    details[fields[3]][index] = word[:-1]
    return details


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


def main():
    my_shirt1 = order_shirt(
        size=order_details["size"],
        shirt_type=order_details["shirt_type"],
        color=order_details["color"],
        payment_type=order_details["payment_type"],
        delivery_details=order_details["delivery_details"]
        )

    my_shirt2 = order_shirt(**order_details)


    print(my_shirt1)
    print(my_shirt2)

    result = count_all_odd_digits(12345)
    print(result)

if __name__ == "__main__":
    main()
