function maxTargetNodes(edges1: number[][], edges2: number[][], k: number): number[] {
    const n=edges1.length+1;
    const m=edges2.length+1;
    const g1:number[][]=Array(n).fill(0).map(()=>[]);
    const g2:number[][]=Array(m).fill(0).map(()=>[]);
    for(const[u,v]of edges1){
        g1[u].push(v);
        g1[v].push(u);
    }
    for(const[u,v]of edges2){
        g2[u].push(v);
        g2[v].push(u);
    }
    function bfs(graph:number[][],start:number,d:number):number{
        if(d<0)return 0;
        const visit=new Array(graph.length).fill(false);
        const queue=[start];
        visit[start]=true;
        let count=1;
        for(let dist=0;dist<d&&queue.length>0;dist++){
            const size=queue.length;
            for(let i=0;i<size;i++){
                const node=queue.shift()!;
                for(const neighbor of graph[node]){
                    if(!visit[neighbor]){
                        visit[neighbor]=true;
                        queue.push(neighbor);
                        count++;
                    }
                }
            }
        }
        return count;
    }
    let maxTree2=0;
    if(k>0){
        for(let i=0;i<m;i++){
            maxTree2=Math.max(maxTree2,bfs(g2,i,k-1));
        }
    }
    const res:number[]=[];
    for(let i=0;i<n;i++){
        res[i]=bfs(g1,i,k)+maxTree2;
    }
    return res;
};