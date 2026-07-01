public class Solution {
    public char FindTheDifference(string s, string t) {
        int x=0;
        foreach (var c in s) x^=c;
        foreach (var c in t) x^=c;
        return (char)x;
    }
}

//QED
//Problem 389 (Easy of Find The Difference) - Jason Balayev (csharp)
