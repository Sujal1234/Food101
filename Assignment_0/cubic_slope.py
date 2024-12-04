def slope_of_cubic(coefficients, x):
    a, b, c = coefficients[:3]
    return 3*a*x*x + 2*b*x + c;
    

print("Enter coefficients of the cubic polynomial, in descending order of the power of terms.")
print("For example, for the polynomial 4x^3 + 3x^2 + 2x + 7 the input would be 4 3 2 7")
print("Enter input: ", end = '')

coeffs = input().strip().split()
coeffs = tuple(int(x) for x in coeffs)

x = int(input("Enter a value to calculate the slope at: "))

print("The slope is", slope_of_cubic(coeffs, x))