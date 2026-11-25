class InvalidMarksError(Exception):
    pass

try:
    marks = float(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
except ValueError:
    print("Please enter valid numeric marks.")
except InvalidMarksError as error:
    print("Error:", error)
finally:
    print("Validation completed.")
