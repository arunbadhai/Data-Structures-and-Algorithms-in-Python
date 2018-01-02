# -*- coding: utf-8 -*-
# @Author: manjusv
# @Date:   2018-01-02 19:18:42
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-02 19:55:24
class ListNode:
	def __init__(self, data):
		self.val = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	# Function to reverse the linkedlist
	def reverseList(self):
		cur = self.head
		prev = None
		while(cur):
			fut = cur.next
			cur.next = prev
			prev = cur
			cur = fut
		self.head = prev

	# insert a new element at the beginning of a list
	def push(self, new_data):
		new_node = ListNode(new_data)
		new_node.next = self.head
		self.head = new_node

	# prints the contents of a list
	def printList(self):
		temp = self.head
		while(temp):
			print temp.val,
			temp = temp.next

llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print "LinkedList before Reversing : ", llist.printList()
llist.reverseList()
print "LinkedList after Reversing : ", llist.printList()
