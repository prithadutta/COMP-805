"""
lab2.py
Pritha Dutta
01/30/2018
"""

def squared(num_list):
    """
    square numbers in num_list
    num_list:list of numbers
    Returns:list of these numbers squared
    """
    new_list=[]
    for num in num_list
       sq_num=pow(num,2):
       new_list.append(sq_num)
    return new_list

t1 = [1,2,3]
res = squared (t1)


def check_title(title_list):
"""
removes strings in title_list that have numbers ad aren't title case
title_list:list of strings
Returns:list of strings that are titles
"""
   newstrlist = [ ]
   for strs in title_list:
		if strs.istitle(): #checks if if string in the list is in title case or and and keeps only the ones with title case
			newstrlist.append(strs)
   return newstrlist

list1 = ['Hello World, 'Hello_world', 'Title'],['Hello_World', 'A great 3 Days', 'hello World'],['10,11,12']
res= ['Hello World', 'Hello-world', 'Title'],[],[]

def restock_inventory(inventory):
	"""
	Increases inventory of each item in dictionary by 10
	inventory: a dictionary with:
		key: string that is the name of the inventory item
		value: integer that equals the number of that item currently on hand
	Returns: updated dictionary where each inventory item is restocked
	"""
    for inventories in inventory:
		inventory[inventories] += 10
    return inventory
         
list1={'pencil':10,'pen':8, 'paper':7}, {'pencil':0, 'pen':3, 'paper':11},{'pencil':0.5,'pen':3.2,'paper':11.0},{'pencil':0.5,'pen':3.2,'paper':11.0}
 res={'pen':18,'paper':17,'pencil':20},{'pen':7,'paper':1,'pencil':10},{'pen':6.8,'paper':21.0,'pencil':10.5}     

def filter_0_items(inventory):
	"""
	Removes items that have a value of 0 from a dictionary of inventories
	inventory: dictionary with:
		key: string that is the name of the inventory item
		value: integer that equals the number of that item currently on hand
	Returns: the same inventory_dict with any item that had 0 quantity removed
	"""
	for inventories in inventory:
		if inventory[inventories] == 0:
			del inventory[inventories]
    return inventory
         

def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: a dictionary of grades with:
    key: string of students name
    value: list of integer grades received in class
    Returns: dictionary that averages out the grades of each student
    """
    dict = {}
    #gets each dictionary and finds it's average
    for i,j in grades.items():
        dict[i] = sum(j)/ float(len(j))
    return dict
