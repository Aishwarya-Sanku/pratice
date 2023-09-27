import json
import re


def update_locator(file_path, page_name, locator_name, locator_value):
    
    with open(file_path, 'r') as file:
        object_repository = json.load(file)

    if page_name not in object_repository:
        raise ValueError("Page not found.")

    
    object_repository[page_name][locator_name] = locator_value

    with open(file_path, 'w') as file:
        json.dump(object_repository, file, indent=2)

#ojdvjofeb
    try:
        update_locator(file_path, page_name, locator_name, locator_value)
        print('Locator updated successfully.')
    except ValueError as e:
        print(f'Error: {str(e)}')






def read_object_repository(file_path):
    try:
        with open(file_path, 'r', encoding='utf8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}



def removeQuotes(file_path) :
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        pattern = r'"(\(page\) => .+?);"'
    updated_content = re.sub(pattern, lambda match: match.group(1), file_content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)



def find_earliest_index_in_arrayB(arrA, arrB):
    earliest_index = float('inf')
    value_with_earliest_index = None

    for value in arrA:
        try:
            index_in_arrB = arrB.index(value)
            if index_in_arrB < earliest_index:
                earliest_index = index_in_arrB
                value_with_earliest_index = value
        except ValueError:
            pass

    return {
        "value": value_with_earliest_index,
        "index": earliest_index if earliest_index != float('inf') else -1,
    }



def find_highest_index_in_arrayB(arrA, arrB):
    highest_index = -1
    value_with_highest_index = None

    for value in arrA:
        try:
            index_in_arrB = arrB.index(value)
            if index_in_arrB > highest_index:
                highest_index = index_in_arrB
                value_with_highest_index = value
        except ValueError:
            pass

    return {
        "value": value_with_highest_index,
        "index": highest_index,
    }


def join_with_alternating_parentheses(array, first_index, last_index):
    result = ""

    for i in range(first_index, last_index + 1):
        value = array[i]
        if (i - first_index) % 2 == 0:
            result += value
        else:
            if i != last_index:
                result += f"({value})."
            else:
                result += f"({value})"

    return result


      
      

       


