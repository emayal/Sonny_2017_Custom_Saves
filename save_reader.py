"""
emayal - 2025-10-17
Sonny (2017) Save Reader
"""

SAVENAME = 'SN1_Spartan'
FILENAME = 'Sonny_2017_Save.txt'

"""
Separators
"""
PRIMARY_SEPARATOR = '$'

PARTY_SEPARATOR = '#UM#'

TREE_SEPARATOR = '#ABM#'
TREE_STRAIN_SEPARATOR = '#AT1#'
TREE_ABILITY_SEPARATOR = '#AT2#'
LEVEL_SEPARATOR = '#LV#'

WHEEL_SEPARATOR = '#ABG#'

TUTORIAL_SEPARATOR = '*X*'
TUTORIAL_VALUE_SEPARATOR = '*T*'

STORY_SEPARATOR = '*S*'

STRAINS_SEPARATOR = ''

INVENTORY_SEPARATOR = ''

NULL = '*NULL*'

"""
List indicies (handled with separate function)
18: Party
19: Learned abilities
20: Ability wheel
21: Tutorials
22: Story
23: Strains
24: Inventory
"""
LIST_INDICIES = [18, 19, 20, 21, 22] #[18, 19, 20, 21, 22, 23, 24]

"""
Field keys
"""
KEYS = [
    'Has data (always 1)',
    'Losing streak (non-negative integer)',
    'FPS (positive integer, default 60)',
    'Is legend (1 for true, 0 for false)',
    'Sonny\'s level (positive integer)',
    'Current zone (non-negative integer)',
    'Current stage (non-negative integer)',
    'Latest zone (non-negative integer)',
    'Latest stage (non-negative integer)',
    'Cash (non-negative integer)',
    'Skill points (non-negative integer)',
    'Rate count (unused)',
    'Rate gap (unused)',
    'Save scene (usually Map)',
    'New shop flag (True/False)',
    'New zone flag (True/False)',
    'Item upgrade popup flag (True/False)',
    'Training popup flag (True/False)',
    'Party list',
    'Learned abilities list',
    'Equipped abilities list (ability id: level, level is a positive integer)',
    'Tutorial flag list (key: value, only change value to True/False',
    'Story key list',
    'Learned strains list',
    'Inventory list',
    'Cannot get Physiotherapy flag (True/False)',
    'Cannot get Adamant flag (True/False)'
]


"""
Takes filename and a separator as input, opens the file with the same filename and returns the entire contents of that file, split using the separator.
"""
def read_save(filename: str, primary_separator: str) -> list:
    with open(filename, 'r', encoding='utf-8') as file:
        line = file.readline()
        contents = line.strip().split(primary_separator)
    return contents

"""

"""
def write_contents(filename: str, savename:str, keys: list, contents: list, list_indicies: list):
    header = '-' * (len(savename) + 2)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('+' + header + '+\n')
        file.write('| ' + savename + ' |\n')
        file.write('+' + header + '+\n\n')
        for index in range(len(keys)):
            if index in list_indicies:
                line = select_splitter(index, contents[index])
            else:
                line = contents[index] + '\n'
            file.write('# ' + keys[index] + '\n')
            file.write(line + '\n')

"""
"""
def split_party(party: str, separator: str) -> str:
    result = ''
    party_list = party.split(separator)
    for member in party_list:
        result += member + '\n'
    return result

"""
Splits the tree field with the tree separators, and returns a string with the separators replaced with newlines or lists.
"""
def split_tree(tree: str, separator: str, strain_separator: str, ability_separator: str, level_separator: str, null_value: str) -> str:
    result = ''
    tree_list = tree.split(separator)
    for strain in tree_list:
        strain_key, abilities = strain.split(strain_separator)
        result += strain_key + '\n'
        if abilities != null_value:
            abilities = abilities.split(ability_separator)
            for ability in abilities:
                position, level = ability.split(level_separator)
                result += '- ' + position + ': ' + level + '\n'
        result += '\n'
    return result

"""
Splits the original field using a main separator, and a key/value separator.
Returns a string with the main separators replaced with newlines and key/value separator replaced with ":".
"""
def split_pair(original: str, separator: str, pair_separator: str) -> str:
    result = ''
    original_list = original.split(separator)
    for pair in original_list:
        key, value = pair.split(pair_separator)
        result += key + ': ' + value + '\n'
    return result

"""
Splits the original string using a single separator, and returns a string with the separators replaced with newlines.
"""
def split_single(original: str, separator: str) -> str:
    result = ''
    original_list = original.split(separator)
    for key in original_list:
        result += key + '\n'
    return result

"""
Selects which splitter function to call based on the index, see comment about indicies at the top.
"""
def select_splitter(index: int, line: str) -> str:
    result = ''
    match index:
        case 18:
            result = split_party(line, PARTY_SEPARATOR)
        case 19:
            result = split_tree(line, TREE_SEPARATOR, TREE_STRAIN_SEPARATOR, TREE_ABILITY_SEPARATOR, LEVEL_SEPARATOR, NULL)
        case 20:
            result = split_pair(line, WHEEL_SEPARATOR, LEVEL_SEPARATOR)
        case 21:
            result = split_pair(line, TUTORIAL_SEPARATOR, TUTORIAL_VALUE_SEPARATOR)
        case 22:
            result = split_single(line, STORY_SEPARATOR)
    return result

"""
Opens the save file and writes it to a new text file in a "readable" format.
"""
def main():
    contents = read_save(SAVENAME, PRIMARY_SEPARATOR)
    write_contents(FILENAME, SAVENAME, KEYS, contents, LIST_INDICIES)

if __name__ == '__main__':
    main()
