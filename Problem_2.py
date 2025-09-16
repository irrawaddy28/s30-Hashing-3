'''
Favourite Genres
This is not a Leetcode problem but frequently asked in interviews. For eg, this was asked in an online assessment test in Amazon.

Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within that genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.

Example 1:
Input:
userSongs['a'] = ['s1', 's2', 's3']
userSongs['b'] = ['s2', 's3', 's4']

songGenres['melody'] = ['s1', 's2']
songGenres['pop'] = ['s3', 's4']

Output:
result['a'] = 'melody'
result['b'] = 'pop'

Solution
1. Hashing
Step 1: Create a song to genre map using songGenres{}
Eg.
song2genre['s1'] = 'melody'
song2genre['s2'] = 'melody'
song2genre['s3'] = 'pop'
song2genre['s4'] = 'pop'

Step 2: For each user, retrieve the list of songs. For each song, get the genre from song2genre{}. Using a countMap (per user), keep a freq count of the genres corresponding to the songs.
Eg.
userSongs['a']=['s1','s2','s3'] --> song2genre{} --> ['melody','melody','pop']
countMap = {'melody':2, 'pop': 1}

Step 3: Get the genre with the max freq count of that user and store the <user, genere> pair in the result map:
Eg. result['a'] = 'melody'

https://youtu.be/32uI-men3Bc?t=3798

Let M = #users, L = avg #songs per user,
    K = #genres, N = avg #songs per genre
Time: max(M(L+K), KN), Space: O(KN + M + K) = O(KN)
'''
from collections import defaultdict
from json import dumps as pretty

def findFavoriteGenres(userSongs, songGenres):
    ''' Time: max(M(L+K), KN), Space: O(KN + M + K) = O(KN) '''
    s2g = defaultdict(str) # O(KN)
    for genre in songGenres: # O(K)
        songs = songGenres[genre]
        for s in songs: # O(N)
            s2g[s] = genre

    result = defaultdict(list) # Space: O(M)
    for user in userSongs: # O(M)
        songs = userSongs[user]
        countMap = defaultdict(int) # Space: O(K)
        mx = 0
        for s in songs: # O(L)
            g = s2g[s]
            countMap[g] += 1
            mx = max(mx, countMap[g])

        for g in countMap: # O(K)
            if mx == countMap[g]:
                if g: # not an empty string
                    result[user].append(g)
                else:
                    result[user] = []
    return result

def run_findFavoriteGenres():
    tests = [({'u1': ['s1', 's2', 's3'], 'u2': ['s2', 's3', 's4']},
              {'melody': ['s1', 's2'], 'pop': ['s3', 's4']},
              {'u1': ['melody'], 'u2': ['pop']}),

             ({'David': ['s1', 's4', 's5', 's6', 's2', 's7'], 'Emma':  ['s2', 's4', 's3', 's5'], 'Malcolm': ['s7', 's8',  's5']},
              {'jazz': ['s1', 's2', 's7'], 'pop': ['s3', 's4', 's5'], 'rock': ['s6', 's8']},
              {'David': ['jazz'], 'Emma': ['pop'], 'Malcolm': ['jazz','rock','pop']}),

              ({"David": ["s1", "s2", "s3", "s4", "s8"],
                "Emma":  ["s5", "s6", "s7"]},
                {"Rock":    ["s1", "s3"],
                 "Dubstep": ["s7"],
                 "Techno":  ["s2", "s4"],
                 "Pop":     ["s5", "s6"],
                 "Jazz":    ["s8", "s9"],},
                {"David": ["Rock", "Techno"], "Emma":  ["Pop"]},
              ),

              ({"David": ["song1", "song2"],
                "Emma":  ["song3", "song4"]},
                {},
                {"David": [],"Emma":  []},
              ),

    ]
    for test in tests:
        userSongs, songGenres, ans = test[0], test[1], test[2]
        print(f"\nuserSongs: {userSongs}")
        print(f"songGenres: {songGenres}")
        result = findFavoriteGenres(userSongs, songGenres)
        print(f"result: {pretty(result)}")
        success = (ans == result)
        print(f"Pass: {success}")
        if not success:
            print("Failed")
            return

run_findFavoriteGenres()
