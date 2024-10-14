# Typing annotations for variables:
# name: type
int_variable: int
float_variable: float
int_variable = 42
float_variable = 42.0  # OK
float_variable = int_variable  # OK


# Typing annotations for functions (-> means "returns")
def int_to_string(i: int) -> str:
    return str(i)


print(int_to_string(42))  # Static typing error, but no runtime error
print(int_to_string(42 // 5))  # Both static and runtime error
