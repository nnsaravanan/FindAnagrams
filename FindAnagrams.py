from WordCompare import word_compare

def find_anagrams(lst):
    anagramsdict = {}
    for w1 in lst:
        templst = lst[:lst.index(w1)] + lst[lst.index(w1)+1:]
        anagramsdict[w1] = [w2 for w2 in templst if word_compare(w1, w2) == 'Anagram']
        
    anagramstr = ''
    for key,val in anagramsdict.items():
        anagramstr += str(key)+": "+str(val)+"\n"
    return anagramstr.strip()

words = ['parse','pares','spare','reaps','spear','pears','hi','texas','roll','spain','yellow','painting']
expected_result = "parse: ['pares', 'spare', 'reaps', 'spear', 'pears']\npares: ['parse', 'spare', 'reaps', 'spear', 'pears']\nspare: ['parse', 'pares', 'reaps', 'spear', 'pears']\nreaps: ['parse', 'pares', 'spare', 'spear', 'pears']\nspear: ['parse', 'pares', 'spare', 'reaps', 'pears']\npears: ['parse', 'pares', 'spare', 'reaps', 'spear']\nhi: []\ntexas: []\nroll: []\nspain: []\nyellow: []\npainting: []"

assert find_anagrams(words) == expected_result # test your function with your own words
