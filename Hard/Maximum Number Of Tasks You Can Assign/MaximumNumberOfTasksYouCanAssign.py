class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def bin_search(arr,target):
            left,right=0, len(arr)-1
            res=len(arr)
            while left<=right:
                mid=(left+right)//2
                if arr[mid]>=target:
                    res=mid
                    right=mid-1
                else:
                    left=mid+1
            return res
        
        def complete_k(k:int)->bool:
            if k>len(workers) or k>len(tasks):
                return False
            selected_tasks=tasks[:k]
            selected_workers=workers[len(workers)-k:]
            pills_remaining=pills
            worker_idx=k-1
            for i in range(k-1,-1,-1):
                task=selected_tasks[i]
                if selected_workers[worker_idx]>=task:
                    worker_idx-=1
                    continue
                if pills_remaining<=0:
                    return False
                min_req=task-strength
                pos=bin_search(selected_workers,min_req)
                if pos>=worker_idx+1:
                    return False
                pills_remaining-=1
                selected_workers.pop(pos)
                worker_idx-=1
            return True
        
        left,right=0,min(len(tasks), len(workers))
        res=0

        while left<=right:
            mid=(left+right)//2
            if complete_k(mid):
                res=mid
                left=mid+1
            else:
                right=mid-1
        return res

#QED
#Problem 2071 (Hard of Maximum Number Of Tasks You Can Assign) - Jason Balayev (python)  
