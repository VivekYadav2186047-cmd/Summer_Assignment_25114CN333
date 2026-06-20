#
//Write a program to Multiply matrices.
#include <stdio.h>

int main() {
    int r1, c1, r2, c2;

    printf("enter rows and columns of first matrix = ");
    scanf("%d %d", &r1, &c1);

    int matrix1[r1][c1];
printf("enter elements of first matrix =\n");
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c1; j++) {
            scanf("%d", &matrix1[i][j]);
        }
    }

    printf("Enter rows and columns of second matrix: ");
    scanf("%d %d", &r2, &c2);

    int matrix2[r2][c2];
printf("enter elements of second matrix =\n");
    for (int i = 0; i < r2; i++) {
        for (int j = 0; j < c2; j++) {
            scanf("%d", &matrix2[i][j]);
        }
    }

    if (c1 != r2) {
        printf("matrix multiplication is not possible.\n");
        return 0;
    }

    int result[r1][c2];

    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            result[i][j] = 0;

            for (int k = 0; k < c1; k++) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }

    printf("resultant Matrix:\n");
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }

    return 0;
}
