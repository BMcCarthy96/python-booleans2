# Create a function that uses DeMorgan's Law to get the expected `True`/`False`
# statement.

# Write your function here.
def de_morgans_law(num1,num2):
    return(not(num1) or not(num2))

print(de_morgans_law(True, True)) # False
print(de_morgans_law(True, False)) # True
print(de_morgans_law(False, False)) # True
print(de_morgans_law("", [])) # True
print(de_morgans_law(2, 2)) # False
print(de_morgans_law(2, 0)) # True
