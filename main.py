from brain import Brain
import re

brain = Brain()


def remove_parentheses_contents(input_list):
    # Regular expression to match parentheses and their contents
    pattern = re.compile(r'\(.*?\)')

    # Remove parentheses and their contents from each list member
    output_list = [pattern.sub('', item) for item in input_list]

    # Strip any leading or trailing whitespace that may result from removal
    output_list = [item.strip() for item in output_list]

    return output_list


brain.add_member()


brain.list1 = remove_parentheses_contents(brain.list1)
brain.list2 = remove_parentheses_contents(brain.list2)


brain.remove_common_member()


brain.list_to_string()

turn_off = False

while not turn_off:
    off_input = input("\nType 'off' To close the program\n")
    if off_input.lower() == "off":
        turn_off = True
    else:
        print("\nWRONG INPUT!\n")
