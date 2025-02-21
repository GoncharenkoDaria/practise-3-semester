def main():
    """
    Calculate the sum of a series using different methods and compare the results.
    """
    import math

    # Presetting the parameters of the summation
# x1 x2
    # x = 1.0
    x = 11.0**0.5

    coefficient = 1.0/x
    sum_ = 0
    ordered_sum = 0
    coefficients = [coefficient]
    n = 0

    # Calculation of all the required coefficients using the Leibniz test
    while abs(coefficient) > 1e-12:
        n += 1
        coefficient *= -1.0*x**2.0/(float(n))
        coefficients.append(coefficient)
    coefficients.pop()

    # Calculation of 3 "different" sums using the calculated coefficients
    for i in range(n):
        sum_ += coefficients[i]

    kahan_sum = 0
    c = 0
    for i in range(n):
        y = coefficients[i] - c
        t = kahan_sum + y
        z = t - kahan_sum
        c = z - y
        kahan_sum = t

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if coefficients[j] > coefficients[j + 1]:
                coefficients[j], coefficients[j +
                                              1] = coefficients[j + 1], coefficients[j]

    # Output of the results
    for i in range(n):
        ordered_sum += coefficients[i]
# value1 value2
    # value = 1.0/math.exp(1)
    value = 1/(11.0**0.5*math.exp(11))

    print("x:  ", x, ",    n:  ", n, ".")
    print(f"f(x) = (1+x)^(-0.5):  {value};")
    print(f"sum_1 (naive):  {sum_:<15},    delta_1:  {value - sum_:<15};")
    print(
        f"sum_2 (ordered):  {ordered_sum:<15},    delta_2:  {value - ordered_sum:<15};")
    print(
        f"sum_3 (Kahan):  {kahan_sum:<15},    delta_3:  {value - kahan_sum:<15}.")


if __name__ == "__main__":
    main()
