from linked_list import LinkedList

if __name__ == '__main__':
      linked_list = LinkedList()

      linked_list.insert('A')
      linked_list.insert('B')
      linked_list.insert('C')
      linked_list.append('D')
      linked_list.insert_after('E','F')
      linked_list.insert_before('X','Z')
      

      print(linked_list)

      print(linked_list.includes('Y'))