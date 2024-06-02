using System;
using System.Collections.Generic;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        Console.OutputEncoding = Encoding.UTF8;
        MainMenu();
    }

    static void MainMenu()
    {
        while (true)
        {
            Console.WriteLine("\nМеню:");
            Console.WriteLine("1. Автор");
            Console.WriteLine("2. Посчитать правую польскую запись");
            Console.WriteLine("3. Проверка на правильность скобок");
            Console.WriteLine("4. Выход");

            Console.Write("Выберите пункт меню: ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    ShowAuthor();
                    break;
                case "2":
                    CalculateRPN();
                    break;
                case "3":
                    CheckBrackets();
                    break;
                case "4":
                    Console.WriteLine("Выход из программы.");
                    return;
                default:
                    Console.WriteLine("Некорректный выбор. Попробуйте еще раз.");
                    break;
            }
        }
    }

    static void ShowAuthor()
    {
        Console.WriteLine("\nАвтор: Бухинник Дмитрий Евгеньевич");
        Console.WriteLine("Нажмите Enter для возврата в меню.");
        Console.ReadLine();
    }

    static void CalculateRPN()
    {
        Console.Write("\nВведите правую польскую запись (через пробел): ");
        string expression = Console.ReadLine();
        string result = EvaluateRPN(expression);
        Console.WriteLine($"Результат: {result}");
        Console.WriteLine("Нажмите Enter для возврата в меню.");
        Console.ReadLine();
    }

    static string EvaluateRPN(string expression)
    {
        var ops = new Dictionary<string, Func<double, double, double>>
        {
            { "+", (a, b) => a + b },
            { "-", (a, b) => a - b },
            { "*", (a, b) => a * b },
            { "/", (a, b) => a / b }
        };

        var stack = new Stack<double>();
        foreach (var token in expression.Split())
        {
            if (ops.ContainsKey(token))
            {
                if (stack.Count < 2)
                    return "Ошибка: недостаточно операндов.";
                
                double b = stack.Pop();
                double a = stack.Pop();
                
                if (token == "/" && b == 0)
                    return "Ошибка: деление на ноль.";

                stack.Push(ops[token](a, b));
            }
            else
            {
                if (double.TryParse(token, out double number))
                {
                    stack.Push(number);
                }
                else
                {
                    return "Ошибка: некорректное значение.";
                }
            }
        }

        return stack.Count == 1 ? stack.Pop().ToString() : "Ошибка: некорректное выражение.";
    }

    static void CheckBrackets()
    {
        Console.Write("\nВведите выражение для проверки скобок: ");
        string expression = Console.ReadLine();
        bool result = IsBalanced(expression);
        Console.WriteLine(result ? "Скобки расставлены правильно." : "Скобки расставлены неправильно.");
        Console.WriteLine("Нажмите Enter для возврата в меню.");
        Console.ReadLine();
    }

    static bool IsBalanced(string expression)
    {
        var stack = new Stack<char>();
        var brackets = new Dictionary<char, char>
        {
            { '(', ')' },
            { '{', '}' },
            { '[', ']' }
        };

        foreach (var ch in expression)
        {
            if (brackets.ContainsKey(ch))
            {
                stack.Push(ch);
            }
            else if (brackets.ContainsValue(ch))
            {
                if (stack.Count == 0 || brackets[stack.Pop()] != ch)
                    return false;
            }
        }

        return stack.Count == 0;
    }
}
