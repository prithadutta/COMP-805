"""
lab3.py
Python practice
Pritha Dutta
02/06/2018
"""


def switch_case(str_list):
    """
    Maps strings in the str_list to a new string of
    same characters, but the first letter contains
    the opposite case
    string_list: list of strings
    Returns: list of original strings, but with
    opposite casing
    """
    newstr=list(map(lambda x:x[0].swapcase()+x[1:],str_list))
    return newstr




def only_even(mixed_list):
    """
    Filters out odd integers and strings that
    contain an odd number of characters.
    mixed_list: list of integers and/or strings
    Returns: list of only integers and strings that
    are even or have an even number of characters.
    """
    newstrlist=list(filter(lambda x: (x.isdigit() and int(x)%2==0) or ((x.isalpha() or x.isalnum()) and len(x)%2==0),mixed_list))
    return newstrlist




def greatest_difference(num_list):
    """
    Finds the maximum and minimum numbers in a_list
    and computes the difference.
    num_list: list of numbers
    Returns: the difference between the maximum and
    minimum numbers in num_list
    """
    d1=max(num_list)- min(num_list)
    return d1




def make_title(words):
    """
    Maps words in a list to words in the same list,
    but as titled strings.
    words: list of words
    Returns: new list of titled words
    """
    newstr=list(map(lambda x:x.title(),words))
    return newstr




def test_title(names):
    """
    Filters out capitalized and non- cap words into
    their respective lists.
    names: list of names
    Returns: both lists for review
    """
    newstr1=list(filter(lambda x:x.isupper(),names))
    newstr2=list(filter(lambda x:x.isupper()==False,names))
    return newstr1,newstr2



def create_word(char_list):
    """
    Takes a list of characters and creates a word
    (list with alpha chars only) from them.
    letters: list of etters
    Returns: list that has alpha characters only
    """
    newstr=[]
    for strs in char_list:
        if strs.isalpha():
               newstr.append(strs)
    return newstr


def three_times_nums(num_list):
    """
    Maps numbers in the num_list to numbers that are
    3 times the original value
    num_list: list of numbers
    Returns: list of numbers that are of three times
    the values in num_list
    """

    newlst=list(map(lambda x:x*3,num_list))
    return newlst



def keep_lowercase(str_list):
    """
    Filters out strings that have uppercase values
    str_list: list of strings
    Returns: list of strings that do not contain
    uppercase values
    """
    newstr=list(filter(lambda x:x.isupper()==False,str_list))
    return newstr




def multiplication_total_of(num_list):
    """
    Multiplies all the numbers in num_list together
    and gives the total
    num_list: list of numbers
    Returns: the multiplied total of the numbers in
    the num_list
    """
    newlst=[]
    prod=1
    for strs in num_list:
        prod=prod*strs
    newlst.append(prod)
    return newlst





def square_nums(number_list):
    """
    Maps numbers in the number_list to numbers of
    same value, but squares the number given
    number_list: list of numbers
    Returns: list from number_list which are squared

    >>> square_nums([1, 2, 3])
    [1, 4, 9]
    >>> square_nums([])
    []
    >>> square_nums([1, -2])
    [1, 4]
    """
    squared=list(map(lambda x:x**2,number_list))
    return squared




def lessthan_5(num_list):
    """
    Filters out numbers less than five
    num_list: list of numbers
    Returns: list of numbers in the original list
    that are less than five
    """
    newlist=list(filter(lambda x:x<5,num_list))
    return newlist



def subtraction_of(number_list):
    """
    Subtracts the numbers in number_list
    number_list: list of numbers
    Returns: the difference of the numbers in the
    number_list
    """
    numberlist=[x-number_list[i-1] for i,x in enumerate(number_list)][1:]
    return numberlist




def double_nums(num_list):
    """
    Maps numbers in the num_list to their doubles
    num_list: list of numbers
    Returns: list of doubled numbers
    """
    newlist=list(map(lambda x:x*2,num_list))
    return num_list



def remove_special_characters(string_list):
    """
    Filters out strings that have non-alphanumeric
    elements
    char_list: list of strings
    Returns: list of strings that have only letters
    or numbers in them
    """
    newlist=list(filter(lambda x:x.isalnum(),string_list))
    return newlist

if __name__=='__main__':
    import doctest
    doctest.testmod()
