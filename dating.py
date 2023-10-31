#!/usr/bin/env python3
# Created by: Anastasia Friedenstein Patino
# Created on: October. 31, 2023
# dating game that checks if you are good lucking or rich
rich = input("Are you rich? (true or false): ").lower()  # Convert input to lowercase
good_looking = input(
    "Are you good looking? (True or False): "
).lower()  # Convert input to lowercase

# Check if either rich or good looking is True
if rich == "true" or good_looking == "true":
    print("You can date my grandchild")
else:
    print("You can't date my grandchild")
