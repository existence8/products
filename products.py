#PYTHON輕鬆學會寫程式#61 計帳程式練習
products = []

while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入價格：')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])
#這邊印出每個p裡的第一格，也就是商品名稱

