# Define a function to calculate BMI
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

# Define a function to interpret BMI values
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Create an empty list to store individual data
individuals = []

# Define a loop to input data for multiple individuals
while True:
    name = input("Enter the name (or type 'exit' to quit): ")
    if name.lower() == 'exit':
        break
    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)

    individual_data = {
        "Name": name,
        "Weight (kg)": weight,
        "Height (m)": height,
        "BMI": bmi,
        "Category": category
    }
    individuals.append(individual_data)

# Display the BMI data for all individuals
print("\nBMI Data:")
for data in individuals:
    print(f"Name: {data['Name']}")
    print(f"Weight: {data['Weight (kg)']} kg")
    print(f"Height: {data['Height (m)']} m")
    print(f"BMI: {data['BMI']:.2f}")
    print(f"Category: {data['Category']}\n")