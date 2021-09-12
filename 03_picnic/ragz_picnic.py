#!/usr/bin/env python3
"""
Date   : 2021-09-11
Purpose: Working with lists
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Working with lists",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "items", metavar="items", nargs="+", help="Items to bring on picnic"
    )

    parser.add_argument(
        "-s", "--sorted", help="A boolean flag to sort", action="store_true"
    )

    return parser.parse_args()


# --------------------------------------------------
def form_items(items):
    """assemble the items string"""

    if len(items) == 1:
        return items.pop()
    elif len(items) == 2:
        return "{} and {}".format(items[0], items[1])
    else:
        all_items = ""
        for i in range(len(items)):
            if i == len(items) - 1:
                all_items = all_items + "and {}".format(items[i])
            else:
                all_items = all_items + items[i] + ", "
        return all_items


# --------------------------------------------------
def sorting(items):
    """sort the items"""

    items.sort()
    return items


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    flag_arg = args.sorted
    items = args.items

    if flag_arg:
        items = sorting(items)

    final_list = form_items(items)

    print("You are bringing {}.".format(final_list))


# --------------------------------------------------
if __name__ == "__main__":
    main()
