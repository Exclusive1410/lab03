integer = []
real_numbers = []
string = ''
boolean = False

#int numbers
for i in range(1, 4):
    integer.append(int(input('Integer #{}: '.format(i))))

#real numbers
for i in range(1, 4):
    real_numbers.append(float(input('Real number #{}: '.format(i))))

#write string
string = input('Write random string:')

print('↓')

#formatting integer numbers
print('Formatted integer numbers:')
for number in integer:
    print('Integer: ', '%5.0f' % number)

print('↓')

#formatting real numbers
print('Formatted real numbers')

print('- Real numbers as numbers with floating point')
for number in real_numbers:
    print('Floating point: ', '{:10}'.format(number))

print('- Real numbers as numbers with fixed point')
for number in real_numbers:
    print('Fixed point: ', f'{number:6.3f}')

print('↓')

#formatting string
print('Formatted string (5 symbols in 1 line)')

for i in range(0, int(len(string)/5) + 1):
    print(string[i*5:(i*5 + 5)])

print('↓')

#formatting boolean
print('Formatted boolean (false):')
print(boolean)