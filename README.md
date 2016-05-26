# What is this?

This is the source for [@pltideasbot](https://twitter.com/pltideasbot), a
Twitter) bot that mashes up programming language theory ideas and tweets them!

Every day (modulo my internet connectivity), it picks two ideas from
[ideas.csv](https://github.com/rntz/plt-ideas-bot/blob/master/ideas.csv), and
publishes a tweet of the form "What if we combined X and Y?".

# How to contribute!

PLT ideas bot needs your ideas! The more ideas it has, the more mashups it can
make without getting boring. Also, the current list is totally biased toward my
research interests. [You can see the list of ideas we have so far
here](https://github.com/rntz/plt-ideas-bot/blob/master/ideas.csv).

You can contribute by making a PR that adds your idea to `ideas.csv`. Or, you
can update an existing idea by adding a URL or author(s)! If making a PR is too
much, just tweet to [@pltideasbot](https://twitter.com/pltideasbot) with the
idea to add. Decisions about what ideas to include are ultimately down to me;
see below for some guidelines.

Ideas have three fields:

1. A short description of the idea is. Keep this short and to the point - it has
   to fit in a tweet with another idea, and maybe some URLs! This is mandatory.

2. Whose idea it is. This should be formatted as a possessive, e.g. "Knuth's".
   Not all ideas have an author! That's ok. This may be omitted from the tweet
   if it doesn't fit.

3. A url, often a link to a paper. Not all ideas have urls! But a URL will never
   be omitted from the tweet if present.

## What makes a good contribution?

In my opinion, good ideas for mashing up:

- Are not overly specific. "Functional reactive programming" is good.
  "Higher-order reactive programming without spacetime leaks" is a great paper,
  but overly specific for a mashup.

- Might or might not have a paper attached! Some powerful ideas, like "garbage
  collection" or "domain-specific languages", are too general to have a single
  originating paper. That's ok!
