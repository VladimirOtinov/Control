#входные данные
input1 = ["Hello", "2", "world", ":-)"]
input2 = ["1234", "1567", "-2", "computer science"]
input3 = ["Russia", "Denmark", "Kazan"]


def func(inp = []):
    outp = []
    for i in range(len(inp)):
        if len(inp[i]) <= 3:
            outp.append(inp[i])
    return outp

print(func(input1))
print(func(input2))
print(func(input3))