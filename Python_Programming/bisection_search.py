""" bisection search
for finding the square root
"""

# TODO: add plot
# Attribution: based on Guttag "Introduction to Computation and Programming Using Python" pp. 33

def square_root(target: float, max_error = 0.001):
    low: float = 0
    high: float = target
    attempt: float = (low + high) / 2
    while abs(attempt ** 2 - target) > max_error:
        if attempt**2 > target:
            high = attempt
        else:
            low = attempt
        attempt = (low + high)/2
    return attempt

print(square_root(9))
