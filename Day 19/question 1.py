# Input number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input first matrix
print("Enter elements of Matrix 1:")
matrix1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix1.append(row)

# Input second matrix
print("Enter elements of Matrix 2:")
matrix2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix2.append(row)

# Add matrices
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

# Display result
print("Sum of matrices:")
for row in result:
    print(row)
