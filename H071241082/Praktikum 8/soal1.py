import re

def validate_string(s: str) -> bool:
    if len(s) != 45:
        return False
    
    pattern = r'^[A-Za-z02468]{40}[13579\s]{5}$'

    return bool(re.match(pattern, s))


input_string = input("Masukkan string: ")
print(validate_string(input_string))  
