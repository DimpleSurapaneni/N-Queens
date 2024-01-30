def ext_one(lst):
    temp = ""
    temp += atl_one(lst)
    temp += atm_one(lst)
    return temp

def atl_one(lst):
    temp = ""
    for item in lst:
        temp += " " + str(item)
    temp += " 0\n"
    return temp

def atm_one(lst):
    temp = ""
    for i, x in enumerate(lst):
        for y in lst[i + 1:]:
            temp += " -" + str(x) + " -" + str(y) + " 0\n"
    return temp

def varmap(r, c, N):
    return r * N + c + 1

def sat_generate_cnf(N):
    output = "c SAT Expression for N=" + str(N) + (" queen\n" if N == 1 else " queens\n")
    size = N * N
    output = output + "c Chess board has " + str(size) + (" position\n" if N == 1 else " positions\n")

    tempG = ""
    for row in range(N):
        A = [varmap(row, column, N) for column in range(N)]
        tempG += ext_one(A)

    for column in range(N):
        A = [varmap(row, column, N) for row in range(N)]
        tempG += ext_one(A)

    for row in range(N - 1, -1, -1):
        A = [varmap(row + x, x, N) for x in range(N - row)]
        tempG += atm_one(A)

    for column in range(1, N):
        A = [varmap(x, column + x, N) for x in range(N - column)]
        tempG += atm_one(A)

    for row in range(N - 1, -1, -1):
        A = [varmap(row + x, N - 1 - x, N) for x in range(N - row)]
        tempG += atm_one(A)

    for column in range(N - 2, -1, -1):
        A = [varmap(x, column - x, N) for x in range(column + 1)]
        tempG += atm_one(A)

    output = output + 'p cnf ' + str(N * N) + ' ' + str(tempG.count('\n') - 1) + '\n' + tempG.strip()
    return output

# Take user input for N
N = int(input("Enter the number of queens (N): "))

# Generate CNF output
result = sat_generate_cnf(N)
print(result)
# Save CNF output to a file
filename = f"queens_{N}.cnf"
with open(filename, 'w') as file:
    file.write(result)

print(f"CNF output saved to {filename}")

