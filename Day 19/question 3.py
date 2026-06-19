# Input number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input matrix
print("Enter elements of the matrix:")
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

# Transpose matrix
transpose = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix[i][j])
    transpose.append(row)

# Display transpose
print("Transpose of the matrix:")
for row in transpose:
    print(row)
