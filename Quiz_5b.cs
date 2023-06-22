using System;

public class Class1
{
	public Class1()
	{
        Rectangle rect1 = new Rectangle(0.3, 0.5, 1.1, 0.7);
        Rectangle rect2 = new Rectangle(0.5, 0.2, 1.1, 2);

        bool pointInBothRectangles = inside(1, 1, rect1) && inside(1, 1, rect2);
    }
}
