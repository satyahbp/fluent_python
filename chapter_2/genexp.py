symbols = '$¢£¥€¤'
symbols_ord = tuple(ord(symbol) for symbol in symbols)
print(symbols_ord)

import array
created_array = array.array("I", (ord(x) for x in symbols))
print(created_array)