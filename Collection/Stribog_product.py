import _pystribog, binascii, pyperclip
from itertools import product

i = 0
for chars in product("ABCDEF", repeat = 5):
	print(''.join(chars))
	i += 1
	if i % 100 == 0:
		print('Итерация: {}'.format(i))
	hsh = '4232d339704e170578fea8f9dea1abf88092a067459f543a5db2c8f3df44b365b9be1323161cec0b13b8c35a50e18a095699d756b2160091aa7b1276557efe69'
	h = _pystribog.StribogHash(_pystribog.Hash512)
	h_update = h.update(str(''.join(chars)))
	res = binascii.hexlify(h.digest()).decode('utf-8')
	if hsh == res:
		print('Искомый пароль: ' + ''.join(chars))
		break