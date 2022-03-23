L = [line.strip() for line in open("puzzles.txt").readlines()]


def poss(loc):
    """
    take location and return the set of possible values for that loc
    """
    global P
    x, y = loc
    return (
        set(range(1, 10))
        - set(P[(x, i)] for i in range(9))
        - set(P[(i, y)] for i in range(9))
        - set(P[(i, k)] for i in range((x // 3) * 3, (x // 3) * 3 + 3) for k in range((y // 3) * 3, (y // 3) * 3 + 3))
    )


def solve():
    global P
    for loc in P:
        if P[loc] == 0:
            s = poss(loc)
            while s:
                P[loc] = s.pop()
                solve()
                P[loc] = 0
            return
    for row in range(9):
        print("\n")
        for col in range(9):
            print(P[(row, col)], "  ", end="")
    print("\n\n" + "-" * 33)
    return


P = dict()
for i, line in enumerate(L[:10]):
    print(f"\nLine {i+1}:", end="")
    for k, c in enumerate(line):
        P[divmod(k, 9)] = int(c)
    solve()
