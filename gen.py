#!/usr/bin/env python3

from collections import namedtuple
import csv, random

TWEET_LENGTH = 140
FORMAT = "What if we combine {} and {}?"

# You can get this from twitter's API but that's a PITA, so we just hard-code
# it. See https://dev.twitter.com/overview/t.co, "Will t.co-wrapped links always
# be the same length?", and
# https://dev.twitter.com/rest/reference/get/help/configuration.
SHORT_URL_LENGTH_ESTIMATE = 24

class Idea(namedtuple('Idea', 'what whose url')):
    def short(self): return self.what
    def long(self):
        if self.whose: return self.whose + ' ' + self.what
        else: return self.short()

def read_ideas(filename="ideas.csv"):
    with open(filename) as f:
        # filter out whitespace lines and lines starting with "--"
        lines = (l for l in f if l.strip() and not l.startswith('--'))
        for line in csv.reader(lines, dialect='unix'):
            assert 1 <= len(line) <= 3
            what  = line[0].strip()
            whose = line[1].strip() if len(line) > 1 else None
            url   = line[2].strip() if len(line) > 2 else None
            if not whose: whose = None
            if not url: url = None
            yield Idea(what, whose, url)

def mashup(a, b):
    """Mashes up two ideas to make a tweet."""
    # generate attributed & unattributed versions
    short = FORMAT.format(a.short(), b.short())
    long = FORMAT.format(a.long(), b.long())
    # generate urls & calculate effective length
    urls = [i.url for i in [a,b] if i.url]
    urls_len = len(urls) * (SHORT_URL_LENGTH_ESTIMATE+1)
    # pick long or short
    text = long if len(long) + urls_len <= 140 else short
    tweet = '\n'.join([text] + urls)
    return (tweet, len(text) + urls_len)

def run(filename="ideas.csv"):
    all_ideas = list(read_ideas(filename))
    while True:
        ideas = random.sample(all_ideas, 2)
        (tweet, length) = mashup(*ideas)
        if length <= TWEET_LENGTH: break
        else: print("Discarding tweet, too long: " ++ tweet)
    print(tweet)

if __name__ == "__main__":
    run()
