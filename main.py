from collections import defaultdict
from itertools import permutations


def anagrams(text):
    counter = defaultdict(int)
    for c in text:
        counter[c] += 1

    odds = []
    side = ""

    for (c, count) in counter.items():
        if count % 2 > 0:
            odds.append((c, count))
        else:
            side += c * (int(count / 2))

    if len(odds) == 0:
        middle = ''
    elif len(odds) == 1:
        middle = odds[0][0] * odds[0][1]
    else:
        return []

    permuted_anagrams = []

    for p in set(permutations(side)):
        lhs = ''.join(p)
        rhs = ''.join(reversed(lhs))
        permuted_anagrams.append(lhs + middle + rhs)

    assert len(permuted_anagrams) == len(set(permuted_anagrams))

    return permuted_anagrams

print(anagrams("aaccsbbbb"))
print(anagrams("a"))
