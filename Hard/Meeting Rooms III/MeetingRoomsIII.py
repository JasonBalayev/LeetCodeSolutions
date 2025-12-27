class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        Determines the room that is booked. Rooms are numbered
        from 0 to n-1. Meetings are assigned to the lowest numbered 
        available room. If no room is available, the meeting is delayed
        until the earliest room becomes free, keeping the same duration.

        Args: 
            n(int): Number of available rooms
            meetings (List(List[int])): List of meetings [start,end]
        
        Returns:
            int: Index of the room that hosted the most meetings
        """
        def heap_push(heap,item):
            """
            Pushes an item into a min heap

            Args:
                heap(list): Min heap as a list
                item: Value to input into the heap
            """
            heap.append(item)
            i=len(heap)-1
            while i>0:
                p=(i-1)//2
                if heap[p]<=heap[i]:
                    break
                heap[p],heap[i]=heap[i],heap[p]
                i=p
        def heap_pop(heap):
            """
            Removes and returns the smallest element from a min heap.

            Args:
                heap(list): Min heap as a list
            
            Returns:
                The smallest element in the heap
            """
            root=heap[0]
            last=heap.pop()
            if heap:
                heap[0]=last
                i=0
                size=len(heap)
                while True:
                    l=2*i+1
                    r=2*i+2
                    smallest=i
                    if l<size and heap[l]<heap[smallest]:
                        smallest=l
                    if r<size and heap[r]<heap[smallest]:
                        smallest=r
                    if smallest==i:
                        break
                    heap[i],heap[smallest]=heap[smallest],heap[i]
                    i=smallest
            return root

        meetings.sort()
        available_rooms=[]
        busy_rooms=[]
        count=[0]*n

        for i in range(n):
            heap_push(available_rooms,i)
        for start,end in meetings:
            duration=end-start
            while busy_rooms and busy_rooms[0][0]<=start:
                _,room=heap_pop(busy_rooms)
                heap_push(available_rooms,room)
            if available_rooms:
                room=heap_pop(available_rooms)
                heap_push(busy_rooms,(end,room))
            else:
                end_time,room=heap_pop(busy_rooms)
                heap_push(busy_rooms,(end_time+duration,room))
            count[room]+=1
        
        max_meetings=max(count)
        for i in range(n):
            if count[i]==max_meetings:
                return i

#QED
#Problem 2402 (Hard of Meeting Rooms III) - Jason Balayev (python)