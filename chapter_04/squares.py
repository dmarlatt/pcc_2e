squares = [value ** 2 for value in range(1, 11)]
print(squares)

# List Comprehension (creating list of tuples of a value and 2 raised to the value, so (x, 2^x))
pow_of_twos = [(value, 2 ** value) for value in range(1, 9)]
print(pow_of_twos, end='\t')
print(type(pow_of_twos))

for pow_of_two in pow_of_twos:
    print(pow_of_two, end='; ')
last_pow_of_two = pow_of_twos[-1:][0]
print(type(last_pow_of_two))
print(last_pow_of_two)
print(last_pow_of_two[0], last_pow_of_two[1], sep='|')
