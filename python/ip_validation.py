def is_valid_IP(strng):
    arr = strng.split('.')
    for i in arr:
        if i.isdigit() == False or len(i) != 1 and int(i[0]) == 0 or int(i) < 0 or int(i) > 255:
            return False

    if len(arr) != 4:
        return False

    return True


print(is_valid_IP('12.255.56.1'))
print(is_valid_IP(''))
print(is_valid_IP('abc.def.ghi.jkl'))
print(is_valid_IP('123.456.789.0'))
print(is_valid_IP('12.34.56'))
print(is_valid_IP('123.045.067.089'))
