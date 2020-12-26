#Contains the data of fruitshop
fruitShop={
    "apple":50,
    "papaya":30,
    "banana":25,
    "orange":35
}

#User gives the required fruit name
fruitSelection=input("Enter the name of the fruit for its price: ").lower()


#Check if the fruit is available in the fruitShop
if fruitSelection in fruitShop:
    print("The fruit is available and the price is ",fruitShop.get(fruitSelection))
else:
    print("The fruit is not available")


