"""
Functions for Rec Room CV2 Python
"""

from dataclasses import dataclass
import math

# Int Class
@dataclass
class Int:
    value: int

# Float Class
@dataclass
class Float:
    value: float

# String Class
@dataclass
class String:
    value: str

# Bool Class
@dataclass
class Bool:
    value: bool

# Color Class
@dataclass
class Color:
    value: str

# Vector3 Class
@dataclass
class Vector3:
    x: float
    y: float
    z: float

# Quaternion Class
@dataclass
class Quaternion:
    w: float
    x: float
    y: float
    z: float

# Math Functions

def Absolute_Value(x: Float) -> Float:
    """
    Outputs the magnitude of the number. Is always positive.
    Inputs: Float
    Outputs: Float
    """
    if (not isinstance(x, Float)):
        raise TypeError("Absolute_Value only accepts float inputs")
    return (Float(abs(x)))

def Acos(value: Float) -> Float:
    """
    Computes the arccosine of a number.
    Inputs: Float
    Outputs: Float
    """
    if (not isinstance(value, Float)):
        raise TypeError("Acos only accepts float inputs")
    return (Float(math.acos(value)))

def Add(a, b): # TODO
    if (isinstance(a, type(b))):
        # Int
        if (isinstance(a, Int)):
            return (Int(a + b))
        
        # Float
        elif (isinstance(a, Float)):
            return (Float(a + b))
        
        # Vector3
        elif (isinstance(a, Vector3)):
            return (Vector3(a.x + b.x, a.y + b.y, a.z + b.z))
        
        # Quaternion
        elif (isinstance(a, Quaternion)):
            return (Quaternion(w=a.w + b.w, x=a.x + b.x, y=a.y + b.y, z=a.z + b.z))
        
        else:
            raise TypeError(f"Unsupported type: {type(a).__name__}")
    else:
        raise TypeError(f"Cannot add different types: {type(a).__name__} and {type(b).__name__}")
    
def Asin(value: Float) -> Float:
    """
    Computes the arcsine of a number.
    Inputs: Float
    Outputs: Float
    """
    if (not isinstance(value, Float)):
        raise TypeError("Asin only accepts float inputs")
    return (Float(math.asin(value)))

def Atan(value: Float) -> Float:
    """
    Computes the arctangent of a number.
    Inputs: Float
    Outputs: Float
    """
    if (not isinstance(value, Float)):
        raise TypeError("Atan only accepts float inputs")
    return (Float(math.atan(value)))

def Atan2(y: Float, x: Float) -> Float:
    """
    Computes the 2-argument arctangent of a number
    Inputs: Float, Float
    Outputs: Float
    """
    if (not isinstance(y, Float) or not isinstance(x, Float)):
        raise TypeError("Atan2 only accepts float inputs")
    return (Float(math.atan2(y, x)))

def Bit_And(): # TODO
    pass

def Bit_Leading_Zeros(): # TODO
    pass

def Bit_Nand(): # TODO
    pass

def Bit_Not(): # TODO
    pass

def Bit_Or(): # TODO
    pass

def Bit_Pop_Count(): # TODO
    pass

def Bit_Rotate_Left(): # TODO
    pass

def Bit_Rotate_Right(): # TODO
    pass

def Bit_Shift_Left(): # TODO
    pass

def Bit_Shift_Right(): # TODO
    pass

def Bit_Trailing_Zeros(): # TODO
    pass

def Bit_Xor(): # TODO
    pass

def Ceil(x: Float) -> Float:
    """
    Returns the least integral value greater than or equal to the input value.
    Inputs: Float
    Outputs: Float
    """
    if (not isinstance(x, Float)):
        raise TypeError("Ceil only accepts float inputs")
    return (Float(math.ceil(x)))

def Ceil_to_Int(x: Float) -> Int:
    """
    Returns the smallest integer value greater than or equal to the input value.
    Inputs: Float
    Outputs: Int
    """
    if (not isinstance(x, Float)):
        raise TypeError("Ceil_to_Int only accepts float inputs")
    return (Int(math.ceil(x)))

def Clamp(Value, Min, Max): # VERIFY
    """
    Clamps a value between a minimum value and maximum value.
    If the minimum is greater than the maximum,
    the minimum value will always be returned no matter the input.
    Inputs: Float, Int
    Outputs: Float, Int
    """
    if (isinstance(Value, type(Min)) and isinstance(Value, type(Max))):
        # Float
        if (isinstance(Value, Float)):
            return (Float(max(Min, min(Value, Max))))
        
        # Int
        elif (isinstance(Value, Int)):
            return (Int(max(Min, min(Value, Max))))
        
        else:
            raise TypeError(f"Unsupported type: {type(Value).__name__}")
    else:
        raise TypeError(f"Cannot clamp different types: {type(Value).__name__}, {type(Min).__name__}, and {type(Max).__name__}")

def Cos(value: Float) -> Float:
    """
    Computes the cosine of a number.
    Inputs: Float
    Outputs: Float
    """
    if (not isinstance(value, Float)):
        raise TypeError("Cos only accepts float inputs")
    return (Float(math.cos(value)))

def Distance(): # TODO
    pass

def Divide(): # TODO
    pass

def Floor(x: Float) -> Float:
    """
    Returns the smallest integral value less than or equal to the input value.
    Inputs: Float
    Outputs: Float
    """
    if (not isinstance(x, Float)):
        raise TypeError("Floor only accepts float inputs")
    return (Float(math.floor(x)))

def Floor_to_Int(x: Float) -> Int:
    """
    Returns the largest integer value less than or equal to the input value.
    Inputs: Float
    Outputs: Int
    """
    if (not isinstance(x, Float)):
        raise TypeError("Floor_to_Int only accepts float inputs")
    return (Int(math.floor(x)))

def Get_Closest(): # TODO
    pass

def Get_Farthest(): # TODO
    pass

def Int_to_Float(x: Int) -> Float:
    """
    Converts an integer to a float.
    Inputs: Int
    Outputs: Float
    """
    if (not isinstance(x, Int)):
        raise TypeError("Int_to_Float only accepts int inputs")
    return (Float(float(x)))

def Inverse_Lerp(): # TODO
    pass

def Inverse_Lerp_Unclamped(): # TODO
    pass

def Lerp(): # TODO
    pass

def Lerp_Unclamped(): # TODO
    pass

def List_Divide(): # TODO
    pass

def List_Max(): # TODO
    pass

def List_Min(): # TODO
    pass

def List_Multiply(): # TODO
    pass

def List_Subtract(): # TODO
    pass

def List_Sum(): # TODO
    pass

def Logarithm(): # TODO
    pass

def Max(): # TODO
    pass

def Min(): # TODO
    pass

def Modulo(): # TODO
    pass

def Multiply(): # TODO
    pass

def Noise(): # TODO
    pass

def Power(): # TODO
    pass

def Quaternion_Create(): # TODO
    pass

def Quaternion_Create_Angle_Axis(): # TODO
    pass

def Quaternion_Create_Euler_Angles(): # TODO
    pass

def Quaternion_create_From_To(): # TODO
    pass

def Quaternion_Create_Look(): # TODO
    pass

def Quaternion_Dot(): # TODO
    pass

def Quaternion_Euler_Angles(): # TODO
    pass

def Quaternion_Get_Angle_Axis(): # TODO
    pass

def Quaternion_Inverse(): # TODO
    pass

def Quaternion_Normalize(): # TODO
    pass

def Quaternion_Rotate_Towards(): # TODO
    pass

def Quaternion_Split(): # TODO
    pass

def Random_Float(): # TODO
    pass

def Random_Int(): # TODO
    pass

def Remainder(): # TODO
    pass

def Root(): # TODO
    pass

def Rotate_Vector(): # TODO
    pass

def Round(): # TODO
    pass

def Round_to_Int(): # TODO
    pass

def Sin(value: Float) -> Float:
    """
    Computes the sine of a number.
    Inputs: Float
    Outputs: Float
    """
    if (not isinstance(value, Float)):
        raise TypeError("Sin only accepts float inputs")
    return (Float(math.sin(value)))

def Slerp(): # TODO
    pass

def Smooth_Damp(): # TODO
    pass

def Subtract(): # TODO
    pass

def Tan(value: Float) -> Float:
    """
    Computes the tangent of a number.
    Inputs: Float
    Outputs: Float
    """
    if (not isinstance(value, Float)):
        raise TypeError("Tan only accepts float inputs")
    return (Float(math.tan(value)))

def Vector_Get_Magnitude(): # TODO
    pass

def Vector3_Angle(): # TODO
    pass

def Vector3_Clamp_Magnitude(): # TODO
    pass

def Vector3_Closest_Point_On_Plane(): # TODO
    pass

def Vector3_Create(): # TODO
    pass

def Vector3_Cross(): # TODO
    pass

def Vector3_Dot(): # TODO
    pass

def Vector3_Inverse(): # TODO
    pass

def Vector3_Inverse_Transform(): # TODO
    pass

def Vector3_Move_Towards(): # TODO
    pass

def Vector3_Normalize(): # TODO
    pass

def Vector3_Project(): # TODO
    pass

def Vector3_Project_On_Plane(): # TODO
    pass

def Vector3_Scale(): # TODO
    pass

def Vector3_Split(): # TODO
    pass

def Vector3_Transform(): # TODO
    pass

# Conversion Functions

def Color_To_HSV(): # TODO
    pass

def Color_To_RGB(): # TODO
    pass

def From_Rec_Room_Object(): # TODO
    pass

def HSV_To_Color(): # TODO
    pass

def Parse_Bool(): # TODO
    pass

def Parse_Color(): # TODO
    pass

def Parse_Float(): # TODO
    pass

def Parse_Int(): # TODO
    pass

def RGB_To_Color(): # TODO
    pass

def To_Rec_Room_Object(): # TODO
    pass

def To_String(): # TODO
    pass

# Logic Functions
def And(): # TODO
    pass

def Equals(): # TODO
    pass

def Execution_Integer_Switch(): # TODO
    pass

def Execution_String_Switch(): # TODO
    pass

def Greater_or_Equal(): # TODO
    pass

def Greater_Than(): # TODO
    pass

def If_Vaule(): # TODO
    pass

def Less_or_Equal(): # TODO
    pass

def Less_Than(): # TODO
    pass

def List_All_True(): # TODO
    pass

def List_Any_True(): # TODO
    pass

def Nand(): # TODO
    pass

def Nor(): # TODO
    pass

def Not(): # TODO
    pass

def Not_Equals(): # TODO
    pass

def Or(): # TODO
    pass

def Value_Integer_Switch(): # TODO
    pass

def Value_String_Switch(): # TODO
    pass

def Xor(): # TODO
    pass

# Time Functions
def Delay(): # TODO
    pass

def Get_Formatted_Time(): # TODO
    pass

def Parse_Time(): # TODO
    pass

def Player_Get_Time_Zone(): # TODO
    pass

def Time_Get_Precise_Seconds(): # TODO
    pass

def Time_Get_Universal_Seconds(): # TODO
    pass

def Time_Get_Universal_Time(): # TODO
    pass

def Time_Get_Unsynced_Universal_Seconds(): # TODO
    pass

def Time_Get_Unsynced_Universal_Time(): # TODO
    pass










# Cletus Functions (apart of the Cletus library)
def Sinh(): # TODO
    pass

def Cosh(): # TODO
    pass

def Tanh(): # TODO
    pass

def Asinh(): # TODO
    pass

def Acosh(): # TODO
    pass

def Atanh(): # TODO
    pass

def Csc(): # TODO
    pass

def Sec(): # TODO
    pass

def Cot(): # TODO
    pass

def Acsc(): # TODO
    pass

def Asec(): # TODO
    pass

def Acot(): # TODO
    pass

def Csch(): # TODO
    pass

def Sech(): # TODO
    pass

def Coth(): # TODO
    pass

def Acsch(): # TODO
    pass

def Asech(): # TODO
    pass

def Acoth(): # TODO
    pass

def Softmax(): # TODO
    pass

def GELU(): # TODO
    pass

def erfc(): # TODO
    pass

def erf(): # TODO
    pass

def ReLU(): # TODO
    pass

def Sigmoid(): # TODO
    pass

def exp(): # TODO
    pass

def Random_Binary_Generator(): # TODO
    pass

def Random_Hex_Generator(): # TODO
    pass

def Xnor(): # TODO
    pass

def Buffer(): # TODO
    pass

def Factorial(): # TODO
    pass

def Reverse_List_String(): # TODO
    pass

def Reverse_String(): # TODO
    pass

def Reverse_List_Int(): # TODO
    pass

def Reverse_List_Float(): # TODO
    pass

def Reverse_List_Bool(): # TODO
    pass

def Reverse_List_Vector3(): # TODO
    pass

def Reverse_List_Color(): # TODO
    pass

def Reverse_List_Quaternion(): # TODO
    pass

def Is_Digit(): # TODO
    pass

def Hex_To_Binary(): # TODO
    pass

def Binary_To_Hex(): # TODO
    pass

def Binary_To_Decimal(): # TODO
    pass

def Decimal_To_Binary(): # TODO
    pass

def Decimal_To_Hex(): # TODO
    pass

def Hex_To_Decimal(): # TODO
    pass

def Decimal_To_Roman_Numerals(): # TODO
    pass

def Roman_Numerals_To_Decimal(): # TODO
    pass

def Is_Roman_Numeral(): # TODO
    pass

def Is_Valid_Hex(): # TODO
    pass

def Is_Valid_Binary(): # TODO
    pass

def Hex_To_RGB(): # TODO
    pass

def RGB_To_Hex(): # TODO
    pass

def Random_Execute(): # TODO
    pass

def Shuffle_String(): # TODO
    pass

def Capitalize(): # TODO
    pass

def CamelCase(): # TODO
    pass

def Approximate_Location_From_Timezone(): # TODO
    pass

def Vector3_Round(): # TODO
    pass

def Vector3_Floor(): # TODO
    pass

def Vector3_Ceil(): # TODO
    pass

def Sqrt(): # TODO
    pass

def Cbrt(): # TODO
    pass

def Log10(): # TODO
    pass

def Ln(): # TODO
    pass

def Log2(): # TODO
    pass

def Linspace(): # TODO
    pass

def Djikstra(): # TODO
    pass

def AStar(): # TODO
    pass

def Floyd_Warshall(): # TODO
    pass

def Shunting_Yard(): # TODO
    pass

def Gamma(): # TODO
    pass

def Sigmoid_Derivative(): # TODO
    pass

def ReLU_Derivative(): # TODO
    pass

def Softmax_Derivative(): # TODO
    pass

def Uniform_Distribution(): # TODO
    pass

def Normal_Distribution(): # TODO
    pass

def Standard_Deviation(): # TODO
    pass

def Variance(): # TODO
    pass

def Covariance(): # TODO
    pass

def Correlation_Coefficient(): # TODO
    pass

def Hypotenuse(): # TODO
    pass

def Angle_Between_Vectors(): # TODO
    pass

def Sign(): # TODO
    pass

def Is_Prime(): # TODO
    pass

def Is_Perfect_Square(): # TODO
    pass

def Is_Armstrong_Number(): # TODO
    pass

def Is_Palindrome(): # TODO
    pass

def Is_Anagram(): # TODO
    pass

def Is_Leap_Year(): # TODO
    pass

def Is_Valid_Email(): # TODO
    pass

def Is_Valid_URL(): # TODO
    pass

def Fibonacci(): # TODO
    pass













