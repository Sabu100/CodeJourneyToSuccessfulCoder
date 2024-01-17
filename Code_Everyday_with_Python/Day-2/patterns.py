def patterns(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

# Taking input and calling the function
user_input = int(input("Enter a number: "))
patterns(user_input)
