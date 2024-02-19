using System;
using System.Collections.Generic;

class Auditoriums // обьект Аудитории
{
    class Auditorium // обьект Аудитория
    {
        public int Seats { get; set; } // Места
        public int FloorNumber { get; set; } // Этаж
        public int RoomNumber { get; set; } // Номер
        /*
         и остальные параметры
        */
    }
    
    private List<Auditorium> auditoriums; // список всех аудиторий
    
    public Auditoriums() // конструктор класса Auditoriums
    {
        auditoriums = new List<Auditorium>(); // инициализация списка аудиторий 
    }
    
    public void AddAuditorium() // метод добавления
    {
        Auditorium newAuditorium = new Auditorium(); // новая аудитория
        Console.Write("Введите количество мест: ");
        newAuditorium.Seats = Convert.ToInt32(Console.ReadLine()); 
        Console.Write("Введите номер этажа: ");
        newAuditorium.FloorNumber = Convert.ToInt32(Console.ReadLine());
        Console.Write("Введите номер аудитории: ");
        newAuditorium.RoomNumber = Convert.ToInt32(Console.ReadLine());
        
        auditoriums.Add(newAuditorium); // добавляем аудиторию в список всех аудиторий
        Console.WriteLine("Аудитория добавлена успешно.");
    }
    
    public void ListAuditoriumsBySeats(int minSeats) // метод выборки по наличию мест
    {
        Console.WriteLine($"Список аудиторий с количеством мест больше-равно {minSeats}:");
        foreach (var auditorium in auditoriums) // для каждой аудитории
        {
            if (auditorium.Seats >= minSeats) // проверяем условие
            {
                Console.WriteLine($"Этаж {auditorium.FloorNumber}, Аудитория {auditorium.RoomNumber}");
            }
        }
    }
     /*
    и остальные необходимые методы
    */
}

class Menu // обьект Меню
{
    
    public Menu() // конструктор класса Menu
    {
        
    }
    
    public void ShowMenu(Auditoriums Auds) // метод показать меню
    {
        int choice;
        int minSeats;
        
        while (true) // делать пока приблизительно всегда
        {
            Console.WriteLine("1. Добавить аудиторию");
            Console.WriteLine("2. Список аудиторий с количеством мест больше-равно заданному");
            Console.Write("Выберите действие (1-2): ");
            
            choice = Convert.ToInt32(Console.ReadLine()); // choice по английски выбор

            switch (choice)
            {
                case 1:
                    Auds.AddAuditorium();
                    break;
                case 2:
                    Console.Write("Введите минимальное количество мест: ");
                    minSeats = Convert.ToInt32(Console.ReadLine());
                    Auds.ListAuditoriumsBySeats(minSeats);
                    break;
            }
        }
    }
}

class Program 
{
  static void Main() 
  {
        Auditoriums Auds = new Auditoriums(); // создаем обьект Аудитории
        Menu menu = new Menu(); // создаем Меню
        menu.ShowMenu(Auds); // Вызываем меню для выбранного обьекта Аудитории
  }
}
