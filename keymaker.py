def shift_characters(word, shift):
    string_of_all_letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    listed_word = []
    for i in range(len(word)):
        listed_word.append(word[i])
    list_of_all_letters = string_of_all_letters.split(",")
    list_of_all_letters += list_of_all_letters * shift
    for i in range(len(listed_word)):
        listed_word[i] = list_of_all_letters[list_of_all_letters.index(listed_word[i]) + shift]
    listed_word = str(listed_word)
    listed_word = listed_word.replace("[", "")
    listed_word = listed_word.replace("]", "")
    listed_word = listed_word.replace(",", "")
    listed_word = listed_word.replace("'", "")
    listed_word = listed_word.replace(" ", "")
    return listed_word


def pad_up_to(word, shift, n):
    resulted_string = word
    for i in range(n):
        shifted_word = shift_characters(word, shift)
        resulted_string += shifted_word
        word = shifted_word
    return resulted_string[:n]


def abc_mirror(word):
    string_of_all_letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    listed_word = []
    for i in range(len(word)):
        listed_word.append(word[i])
    list_of_all_letters = string_of_all_letters.split(",")
    for i in range(len(word)):
        listed_word[i] = list_of_all_letters[25 - list_of_all_letters.index(listed_word[i])]
    listed_word = str(listed_word)
    listed_word = listed_word.replace("[", "")
    listed_word = listed_word.replace("]", "")
    listed_word = listed_word.replace(",", "")
    listed_word = listed_word.replace("'", "")
    listed_word = listed_word.replace(" ", "")
    return listed_word


def create_matrix(word1, word2):
    string_of_all_letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    basic_list = string_of_all_letters.split(",")
    result = ""
    for i in range(len(word2)):
        shift = basic_list.index(word2[i])
        shifted_word = shift_characters(word1, shift)
        result += shifted_word
        if i != len(word2) - 1:
            result += ","
    result = result.split(",")
    return result


def zig_zag_concatenate(matrix):
    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    'adgjkhebcfil'
    """
    pass


def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    'fghabcde'
    """
    pass


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    'abej'
    """
    pass


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    pass


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    pass


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


if __name__ == '__main__':
    name = input("Enter your name! ").lower()
    print(f'Your key: {hash_it(name)}')
