# Garvin Stewart
# 3/29/2026
# Module 1.3

def countdown(bottles):
    # The function manages the countdown loop
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.\n")
        elif bottles == 1:
            # Change lyrics to singular when down to 1
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall.\n")

        # Decrease the bottle count by 1
        bottles -= 1

def main():
    # Ask the user how many bottles are on the wall
    try:
        starting_bottles = int(input("How many bottles of beer are on the wall? "))

        # Pass that input to the function
        countdown(starting_bottles)

        # Back in the main program, remind the user to buy more beer
        print("There are no more bottles of beer on the wall. Time to buy more beer!")
    except ValueError:
        print("Please enter a valid whole number.")

# Run the program
main()