public class Solution {
    public IList<string> FizzBuzz(int n) {
        var answer=new string[n];
        for(int i=1;i<=n;i++){
            if(i%15==0)answer[i-1]="FizzBuzz";
            else if(i%3==0)answer[i-1]="Fizz";
            else if(i%5==0)answer[i-1]="Buzz";
            else answer[i-1]=i.ToString();
        }
        return answer;
    }
}
//QED
//Problem 412 (Easy of Fizz Buzz) - Jason Balayev (csharp)
