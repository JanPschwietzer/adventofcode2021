using System;
using System.IO;
using System.Text;

namespace Übungen
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            string text = File.ReadAllText("../../Input.txt");
            string[] sNumbers = text.Split('\n');

            Console.WriteLine($"Star 1: {StarOne(sNumbers)}");
            Console.WriteLine($"Star 2: {StarTwo(sNumbers)}");
        }


        public static int StarOne(string[] numbers)
        {
            int counter = 0;
            int comp = 0;

            foreach (string value in numbers)
            {
                if (comp != 0 && comp < System.Convert.ToInt32(value))
                {
                    counter++;
                }
                comp = System.Convert.ToInt32(value);
            }

            return counter;
        }


        public static int StarTwo(string[] numbers)
        {
            int counter = 0;

            for (int i = 0; i < numbers.Length - 3; i++)
            {
                if (System.Convert.ToInt32(numbers[i]) + System.Convert.ToInt32(numbers[i+1]) + System.Convert.ToInt32(numbers[i+2]) < System.Convert.ToInt32(numbers[i+1]) + System.Convert.ToInt32(numbers[i+2]) + System.Convert.ToInt32(numbers[i+3]))
                {
                    counter++;
                }
            }

            return counter;
        }
    }
}
