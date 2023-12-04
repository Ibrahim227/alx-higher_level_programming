#!/usr/bin/python3
if __name__ == "__main__":
    def new_in_list(my_list, idx, element):
        if idx < 0:
            return my_list.copy()
        if idx >= len(my_list):
            return my_list.copy()
        my_list[idx] = element
        return my_list
