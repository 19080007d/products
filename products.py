products=[]
while True:
    name=input('enter the name of the product:')
    if name=='q':
        break
    price=input('enter the price of the product:')
    products.append([name.strip(),price.strip()])
print(products)