import LinkedLists as li

def findMergeNode(head1, head2):
    curr1 = head1
    curr2 = head2

    while curr1 != curr2:
        if curr1.next == None:
            curr1 = head2
        else:
            curr1 = curr1.next
        
        if curr2.next == None:
            curr2 = head1
        else:
            curr2 = curr2.next
    return curr1.data