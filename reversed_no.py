def reverse_number(num):
    return int(str(num)[::-1])

# Example: Reverse the number 12345
original_number = int(input("Enter the number:"))
reversed_number = reverse_number(original_number)

print(f"Original Number: {original_number}")
print(f"Reversed Number: {reversed_number}")
