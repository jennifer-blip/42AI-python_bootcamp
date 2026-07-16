kata = "The right format"
pad_char = '-'

padded_string = f'{kata:{pad_char}>41}'

print(len(kata.rjust(42, '-')))
print(len(padded_string))