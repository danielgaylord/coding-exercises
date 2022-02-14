cases = int(input())

for case in range(1, cases + 1):
    country = input()
    person = ""
    vowels = "aeiou"
    if (country.lower())[-1] in vowels:
        person = "Alice"
    elif (country.lower())[-1] == "y":
        person = "nobody"
    else:
        person = "Bob"
    print(f"Case #{case}: {country} is ruled by {person}.")