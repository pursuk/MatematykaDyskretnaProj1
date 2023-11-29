import math,csv, statistics
def gen_podzbiorow(n, k=10, A=None):
    if A is None:
        A = set()
    subsets = [A.copy()]
    base_set = {*range(1, n + 1)}
    while len(A)!=n:
        a = max(base_set - A)
        A.add(a)
        # filtrowanie elementów większych niż a
        A = {x for x in A if x<=a}
        subsets.append(A.copy())
        if len(subsets) > k-1:
            break
    return subsets

def kelem_podzbior(n,p,k):
    """

    :param n: największy element zbioru głównego
    :param p: ilość generowanych podzbiorów, 0 oznacza wszystkie
    :param k: ilość elementów w podzbiorze
    :return:
    """
    if p == 0:
        p = math.comb(n,k)
    main_set = {*range(1, n + 1)}
    subset = {*range(1, k + 1)}
    subsets = [subset.copy()]
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


def zadanie1():
    start_set = {1, 2, 3, 5}
    subsets = gen_podzbiorow(7,10, start_set)
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


def load_players(file):
    players = []
    with open(file, newline='') as csvfile:
        player_reader = csv.reader(csvfile)
        for i,row in enumerate(player_reader):
            players.append((i+1, row[0], row[1]))
    return players

def gen_matches(players):
    matches = kelem_podzbior(len(players),0,4)
    matches_with_players = []
    for match in matches:
        players_in_match = []
        for player_id in list(match):
            players_in_match.append(players[player_id-1])
        matches_with_players.append(players_in_match)
    return matches_with_players


def get_skill_average(players):
    skill_sum = 0
    for player in players:
        skill_sum = skill_sum + int(player[2])
    avg = skill_sum/len(players)
    return avg

def find_best_match(players, mapped_matches):
    skill_avg = get_skill_average(players)
    # print(skill_avg)
    best_skill_delta = 999
    best_match = 'nie ma, zesralo sie'
    for match in mapped_matches:
        match_skill_avg = get_skill_average(match)
        # print(match_skill_avg)
        skill_delta = abs(skill_avg-match_skill_avg)
        match = (match, round(skill_delta, 2))
        if skill_delta < best_skill_delta:
            best_match = match
            best_skill_delta = skill_delta
    return best_match


def filter_best_match_players(best_match, matches):
    best_match_player_ids = [x[0] for x in best_match[0]]
    filtered_list = []
    for match in matches:
        player_ids = [x[0] for x in match]
        if not any(id in set(player_ids) for id in best_match_player_ids):
            # print("removing match:")
            # print(match)
            filtered_list.append(match)
    return filtered_list


def gen_teams(players):
    remapped_players = []
    for i, player in enumerate(players):
        player = (i+1, player[1], player[2])
        remapped_players.append(player)
    teams = kelem_podzbior(len(players),0,2)
    teams_with_players = []
    for team in teams:
        players_in_team = []
        for player_id in list(team):
            players_in_team.append(players[player_id-1])
        teams_with_players.append(players_in_team)
    return teams_with_players



def find_best_teams(teams,players):
    match_skill_avg = get_skill_average(players)
    best_skill_delta = 999
    for team in teams:
        team_skill_avg = statistics.mean([int(player[2]) for player in team])
        skill_delta = abs(team_skill_avg-match_skill_avg)
        if skill_delta < best_skill_delta:
            team1 = team
            best_skill_delta = skill_delta
    team2 = list(set(players)-set(team1))
    return team1,team2



if __name__ == '__main__':
    players = load_players('./data.csv')
    mapped_matches = gen_matches(players)
    final_match_list = []
    while len(mapped_matches) != 0:
        best_match = find_best_match(players, mapped_matches)
        mapped_matches = filter_best_match_players(best_match, mapped_matches)
        final_match_list.append(best_match)

    for match in final_match_list:
        players = match[0]
        teams = gen_teams(players)
        team1, team2 = find_best_teams(teams, players)
        print("__________________________________________\nMECZ")
        print(team1)
        print('vs')
        print(team2)





