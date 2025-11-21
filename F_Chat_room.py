string_  = input()
index = 0
hello = "hello"
hello_index = 0
while index < len(string_) and hello_index < len(hello):
        if string_[index] == hello[hello_index]:
                index+=1
                hello_index+=1
        else:
                index+=1
if hello_index == len(hello):
        print("YES")
else:
        print("NO")
        