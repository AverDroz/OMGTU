def calculate_milk_price(x, y, z, p):
    v = x * y * z
    s = 2 * (x*y + y*z + z*x)
    return p * s / v

filename = "input1.txt"
data = []

with open(filename, "rt") as f:
    n = int(f.readline())

    min_price = float("inf")
    firm = 0

    for i in range(n):
        x1, y1, z1, x2, y2, z2, p1, p2 = map(float, f.readline().split())

        milk_price = calculate_milk_price(x1, y1, z1, p2) - calculate_milk_price(x2, y2, z2, p1)

        denominator = (x2*y2*z2*s1 - x1*y1*z1*s2)
        if denominator != 0:
            milk_price /= denominator

        if milk_price < min_price:
            min_price = milk_price
            firm = i + 1

min_price = round(min_price * 1000, 2)
print(f"Firm: {firm}, Minimum Price: {min_price}")
