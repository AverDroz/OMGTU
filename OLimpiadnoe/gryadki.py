def calculate_formula(k, l, n, m):
    return k * (2 * l + 2 * n) + (k ** 2 + k) * m

def calculate_loop(k, l, n, m):
    s = 0
    for j in range(k):
        s += 2 * l + 2 * n + 2 * m + j * 2 * m
    return s

def main():
    K = [1, 2, 3, 20]
    l = 7
    n = 5
    m = 10

    # Формула
    for k in K:
        result_formula = calculate_formula(k, l, n, m)
        print(f"{k}: {result_formula}")

    print()

    # Цикл
    for k in K:
        result_loop = calculate_loop(k, l, n, m)
        print(f"{k}: {result_loop}")

if __name__ == "__main__":
    main()
