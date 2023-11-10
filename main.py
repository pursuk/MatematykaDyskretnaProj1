def substract(x1,x2):
    """

    :param x1: zbiór początkowy
    :param x2: zbiór odejmowany
    :return result: różnica zbiorów A-B
    """
    result = x1.copy()
    for x in x1:
        if x in x2:
            result.remove(x)
    return result



def gen_podzbiorow(n,A=[]):
    subsets = []
    base_set = [*range(1,n+1)]
    dziala = True
    while dziala:
        try:
            a = max(substract(base_set, A))
        except ValueError:
            dziala = False
        A.append(a)
        # filtrowanie elementów większych niż a
        A = [x for x in A if x<=a]
        A.sort()
        subsets.append(A.copy())
    return subsets



if __name__ == '__main__':
    zupa = [1,2,3,5]
    subsets = gen_podzbiorow(7, zupa)
    for item in subsets:
        print(item)
