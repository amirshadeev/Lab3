def solve(heads, legs):
    y = (legs - heads*2) // 2
    x = heads - y
    print(f"кроликов:{y}")
    print(f"куриц:{x}")

heads = 35
legs = 94
solve(heads,legs)