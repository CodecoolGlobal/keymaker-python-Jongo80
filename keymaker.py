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
    result = ""
    for z in range(len(matrix)):
        count2 = z
        count = z + 1
        if z % 2 == 0 or z == 0:
            for i in range(len(matrix)):
                result += matrix[i][count2:count]
        else:
            for i in reversed(range(len(matrix))):
                result += matrix[i][count2:count]
    return result


def rotate_right(word, n):
    answer = ""
    while True:
        if n > len(word):
            n = n - len(word)
        else:
            break
    if n == 0:
        answer += word
    if n > 0:
        for i in reversed(range(n + 1)):
            if i != 0:
                answer += word[-i]
        answer += word[:-n]
    elif n < 0:
        n = n - 2 * n
        answer = ""
        while True:
            if n > len(word):
                n = n - len(word)
            else:
                break
        if n == 3:
            count = n + 1
        elif n == 4:
            count = n - 1
        elif n > 4:
            count = n - 1
            for i in range(n - 4):
                count -= 2
        elif n < 3:
            count = n + 1
            for i in range(3 - n):
                count += 2
        if len(word) > 6:
            for i in range(len(word) - 6):
                count += 1
        elif len(word) < 6:
            for i in range(6 - len(word)):
                count -= 1
        for i in reversed(range(count)):
            if i != 0:
                answer += word[-i]
        answer += word[:n]
    return answer


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
