using System;
using System.Linq;

class Program
{
    static void Main()
    {
        Console.Write("Введите N: ");
        int N = int.Parse(Console.ReadLine());

        int[][] sets = new int[N][];
        for (int i = 0; i < N; i++)
        {
            Console.Write($"Введите элементы для множества {i + 1} через пробел: ");
            string input = Console.ReadLine();
            sets[i] = Array.ConvertAll(input.Split(' '), int.Parse);
        }

        int[] intersection = FindIntersection(sets);
        int[] union = FindUnion(sets);
        Console.WriteLine("Пересечение всех множеств: " + string.Join(" ", intersection));
        Console.WriteLine("Объединение всех множеств: " + string.Join(" ", union));

        for (int i = 0; i < N; i++)
        {
            int[] complement = FindComplement(sets[i], union);
            Console.WriteLine($"Дополнение множества {i + 1} относительно объединения: " + string.Join(" ", complement));
        }
    }

    static int[] FindIntersection(int[][] sets)
    {
        if (sets.Length == 0)
            return new int[0];

        int[] result = sets[0];

        for (int i = 1; i < sets.Length; i++)
        {
            result = Intersect(result, sets[i]);
        }

        return result;
    }

    static int[] Intersect(int[] arr1, int[] arr2)
    {
        int[] result = new int[Math.Min(arr1.Length, arr2.Length)];
        int index = 0;

        foreach (int item in arr1)
        {
            if (Array.IndexOf(arr2, item) != -1)
            {
                result[index] = item;
                index++;
            }
        }

        Array.Resize(ref result, index);
        return result;
    }

    static int[] FindUnion(int[][] sets)
    {
        int totalLength = 0;

        foreach (int[] set in sets)
        {
            totalLength += set.Length;
        }

        int[] result = new int[totalLength];
        int index = 0;

        foreach (int[] set in sets)
        {
            foreach (int item in set)
            {
                result[index] = item;
                index++;
            }
        }

        Array.Resize(ref result, index);
        return result.Distinct().ToArray();
    }

    static int[] FindComplement(int[] set, int[] universe)
    {
        int[] result = new int[universe.Length];
        int index = 0;

        foreach (int item in universe)
        {
            if (Array.IndexOf(set, item) == -1)
            {
                result[index] = item;
                index++;
            }
        }

        Array.Resize(ref result, index);
        return result;
    }
}
