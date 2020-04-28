import LinkedLists as li

def removeDuplicates(head):
    if head == None or head.next == None:
        return head
    result = head
    while head.next != None:
        if head.data == head.next.data:
            temp = head.next
            head.next = temp.next
        else:
            head = head.next
    return result

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

li1 = li.LinkedList()

li1.append(10)
li1.append(10)
li1.append(20)
li1.append(20)
li1.append(30)
li1.append(40)
li1.append(40)

dup = removeDuplicates(li1.head)
print_singly_linked_list(dup, " ")