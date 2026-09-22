def main():
    age = 20
    result = determine_age_category(age)
    print(result)

def determine_age_category(age):
    if age < 18:
        return "child"
    elif age < 65:
        return "adult"
    else:
        return "GG"

main()