func largestPathValue(colors string, edges [][]int) int {
    n:=len(colors)
    graph:=make([][]int,n)
    degree:=make([]int,n)
    for _,edge:=range edges{
        from,to:=edge[0],edge[1]
        graph[from]=append(graph[from],to)
        degree[to]++
    }
    dp:=make([][]int,n)
    for i:=0;i<n;i++{
        dp[i]=make([]int,26)
        colorIdx:=int(colors[i]-'a')
        dp[i][colorIdx]=1
    }
    queue:=make([]int,0)
    for i:=0;i<n;i++{
        if degree[i]==0{
            queue=append(queue,i)
        }
    }
    visit:=0
    maxVal:=0
    for len(queue)>0{
        node:=queue[0]
        queue=queue[1:]
        visit++
        for _,neighbor:=range graph[node]{
            for color:=0;color<26;color++{
                add:=0
                if int(colors[neighbor]-'a')==color{
                    add=1
                }
                if dp[node][color]+add>dp[neighbor][color] {
                    dp[neighbor][color]=dp[node][color]+add
                }
            }
            degree[neighbor]--
            if degree[neighbor]==0{
                queue=append(queue,neighbor)
            }
        }
        for color:=0;color<26;color++{
            if dp[node][color]>maxVal {
                maxVal=dp[node][color]
            }
        }
    }
    if visit==n{
        return maxVal
    }
    return -1
}

func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}

//QED
//Problem 1857 (Hard of Largest Color Value In A Directed Graph) - Jason Balayev (go)