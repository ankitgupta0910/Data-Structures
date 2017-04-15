def isAnagram(word1, word2):
    if len(word1) is len(word2):
        temp1 = ''.join(sorted(word1))
        temp2 = ''.join(sorted(word2))
        if temp1 == temp2:
            print True
    else:
        print False


isAnagram("ankit", "tikna")
