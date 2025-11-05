for _ in range(int(input())):
        n = int(input())
        A = input().split()
        B = input().split()
        C = input().split()
        a, b, c = 0, 0, 0

        if n == 1:
                if A != B and A != C:
                        a += 3
                if B != A and B != C:
                        b += 3
                if C != A and C != B:
                        c += 3
                if A == B and B != C:
                        a += 1
                        b += 1
                elif A == C and C != B:
                        a += 1
                        c += 1
                elif B == C and C != A:
                        b += 1
                        c += 1
                print(a, b, c)
                continue

        freq = {}
        for word in A:
                freq[word] = freq.get(word, 0) + 1
        for word in B:
                freq[word] = freq.get(word, 0) + 1
        for word in C:
                freq[word] = freq.get(word, 0) + 1

        for word in A:
                if freq[word] == 1:
                        a += 3
                elif freq[word] == 2:
                        a += 1
        for word in B:
                if freq[word] == 1:
                        b += 3
                elif freq[word] == 2:
                        b += 1
        for word in C:
                if freq[word] == 1:
                        c += 3
                elif freq[word] == 2:
                        c += 1

        print(a, b, c)
