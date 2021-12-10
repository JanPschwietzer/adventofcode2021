using System;
using System.Collections.Generic;
using System.Linq;

namespace AdventOfCode
{
    public class Program
    {
        public static void Main(string[] args)
        {
            string text = File.ReadAllText("$PATH");
            string[] array = text.Split("\n");

            Console.WriteLine($"Star 1: {StarOne(array)}");
            Console.WriteLine($"Star 2: {StarTwo(array)}");
        }

        public static int StarOne(string[] array)
        {
            int counter1 = 0;
            int counter0 = 0;

            string gamma = "";
            string epsilon = "";

            for (int i = 0; i < array[0].Length; i++)
            {
                foreach (string value in array)
                {
                    if (value[i] == '1') counter1++;
                    else if (value[i] == '0') counter0++;
                }

                if (counter1 >= counter0)
                {
                    gamma += "1";
                    epsilon += "0";
                }
                else
                {
                    gamma += "0";
                    epsilon += "1";
                }

                counter1 = 0;
                counter0 = 0;
            }

            return System.Convert.ToInt32(gamma, 2) * System.Convert.ToInt32(epsilon, 2);
        }

        public static int StarTwo(string[] array)
        {
            string gamma;
            string epsilon;
            int lenBinNum = 12;
            int counter1;
            char isOne;

            List<string> gammaList = new List<string>(array);
      

            for (int i = 0; i < lenBinNum; i++)
            {
                counter1 = 0;

                for (int j = 0; j < gammaList.Count; j++)
                {
                    if (gammaList[j][i] == '1') counter1++;
                }

                int gammaListCount = 0;
                if (gammaList.Count % 2 == 1) gammaListCount = (gammaList.Count + 1) / 2;
                else gammaListCount = gammaList.Count / 2;

                if (counter1 >= gammaListCount) isOne = '1';
                else isOne = '0';

                for (int k = gammaList.Count - 1; k >= 0; k--)
                {
                    if (gammaList[k][i] != isOne && gammaList.Count != 1) gammaList.RemoveAt(k);
                }
            }
            gamma = gammaList[0];


            List<string> epsilonList = new List<string>(array);

            for (int i = 0; i < lenBinNum; i++)
            {
                counter1 = 0;

                for (int j = 0; j < epsilonList.Count; j++)
                {
                    if (epsilonList[j][i] == '1') counter1++;
                }

                int epsilonListCount = 0;
                if (epsilonList.Count % 2 == 1) epsilonListCount = (epsilonList.Count + 1) / 2;
                else epsilonListCount = epsilonList.Count / 2;

                if (counter1 >= epsilonListCount) isOne = '1';
                else isOne = '0';

                for (int k = epsilonList.Count - 1; k >= 0; k--)
                {
                    if (epsilonList[k][i] == isOne && epsilonList.Count != 1) epsilonList.RemoveAt(k);
                }
            }
            epsilon = epsilonList[0];

            return System.Convert.ToInt32(gamma, 2) * System.Convert.ToInt32(epsilon, 2);
        }
    }
}
