using System;
using System.Collections.Generic;

class Auditorium // обьект Аудитория
{
    private int Seats { get; set; } // Места
    private int FloorNumber { get; set; } // Этаж
    private int RoomNumber { get; set; } // Номер
    private int HasProjector { get; set; } // Проектор
    /*
     и остальные параметры
    */

    public Auditorium(int seats, int floorNumber, int roomNumber, int hasProjector) // Конструктор класса Аудитория
  {
      Seats = seats;
      FloorNumber = floorNumber;
      RoomNumber = roomNumber;
      HasProjector = hasProjector;
  }

  public void ShowInfo() // Метод вывода информации
  {
      Console.Write($" Количество мест: {Seats} |");
      Console.Write($" Номер этажа: {FloorNumber} |");
      Console.Write($" Номер кабинета: {RoomNumber} |");
      Console.WriteLine($" Есть проектор: {HasProjector} |");
  }

  public bool IsHasProjector() // Медод проверки на наличие проектора
  {
    if(HasProjector == 1)
    {
      return true;
    }
    else
    {
      return false;
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

    public void ShowMenu(List<Auditorium> auditoriumList) // метод показать меню, принимающий список аудиторий
    {
        int seats;
        int floorNumber;
        int roomNumber;
        int hasProjector;
        int choice;

        while (true) // делать пока приблизительно всегда
        {
            Console.WriteLine();
            Console.WriteLine("1. Добавить аудиторию");
            Console.WriteLine("2. Список аудиторий с проектором");
            Console.Write("Выберите действие (1-2): ");

            choice = Convert.ToInt32(Console.ReadLine()); // choice по английски выбор

            switch (choice)
            {
                case 1:
                    Console.Write("Введите количество мест: ");
                    seats = Convert.ToInt32(Console.ReadLine()); 
                    Console.Write("Введите номер этажа: ");
                    floorNumber = Convert.ToInt32(Console.ReadLine());
                    Console.Write("Введите номер аудитории: ");
                    roomNumber = Convert.ToInt32(Console.ReadLine());
                    Console.Write("Введите наличие проектора(1 - есть, 0 - нет): ");
                    hasProjector = Convert.ToInt32(Console.ReadLine());
                    Auditorium newAuditorium = new Auditorium(seats, floorNumber, roomNumber, hasProjector); // новая аудитория
                    auditoriumList.Add(newAuditorium); // добавляем новую аудиторию в список
                    break;
                case 2:
                    foreach(Auditorium auditorium in auditoriumList)
                    {
                        if(auditorium.IsHasProjector() == true)
                      {
                        auditorium.ShowInfo();
                      }
                    }
                    break;
            }
        }
    }
}

class Program 
{
  public static void Main () 
  {
    List<Auditorium> auditoriumList = new List<Auditorium>();
    Menu menu = new Menu();
    menu.ShowMenu(auditoriumList);
  }
  
}
