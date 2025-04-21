# Codenames Word Pack

This is a collection of word lists from different expansions and add-ons for Codenames.
I use these word lists to create my own custom word pack for the online version of 
Codenames, available at:

https://codenames.game/

To create the custom word pack, simply run:

`./word.py`

The word lists contain a list of words from that particular expansion/add-on. It uses
the following syntax:

1. If a line starts with the # (pound) sign, it is a comment
2. If the word starts with the - (minus) sign, it is excluded from my aggregate word pack.
3. If the word starts with the = (equal) sign, it is a duplicate word from earlier word packs.
4. If the word starts with the > (greater than) sign, it is replaced by the next word (see next point).
5. If the word starts with the < (less than) sign, it is replacing the previous word, which must have started with >.