#!/usr/bin/python3
def element_at(my_list, idx):
    """fetches elments from my_list"""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
