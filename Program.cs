/*// Задача 2: Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.
Console.WriteLine("imput a nummer1: ");
int num1=Convert.ToInt32(Console.ReadLine());
Console.WriteLine("imput a nummer2: ");
int num2=Convert.ToInt32(Console.ReadLine());

if (num1 < num2)
    Console.WriteLine ("maximal nammber " + num2);
else
    Console.WriteLine ("maximal nammber " + num1);
    
    //Задача 4: Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.

Console.WriteLine("imput a nummer1: ");
int num1=Convert.ToInt32(Console.ReadLine());
Console.WriteLine("imput a nummer2: ");
int num2=Convert.ToInt32(Console.ReadLine());
Console.WriteLine("imput a nummer3: ");
int num3=Convert.ToInt32(Console.ReadLine());
if (num1>num2)
           if (num1>num3)
           Console.WriteLine("maximal nammber " + num1);
           else
           Console.WriteLine("maximal nammber " + num3);
else 
     if(num2 > num3)
     Console.WriteLine ("maximal nammber " + num2);
     else
     Console.WriteLine ("maximal nammber " + num3);

     //Задача 6: Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).
Console.WriteLine("imput a nummer1: ");
int num=Convert.ToInt32(Console.ReadLine());

if (num % 2 == 0)
Console.WriteLine ("nammber is even ");
else 
Console.WriteLine ("nammber is odd");

//Задача 8: Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
Console.WriteLine("imput a nummer1: ");
int N=Convert.ToInt32(Console.ReadLine());
 int current = 2;
if (N>0)
    
    while (current<=N)
    {
        Console.Write (current+",");
        current=current+2;
    }
*/