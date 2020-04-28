def sortedInsert(head, data):
    newNode = DoublyLinkedListNode(data)
    if head is None:
        return newNode
    temp = head
    if (data >= temp.data):
        while True:
            if (temp.next is not None):
                if (data <= temp.next.data):
                    newNode.next = temp.next
                    temp.next = newNode
                    newNode.prev = temp
                    newNode.next.prev = newNode
                    return head
                else:
                    temp = temp.next
            else:
                temp.next = newNode
                newNode.prev = temp
                return head
    else:
        temp.prev = newNode
        newNode.next = temp
        head = newNode
        return head