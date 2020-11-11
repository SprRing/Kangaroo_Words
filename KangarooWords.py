import re

def LCS(s1, s2):
    if len(s2) >= len(s1):
        return False
    s1 = s1.lower()
    s2 = s2.lower()
    a, b= len(s1), len(s2)
    spot = -1
    if s2 in s1:
        spot = s1.find(s2)+len(s2)-1
    res = [[0 for i in range(b+1)] for j in range(a+1)]
    for i in range(1, a+1):
        for j in range(1, b+1):
            if s1[i-1] == s2[j-1] and i-1 != spot:
                res[i][j] = res[i-1][j-1] + 1
            else:
                res[i][j] = max(res[i][j-1], res[i-1][j])
    return res[a][b] == len(s2)



def KangarooWords(words, wordsToSynonyms, wordsToAntonyms):
    hash = {}
    res = []
    count = 0
    for i in wordsToSynonyms:
        temp = re.split(r'\W+', i)
        for j in range(1, len(temp)):
            if LCS(temp[0], temp[j]):
                if temp[0] not in hash:
                    hash[temp[0]] = [temp[j]]
                else:
                    hash[temp[0]] = hash[temp[0]].append(temp[j])
    for i in wordsToAntonyms:
        temp = re.split(r'\W+', i)
        for j in range(1, len(temp)):
            if LCS(temp[0], temp[j]):
                if temp[0] not in hash:
                    hash[temp[0]] = [temp[j]]
                else:
                    hash[temp[0]] = hash[temp[0]].append(temp[j])
    for i in words:
        if i in hash:
            if i not in res:
                res.append(i)
                count += 1
            else:
                count += 2
    return count

words = [
"curtail",
"scion",
"barren",
"amicable",
"departed",
"blossom"]
wordsToSynonyms = [
"scion:son",
"blossom:bloom",
"curtail:cut",
"departed:dead",
"barren:bare",
"amicable:amiable"]
wordsToAntonyms= []


result = KangarooWords(words, wordsToSynonyms, wordsToAntonyms)
print(result)