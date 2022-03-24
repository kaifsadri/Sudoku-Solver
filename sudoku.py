from collections import defaultdict

L = [line.strip() for line in open("puzzles.txt").readlines()]

# structure to hold the neighbors of a particular cell.
# This is used for fast lookups into the 9x9 grid
V = defaultdict(set)
for row in range(9):
    for col in range(9):
        for i in range(9):
            V[(row, col)].add((row, i))
            V[(row, col)].add((i, col))
            for t in range((row // 3) * 3, (row // 3) * 3 + 3):
                for k in range((col // 3) * 3, (col // 3) * 3 + 3):
                    V[(row, col)].add((t, k))


def solve():
    global P, V
    for loc in P:
        if P[loc] == 0:
            for n in {1, 2, 3, 4, 5, 6, 7, 8, 9} - set(P[l] for l in V[loc]):
                P[loc] = n
                solve()
                P[loc] = 0
            return
    # here is a solution, so print it
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
