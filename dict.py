phone_book = {"Alice": "0348938593", "Bob": "03048398", "Charlie" : "3849898594"}
phone_book.update(Diana = 29893748374)

phone_book["Bob"] = "3434354"
del phone_book["Charlie"]
print(phone_book)
print(phone_book.get("Eve"))        
#remove the last command from the first file cause it will return None since there is no key "Eve" #print(phone_book.get("Eve"))        
