// gcc -o hello -fopenmp one.cpp
// ./hello

// including the libraries
#include <bits/stdc++.h>
#include <iostream>
#include <omp.h>
// #include <cstdlib>


using namespace std;

// declaring the size
const int sizen = 716;

//716 == 1.236

// declaring matrix
int costMatrixA[sizen][sizen];
int costMatrixB[sizen][sizen];
int productMat[sizen][sizen];



int main()
{   // records time
    double start;
    double end;
    start = omp_get_wtime();



    int i, j, k;
    srand(time(0));


    // initialisation (creating random matrices)
    for (i = 0; i < sizen; i++)
    {
        for (j = 0; j < sizen; j++)
        {
            costMatrixA[i][j] = 1 + rand() % 10;
            costMatrixB[i][j] = 1 + rand() % 10;
            productMat[i][j] = 0;
        }
    }

    // int cost_A[sizen][sizen];

    int x, y;
    for (x = sizen - 1; x >= 0; x--)
    {
        for (y = sizen - 1; y >= 0; y--)
        {
            if (y == sizen - 1 && x == sizen - 1) // for last corner cell
            {
                costMatrixA[x][y] = costMatrixA[x][y];
            }
            else if (y == sizen - 1 && x != sizen - 1) // for last column
            {
                costMatrixA[x][y] = costMatrixA[x][y] + costMatrixA[x + 1][y];
            }
            else if (y != sizen - 1 && x == sizen - 1) // for last column
            {
                costMatrixA[x][y] = costMatrixA[x][y] + costMatrixA[x][y + 1];
            }
            else
            {
                costMatrixA[x][y] = costMatrixA[x][y] + min(costMatrixA[x][y + 1], costMatrixA[x + 1][y]);
            }
        }
    }

    int cost_B[sizen][sizen];

    for (x = sizen - 1; x >= 0; x--)
    {
        for (y = sizen - 1; y >= 0; y--)
        {
            if (y == sizen - 1 && x == sizen - 1) // for last corner cell
            {
                cost_B[x][y] = costMatrixB[x][y];
            }
            else if (y == sizen - 1 && x != sizen - 1) // for last column
            {
                cost_B[x][y] = costMatrixB[x][y] + cost_B[x + 1][y];
            }
            else if (y != sizen - 1 && x == sizen - 1) // for last column
            {
                cost_B[x][y] = costMatrixB[x][y] + cost_B[x][y + 1];
            }
            else
            {
                cost_B[x][y] = costMatrixB[x][y] + min(cost_B[x][y + 1], cost_B[x + 1][y]);
            }
        }
    }

    //creating productMat as explained in the beginning
    for (i = 0; i < sizen; i++)
    {
        for (j = 0; j < sizen; j++)
        {
            for (k = 0; k < sizen; k++)
                productMat[i][j] += costMatrixA[i][k] * cost_B[k][j];
        }
    }

    //filter of size 4 x n
    int filterArray[4][sizen];
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < sizen; j++)
            filterArray[i][j] = rand() % 2;
    }

    // matrix of dimension (sizen/c) x 1 where c = 4
    int finalMat[sizen / 4];
    // applying the filter

//    #pragma omp parallel for schedule (auto) 
    for (i = 0; i < sizen - 4; i += 4)
    {
        int sum = 0;
        // dot product of 4xn portion of productMat
        // #pragma omp parallel for schedule (auto)
        for (j = 0; j < sizen; j++)
        {
            // #pragma omp parallel for reduction(+:sum)
            for (int filterRow = 0; filterRow < 4; filterRow++)
            {
                sum += productMat[i + filterRow][j] * filterArray[i][j];
            }
        }
        finalMat[i / 4] = sum;
    }

    end = omp_get_wtime();
    printf("Work took %f seconds\n", end - start);

    return 0;
}