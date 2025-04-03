class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class CLL:
    def _init_(self):
        self.head=None
        self.temp=None
        self.tail=None
    def creation(self):
        num=int(input("Enter the no of nodes:"))
        for i in range(num):
            data=int(input("Enter the no of data for the nodes:"))
            newnode=Node(data)
            if self.head is None:
                self.head=newnode
                self.temp=newnode
                self.tail=newnode
            else:
                self.temp.next=newnode
                self.temp=newnode
                self.tail=newnode
                self.tail.next=self.head
    def display(self):
        self.temp=self.head
        while self.temp.next is not self.head:
            print(self.temp.data, end ="->")
            self.temp=self.temp.next
        print(self.temp.data)

    def InsertionAtbeg(self):
        print("Insertion At Begin of the list:")
        data=int(input("Enter the node data:"))
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
        self.tail.next=self.head
    def InsertionAtend(self):
        print("Insertion At end of the list:")
        data=int(input("enter the data value:"))
        newnode=Node(data)
        self.temp=self.head
        while self.temp is not self.tail:
            self.temp=self.temp.next
        newnode.next=self.head
        self.tail.next=newnode
        self.tail=newnode
    def InsertionAtMiddle(self):
        print("Insertion At Middle of the list:")
        data=int(input("Enter the data value:"))
        newnode=Node(data)
        position=int(input("Enter the position value:"))
        self.temp=self.head
        for i in range(position-1):            
            prev=self.temp
            self.temp = self.temp.next
        newnode.next=self.temp
        prev.next= newnode
    def DeletionAtbegin(self):
        print("Deletion At begin of the list:")
        self.temp=self.head
        self.head=self.head.next
        del(self.temp)
        self.tail.next=self.head
    def DeletionAtend(self):
        print("Deletion At end of the list:")
        self.temp=self.head
        while self.temp is not self.tail:
            prev=self.temp
            self.temp=self.temp.next
        prev.next=self.head
        prev=self.tail
    def DeletionAtMiddle(self):
        print("Deletion At Middle of the list:")
        position=int(input("Enter the position value to remove:"))
        self.temp=self.head
        for i in range(position-1):
            prev=self.temp
            self.temp=self.temp.next
        prev.next=self.temp.next

        



        
    
    

a=CLL() 
a.creation()
a.display()
a.InsertionAtbeg()
a.display()
a.InsertionAtend()
a.display()
a.InsertionAtMiddle()
a.display()
a.DeletionAtbegin()
a.display()
a.DeletionAtend()
a.display()
a.DeletionAtMiddle()
a.display()