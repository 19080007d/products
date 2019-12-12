products = []
with open('products.csv', 'r', encoding='utf-8')as f:
    for line in f:
        if '商品,价格' in line:
            continue
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)
while True:
    name = input('enter the name of the product:')
    if name == 'q':
        break
    price = input('enter the price of the product:')
    products.append([name.strip(), price.strip()])
print(products)
with open('products.csv', 'w', encoding='utf-8')as f:
    f.write('商品,价格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')
