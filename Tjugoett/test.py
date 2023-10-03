# Example lists
list1 = ["Item 1", "Item 2", "Item 3"]
list2 = ["A", "B"]

# UI width
ui_width = 50

# Initialize indices for both lists
index1 = 0
index2 = 0

while index1 < len(list1) or index2 < len(list2):
    # Initialize strings for left, center, and right sections
    left_section = "|"
    center_section = "|"
    right_section = "|"

    # Populate left section
    if index1 < len(list1):
        left_section += f" {list1[index1]}"
        index1 += 1

    # Populate center section
    if index2 < len(list2):
        center_section += f" {list2[index2]}"
        index2 += 1

    # Populate right section
    right_section += " " * (ui_width - len(left_section) - len(center_section)) + "|"

    # Print the complete UI line
    print(left_section + center_section + right_section)
