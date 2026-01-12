class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        fast, slow를 이동해서 만나면, slow를 head로 보낸후 같은 속도로 이동해서 다시 만나게 되는 지점이 cycle의 시작점...
        
        너무 천재적이고 알수가 없다.

        그림 그리면 풀수있음. 항상 겹친다.
        1) 길이를 Cycle 시작점까지를 a, 시작지점으로부터 slow, fast가 만난 지점을 b로, Cycle을 길이를 c로 놓는다. 
        2) Slow 와 Fast가 만난걸 수식으로 표시하면, 2*(a+b) = a+b+k*c
        3) a = k*c-b
        4) Slow를 head로 보내고 a만큼을 이동시키면, 같은 속도로 Fast를 움직이면 b로부터 k*c-b를 이동하면 k*c 사이클 시작점에 도착함.

        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
