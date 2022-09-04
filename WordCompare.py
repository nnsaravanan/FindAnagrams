def word_compare(word1, word2='steal'):
    if type(word1) != str or type(word2) != str:
        return 'Those aren\'t strings!'
    elif sorted(word1.lower()) != sorted(word2.lower()):
        return (word1,word2)
    else:
        return 'Anagram'

assert word_compare('Angle','angel') == 'Anagram'
assert word_compare('word','hello') == ('word','hello')
assert word_compare(2,'goodbye') == 'Those aren\'t strings!'
assert word_compare('steal') == 'Anagram'
