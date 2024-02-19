def miles_to_kilometers(miles):
    return miles * 1.609344

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def pounds_to_kilograms(pounds):
    return pounds * 0.45359237

def distance():
    miles = float(input("Enter distance in miles: "))
    kilometers = miles_to_kilometers(miles)
    print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")

def weight():
    pounds = float(input("Enter weight in pounds: "))
    kilograms = pounds_to_kilograms(pounds)
    print(f"{pounds} pounds is equal to {kilograms:.2f} kilograms.")

def temperature():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")

def main():
    distance()
    weight()
    temperature()

if __name__ == "__main__":
    main()
