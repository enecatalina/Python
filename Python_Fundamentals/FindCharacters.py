test_list=['hello','world','my','name','is','Anna']


def find_character(word_list, char):
    new_list = []
    for i in range(0, len(word_list)):

        if word_list[i].find(char) > 0:
            new_list.append(word_list[i])

    print new_list

find_character(test_list, 'o')