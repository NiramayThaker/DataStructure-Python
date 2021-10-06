class Node:
	def __init__(self, data=None, next=None) -> None:
		self.data = data
		self.next = next


class LinkedList:
	def __init__(self) -> None:
		self.head = None

	def insert_at_beginning(self, data):
		"""It Insert node at beginning, that is at first position"""

		node = Node(data, self.head)
		self.head = node

	def insert_at_end(self, data):
		"""It insert at last element"""

		if self.head is None:
			self.head = Node(data, None)
			return
		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data, None)

	def print_list(self):
		"""Print the element in linked list"""

		if self.head is None:
			print("List is empty: ")
			return
		itr = self.head
		# llstr = ''                                                                      # Another
		while itr:
			# llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)                 # Way
			print(str(itr.data) + ' --> ', end='')
			itr = itr.next
		print()

	# print(llstr)                                                                      # To do it

	def find_length(self):
		"""Will return length of linked list"""

		itr = self.head
		count = 0
		while itr:
			count += 1
			itr = itr.next
		return count

	def insert_using_index(self, index, data):
		"""It insert by finding index"""

		if index < 0 or index > self.find_length():
			raise Exception("Invalid Index")
		if index == 0:
			self.insert_at_end(data)
			return

		itr = self.head
		count = 0
		while itr:
			if count == index - 1:
				itr.next = Node(data, itr.next)
				break
			itr = itr.next
			count += 1

	def insert_values(self, data_list):
		"""It takes input of list and insert one by one element in new linked list"""

		self.head = None
		for data in data_list:
			self.insert_at_end(data)

	def remove_at(self, index):
		"""It removes element by finding it through its index"""

		if 0 > index < self.findlength():
			raise Exception("invalid input")

		if index == 0:
			self.head = self.head.next
			return

		itr = self.head
		count = 0
		while itr:
			if count == index - 1:
				itr.next = itr.next.next
				break
			itr = itr.next
			count += 1

	def remove_with_data(self, data):
		"""Will take a string and remove it from the list"""

		itr = self.head
		temp_list = []
		while itr:
			temp_list.append(str(itr.data))
			itr = itr.next
		for i in temp_list:
			if data in i:
				temp_list.remove(i)
		self.insert_values(temp_list)


if __name__ == '__main__':
	ll = LinkedList()
	# Insert at beginning function use
	ll.insert_at_beginning(100)
	ll.insert_at_beginning(34)
	ll.insert_at_beginning(50)
	ll.print_list()

	# Insert at end function use (HERE 23 and 78 is inserted after last node 100)
	ll.insert_at_end(23)
	ll.insert_at_end(78)
	ll.print_list()

	# Using insert value function which will create a whole new linked list from provided list
	cars = ["Audi", "BMW", "Jaguar", "Ferrari"]
	ll.insert_values(cars)
	ll.print_list()

	# Toyota will be inserted at second position (AFTER BMW and BEFORE JAGUAR)
	ll.insert_using_index(2, "Toyota")
	ll.print_list()

	# Will remove element as per index
	ll.remove_at(0)
	ll.print_list()

	# Will remove the entered string from list
	ll.remove_with_data("BMW")
	ll.print_list()
