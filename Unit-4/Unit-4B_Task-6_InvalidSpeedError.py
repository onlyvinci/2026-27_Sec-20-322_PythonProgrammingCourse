class InvalidSpeedError(Exception):
    pass

try:
    speed = float(input("Enter vehicle speed: "))
    if speed < 0 or speed > 120:
        raise InvalidSpeedError("Speed must be between 0 and 120 km/h.")
    print("Valid speed:", speed)
except ValueError:
    print("Please enter a valid number.")
except InvalidSpeedError as error:
    print("Error:", error)
