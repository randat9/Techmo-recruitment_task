import sys


def filter_results(results):
    remaining = set(range(len(results)))  # Indeksy wyników, które nie zostały usunięte

    for i, (C_i, P_i, J_i) in enumerate(results):
        for j in range(i + 1, len(results)):
            C_j, P_j, J_j = results[j]
            if C_i <= C_j and P_i <= P_j and J_i >= J_j:
                remaining.discard(j)  # Usuwamy wynik j
            elif C_j <= C_i and P_j <= P_i and J_j >= J_i:
                remaining.discard(i)  # Usuwamy wynik i
                break  # Przerywamy dalsze porównania dla i

    return len(remaining)


if __name__ == "__main__":
    try:
        with open("input.txt", "r") as file:
            lines = file.readlines()
            n = int(lines[0].strip())
            results = [tuple(map(int, line.split())) for line in lines[1:n + 1]]

        result = filter_results(results)
        print(result)

        with open("output.txt", "w") as file:
            file.write(str(result) + "\n")
    except Exception as e:
        print(f"Błąd: {e}")
