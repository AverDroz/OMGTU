using System;
using System.Globalization;

namespace ProductionIntensification
{
    class Program
    {
        static void Main(string[] args)
        {
            // Чтение данных из файла
            string startDateString = Console.ReadLine();
            string endDateString = Console.ReadLine();
            DateTime startDate = DateTime.ParseExact(startDateString, "dd.MM.yyyy", CultureInfo.InvariantCulture);
            DateTime endDate = DateTime.ParseExact(endDateString, "dd.MM.yyyy", CultureInfo.InvariantCulture);
            int initialProduction = Convert.ToInt32(Console.ReadLine());

            // Вычисление разницы в днях
            TimeSpan diff = endDate - startDate;
            int days = diff.Days + 1;

            // Расчет суммарного объема продукции
            int totalProduction = initialProduction;
            for (int i = 1; i < days; i++)
            {
                totalProduction += initialProduction + i;
            }

            // Вывод результата
            Console.WriteLine(totalProduction);
        }
    }
}
