def get_word(eng_list, e_word):
    for key in eng_list:
        if e_word.lower() in key:
            print (e_word, ':', eng_list[e_word.lower()])
            break
        else:
            print ('Dont have this word!!!!')
            break

english = {'cat':['con mèo', 'mèo'], 'hello':['xin chào','chào'], 'bye':['tạm biệt'], 'dog':['con chó', 'chó'], 'sum': ['mặt trời'],
            'sorry':['xin lỗi'], 'apple':['quả táo']}

word = input('Enter e_word: ')

get_word(english, word)
