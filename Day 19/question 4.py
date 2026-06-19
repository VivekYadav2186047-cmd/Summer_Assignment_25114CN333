# Find sum of principal diagonal elements

n = int(input("Enter size of square matrix: "))

matrix = []
print("Enter matrix elements:")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)

diagonal_sum = 0

for i in range(n):
    diagonal_sum += matrix[i][i]

print("Sum of diagonal elements =", diagonal_sum)
