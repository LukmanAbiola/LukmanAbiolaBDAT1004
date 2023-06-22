using System;

public class Class1
{
	public Class1()
	{
        string word1 = "Supercalifragilisticexpialidocious";
        string word2 = "Honorificabilitudinitatibus";
        string word3 = "Bababadalgharaghtakamminarronnkonn";

        string longestWord = word1;
        if (word2.Length > longestWord.Length)
        {
            longestWord = word2;
        }
        if (word3.Length > longestWord.Length)
        {
            longestWord = word3;
        }

        Console.WriteLine(longestWord);  // Supercalifragilisticexpialidocious
    }
}
