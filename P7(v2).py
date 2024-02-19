def miles_to_kilometers(miles):
    return miles * 1.609344

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def pounds_to_kilograms(pounds):
    return pounds * 0.45359237

def distance(miles):
    return miles_to_kilometers(miles)

def weight(pounds):
    return pounds_to_kilograms(pounds)

def temperature(fahrenheit):
    return fahrenheit_to_celsius(fahrenheit)

def main():
    miles = float(input("Enter distance in miles: "))
    kilometers = distance(miles)
    print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")

    pounds = float(input("Enter weight in pounds: "))
    kilograms = weight(pounds)
    print(f"{pounds} pounds is equal to {kilograms:.2f} kilograms.")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = temperature(fahrenheit)
    print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")

if __name__ == "__main__":
    main()
