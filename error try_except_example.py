#skip def div42by(divideBy):
#skip     return 42 / divideBy

#skip print(div42by(2))
#skip print(div42by(12))
#skip print(div42by(0))
#skip print(div42by(1))

# above code will only execute to div by 0 then error and crash, it will never get to div by 1
# because the error stops the execution due to div by zero


def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))




print('How many dogs do you have?')
numDogs = input()
if int(numDogs) >= 4:
    print('That is a lot of dogs.')
else:
    print('That is not that many dogs.')
# if a user enters an alpha numeric number this will error, example 'six'


print('How many dogs do you have?')
numDogs = input()
try:
    if int(numDogs) >= 4:
        print('That is a lot of dogs.')
    else:
        print('That is not that many dogs.')
except ValueError:
    print('You did not enter a numerical value.')

