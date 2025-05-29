func maxTargetNodes(edges1 [][]int, edges2 [][]int) []int {
    n:=len(edges1)+1
    m:=len(edges2)+1
    g1:=make([][]int,n)
    g2:=make([][]int,m)
    for _,edge:=range edges1{
        u,v:=edge[0],edge[1]
        g1[u]=append(g1[u],v)
        g1[v]=append(g1[v],u)
    }
    for _,edge:=range edges2{
        u,v:=edge[0],edge[1]
        g2[u]=append(g2[u],v)
        g2[v]=append(g2[v],u)
    }
    color:=func(graph[][]int,size int)([]int,[]int){
        colors:=make([]int,size)
        for i:=range colors{
            colors[i]=-1
        }
        count:=make([]int,2)
        var dfs func(node,c int)
        dfs=func(node,c int){
            colors[node]=c
            count[c]++
            for _,next:=range graph[node]{
                if colors[next]==-1{
                    dfs(next,1-c)
                }
            }
        }
        dfs(0,0)
        return colors,count
    }
    c1,cnt1:=color(g1,n)
    _,cnt2:=color(g2,m)
    tree2Max:=cnt2[0]
    if cnt2[1]>tree2Max{
        tree2Max=cnt2[1]
    }
    res:=make([]int,n)
    for i:=0;i<n;i++{
        nodeColor:=c1[i]
        sameAsNodeColor:=cnt1[nodeColor]
        res[i]=sameAsNodeColor+tree2Max
    }
    return res
}

//QED
//Problem 3373 (Hard of Maximize The Number Of Target Nodes After Connecting Trees II) - Jason Balayev (go)