def bmi(height, weight):
    height_meter = height / 100.0
    weight_kg = weight
    return weight_kg / (height_meter ** 2)

def define_bmi_method(name):
    # Define a new method with the given name
    # that calls the bmi method with the given arguments
    def method(height, weight):
        result = bmi(height, weight)
        if name == "underweight":
            return result < 18.5
        elif name == "normal":
            return result >= 18.5 and result < 25
        elif name == "overweight":
            return result >= 25 and result < 30
        elif name == "obese":
            return result >= 30
        else:
            raise ValueError("Invalid BMI category")

    return method

# Define methods for different BMI categories
underweight = define_bmi_method("underweight")
normal = define_bmi_method("normal")
overweight = define_bmi_method("overweight")
obese = define_bmi_method("obese")

# Test the methods
print("Is 50kg and 170cm underweight?", underweight(170, 50))  # True
print("Is 65kg and 170cm normal weight?", normal(170, 65))  # True
print("Is 80kg and 170cm overweight?", overweight(170, 80))  # True
print("Is 100kg and 170cm obese?", obese(170, 100))  # True
