def count_recon_groups(N):
    if N < 3:
        return 0
    if N == 3:
        return 1
    return count_recon_groups(N // 2) + count_recon_groups(N - N // 2)

with open("Отбор в разведку/input_s1_01.txt", "r") as file:
    N = int(file.readline().strip())
print(count_recon_groups(N))