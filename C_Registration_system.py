from collections import Counter
name = Counter()


for _ in range(int(input())):
        m = input()
        if name[m] == 0:
                print("OK")
                name[m] += 1
        else:
                print(f"{m}{name[m]}")
                name[m] += 1
                