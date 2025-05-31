from typing import List
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n=len(edges)
        def calc_dist(start_n):
            dist=[-1]*n
            dist[start_n]=0
            curr=start_n
            step=0
            while curr!=-1 and dist[curr]==step:
                next_n=edges[curr]
                step+=1
                if next_n!=-1 and dist[next_n]==-1:
                    dist[next_n]=step
                    curr=next_n
                else:
                    break
            
            return dist
        dist_from_n1=calc_dist(node1)
        dist_from_n2=calc_dist(node2)
        min_max_dist=float('inf')
        res=-1
        for i in range(n):
            if dist_from_n1[i]!=-1 and dist_from_n2[i]!=-1:
                max_dist=max(dist_from_n1[i],dist_from_n2[i])
                if max_dist<min_max_dist:
                    min_max_dist=max_dist
                    res=i
        return res
    
#QED
#Problem 2359 (Medium of Find Closest Node To Given Two Nodes) - Jason Balayev (go)