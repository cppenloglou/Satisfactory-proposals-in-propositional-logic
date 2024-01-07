import sys
import os
import random

def new_value(r, i, j, problem):
    for jj in range(j):
        if abs(problem[i][jj]) == r:
            return False
    return True

def new_problem(N, M, K):
    problem = [[0] * K for _ in range(M)]
    for i in range(M):
        for j in range(K):
            while True:
                r = random.randint(1, N)
                if new_value(r, i, j, problem):
                    break
            problem[i][j] = r
            r = random.randint(0, 99)
            if r < 50:
                problem[i][j] = -problem[i][j]
    return problem

def syntax_message():
    print("Use syntax:\n\n")
    print("\tbcsp_generator.py <prefix> <id1> <id2> <N> <M> <K>\n\n")
    print("where:\n ")
    print("\t<prefix> = the prefix of the filename of the instances to be generated\n")
    print("\t<id1> = a number indicating the suffix of the first instance.\n")
    print("\t<id2> = a number indicating the suffix of the last instance.\n")
    print("\t<N> = number of propositions\n")
    print("\t<M> = number of sentences\n")
    print("\t<K> = number of propositions per sentence\n")

def number2string(n):
    s = ""
    while n > 0:
        s = chr((n % 10) + ord('0')) + s
        n //= 10
    return s

def write_to_file(id, filename, N, M, K, problem):
    s = filename + "_" + number2string(id) + ".txt"
    with open(s, 'w') as fout:
        fout.write(f"{N} {M} {K}\n")
        for i in range(M):
            fout.write(" ".join(map(str, problem[i])))
            fout.write("\n")

def main():
    if len(sys.argv) != 7:
        print("Wrong number of arguments. Use correct syntax:\n")
        syntax_message()
        return -1

    id1 = int(sys.argv[2])
    id2 = int(sys.argv[3])
    N = int(sys.argv[4])
    M = int(sys.argv[5])
    K = int(sys.argv[6])

    if id1 <= 0 or id2 <= 0 or id1 > id2 or N <= 0 or M <= 0 or K <= 0:
        syntax_message()
        return -1

    random.seed()

    for i in range(id1, id2 + 1):
        problem = new_problem(N, M, K)
        write_to_file(i, sys.argv[1], N, M, K, problem)

if __name__ == "__main__":
    main()
