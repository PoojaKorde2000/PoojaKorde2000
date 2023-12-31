
def get_weather_data(date):
    temperature = 25 
    return temperature

def get_wind_speed_data(date):
    wind_speed = 10  
    return wind_speed

def get_pressure_data(date):
    pressure = 1012 
    return pressure

def main():
    while True:
        print("Options:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_weather_data(date)
            print(f"The temperature on {date} is {temperature} degrees Celsius.\n")
        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_data(date)
            print(f"The wind speed on {date} is {wind_speed} km/h.\n")
        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_data(date)
            print(f"The pressure on {date} is {pressure} hPa.\n")
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
