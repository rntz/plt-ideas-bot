#!/usr/bin/env python3

from collections import namedtuple
import csv, random

FORMAT = "What if we combine {} and {}?"

Idea = namedtuple('Idea', 'text url')

def read_ideas(filename="ideas.csv"):
    with open(filename) as f:
        return [convert(line) for line in csv.reader(f)]
        for line in csv.reader(f):
            assert 1 <= len(line) <= 2
            text = line[0]
            url =  line[1] if len(line) > 1 else None
            yield Idea(text, url)

def generate(all_ideas):
    """Generates a random mash-up of ideas given a list of ideas."""
    ideas = idea_a, idea_b = random.sample(all_ideas, 2)
    text = FORMAT.format(idea_a.text, idea_b.text)
    urls = [idea.url for idea in ideas if idea.url is not None]

def run(filename="ideas.csv"):
    ideas = list(read_ideas(filename))
    while True:
        g = generate(ideas)
        if g.length_ok(): break
        else: print("Discarding: " ++ str(g))
    return g

print("loaded")
