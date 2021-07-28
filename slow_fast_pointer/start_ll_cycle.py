'''
    Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
'''
from linked_list import LinkedList, Node

def find_start_cycle_node(ll):
    slow = ll.head
    fast = ll.head
    index = None
    cycle_length = 0
    
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            index = slow
            break
    
    while(True):
        index = index.next
        cycle_length += 1
        if index == slow:
            break
    
    slow = ll.head
    fast = ll.head
    
    while cycle_length > 0:
        fast = fast.next
        cycle_length -= 1
        
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    print(slow.data)

if __name__ == '__main__':
    l_list = LinkedList()
    
    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)
    fourth_node = Node(4)
    
    l_list.head = first_node
    first_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = second_node
    
    find_start_cycle_node(l_list)