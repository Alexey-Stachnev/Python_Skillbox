inp = input()
result = 'yes' if(len(inp.replace('0', '')) == len(inp) - len(inp.replace('0', ''))) else 'no'
print(result)