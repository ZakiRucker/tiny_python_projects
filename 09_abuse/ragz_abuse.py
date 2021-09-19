#!/usr/bin/env python3
"""
Date   : 2021-09-17
Purpose: Heap abuse
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2)

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default=3)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()
    if args.seed is None:
        pass
    else:
        if args.seed < -1:
            parser.error(f'--seed "{args.seed}" must be > positive')
    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_adj = args.adjectives
    num_insults = args.number
    random.seed(args.seed)

    adjectives = """bankrupt base caterwauling corrupt cullionly
                 detestable dishonest false filthsome filthy foolish
                 foul gross heedless indistinguishable infected
                 insatiate irksome lascivious lecherous loathsome
                 lubbery old peevish rascaly rotten ruinous scurilous
                 scurvy slanderous sodden-witted thin-faced toad-spotted
                 unmannered vile wall-eyed""".split()

    nouns = """Judas Satan ape ass barbermonger beggar block boy
            braggart butt carbuncle coward coxcomb cur dandy degenerate
            fiend fishmonger fool gull harpy jack jolthead knave liar
            lunatic maw milksop minion ratcatcher recreant rogue scold
            slave swine traitor varlet villain worm""".split()

    for _ in range(num_insults):
        adj_string = random.sample(adjectives, num_adj)
        descriptive = ", ".join(adj_string)
        print(f"You {descriptive} {random.choice(nouns)}!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
