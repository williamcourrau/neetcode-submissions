public class Solution {

    public string Encode(IList<string> strs) 
    {
        var sep = "#";
        var ans = string.Empty;
        foreach(var str in strs)
        {
            var temp = "";
            var wordLength = str.Length;
            temp = $"{wordLength}{sep}{str}";

            Console.WriteLine(temp);

            ans += temp;
        }

        return ans;
    }

    public List<string> Decode(string s) 
    {
        var ans = new List<string>();
        var wordLen = string.Empty;  
        for(int i = 0; i < s.Length; i++)
        {
            // var wordLen =+ s[i];  
            Console.WriteLine(wordLen);
            var current = s[i];
            if(current != '#')
            {
                wordLen += s[i];  
            }

            if(current == '#') // iterate until get the other word
            {
                //Console.WriteLine(wordLen);
                var limit = i + Int32.Parse(wordLen);
                var wordAdd = string.Empty;
                
                for(int y = i + 1; y <= limit; y++)
                {
                    //Console.WriteLine(s[y]);
                    wordAdd += s[y];
                }
                
                ans.Add(wordAdd);
                wordLen = "";
                i = limit;
                //Console.WriteLine(wordLen);
            }
        }

        return ans;
    }
}
