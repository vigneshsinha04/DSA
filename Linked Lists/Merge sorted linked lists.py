import LinkedLists as li

def mergeLists(head1, head2):
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.data <= head2.data:
        head = head1
        curr1 = head1.next
        curr2 = head2
    else:
        head = head2
        curr1 = head1
        curr2 = head2.next

    curr = head

    while True:
        if curr1 is None:
            curr.next = curr2
            break
        elif curr2 is None:
            curr.next = curr1
            break
        
        if curr1.data <= curr2.data:
            curr.next = curr1
            curr1 = curr1.next

        else:
            curr.next = curr2
            curr2 = curr2.next
        curr = curr.next
    return head

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

li1 = li.LinkedList()
li2 = li.LinkedList()

li1.append(10)
li1.append(20)
li1.append(30)
li1.append(40)

li2.append(11)
li2.append(20)
li2.append(32)
li2.append(48)

li3 = mergeLists(li1.head, li2.head)

print_singly_linked_list(li3, " ")