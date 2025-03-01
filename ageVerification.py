import subprocess

def age_verification():
    print("👋 Welcome to the Age Verification System!\n")

    name = input("Enter your name: ").strip()  # Strip removes unnecessary spaces
    print(f"\nHello {name}, let's check your access eligibility.\n")

    while True:
        try:
            age = int(input("Enter your age: "))  
            break  # If input is correct, break the loop
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")

    if age < 18:
        print(f"❌ Sorry {name}, you are not allowed to access this content.\n")
    elif age == 18:
        print(f"🎉 Congratulations {name}, you just turned 18! Welcome.\n")
    else:
        print(f"✅ Access granted, {name}. Enjoy your content!\n")

    print("🎉 Thank you for using our system! Have a great day.\n")

# Run the function
age_verification()
