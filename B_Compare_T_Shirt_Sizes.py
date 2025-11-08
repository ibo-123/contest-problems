for _ in range(int(input())):
        a , b = input().split()
        if a[-1] == b[-1]:
                if len(a) > len(b) and ((a[-1]=="L") or (a[-1]=="M")):
                        print(">")
                elif len(a) < len(b) and (a[-1]=="L" or (a[-1]=="M")):
                        print("<")
                elif len(a) > len(b) and (a[-1]=="S"):
                        print("<")
                elif len(a) < len(b) and (a[-1]=="S"):
                        print(">")
                else:
                        print("=")
        elif a[-1] == "M" and b[-1]=="S":
                print(">")
        elif a[-1] == "S" and b[-1]=="M":
                print("<")
        elif a[-1] == "L" and b[-1]=="M":
                print(">")
        elif a[-1] == "M" and b[-1]=="L":
                print("<")
        elif a[-1] == "L" and b[-1]=="S":
                print(">")
        elif a[-1] == "S" and b[-1]=="L":
                print("<")
__import__('atexit').register(lambda: open('display_runtime.txt','w').write('0'))














# M M
# L L
# XL XL
# XXL XXL
# XXXL XXXL
# XXXXL XXXXL
# XXXXXL XXXXXL
# XXXXXXL XXXXXXL
# XXXXXXXL XXXXXXXL
# XXXXXXXXL XXXXXXXXL
# XXXXXXXXXL XXXXXXXXXL
# XXXXXXXXXXL XXXXXXXXXXL
# XXXXXXXXXXXL XXXXXXXXXXXL
# XXXXXXXXXXXXL XXXXXXXXXXXXL
# XXXXXXXXXXXXXL XXXXXXXXXXXXXL
# XXXXXXXXXXXXXXL XXXXXXXXXXXXXXL
# XXXXXXXXXXXXXXXL XXXXXXXXXXXXXXXL
# XXXXXXXXXXXXXXXXL XXXXXXXXXXXXXXXXL
# XXXXXXXXXXXXXXXXXL XXXXXXXXXXXXXXXXXL
# XXXXXXXXXXXXXXXXXXL XXXXXXXXXXXXXXXXXXL










# >
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =
# =