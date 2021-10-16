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
    """
    >>> pad_up_to('abb', 5, 11)
    'abbfggkllpq'
    """
    pass


def abc_mirror(word):
    """
    >>> abc_mirror('abcd')
    'zyxw'
    """
    pass


def create_matrix(word1, word2):
    """
    >>> create_matrix('mamas', 'papas')
    ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """
    pass


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
