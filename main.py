def gen_podzbiorow(n, A=None):
    if A is None:
        A = {}
    subsets = []
    base_set = {*range(1, n + 1)}
    while len(A)!=n:
        a = max(base_set - A)
        A.add(a)
        # filtrowanie elementów większych niż a
        A = {x for x in A if x<=a}
        subsets.append(A.copy())
    return subsets

def kelem_podzbior(n,p,k):
    subsets = []
    main_set = {*range(1, n + 1)}
    subset = {*range(1, k + 1)}
    for o in range(p-1):
        a_min = min({x+1 for x in subset} - subset)
        LU = {x if x != a_min else x+1 for x in subset}
        i = len({x for x in subset if x < a_min})
        L = {*list(main_set)[0:i-1]}
        U = {i for i in LU if i > a_min}
        subset = L | {a_min} | U
        subsets.append(subset.copy())
    return subsets


def permutacje(n, p, X = None):
    """

    :param n: najwiekszy element zbioru głównego
    :param p: ilość genertowanych permutacji
    :param X: początkowa permutacja
    :return:
    """
    A = X.copy()
    if A is None:
        A = [*range(1,n+1)]
    permutations = [A.copy()]
    for _ in range(p-1):
        j_list = []
        ak_list = []
        for i,x in enumerate(A):
            try:
                if A[i+1] > A[i]:
                    j_list.append(i)
            except IndexError:
                pass
        try:
            j_max = max(j_list)
        except:
            break

        if A[j_max + 1:] is not None:
            for ak in A[j_max + 1:]:
                if ak > A[j_max]:
                    ak_list.append(ak)
        if ak_list is not None:
            ak_min = min(ak_list)
            #szukamy indeksu ak
            ak_pos = A.index(ak_min)
            A[ak_pos] = A[j_max]
            A[j_max] = ak_min
        if j_max < 5:
            prawa = A[j_max+1:].copy()
            prawa.reverse()
            A[j_max+1:] = prawa
        permutations.append(A.copy())
    return permutations






if __name__ == '__main__':
    start_set = {1, 2, 3, 5}
    subsets = gen_podzbiorow(7, start_set)
    for item in sorted(subsets, key=len):
        print(item)
    print('\n___________________________________________________')
    n = 7
    p = 10
    k = 5

    for subset in kelem_podzbior(n, p, k):
        print(subset)
    print('\n___________________________________________________')
    n = 6
    p = 10
    X = [4, 5, 6, 3, 2, 1]
    for item in permutacje(n,p,X):
        print(item)





