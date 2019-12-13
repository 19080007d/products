# 检查档案的有无
import os


def read_file(filename):
    products = []
    if os.path.isfile(filename):
        print('find it')
        # 读取档案
        with open(filename, 'r', encoding='utf-8')as f:
            for line in f:
                if '商品,价格' in line:
                    continue
                name, price = line.strip().split(',')
                products.append([name, price])

    else:
        print('not find the file')
    return products


def print_file(products):
    for p in products:
        print(p[0], '的价格是', p[1])


def user_input(products):
    # 补充档案
    while True:
        name = input('enter the name of the product:')
        if name == 'q':
            break
        price = input('enter the price of the product:')
        products.append([name.strip(), price.strip()])
    print(products)
    return products


def write_file(filename):
    # 写档案
    with open(filename, 'w', encoding='utf-8')as f:
        f.write('商品,价格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')


products = read_file('products.csv')
print_file(products)
products = user_input(products)
write_file('products.csv')
