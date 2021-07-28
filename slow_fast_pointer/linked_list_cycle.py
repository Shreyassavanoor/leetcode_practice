'''
    Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
'''
from linked_list import LinkedList, Node

def detect_cycle(ll):
    slow, fast = ll.head, ll.head
    
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            print(True)
            return
    print(False)

if __name__ == '__main__':
    l_list = LinkedList()
    
    first_node = Node("a")
    second_node = Node("b")
    third_node = Node("c")
    
    l_list.head = first_node
    first_node.next = second_node
    second_node.next = third_node
    
    detect_cycle(l_list)
    
    fourth_node = Node("d")
    third_node.next = fourth_node
    fourth_node.next = second_node
    
    detect_cycle(l_list)
    
