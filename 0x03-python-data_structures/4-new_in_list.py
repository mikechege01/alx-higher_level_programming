#!/usr/bin/python3
# Task 4

def new_in_list(my_list, idx, element):
    """replaces an element in a list at a given index"""
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
