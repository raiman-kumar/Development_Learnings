# # array in DSA
# # array applies through list in python

# myarr = [12,18,16,14,22,11]
# print(myarr)

# n = 5000
# print("start")
# for i in range(n):
#     print(i)
# print("stop")

# n = 5
# for i in range(n):
#     for j in range(n):
#         print(i,j)

# n = 5
# count = 0
# for i in range(n):
#     count += 1
# print(count)

# n = 5
# count = 0
# for i in range(n):
#     for j in range(n):
#         count += 1
# print(count)

# n = 1000
# count = 0

# while n > 0:
#     count += 1
#     n = n // 2

# print(count)

# # find largest elemeent in array

# mylist = [10, 5, 18, 7, 20, 3]
# largest = mylist[0]
# for i in mylist:
#     if i > largest:
#         largest = i
# print(largest)

# # find second largest in array

# mylist = [10, 5, 18, 7, 20, 3]
# largest = mylist[0]
# second_largest = mylist[0]
# for i in mylist:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest and i != largest:
#         second_largest = i
# print(second_largest)

# arr = [10,20,30,40,50]

# print(arr[0])
# print(arr[2])
# print(arr[4])

# # traversal in array

# arr = [10,20,30,40,50]
# print(arr)

# # method 1 : via pythonic
# for i in arr:
#     print(i)

# # method 2 : via index

# for i in range(len(arr)):
#     print(arr[i])

# # method 3 : professional

# for index, value in enumerate(arr):
#     print(index, value)

# # sum of the elements
# summ = 0
# for i in arr:
#     summ += i
# print(summ)

# # count even numbers
# arr = [10,25,18,31,40]
# count = 0

# for i in arr:
#     if i % 2 == 0:
#         count += 1

# print(count)

# # largest element in array
# largest = arr[0]
# for i in arr:
#     if i > largest:
#         largest = i

# print(largest)

# # searching an element in array
# # linear search

# arr = [10,20,30,40,50]

# for index, value in enumerate(arr):
#     if value == 40:
#         print(value,"found at index",index)
#         break

# # binary search

# arr = [10,20,30,40,50]
# target = 30
# def binary_search(array,target_value):
#     left = 0
#     right = len(array)-1
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target_value:
#             return mid
#         elif target_value > array[mid]:
#             left = mid + 1
#         elif target_value < array[mid]:
#             right = mid - 1
#     else:
#         return -1

# status = binary_search(arr,target)
# if  status == -1:
#     print('element not found')
# else:
#     print(target,'found at index',binary_search(arr,target))

# # sorting 
# # bubble sort

# arr = [50,20,10,40,30,60,35,23,75,11]
# for j in range(len(arr)-1):
#     swapped = False
#     for i in range(len(arr)-j-1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#             swapped = True
#     if swapped == False:
#         break
# print(arr)

# # selection sort

# arr = [50,20,10,40,30,60,35,23,75,11]
# for j in range(len(arr)-1):
#     minimum = j
#     for i in range(j,len(arr)):
#         if arr[minimum] > arr[i]:
#             minimum = i
#     if minimum != j:
#         arr[j], arr[minimum] = arr[minimum], arr[j]
# print(arr)

# # insertion sort

# arr = [50,20,40,30,10]

# for i in range(1,len(arr)):
#     insert_index = i
#     current_value = arr[i]

#     for j in range(i-1,-1,-1):
#         if arr[j] > current_value:
#             arr[j+1] = arr[j]
#             insert_index = j
#         else:
#             break
#     arr[insert_index] = current_value

# print(arr)

# # recursion

# def show(n):
#     if n == 0: # base case
#         return
#     print('show method calling')
#     show(n-1)  # recursive relation
# show(3)

# # print 1 to n
# def show(n):
#     if n == 0: # base case
#         return 0   
#     show(n-1)  # recursive relation
#     print(n)   # print backword
# show(5)

# # print n to 1
# def show(n):   # base case
#     if n == 0: # recursive relation
#         return 0   
#     print(n)   # print forward
#     show(n-1)
# show(5)

# # sum of n to 1
# def add(n):
#     if n == 0: 
#         return 0
    
#     return n + add(n-1)  
# print(add(5))

# # factorial
# def fact(n):
#     if n == 0: 
#         return 1   
#     return n * (n-1)
    
# print(fact(5))

# # fibonacci
# def fib(n):
#     if n <= 0: 
#         return []
#     if n == 1:
#         return [0]
#     series = [0, 1]
#     for _ in range(2, n):
#         next_term = series[-1] + series[-2]
#         series.append(next_term)       
#     return series

# print(fib(5))

# # power a^b using recursion

# def power(a,b):
#     if b == 0:
#         return 1
#     if b == 1:
#         return a

# # quick sort

# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1

#     for j in range(low, high):
#         if array[j] <= pivot:
#             i += 1
#             array[i], array[j] = array[j], array[i]

#     array[i+1], array[high] = array[high], array[i+1]
#     return i+1

# def quicksort(array, low=0, high=None):
#     if high is None:
#         high = len(array) - 1

#     if low < high:
#         pivot_index = partition(array, low, high)
#         quicksort(array, low, pivot_index-1)
#         quicksort(array, pivot_index+1, high)

# arr = [64, 43, 67, 34, 25, 83, 12, 22, 11, 90, 5]
# quicksort(arr)
# print("Sorted array:", arr)

# # merge sort

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]

#     sortedLeft = merge_sort(left_half)
#     sortedRight = merge_sort(right_half)

#     return merge(sortedLeft, sortedRight)

# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# unsorted_arr = [33, 74, 6, 10, 15, 23, 55, 13, 64]
# sorted_arr = merge_sort(unsorted_arr)
# print("Sorted array:", sorted_arr)

# # counting sort


# def counting_sort(array):
#     if not array:
#         return array
        
#     max_val = max(array)
#     count = [0] * (max_val + 1)

#     for num in array:
#         count[num] += 1
        
#     array[:] = []

#     for num, freq in enumerate(count):
#         array.extend([num] * freq)

#     return array

# unsorted_arr = [4, 7, 3, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
# sorted_arr = counting_sort(unsorted_arr)
# print("Sorted array:", sorted_arr)

# class linked_list:
#     data = None
#     address = None

# def fact(n):
#     factorial = 1
#     for i in range(2,n+1):
#         factorial = factorial * i
#     print(factorial)
# fact(5)

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
# print(fact(6))

# def fact(n):
#     if n == 0:
#         return 1
#     print(n)
#     return n * fact(n-1)
# print(fact(6))

# def fib(n):
#     num1, num2 = 0, 1
#     print(num1)
#     print(num2)
#     for i in range(n-2):
#         num3 = num1 + num2
#         num1 = num2
#         num2 = num3
#         print(num3)
# fib(6)

# def fib(n):
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     series = [0,1]
#     for i in range(2,n):
#         new_value = series[-1] + series[-2]
#         series.append(new_value)
#     return series
# print(fib(8))

# # insertion sort without recursion

# array = [3,2,4,6,8,5,7,1]

# for i in range(1,len(array)):
#     insert_index = i
#     insert_value = array.pop(i)
#     for j in range(i-1,-1,-1):
#         if array[j] > insert_value:
#             insert_index = j
#     array.insert(insert_index,insert_value)

# print(array)

# array = [10,20,30,60,50,40]
# for i in range(len(array)):
#     for j in range(len(array)-i-1):
#         if array[j] >= array[j+1]:
#             array[j], array[j+1] = array[j+1], array[j]
# print(array)

# # simple stack using linked list

# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next : None

# class linkedliststack:
#     def __init__(self):
#         self.top = None

#     def push(self, item):
#         new_node = node(item)
#         new_node.next = self.top
#         self.top = new_node
#         print(item,'inserted into the stack')

# lls = linkedliststack()
# lls.push(10)

# # simple tree implimentation using linked list
# class node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class tree:
#     def push(data):
#         new_node = node(data)

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data, end=" ")
#         inorder(root.right)

# root = node(10)
# node_b = node(20)
# node_c = node(30)
# node_d = node(40)
# node_e = node(50)

# root.left = node_b 
# root.right = node_c

# node_b.left = node_d
# node_b.right = node_e  

# inorder(root)

# # a simple linked list

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# node1 = Node(10)
# node2 = Node(30)
# node3 = Node(20)
# node4 = Node(40)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# # using loop

# nodes = [node1,node2,node3,node4]
# for i in nodes:
#     print(i.data)
#     if i.next == None:
#         break

# # using recursion method1

# def travarsal(node):
#     print(node.data)
#     if node.next != None:
#         travarsal(node.next)

# # using recursion method2

# def travarsal(node):
#     print(node.data)
#     if node.next == None:
#         return
#     travarsal(node.next)

# travarsal(node1)

# # created array and perform travrsal

# my_array = []

# my_array.append(110)
# my_array.append(190)
# my_array.append(120)

# for i in range(len(my_array)):
#     print(my_array[i])

# # created linked list and perform travrsal

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# node1 = Node(200)
# node2 = Node(300)
# node1.next = node2
# node3 = Node(400)
# node2.next = node3

# def traverse(node):
#     print(node.data)
#     if node.next == None:
#         return
#     traverse(node.next)
# print('travrse')
# traverse(node1)

# # traversal using loop
# print("traversal using loop")
# node = node1
# while node.data != None:
#     print(node.data)
#     if node.next == None:
#         break
#     node = node.next

# # stack using array (python list)

# my_stack = []
# user_input = None

# def insert(data):
#     my_stack.append(data)

# def delete():
#     my_stack.pop()

# def show_top_of_stack():
#     return my_stack[-1]

# def ask():
#     global user_input
#     user_input = int(input("""
# -: what do you want to do with stack :-
#       press 1 to insert the data
#       press 2 to delete the data
#       press 3 to view the data
#       press 0 to exit
# """))

# ask()
# while user_input:
#     if user_input == 1:
#         if len(my_stack) == 5:
#             print("stack is full")
#         else:
#             data = input("""enter the data
# """)    
#             insert(data)
#             print("data inserted")

#     elif user_input == 2:
#         if len(my_stack) == 0:
#             print("stack is empty")
#         else:
#             delete()
#             print("data deleted")

#     elif user_input == 3:
#         print(show_top_of_stack())

#     elif user_input not in [1,2,3]:
#         print("enter correct input")

#     ask()
# print("thank you!")

# # stack using linked list

# user_input = None
# top = None
# size = 0

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# def insert(data):
#     global top, size
#     new_node = Node(data)
#     new_node.next = top
#     top = new_node
#     size += 1

# def delete():
#     global top, size
#     top = top.next
#     size -= 1

# def show_top_of_stack(top):
#     if top.next == None:
#         print(top.data)
#         return
#     show_top_of_stack(top.next)


# def ask():
#     global user_input
#     user_input = int(input("""
# -: what do you want to do with stack :-
#       press 1 to insert the data
#       press 2 to delete the data
#       press 3 to view the data
#       press 0 to exit
# """))

# ask()
# while user_input:
#     if user_input == 1:
#         if size == 5:
#             print("stack is full")
#         else:
#             data = input("""enter the data
# """)    
#             insert(data)
#             print("data inserted")
#             size += 1

#     elif user_input == 2:
#         if size == 0:
#             print("stack is empty")
#         else:
#             delete()
#             print("data deleted")
#             size -= 1

#     elif user_input == 3:
#         if size != 0:
#             print("stack data")
#             show_top_of_stack(top)
#         else:
#             print("stack is empty")

#     elif user_input not in [1,2,3]:
#         print("enter correct input")

#     ask()
# print("thank you!")

# # queue using array (python list)

# my_queue = []
# user_input = None

# def insert(data):
#     my_queue.append(data)

# def delete():
#     my_queue.pop(0)

# def show_front_of_queue():
#     return my_queue[0]

# def ask():
#     global user_input
#     user_input = int(input("""
# -: what do you want to do with queue :-
#       press 1 to insert the data
#       press 2 to delete the data
#       press 3 to view the data
#       press 0 to exit
# """))

# ask()
# while user_input:
#     if user_input == 1:
#         if len(my_queue) == 5:
#             print("queue is full")
#         else:
#             data = input("""enter the data
# """)    
#             insert(data)
#             print("data inserted")

#     elif user_input == 2:
#         if len(my_queue) == 0:
#             print("queue is empty")
#         else:
#             delete()
#             print("data deleted")

#     elif user_input == 3:
#         print(show_front_of_queue())

#     elif user_input not in [1,2,3]:
#         print("enter correct input")

#     ask()
# print("thank you!")

# # queue using linked list

# user_input = None
# front = None 
# size = 0

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def insert(data):
#     global front, size
#     new_node = Node(data)
#     if front == None:
#         front = new_node
#     else:
#         front.next = new_node
#     size += 1

# def delete():
#     global front, size
#     if front == None:
#         print("queue is empty")
#     else:
#         front = front.next
#         size -= 1

# def show_front_of_queue(front):
#     if front == None:
#         print("queue is empty")
#         return
#     if front.next == None:
#         print(front.data)
#         return
#     show_front_of_queue(front.next)

# def ask():
#     global user_input
#     user_input = int(input("""
# -: what do you want to do with queue :-
#       press 1 to insert the data
#       press 2 to delete the data
#       press 3 to view the data
#       press 0 to exit
# """))

# ask()
# while user_input:
#     if user_input == 1:
#         if size == 5:
#             print("queue is full")
#         else:
#             data = input("""enter the data
# """)    
#             insert(data)
#             print("data inserted")

#     elif user_input == 2:
#         if size == 0:
#             print("queue is empty")
#         else:
#             delete()
#             print("data deleted")

#     elif user_input == 3:
#         show_front_of_queue(front)

#     elif user_input not in [1,2,3]:
#         print("enter correct input")

#     ask()
# print("thank you!")

# # tree using array (python list), complete binary tree (heap tree), formulae 2n+1, 2n+2

# my_tree = []

# def insert_data(tree, value):
#     tree.append(value)
#     element_index = len(tree)-1
#     parent_index = find_parent_index(element_index)
#     while parent_index != -1:
#         if tree[parent_index] < tree[element_index]:
#             tree[parent_index], tree[element_index] = tree[element_index], tree[parent_index]
#             element_index = parent_index
#             parent_index = find_parent_index(element_index)
#         else:
#             break

# def find_parent_index(index_of_data):
#     if index_of_data == 0:
#         return -1
#     elif index_of_data % 2 == 0:
#         return ((index_of_data - 2) // 2)
#     else:
#         return ((index_of_data - 1) // 2)

# def delete(tree):
#     tree[0], tree[-1] = tree[-1], tree[0]
#     tree.pop()
#     parent_index = 0
#     left_child_index, right_child_index = find_child_index(tree, parent_index)
#     while tree[left_child_index] > tree[parent_index] or tree[right_child_index] > tree[parent_index]:
#         if right_child_index == None:
#             tree[left_child_index], tree[parent_index] = tree[parent_index], tree[left_child_index]
#             break

#         elif tree[left_child_index] > tree[right_child_index]:
#             tree[left_child_index], tree[parent_index] = tree[parent_index], tree[left_child_index]
#             parent_index = left_child_index
#             left_child_index, right_child_index = find_child_index(tree,parent_index)
#             if len(tree)-1 < left_child_index:
#                 break
#         else:
#             tree[right_child_index], tree[parent_index] = tree[parent_index], tree[right_child_index]
#             parent_index = right_child_index
#             left_child_index, right_child_index = find_child_index(tree,parent_index)
#             if len(tree)-1 < left_child_index:
#                 break

# def find_child_index(tree, index_of_parent):
#     left = index_of_parent*2+1
#     right = index_of_parent*2+2
#     if right <= len(tree)-1:
#         return left, right
#     else:
#         return left , None

# def show_heap_tree(tree):
#     if len(tree) == 0:
#         print("tree is empty")
#         return
#     print("tree data")

#     n = 0
#     minimum = 0
#     maximum = 2*minimum+1
#     for i in range(len(tree)):
#         if minimum < len(tree) <= maximum :
#             n += 1
#             break
#         n += 1
#         minimum = maximum
#         maximum = 2*minimum+1
#     start_index = 0
#     m = 1
#     for i in range(n):
#         for j in range(start_index,m):
#             print(tree[j], end=" ")
#             if tree[j] == tree[-1]:
#                 break
#             start_index += 1
#         m = 2*m+1
#         print()        

# def ask():
#     user_input = int(input("""
# -: what do you want to do with heap tree :-
#       press 1 to insert the data
#       press 2 to delete the data
#       press 3 to view the data
#       press 0 to exit
# """))
#     return user_input

# user_input = ask()
# while user_input:
#     if user_input == 1:
#         data = int(input("""enter the data
# """))
#         insert_data(my_tree, data)
#         print("data inserted")

#     elif user_input == 2:
#         if len(my_tree) == 0:
#             print("tree is empty")
#         else:
#             delete(my_tree)
#             print("data deleted")

#     elif user_input == 3:
#         show_heap_tree(my_tree)

#     elif user_input not in [1,2,3]:
#         print("enter correct input")

#     user_input = ask()
# print("thank you!")

# # simple binary tree using linked list data feeding using hard code

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)
# node6 = Node(60)

# root = node1
# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5
# node3.left = node6

# # pre-order traversal
# print("pre-order traversal")
# def traverse(node):
#     if node == None:
#             return
#     print(node.data)
#     if node.left != None:
#         traverse(node.left)
#     if node.right != None:
#         traverse(node.right)
# traverse(root)

# # in-order traversal
# print("in-order traversal")
# def traverse(node):
#     if node == None:
#         return
#     if node.left != None:
#         traverse(node.left)
#     print(node.data)
#     if node.right != None:
#         traverse(node.right)
# traverse(root)

# # post-order traversal
# print("post-order traversal")
# def traverse(node):
#     if node == None:
#         return
#     if node.left != None:
#         traverse(node.left)
#     if node.right != None:
#         traverse(node.right)
#     print(node.data)
# traverse(root)

# def traverse(node):
#     if node == None:
#         return
#     print(node.data)
#     if node.left != None:
#         traverse(node.left)
#     if node.right != None:
#         traverse(node.right)
# traverse(root)

# simple binary search tree using linked list data feeding using soft code

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = None

def insert_data(current_node, new_node):
    if current_node == None:
        current_node = new_node
    elif current_node.data == new_node.data:
        return 
    elif current_node.data > data and current_node.left == None:
        current_node.left = new_node
    elif current_node.data > data and current_node.left != None:
        insert_data(current_node.left, new_node)
    elif current_node.data < data and current_node.right == None:
        current_node.right = new_node
    elif current_node.data < data and current_node.right != None:
        insert_data(current_node.right, new_node)
    return current_node
    
def find_leaf_nodes(node):
    if node.left == None and node.right == None:
        return [node.data]
    l1 = find_leaf_nodes(node.left)
    r1 = find_leaf_nodes(node.right)
    return l1 + r1
         
    
def find_parent_node(node, leaf_node_data):
    if node.data == leaf_node_data:
        return
    # if node.left != None and node.left.data == leaf_node_data:
    #     return node
    # elif node.right != None and node.right.data == leaf_node_data:
    #     return node
    # elif node.left != None and node.left.data != leaf_node_data:
    #     return find_parent_node(node.left, leaf_node_data)
    # elif node.right != None and node.right.data != leaf_node_data:
    #     return find_parent_node(node.right, leaf_node_data)

def delete(node, leaf_node):
    if node.left == None and node.right == None:
        node = None
    elif node.left != None and node.left.data == leaf_node:
        node.left = None
    elif node.right != None and node.right.data == leaf_node:
        node.right = None
    elif node.left != None and node.left.data != leaf_node:
        node = delete(node.left, leaf_node)
    elif node.right != None and node.right.data != leaf_node:
        node = delete(node.right, leaf_node)
        
    return node

def show_tree1(node):
    # pre-order traversal
    print(node.data)
    if node.left != None:
        show_tree1(node.left)
    if node.right != None:
        show_tree1(node.right)

def show_tree2(node):
    # in-order traversal
    if node.left != None:
        show_tree2(node.left)
    print(node.data)
    if node.right != None:
        show_tree2(node.right)

def show_tree3(node):
    # post-order traversal
    if node.left != None:
        show_tree3(node.left)
    if node.right != None:
        show_tree3(node.right)
    print(node.data)
    
def ask():
    user_input = int(input("""
-: what do you want to do with binary tree :-
      press 1 to insert the data
      press 2 to delete the data
      press 3 to view the data
      press 0 to exit
"""))
    return user_input

leaf_nodes = []
user_input = ask()
while user_input:
    if user_input == 1:
        data = int(input("""enter the data
"""))     
        new_node = Node(data)
        value = insert_data(root, new_node)
        if value == None:
            print("data already inserted")
        else:
            root = value
            print("data inserted")

    elif user_input == 2:
        if root == None:
            print("tree is empty")
        else:
            print("you can delete only leaf nodes and you have these leaf nodes")
            leaf_nodes = find_leaf_nodes(root)
            print(leaf_nodes)
            leaf_node_data = input("""which leaf node you want to delete (give value)
""")
            parent_node = find_parent_node(root, leaf_node_data)
            value = delete(root, leaf_node_data)
            root = value
            print("data deleted")

    elif user_input == 3:
        if root == None:
            print("tree is empty")
        else:
            value = int(input("""which traversal you want
press 1 for pre-order
press 2 fro in-order
press 3 for post-order
"""))
            if value == 1:
                show_tree1(root)
            elif value == 2:
                show_tree2(root)
            elif value == 3:
                show_tree3(root)
            else:
                print("select only from available option")
                print("by default pre-order")
                show_tree1()

    elif user_input not in [1,2,3]:
        print("enter correct input")

    user_input = ask()
print("thank you!")