#reference: https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python

class Node():
    def __init__(self, data=None, next_node=None):
        self.data=data
        self.next_node=next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node
    '''
    def set_next(self, new_next):
        self.next_node=new_next
    '''

#Implementation of a linked list

class LinkedList():
    def __init__(self, x=None):
        self.head=Node(x)

    #Inserts next to head
    def insert(self, data):
        temp=Node(data, self.head.next_node)
        self.head.next_node=temp

    #Inserts to last
    def insertToLast(self, data):
        temp=Node(data, None)
        temp2=self.head
        while temp2.next_node!=None:
            temp2=temp2.next_node
        temp2.next_node=temp
        
    def size(self):
        count=0
        temp=self.head
        while temp:
            count=count+1
            temp=temp.next_node
        return count

    def printList(self):
        temp=self.head
        print "Contents of linked list"
        while temp:
            data=temp.get_data()
            print data
            temp=temp.get_next()

    def contains(self, value):
        temp=self.head
        while temp:
            if temp.data==value:
                return True
            temp=temp.next_node
        return False
    
    #head=1
    def delete(self, node_number):
        size=self.size()
        if node_number>size:
            return
        if node_number==1:
            temp=self.head
            self.head=self.head.next_node
            temp.next_node=None
        else:
            count=0
            temp=self.head
            while count<(node_number-2):
                temp=temp.next_node
                count=count+1
            temp.next_node=temp.next_node.next_node

    def deleteValue(self, value):
        temp=self.head
        #value at head
        while temp.data==value:
            self.head=self.head.next_node
            temp=self.head
        #value after head
        prev=temp
        cur=prev.next_node
        while cur:
            if cur.data==value:
                prev.next_node=cur.next_node
                if prev.next_node==None:
                    break
                cur.next_node=None
            prev=prev.next_node
            cur=prev.next_node
            
    def reverseList(self):
        prev=self.head
        cur=prev.next_node
        nex=cur.next_node
        while nex!=None:
            cur.next_node=prev
            prev=cur
            cur=nex
            nex=nex.next_node
        cur.next_node=prev
        self.head.next_node=None
        self.head= cur

    #Remove duplicates 
    def remDuplicate(self):
        unique=[]
        prev=self.head
        chk=prev.next_node
        unique.append(prev.data)
        while chk:
            data=chk.data
            if data in unique:
                prev.next_node=chk.next_node
                chk.next_node=None
                chk=prev.next_node
            else:
                unique.append(data)
                prev=chk
                chk=chk.next_node

    #FOLLOW UP
    #How would you solve this problem if a temporary buffer is not allowed?


    #Find the kth to last element
    def kthToLastElement(self, k):
        self.reverseList()
        temp=self.head
        count=0
        while count<k:
            temp=temp.next_node
            count=count+1
        data=temp.data
        self.reverseList()
        return data

    #Write code to partition a linked list around a value x, such that all nodes
    #less than x come before all nodes greater than or equal to x.      
    def Partition(self, pivot):
        #METHOD 1. TAKES TWICE AS MUCH SPACE
        if type(self.head.data)!=int:
            return
        small=LinkedList()
        big=LinkedList()
        temp=self.head
        while temp:
            if temp.data<=pivot:
                small.insert(temp.data)
                if temp.next_node==None:
                    break
                else:
                    temp=temp.next_node
            else:
                big.insert(temp.data)
                if temp.next_node==None:
                    break
                else:
                    temp=temp.next_node
        smalltemp=small.head
        while smalltemp.next_node!=None:
            smalltemp=smalltemp.next_node
        smalltemp.next_node=big.head.next_node
        small.delete(1)
        return small
        
    #Implement a function to check if a linked list is a palindrome.
    def isPalindrome(self):
        #to position the slow and fast pointer
        slow=self.head
        fast=self.head
        while fast:            
            if fast.next_node==None or fast.next_node.next_node==None:
                break
            else:
                fast=fast.next_node.next_node
            slow=slow.next_node
        if fast.next_node:
            fast=fast.next_node
        #to reverse the list post the slow pointer
        prev=slow.next_node
        cur=prev.next_node
        nex=cur.next_node
        while nex!=None:
            cur.next_node=prev
            prev=cur
            cur=nex
            if nex.next_node==None:
                break
            else:
                nex=nex.next_node
        cur.next_node=prev
        slow.next_node.next_node=None
        slow.next_node=fast
        #to check if its a palindrome
        slow=slow.next_node
        temp=self.head
        while slow:
            if temp.data!=slow.data:
                return False
            if slow.next_node==None:
                break
            else:
                slow=slow.next_node
            temp=temp.next_node
        return True
            

#Given a circular linked list, implement an algorithm which returns the node at
#the beginning of the loop.
def circular(LL):
    ids=[]
    temp=LL.head
    ids.append(id(temp))
    temp=temp.next_node
    while temp:
        if id(temp) in ids:
            return temp
        else:
            ids.append(id(temp))
            temp=temp.next_node
    return         

#You have two numbers represented by a linked list, where each node contains a
#single digit. The digits are stored in reverse order, such that the Ts digit is at the
#head of the list. Write a function that adds the two numbers and returns the sum
#as a linked list.
def addReverse(LL1, LL2):
    temp1=LL1.head
    num1=0
    unit1=1
    while temp1:
        data=temp1.data
        data=data*unit1
        num1=num1+data
        unit1=unit1*10
        temp1=temp1.next_node
    temp2=LL2.head
    num2=0
    unit2=1
    while temp2:
        data=temp2.data
        data=data*unit2
        num2=num2+data
        unit2=unit2*10
        temp2=temp2.next_node
    result=str(num1+num2)
    output=LinkedList()
    for i in result:
        output.insert(int(i))
    output.head=output.head.next_node
    return output

#FOLLOW-UP. Suppose the digits are stored in forward order. Repeat the above problem.
def addForward(LL1, LL2):
    temp1=LL1.head
    str1=''
    while temp1:
        data=temp1.data
        str1=str1+str(data)
        temp1=temp1.next_node
    temp2=LL2.head
    str2=''
    while temp2:
        data=temp2.data
        str2=str2+str(data)
        temp2=temp2.next_node
    result=str(int(str1)+int(str2))
    result=result[::-1]
    output=LinkedList()
    for i in result:
        output.insert(int(i))
    output.head=output.head.next_node
    return output
