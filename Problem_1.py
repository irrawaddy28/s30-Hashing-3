'''
187 Repeated DNA Sequence
https://leetcode.com/problems/repeated-dna-sequences/description/

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

    For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Constraints:
1 <= s.length <= 10^5
s[i] is either 'A', 'C', 'G', or 'T'.

Solution
1. Sliding Window w/ Hashing
We go through the string from left to right grabbing every K-character (here K = 10) long substring. We add the substring to a hash set h.  If the substring was already added to h before, we add it to another hash set result (which stores all substrings with freq count >= 2). Note that we could not have used a list for the result since the list would have appended multiple instances (specifically, freq count - 1 instances) of substrings whose freq count >= 2.
https://youtu.be/kgKcuTIv6wk?t=4270
Time: O(min(N-K,K)*10) = O(min(N-K,K)), Space: O(min(N-K,K)*10) = O(min(N-K,K))
'''
from typing import List
def findRepeatedDnaSequences(s: str) -> List[str]:
    if not s:
        return []
    N = len(s)
    K = 10
    if N < K:
        return []

    h, result = set(), set()
    for i in range(N-(K-1)): # 0,,,,N-K,N-(K-1),...,N-1
        substr = s[i:i+K] # O(10)
        if substr in h:
            result.add(substr) # substrings with freq count = 2
        h.add(substr) # substrings with freq count = 1

    return list(result)

def run_findRepeatedDnaSequences():
    tests = [("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC", "CCCCCAAAAA"]),
             ("AAAAAAAAAAAAA", ["AAAAAAAAAA"]),
    ]
    for test in tests:
        s, ans = test[0], test[1]
        print(f'\ns: {s}')
        result = findRepeatedDnaSequences(s)
        print(f"result: {result}")
        success = (sorted(ans) == sorted(result))
        print(f"Pass: {success}")
        if not success:
            print(f"Failed")
            return

run_findRepeatedDnaSequences()