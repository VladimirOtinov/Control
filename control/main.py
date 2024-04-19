#входные данные
input1 = ["Hello", "2", "world", ":-)"]
input2 = ["1234", "1567", "-2", "computer science"]
input3 = ["Russia", "Denmark", "Kazan"]


def func(inp = [], outp = []):
    for i in range(len(inp)):
        if len(inp) <= 3:
            outp.append(inp[i])


