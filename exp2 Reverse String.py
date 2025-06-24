# a) Reverse of a String
string_input = input("Enter a string: ")
reversed_string = string_input[::-1]
print("Reversed String:", reversed_string)

# b) Reverse of an Array
array_input = list(map(int, input("Enter array elements (space separated): ").split()))
reversed_array = array_input[::-1]
print("Reversed Array:", reversed_array)

# c) Concatenation of Two Strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
concatenated = str1 + str2
print("Concatenated String:", concatenated)
