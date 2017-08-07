class AlternateList(list):
    """ A list that has alternate values the same """

    def is_alternate_list(self):
        """
        (AlternateList) -> bool
        
        Returns true if the list has alternating values

        Precondition: list length has to be greater than or equal to two

        >>> a = AlternateList([1,2,1])
        >>> a.is_alternate_list()
        True
        >>> a = AlternateList([1,2,3])
        >>> a.is_alternate_list()
        False
        >>> a = AlternateList([1,1,1])
        >>> a.is_alternate_list()
        False
        """

        if len(self) < 2:
            return False

        a = set(self[0:len(self):2])
        b = set(self[1:len(self):2])

        return len(a) == 1 and len(b) == 1 and a != b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
