import string 

str = 'band, sand, brand'
substr = 'and'

def count_sub_str(str, substr):
    count = str.count(substr)
    return count

print('num times is: ', count_sub_str(str, substr))
