#PYTHON輕鬆學會寫程式#61 計帳程式練習


#讀取舊檔 (#65-66)
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #continue是跳過本次迴圈中剩餘動作，繼續下一迴圈
			products.append(line.strip().split(','))
		return products

#使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入價格：')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

#印出所有購買記錄
def print_history(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#62寫入檔案
def write_file(products,filename):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

#主檔
def main():
	#檢查舊檔是否存在
	filename = 'products.csv'
	import os #operating system
	if os.path.isfile(filename):
		print('找到舊檔!')
		products=read_file(filename)
	else:
		print('找不到舊案!')

	products = user_input(products)
	print_history(products)
	write_file(products, filename)

#if __name__ == '__main__'
main()

