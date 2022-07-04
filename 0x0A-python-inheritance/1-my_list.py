#!/usr/bin/python3
class MyList(list):
    """A derived class MyList of base clase list"""

    def print_sorted(self):
        """
            Prints list in ascending order.
                Returns:
                    list (int): List in ascending order
        """

        return self.sort()
