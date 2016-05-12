import sys
from collections import defaultdict

words=defaultdict(lambda: 0)

for line in sys.stdin:
    for word in line.strip().split(' '):
        words[word] += 1

for word, freq in words.iteritems():
    print word, freq
