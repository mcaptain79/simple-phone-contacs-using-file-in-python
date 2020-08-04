class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        self.previous = None
#making a linked list data structure in order to be able to save data and restore from file
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,key):
        node = Node(key)
        if self.head == None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.previous = node
        self.head = node
    def search(self,key):
        node = self.head
        while node != None:
            if node.key == key:
                return node
            node = node.next
        return None
    def delete(self,key):
        node = self.search(key)
        if self.head == None or node == None:
            return None
        if node.previous == None:
            self.head = self.head.next
            self.head.previous = None
            return node
        if node.next == None:
            self.tail = self.tail.previous
            self.tail.next = None
            return node
        node.next.previous = node.previous
        node.previous.next = node.next
        return node
    def print_list(self):
        x = self.head
        while x != None:
            print(x.key)
            x = x.next
#making a member class that has name,family and phone number
class Member:
    #initializing
    def __init__(self,name = '',family = '',phoneNumber = ''):
        self.name = name
        self.family = family
        self.phoneNumber = phoneNumber
    #overriding str method in order to be able to print object
    def __str__(self):
        return 'name: '+self.name+' family: '+self.family+' phone number: '+self.phoneNumber
    #overriding eq method in order to be able to compare object based on members
    def __eq__(self, otherObj):
        if self.name == otherObj.name and self.family == otherObj.family:
            return True
        return False
#phoneContanct class
class PhoneContact:
    #initializing our linkedList by reading from a file line by line
    def __init__(self):
        self.myLinkedList = LinkedList()
        f = open('contacts.txt','r')
        for i in f:
            self.myLinkedList.insert(Member(i.split()[0],i.split()[1],i.split()[2]))
    #printing our menue
    def printMenue(self):
        print('1)add\n2)edit\n3)delete\n4)show list\n5)exit') 
    #adding a member
    def add(self):
        myMember = Member(input('name: '),input('family: '),input('phone number: '))
        self.myLinkedList.insert(myMember)
    #editing a member by giving name and family
    def edit(self):
        memberToEdit = Member(input('name: '),input('fmaily: '))
        myMember = self.myLinkedList.search(memberToEdit)
        if myMember == None:
            print('no such a member')
        #note that you should enter information with space between
        else:
            name,family,phoneNumber = input('enter complete information in edited mode: ').split()
            myMember.key = Member(name,family,phoneNumber)
    def delete(self):
        name,family = input('enter name and family: ').split()
        myMember = Member(name,family)
        res = self.myLinkedList.delete(myMember)
        if res == None:
            print('no such a member')
        else:
            print('successfully deleted')
    def printContactList(self):
        self.myLinkedList.print_list()
    """
    in this method before you want to exit we rewrite file by list members
    note that in this project we work with linked list in order to be able
    to use our methods in proper way and be easier to manage file
    """
    def exitContacts(self):
        f = open('contacts.txt','w+')
        x = self.myLinkedList.head
        while x != None:
            f.write(x.key.name+' '+x.key.family+' '+x.key.phoneNumber)
            f.write('\n')
            x = x.next
        f.close()
    #engine of the program 
    #we just need to run this method
    def engine(self):
        while True:
            self.printMenue()
            myInput = input('enter the operation you want to do: ')
            if myInput == '1':
                self.add()
            elif myInput == '2':
                self.edit()
            elif myInput == '3':
                self.delete()
            elif myInput == '4':
                self.printContactList()
            elif myInput == '5':
                self.exitContacts()
                return
            else:
                print('invalid input')
pf = PhoneContact()
pf.engine()













