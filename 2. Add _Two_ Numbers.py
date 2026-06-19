class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=l1
        count=""
        while head!=None:
            count+=str(head.val)
            head=head.next
        count=int(count[::-1])
        tail=l2
        count1=""
        while tail!=None:
            count1+=str(tail.val)
            tail=tail.next
        count1=int(count1[::-1])
        add=count+count1
        newlist=None
        for i in str(add)[::-1]:
            if newlist==None:
                newlist=ListNode(int(i))
                head=newlist
                
            else:
                n1=ListNode(int(i))
                newlist.next=n1
                newlist=n1
                
        return head      

                

        
        
