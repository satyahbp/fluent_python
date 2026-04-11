# map () and filter()

def test_map(x):
    print("in map")
    return x*2

def is_even(x):
    print("In filter")
    if x%2 == 0:
        return True
    return False

num_list = [1, 2, 3, 4, 5]
arr = map(test_map, num_list)

print(list(arr))

filtered_list = filter(is_even, num_list)

print(list(filtered_list))


symbols = '$¢£¥€¤'
mapped_symbols = list(map(ord, symbols))
beyond_ascii = list(filter(lambda c: c > 127, mapped_symbols))
print(beyond_ascii)