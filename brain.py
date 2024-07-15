
class Brain:

    def __init__(self):
        self.list1 = []
        self.list2 = []

    def string_to_list(self, input_string):
        # Split the input string by commas and remove any leading/trailing whitespace from each element
        members_list = [member.strip() for member in input_string.split(',')]
        return members_list

    def add_member(self):
        list1 = input("Paste the first list: \n")
        self.list1 = self.string_to_list(list1)
        list2 = input("Paste the second list: \n")
        self.list2 = self.string_to_list(list2)

    def remove_common_member(self):
        set1 = {item.lower() for item in self.list1}
        set2 = {item.lower() for item in self.list2}

        common_elements = set1.intersection(set2)

        self.list1 = [item for item in self.list1 if item.lower() not in common_elements]
        self.list2 = [item for item in self.list2 if item.lower() not in common_elements]

    def list_to_string(self):
        result_string1 = ', '.join(self.list1)
        result_string2 = ', '.join(self.list2)
        print("\n----First list: ")
        print(result_string1)
        print("\n----Second list: ")
        print(result_string2)
