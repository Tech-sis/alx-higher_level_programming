#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in my_list:
        if idx < 0:
            return None
        length = len(my_list)
        
        if idx > length - 1:
            return None
    return(my_list[idx])
