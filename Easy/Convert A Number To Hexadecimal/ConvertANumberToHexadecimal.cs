public class Solution {
    public string ToHex(int num) {
         char[] s = new char[8];
         int i=8;
         uint n=(uint)num;
         do{
            s[--i]="0123456789abcdef"[(int)(n&15)];
         } while((n>>=4)!=0);
         return new string(s,i,8-i);
    }
}

//QED
//Problem 405 (Easy of Convert A Number To Hexadecimal) - Jason Balayev (csharp)