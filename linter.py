"""
LaTex linter with an fresh and easy menu
"""
import os
from getrules import (get_rule_newline_after_dot, get_rule_space_after_percent,
remove_empty_lines, get_rule_intention_tabs, check_if_valid_file)

def main():
    """Main file"""
    if check_if_valid_file() is True:
        while True:
            print("------------Menu-------------")
            print("1) Apply the rules and create edited file")
            print("q) Quit.")

            choice = input("--> ")

            if choice == "q":
                print("")
                os.remove("output.tex")
                break

            if choice == "1":
                get_rule_newline_after_dot()
                get_rule_space_after_percent()
                remove_empty_lines()
                get_rule_intention_tabs()
                print("You have now created a new edited file: output.tex")
            else:
                print("That is not a valid choice. You can only choose from the menu.")
            break

main()
