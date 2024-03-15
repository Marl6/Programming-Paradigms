#here we created an array of products
product_names = ["Shirt", "Headphones", "Monitor", "Cable"]

# we then created a variable named filtered_names in which we save the products having characters more than 5
filtered_names = [name for name in product_names if(len(name)>=5)]

# we then print the list generated after iterating through our product_names array
print(filtered_names)
