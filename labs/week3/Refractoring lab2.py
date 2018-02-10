"""
lab3.py
Refractoring lab2.py
Pritha Dutta
02/06/2018
"""

def squared(num_list):
    """
    square numbers in num_list
    num_list:list of numbers
    Returns:list of these numbers squared
    """
    new_list=[]
    for num in num_list:
        new_list.append(pow(num,2))
    return new_list
    
Test Cases: [1, 2, 3], [], [-1, -2, -3], [1, 0]

Expected Results: [1, 4, 9], [], [1, 4, 9], [1, 0]

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
		if strs.istitle() and strs.isalpha: #checks if if string in the list is title case
			newstrlist.append(strs)
    return newstrlist
    
Test Cases: ['Hello World', 'Hello_world', 'Title'], ['Hello_World', 'A great 3 Days', 'hello World'], [‘10, 11, 12’]

Expected Results: ['Hello World', 'Hello_world', 'Title'], [], []

def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: a dictionary with:
    key: string that is the name of the inventory item
    value: integer that equals the number of that item currently on hand
    Returns: updated dictionary where each inventory item is restocked
    """
    new_inventory={}
    for key,val in inventory.items():
        new_inventory[key] = val+10
    return new_inventory
    
    
Test Cases: {'pencil':10, 'pen':8, 'paper':7}, {'pencil':0, 'pen':-3, 'paper':-11}, {'pencil':0.5, 'pen':-3.2, 'paper':11.0}

Expected Results: {'pencil':20, 'pen':18, 'paper':17}, {'pencil':10, 'pen':7, 'paper':-1}, {'pencil':10.5, 'pen':6.8, 'paper':21.0}

Actual Results: {'pen':18, 'paper':17, 'pencil':20}, {'pen':7, 'paper':-1, 'pencil':10}, {'pen':6.8, 'paper':21.0, 'pencil':10.5}

def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: dictionary with:
    key: string that is the name of the inventory item
    value: integer that equals the number of that item currently on hand
    Returns: the same inventory_dict with any item that had 0 quantity removed
    """
    new_inventory = {}
    for k,v in inventory.items():
		if v! == 0:
		  new_inventory[k]=v
    return inventory
    
    
Test Cases: {'pencil':10, 'pen':8, 'paper':7}, {'pencil':0, 'pen':-3, 'paper':-11}, {'pencil':0.5, 'pen':-3.2, 'paper':0.0}

Expected Results: {'pen':8, 'paper':7, 'pencil':10}, {'pen':-3, 'paper':-11}, {'pen':-3.2, 'pencil':0.5}

def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: a dictionary of grades with:
    key: string of students name
    value: list of integer grades received in class
    Returns: dictionary that averages out the grades of each student
    """
    new_grades = {}
    #gets each dictionary and finds it's average
    for stu_name, stu_grades in grades.items():
        new_grades[stu_name] = sum(stu_grades)/ (len(stu_grades))
    return new_grades
    
    
Test Cases: {'Michael' :[100, 78, 88, 900/10], 'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]}, {'Michael' :[5*20, 188 * .5, 88], 'Daniel':[80.5, .15, 66, 64.0] 'Josh':[99 + 1 * -2, 40/.5]}, {'Michael' :[78], 'Daniel':[90], 'Josh':[900/-9]}

Expected Results: {'Josh' : 87.0, 'Daniel': 79.0, 'Michael': 89.0}, {'Josh' : 88.5, 'Daniel': 52.6625, 'Michael': 94.0}, {'Josh' : -100.0, 'Daniel': 90.0, 'Michael': 78.0}
