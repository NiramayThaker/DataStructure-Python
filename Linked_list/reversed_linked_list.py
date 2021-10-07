class Node:
	def __init__(self, data=None, next=None) -> None:
		self.data = data
		self.next = next


class LinkedList:
	def __init__(self) -> None:
		self.head = None

	def insert_at_beginning(self, data):
		"""Insert at first element"""

		node = Node(data, self.head)
		self.head = node

	def insert_at_end(self, data):
		"""Insert at last element"""

		if self.head is None:
			self.head = Node(data, None)
			return
		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data, None)

	def insert_values(self, data_list):
		"""It takes input of list and insert one by one element in new linked list"""

		self.head = None
		for data in data_list:
			self.insert_at_end(data)

	def print_list(self):
		"""Print the elements of list"""

		if self.head is None:
			print("List is empty: ")
			return
		itr = self.head
		while itr:
			print(str(itr.data) + ' --> ', end='')
			itr = itr.next
		print()

	def reverse_linked_list(self):
		"""Will reverse the linked list"""

		itr = self.head
		ll_list = []
		reversed_ll_list = []
		while itr:
			ll_list.append(str(itr.data))
			itr = itr.next
		for i in range(len(ll_list)-1, -1, -1):
			reversed_ll_list.append(ll_list[i])
		self.insert_values(reversed_ll_list)


if __name__ == "__main__":
	ll = LinkedList()

	ll.insert_at_beginning(10)
	ll.insert_at_end(20)
	ll.insert_at_beginning(30)
	ll.insert_at_beginning(40)
	ll.insert_at_beginning(50)
	ll.insert_at_beginning(60)
	ll.insert_at_beginning(70)
	ll.insert_at_end(80)
	ll.insert_at_end(90)

	ll.print_list()

	ll.reverse_linked_list()
	ll.print_list()
