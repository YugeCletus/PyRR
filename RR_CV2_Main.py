# main.py
from cv2_functions import *

class CV2Backend:
    def __init__(self):
        self.functions = {}  # Function registry
        self.register_functions()

    def register_function(self, name, arg_types, return_type, func):
        """Registers a function with strict type constraints."""
        self.functions[name] = (arg_types, return_type, func)

    def call_function(self, name, *args):
        """Calls a function while enforcing type constraints."""
        if name not in self.functions:
            raise ValueError(f"Function '{name}' not found.")

        arg_types, return_type, func = self.functions[name]

        # Ensure the correct number of arguments
        if len(args) != len(arg_types):
            raise TypeError(f"'{name}' expects {len(arg_types)} arguments, got {len(args)}")

        # Ensure argument types are correct
        for i, (arg, expected_type) in enumerate(zip(args, arg_types)):
            if isinstance(arg, expected_type):
                continue
            if expected_type == float and isinstance(arg, int):  # Special case where float can also accept int
                continue
            raise TypeError(f"Argument {i+1} of '{name}' must be {expected_type.__name__}, got {type(arg).__name__}")

        result = func(*args)

        # Ensure return value is of the correct type
        if not isinstance(result, return_type):
            raise TypeError(f"Return value of '{name}' must be {return_type.__name__}, got {type(result).__name__}")

        # Special conditions for certain types
        if return_type == float and abs(result) > 10**7:  # example condition for float precision
            raise ValueError(f"Float result is out of bounds: {result}")

        if return_type == str and len(result) > 512:  # Special string length condition
            raise ValueError(f"String length exceeds 512 characters: {len(result)}")

        return result

    def register_functions(self):
        """Registers all predefined functions."""
        self.register_function("Absolute_Value", (float,), float, absolute_value)
        self.register_function("Int_To_Float", (int,), float, int_to_float)
        self.register_function("Lerp", (float, float, float), float, lerp)
        self.register_function("Clamp", (float, float, float), float, clamp)
        self.register_function("Add_Vectors", (Vector3, Vector3), Vector3, add_vectors)
        self.register_function("Multiply_Quaternions", (Quaternion, Quaternion), Quaternion, multiply_quaternions)

# Initialize CV2Backend
cv2_backend = CV2Backend()

# Test the function calls with type constraints
print(cv2_backend.call_function("Absolute_Value", -10.5))  # Should print: 10.5
