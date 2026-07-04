public class Solution {
    public int MinScore(int n, int[][] roads) {
        var g=new List<int[]>[n+1];
        for(int i=1;i<=n;i++)
            g[i]=new List<int[]>();
        foreach(var r in roads){
            g[r[0]].Add(new[]{r[1],r[2]});
            g[r[1]].Add(new[]{r[0],r[2]});
        }
        var v=new bool[n+1];
        int answer=int.MaxValue;
        var stack=new Stack<int>();
        stack.Push(1);
        while(stack.Count>0){
            int u=stack.Pop();
            if(v[u])continue;
            v[u]=true;
            foreach(var e in g[u]){
                answer=Math.Min(answer,e[1]);
                if(!v[e[0]])
                    stack.Push(e[0]);
            }
        }
        return answer;
    }
}
//QED
//Problem 2492 (Medium of Minimum Score Of A Path Between Two Cities) - Jason Balayev (csharp)
