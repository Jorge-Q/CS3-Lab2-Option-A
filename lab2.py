# Created by:Jorge Quinonez
# Last date modified: October 18, 2018
# Assignment: Lab 2, Version A
# Professor: Diego Aguirre

class Node(object):

    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, data):  # Insertion method for my LinkedList class
        if self.head is None:
            self.head = Node(data, None)
            self.size += 1
        else:
            temp = self.head
            new_node = Node(data, None)
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            self.size += 1

    def getHead(self):
        return self.head

    def getSize(self):
        return self.size

    # Solution #1,comparing all elements with one another to find duplicates
    def solution1(self):
        currentNode = self.head
        while currentNode is not None:  # Comparing every element with one another with nested while loops
            nextNode = currentNode.next
            while nextNode is not None:
                if currentNode.data == nextNode.data:
                    print("Duplicate found:", currentNode.data)
                nextNode = nextNode.next
            currentNode = currentNode.next

    # Solution #2, sorting the linked list using bubble sort
    def solution2(self):
        yes_no = True
        while yes_no is True:
            yes_no = False  # Boolean is immediately set to False ending the loop, unless elements are switched
            temp = self.head
            while temp.next is not None:
                if temp.data > temp.next.data:
                    place_holder = Node(temp.data, None)
                    temp.data = temp.next.data
                    temp.next.data = place_holder.data
                    yes_no = True
                temp = temp.next

    # Solution #4, creating a list of booleans that tell you if a number is repeated on the list
    def solution4(self):
        temp = self.head
        size = self.getSize() + 1  # Size is m + 1
        yes_no = [False] * size  # All are set to false until the numbers are seen more than once in the LL
        seen_numbers = []  # To keep track of seen numbers
        duplicates_counter = 0
        while temp is not None:
            if temp.data in seen_numbers:  # If the current number has been seen before in the LL
                yes_no[temp.data] = True
                duplicates_counter += 1
            else:
                seen_numbers.append(temp.data)
            temp = temp.next

        temp = self.head  # Resetting temp to head again to print results from numbers on list
        while temp is not None:  # Printing the entire list with a boolean to know if it appears more than once in LL
            print("There are duplicates of ", temp.data, ": ", yes_no[temp.data])
            temp = temp.next
        print("The total number of found repeats is:", duplicates_counter)


# Method used to print the linked list to test that other methods are working properly
def print_LL(head):
    if head is None:
        print("Linked List is empty")
    else:
        temp = head
        num_elements = 0
        while temp is not None:
            print(temp.data)
            num_elements += 1
            temp = temp.next
        print("Total number of elements is:", num_elements)


# Method that is used for Solution#3, splits a linked list in half and returns the head of those two LL
def split_LL(head):
    if head is None or head.next is None:
        return head, None
    else:
        mid_node = head  # mid_node will reach the middle of the list by the time end_node reaches None
        end_node = head.next
        while end_node is not None:
            end_node = end_node.next
            if end_node is not None:
                mid_node = mid_node.next
                end_node = end_node.next

    first_half = head  # First half begins at the original head
    second_half = mid_node.next  # Saving where the second half starts
    mid_node.next = None  # Breaking the link between the first and second half
    return first_half, second_half


# Method that is used for Solution#3, method sorts the elements of two linked lists into a single sorted linked list
def mergeSort(first_half, second_half):
    new_head = Node(None, None)
    temp = new_head
    while first_half is not None and second_half is not None:  # As long as neither of the lists are empty
        if first_half.data <= second_half.data:  # If
            temp.next = first_half
            first_half = first_half.next
        else:
            temp.next = second_half
            second_half = second_half.next
        temp = temp.next
    if first_half is None:  # If the left LL is empty we add the remaining right LL to our new LL
        temp.next = second_half
    elif second_half is None:  # If the right LL is empty we add the remaining left LL to our new LL
        temp.next = first_half
    return new_head.next  # Returning new sorted linked list, skipping the empty node that we created


# Solution #3, sorting the linked list by using merge sort
def solution3(head):
    if head is None or head.next is None:
        return head
    else:
        first_half, second_half = split_LL(head) # Splitting the linked list in half
        first_half = solution3(
            first_half)  # Will recursively call until the the lists are made up of individual elements
        second_half = solution3(second_half)
    return mergeSort(first_half, second_half)  # Merging the lists


def main():
    file_activision = open("activision.txt", "r")
    file_vivendi = open("vivendi.txt", "r")
    bubble_List = LinkedList()
    merge_List = LinkedList()
    solution4_List = LinkedList()
    # Using multiple LL, one for Bubble Sort, another for Merge Sort, another for solution 4 since instructions
    # stated to use an unordered one
    for line in file_activision:
        number_id = int(line.strip())
        bubble_List.insert(number_id)
        merge_List.insert(number_id)
        solution4_List.insert(number_id)
    for line in file_vivendi:
        number_id = int(line.strip())
        bubble_List.insert(number_id)
        merge_List.insert(number_id)
        solution4_List.insert(number_id)

    print("****************************************")
    print("Test for Solution #1:")
    print("The following duplicates were found:")
    bubble_List.solution1()
    print("****************************************")
    print("Test for Solution #2:")
    print("The linked list will now be sorted using bubble sort.")
    bubble_List.solution2()
    bubble_head = bubble_List.getHead()
    print_LL(bubble_head)
    print("****************************************")
    print("Test for Solution #3:")
    print("The linked list will now be sorted using merge sort.")
    head = merge_List.getHead()
    sorted_LL = solution3(head)
    print_LL(sorted_LL)
    print("****************************************")
    print("Test for Solution #4")
    solution4_List.solution4()
    print("****************************************")


main()
