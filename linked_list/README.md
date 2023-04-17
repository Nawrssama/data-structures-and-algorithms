# Linked List

> - Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

> - adding a node to the end of the linked list

> - arguments: value, new value
    adds a new node with the given new value immediately before the first node that has the value specified

> - arguments: value, new value
    adds a new node with the given new value immediately after the first node that has the value specified


## Approach & Efficiency

## big(o) for insert
> - Time --> O(1) because there no looping over the list
> - space -->O(1) because there is no use of an extra space

## big(o) for append
> - Time --> O(n) 
> - space -->O(1) 

## big(o) for insert-befor
> - Time --> O(n) 
> - space -->O(1) 

## big(o) for insert-after
> - Time --> O(n) 
> - space -->O(1) 


linked-list-insertions
# Whiteboard Process links
## insert
![add to the first ](./screenshots/insert.png)
## append
![add to the end ](./screenshots/append.png)
## insert-befor
![add befor ](./screenshots/insert-before.png)
## insert-after
![adding after ](./screenshots/insert-after.png)



## Solution
///   -->

  class LinkedList:

    def __init__(self):
        """
        Initialize a LinkedList instance.
        """
        self.head = None

    def insert(self,value):
        """
        Insert a node with the given value at the beginning of the linked list.

        Parameters:
        - value: Any data type
          The value to be stored in the new node.
        """
      
        node =Node(value)
        if self.head == None:
            self.head = node 
        else:
            node.next = self.head
            self.head = node        

    
    def includes (self,key):
        """
        Check whether the linked list contains a node with the given value.

        Parameters:
        - key: Any data type
          The value to search for.

        Returns:
        - bool
          True if the value is found in any node of the linked list, False otherwise.
        """
       
        temp = self.head
        if temp is None:
              return False
        while temp is not None:
              if temp.value == key:
                   return True
              temp = temp.next
        return False

    def append(self,value):

        """
        Insert a node with the given value at the end of the linked list.

        Parameters:
        - value: Any data type
          The value to be stored in the new node.
        """
       
        node = Node(value)
        
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def insert_after(self,target,value):
         
         """
        Insert a node with the given value after the first node with the given target value.

        Parameters:
        - target: Any data type
          The value of the node after which the new node should be inserted.
        - value: Any data type
          The value to be stored in the new node.
        """
       
         if self.includes(target):
            node = Node(value)
            if self.head == None :
              self.insert(value)

            else:
              currnet = self.head
              while currnet.value is not target:
                   currnet = currnet.next
              target = currnet 
              node.next = target.next
              target.next = node
         else:
             print("this target value does not exists")

    def insert_before(self,target,value):

         """
        Insert a node with the given value before the first node with the given target value.

        Parameters:
        - target: Any data type
          The value of the node before which the new node should be inserted.
        - value: Any data type
          The value to be stored in the new node.
        """
        
         if self.includes(target):
            node = Node(value)
            if self.head == None or self.head.value == target:
              self.insert(value)

            else:
              currnet = self.head
              while currnet.next.value is not target:
                   currnet = currnet.next
              target = currnet 
              node.next = target.next
              target.next = node
         else:
             print("this target value does not exists")               
     
         
    def __str__(self):
        """
        Generate a string representation of the linked list.

        Returns:
        - str
          A string representation of the linked list.
        """
        output = ""
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} -> '
                current = current.next
            
            output += " None"
        return output  
                          
              -->


# Pull Request link :  

