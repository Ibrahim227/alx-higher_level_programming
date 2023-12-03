#!/usr/bin/python3
if __name__ == "__main__":
    def element_at(my_list, idx):
        if idx < 0:
            return None
        if idx > len(my_list):
            return None
        print("Element at {:d} is {}".format(idx, elemet_at(my_list, idx)))
