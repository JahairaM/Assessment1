#Step 1 Create 3 list and fill them in with student information Name, Hometown and Favorite food
names = ["Jahaira","Michael", "Mariah","Abe"]
hometown = ["Detroit", "Southfield", "Chicago", "Orlando"]
fav_food = ["Pizza", "Seafood", "Burgers", "Soup"]

#T
def display_student_info(index):
    print(f"Name: {names[index]}")

    category = ""
    while category.lower() not in ["hometown", "favorite food"]:
        category = input("Which category would you like to display? (hometown or favorite food): ")
        if category.lower() == "hometown":
            print(f"Hometown: {hometown[index]}")
        elif category.lower() == "favorite food":
            print(f"Favorite food: {fav_food[index]}")
        else:
            print("Please enter a valid category (hometown or favorite food).")
def main():
    while True:
        try:
            student_number = int(input("Enter a student number (1 to 4): "))
            if 1 <= student_number <= len(names):
                index = student_number - 1  # Convert number to index (0-based)
                display_student_info(index)
            else:
                # Inform the user if the number is out of range
                print(f"Invalid number. Please enter a number between 1 and 4.")
                continue
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a number.")
            continue

        # Ask user if they want to learn about another student or see a list of all students
        action = input("Would you like to (1) Learn about another student or (2) See a list of all students? (Enter 1 or 2): ")
        if action == "1":
            continue
        elif action == "2":
            print("List of all students:")
            for i, name in enumerate(names):
                print(f"{i + 1}. {name}")
        else:
            # Inform the user if the choice is invalid
            print("Invalid choice. Please enter 1 or 2.")

        # Ask if the user wants to learn about another student or exit
        another = input("Would you like to learn about another student? (yes or no): ")
        if another.lower() != "yes":
            print("Thank you for using the student information program. Goodbye!")
            break

# Start the program
if __name__ == "__main__":
    main()

