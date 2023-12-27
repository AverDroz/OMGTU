using System;

class MatrixDeterminantCalculator
{
    static void Main()
    {
        Console.WriteLine("Введите размерность матрицы (n): ");
        int n = int.Parse(Console.ReadLine());

        double[,] matrix = new double[n, n];

        Console.WriteLine("Введите элементы матрицы построчно через пробел:");

        for (int i = 0; i < n; i++)
        {
            Console.WriteLine($"Введите элементы строки {i + 1}: ");
            string[] rowElements = Console.ReadLine().Split(' ');

            for (int j = 0; j < n; j++)
            {
                matrix[i, j] = double.Parse(rowElements[j]);
            }
        }

        double determinant = CalculateDeterminant(matrix);
        Console.WriteLine($"Determinant: {determinant}");
    }

    static double CalculateDeterminant(double[,] matrix)
    {
        int size = matrix.GetLength(0);

        // Базовый случай: матрица 1x1
        if (size == 1)
        {
            return matrix[0, 0];
        }

        double determinant = 0;

        // Рекурсивно вычисляем определитель
        for (int i = 0; i < size; i++)
        {
            double sign = (i % 2 == 0) ? 1 : -1;
            double subDeterminant = sign * matrix[0, i] * CalculateDeterminant(GetSubmatrix(matrix, 0, i));
            determinant += subDeterminant;
        }

        return determinant;
    }

    static double[,] GetSubmatrix(double[,] matrix, int excludingRow, int excludingColumn)
    {
        int size = matrix.GetLength(0);
        double[,] submatrix = new double[size - 1, size - 1];

        int newRow = 0;
        for (int i = 0; i < size; i++)
        {
            if (i == excludingRow)
            {
                continue;
            }

            int newColumn = 0;
            for (int j = 0; j < size; j++)
            {
                if (j == excludingColumn)
                {
                    continue;
                }

                submatrix[newRow, newColumn] = matrix[i, j];
                newColumn++;
            }

            newRow++;
        }

        return submatrix;
    }
}
