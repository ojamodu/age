# Program to check if age is between 10 and 20 years

def get_valid_age():
    """Prompt user for age and validate input."""
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Age cannot be negative. Please try again.")
                continue
            return age
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_age_range(age):
    """Check if age is between 10 and 20 inclusive."""
    if 10 <= age <= 20:
        print(f"Your age ({age}) is between 10 and 20 years.")
    else:
        print(f"Your age ({age}) is NOT between 10 and 20 years.")

# Main program
if __name__ == "__main__":
    age = get_valid_age()
    check_age_range(age)
