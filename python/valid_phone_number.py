import re


def valid_phone_number(phone_number):
    if re.findall("\((\d{3})\)\s(\d{3})\-(\d{4})", phone_number) and len(phone_number) == 14:
        return True

    return False

print(valid_phone_number("(123) 456-7890"))
print(valid_phone_number("(1111)555 2345"))
print(valid_phone_number("(098) 123 4567"))
print(valid_phone_number("(123)456-7890"))
print(valid_phone_number("abc(123)456-7890"))
print(valid_phone_number("(123)456-7890abc"))
print(valid_phone_number("abc(123)456-7890abc"))
print(valid_phone_number("abc(123) 456-7890"))
print(valid_phone_number("(123) 456-7890abc"))
print(valid_phone_number("abc(123) 456-7890abc"))
print(valid_phone_number("(333) 185-0594"))
