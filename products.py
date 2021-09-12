#PYTHON輕鬆學會寫程式#61 計帳程式練習

products = []

#檢查舊檔是否存在
import os #operating system
if os.path.isfile('products.csv'):
	print('找到舊檔!')

	#讀取舊檔 (#65-66)
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #continue是跳過本次迴圈中剩餘動作，繼續下一迴圈
			products.append(line.strip().split(','))
		print(products)
else:
	print('找不到舊案!')

#使用者輸入
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入價格：')
	price = int(price)
	products.append([name, price])
print(products)

#印出所有購買記錄
for p in products:
	print(p[0], '的價格是', p[1])

#62寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')


