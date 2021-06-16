import _pystribog
import binascii
import pyperclip

h = _pystribog.StribogHash(_pystribog.Hash512)
password = "GhjcnjFkbyf777"
h_update = h.update(password)
res = binascii.hexlify(h.digest()).decode('utf-8')
pyperclip.copy(res)
print(res) 