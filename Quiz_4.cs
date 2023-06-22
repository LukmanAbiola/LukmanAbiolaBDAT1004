using System;

public class Class1
{
	public Class1()
	{

        public class Program
    {
        public static void Main()
        {
            int n;
            Console.Write("Input the number of elements to be stored in the array: ");
            n = Convert.ToInt32(Console.ReadLine());

            int[] arr = new int[n];
            int[] evenArr = new int[n];
            int[] oddArr = new int[n];
            int evenCount = 0;
            int oddCount = 0;

            Console.WriteLine($"Input {n} elements in the array:");
            for (int i = 0; i < n; i++)
            {
                Console.Write($"element - {i} : ");
                arr[i] = Convert.ToInt32(Console.ReadLine());

                if (arr[i] % 2 == 0)
                {
                    evenArr[evenCount] = arr[i];
                    evenCount++;
                }
                else
                {
                    oddArr[oddCount] = arr[i];
                    oddCount++;
                }
            }

            Console.Write("The Even elements are: ");
            for (int i = 0; i < evenCount; i++)
            {
                Console.Write($"{evenArr[i]} ");
            }

            Console.Write("\nThe Odd elements are: ");
            for (int i = 0; i < oddCount; i++)
            {
                Console.Write($"{oddArr[i]} ");
            }
        }
    }


}
}
