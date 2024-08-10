# 1. Print Statement
print("Welcome to the Interactive Supercar Showroom!")

# 2. List with at least 2 list functions
supercars = ["Ferrari LaFerrari", "Bugatti Chiron", "McLaren P1", "Lamborghini Aventador"]
supercars.append("Porsche 918 Spyder")   # Append a new supercar to the list
supercars.sort()                         # Sort the list alphabetically
print(f"Alphabetically Sorted Supercar List: {supercars}")

# User Input for favorite supercar
favorite = input("Enter your favorite supercar from the list above: ")

# 3. If, elif, and else statement
if favorite in supercars:
    print(f"{favorite} is available in the showroom!")
elif favorite == "Tesla Roadster":
    print(f"{favorite} is not a traditional supercar, but it's still impressive!")
else:
    print(f"Sorry, {favorite} is not available in the showroom.")

# 4. For loop
print("\nAvailable Supercars:")
for car in supercars:
    print(car)

# 5. Function with a return value
def car_price(car_name):
    prices = {
        "Ferrari LaFerrari": 1400000,
        "Bugatti Chiron": 3000000,
        "McLaren P1": 1300000,
        "Lamborghini Aventador": 500000,
        "Porsche 918 Spyder": 845000
    }
    return prices.get(car_name, "Price not available")

# User input for selecting a supercar to get its price
chosen_car = input("\nEnter the name of the supercar you want to know the price of: ")
price = car_price(chosen_car)
print(f"The price of the {chosen_car} is ${price}.")

# 6. Dictionary with at least 2 dictionary functions
supercar_specs = {
    "Ferrari LaFerrari": {"Top Speed": 217, "0-60 mph": 2.4},
    "Bugatti Chiron": {"Top Speed": 261, "0-60 mph": 2.3},
    "McLaren P1": {"Top Speed": 217, "0-60 mph": 2.6},
    "Lamborghini Aventador": {"Top Speed": 217, "0-60 mph": 2.9},
    "Porsche 918 Spyder": {"Top Speed": 211, "0-60 mph": 2.5}
}

# Using dictionary functions
all_specs = supercar_specs.items()        # Get all items (key-value pairs)
ferrari_speed = supercar_specs.get("Ferrari LaFerrari").get("Top Speed")  # Get Ferrari's top speed
print("\nAll Supercar Specs:")
for car, specs in all_specs:
    print(f"{car}: Top Speed = {specs['Top Speed']} mph, 0-60 mph = {specs['0-60 mph']} seconds")

print(f"\nThe top speed of the Ferrari LaFerrari is {ferrari_speed} mph.")

# 7. While loop (bonus example)
counter = 3
while counter > 0:
    print(f"{counter} supercars remain in the special showcase!")
    counter -= 1

print("End of the Interactive Supercar Showroom tour!")
