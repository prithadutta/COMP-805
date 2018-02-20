"""
lab2.py
Refractoring lab2.py
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
    for num in num_list:
        new_list.append(pow(num,2))
    return new_list



def check_title(title_list):
    """
    removes strings in title_list that have numbers ad aren't title case
    title_list:list of strings
    Returns:list of strings that are titles
    """
    newstrlist = []
    for strs in title_list:
 	      if strs.istitle() and strs.isalpha():#checks if if string in the list is title case
                newstrlist.append(strs)
    return newstrlist

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
		if v!= 0:
		  new_inventory[k]=v
    return inventory


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
