# GEO1000 - Assignment 2
# Authors :
# Studentnumbers :

def reverse_part(part):
    """Take as input a list
    Returns a new list with elements in input reversed
    Note: Pure function, so should not modify input!
    
    Example:
    
        >>> reverse_part(['t', 'h', 'i', 's'])
        ['s', 'i', 'h', 't']
    """
    rev_part = part[:]
    rev_part.reverse()
    return rev_part


def part_to_str(part):
    """Take as input a list with letters.
    Returns a new string with letters in the input list

    Example:

        >>> part_to_str(['a', 'b', 'c'])
        "abc"

    """
    string = ''
    for i in part:
        string += i
    return string


def split_in_parts(sentence):
    """Split the string into a list of lists (either containing letters, or just
    one character not part of the alphabet).

    Example:

        >>> split_in_parts("this is.")
        [['t', 'h', 'i', 's'], [' '], ['i', 's'], ['.']]

    """
    sentence_list = []
    sublist = []
    for char in sentence:
        if ord('A') <= ord(char) <= ord('z'):
            sublist.append(char)
        else:
            if sublist:
                sentence_list.append(sublist)
                sublist = []
            sentence_list.append([char])
    if sublist:
        sentence_list.append(sublist)
    return sentence_list


# or only consider ordinary sentence that stars with a letter and does not end with a letter ?


def reverse_relevant_parts(parts):
    """Reverse only those sublists consisting of letters
    
    Input: list of lists, e.g. [['t', 'h', 'i', 's'], [' '], ['i', 's'], ['.']]
    Returns: list with sublists reversed that consist of letters only.
    """
    rev_rel_parts = []
    for sublist in parts:
        if ord('A') <= ord(sublist[0]) <= ord('z'):
            rev_rel_parts.append(reverse_part(sublist))
        else:
            rev_rel_parts.append(sublist)
    return rev_rel_parts


def glue(parts):
    """Transforms the list of sublists back into a new string
    
    Returns: string
    """
    glue_string = ''
    for sublist in parts:
        glue_string += part_to_str(sublist)
    return glue_string


def encrypt(sentence):
    """Reverses all consecutive letter parts in a string.
    
    Input: a string
    Returns: a string
    """
    return glue(reverse_relevant_parts(split_in_parts(sentence)))


if __name__ == "__main__":
    paragraph = "toN ylno si ti ysae ot eil htiw spam, ti's laitnesse. oT yartrop lufgninaem spihsnoitaler rof a xelpmoc, eerht-lanoisnemid dlrow no a talf teehs fo repap ro a oediv neercs, a pam tsum trotsid ytilaer. sA a elacs ledom, eht pam tsum esu slobmys taht tsomla syawla era yllanoitroporp hcum reggib ro rekciht naht eht serutaef yeht tneserper. oT diova gnidih lacitirc noitamrofni ni a gof fo liated, eht pam tsum reffo a evitceles, etelpmocni weiv fo ytilaer. erehT's on epacse morf eht cihpargotrac xodarap: ot tneserp a lufesu dna lufhturht erutcip, na etarucca pam tsum llet etihw seil. --- woH ot eil htiw spam, kraM reinomnoM, 1996."
    print(encrypt(paragraph))
    assert encrypt(encrypt(paragraph)) == paragraph
