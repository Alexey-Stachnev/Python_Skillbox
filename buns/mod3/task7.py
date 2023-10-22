inp = input()
result = [inp.split()[i] == inp.split()[j] for i in range(len(inp.split())) for j in range(i+1, len(inp.split()))]
print(True in result)