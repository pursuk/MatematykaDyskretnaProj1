def substract(x1,x2):
    """

    :param a: zbiór początkowy
    :param b: zbiór odejmowany
    :return: różnica zbiorów A-B
    """
    result = x1.copy()
    for x in x1:
        if x in x2:
            result.remove(x)
    return result



def gen_podzbiorow(base_set,A=[]):
    subsets = []
    dziala = True
    while dziala:
        try:
            a = max(substract(base_set, A))
        except ValueError:
            dziala = False
        A.append(a)
        # filtrowanie elementów większych niż a
        A = [x for x in A if x<=a]
        subsets.append(A)
    return subsets



if __name__ == '__main__':
    dupa = [1,2,3,4,5,6,7]
    zupa = [1,2,3,5]
    subsets = gen_podzbiorow(dupa, zupa)
    for item in subsets:
        print(item)
