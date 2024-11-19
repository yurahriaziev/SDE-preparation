# aaabbccc --> 3a2b3c
# abcd --> 1a1b1c1d
# ' ' --> ''

def encode(input):
    if not input or len(input) < 0:
        return ''
    
    counter = 0
    prev_char = ''
    final_str = ''
    for i in input:
        if i == prev_char:
            counter += 1
        else:
            if prev_char != '':
                final_str += str(counter) + prev_char
            prev_char = i
            counter = 1
    final_str += str(counter) + prev_char
    return final_str

# print(encode('aaaaaaaaaaaaaaaaaa'))
print('i' not in 'test')
