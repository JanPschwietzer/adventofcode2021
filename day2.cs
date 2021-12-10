using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

namespace Übungen
{
    class MainClass
    {
        public static void Main(string[] args)
        {

            string text = File.ReadAllText("../../Input.txt");
            string[] array = text.Split('\n');
            List<string> list = SplitSpacesInArray(array);


            PrintToConsole(list.ToArray());
            PrintToConsole(list.ToArray(), false);
        }

        /*  PrintToConsole Method
         *
         *  can either print the result of Star 1 or Star 2 to the console.
         * 
         */

        public static void PrintToConsole(string[] array, bool star1 = true)
        {
            if (star1)
            {
                Console.WriteLine($"Star 1: {StarOne(array)}");
            }
            else
            {
                Console.WriteLine($"Star 2: {StarTwo(array)}");
            }
        }


        /*  SplitSpacesInArray Method
         *
         *  Takes the raw data where the "\n"'s are splitted already and
         *  returns a list with the instructions and values splitted 
         * 
         */

        public static List<string> SplitSpacesInArray(string[] array)
        {

            List<string> newArray = new List<string>();

            for (int i = 0; i < array.Length; i++)
            {
                string[] valueCut = array[i].Split(null);

                Console.WriteLine(valueCut[0]);

                for (int j = 0; j < valueCut.Length; j++)
                {
                    newArray.Add(valueCut[j]);
                }
            }
            return newArray;
        }


        /*  StarOne Method
         *
         *  calculates the result of the first star, takes a string array
         *  the SplitSpacesInArray Method needs to be called first to seperate
         *  the values and instructions and the List needs to be converted into an array.
         * 
         */

        public static int StarOne(string[] array)
        {
            int posX = 0;
            int posY = 0;

            for (int i = 0; i < array.Length; i += 2)
            {
                Console.WriteLine(array[i]);
                if (array[i] == "forward") posX += System.Convert.ToInt32(array[i + 1]);
                else if (array[i] == "down") posY += System.Convert.ToInt32(array[i + 1]);
                else if (array[i] == "up") posY -= System.Convert.ToInt32(array[i + 1]);
            }

            return posX * posY;
        }

        /*  StarOne Method
         *
         *  same as with the StarOne Method
         * 
         */

        public static int StarTwo(string[] array)
        {
            int posX = 0;
            int posY = 0;
            int aim = 0;

            for (int i = 0; i < array.Length; i++)
            {
                if (array[i] == "forward")
                {
                    posX += System.Convert.ToInt32(array[i + 1]);

                    if (aim != 0) posY += aim * System.Convert.ToInt32(array[i + 1]);
                }
                else if (array[i] == "down") aim += System.Convert.ToInt32(array[i + 1]);
                else if (array[i] == "up") aim -= System.Convert.ToInt32(array[i + 1]);

            }

            return posX * posY;
        }


    }
}
