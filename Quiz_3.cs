using System;

public class Class1
{
	public Class1()
	{
        public static double TriangleArea(double a, double b, double c)
        {
            double s = (a + b + c) / 2; // calculate the semi-perimeter
            double area = Math.Sqrt(s * (s - a) * (s - b) * (s - c)); // calculate the area using Heron's formula
            return area;
        }

        Testing the function
double area = TriangleArea(2, 2, 2);
        Console.WriteLine(area); // 1.7320508075688772
    }
}
