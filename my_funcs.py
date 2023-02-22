def my_func_1():
	print('hello from my_func_1')

def my_func_2():
	print('my_func_2 says hello')

my_func_map = {	'my_func_1':my_func_1,
		'my_func_2':my_func_2 }

def try_func(func_name):
	b = True
	for itr in my_func_map.items():
		if itr[0] == func_name:
			b = False
			itr[1]()
			break
	if b:
		print('Did not find function:')
		print('\t' + itr[0])

#def main():
##	my_func_map['my_func_1']()
#	try_func('my_func_1')
#	try_func('dne')
#	try_func('my_func_2')
#
#if __name__ == "__main__":
#	main()
