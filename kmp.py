'''
KMP 알고리즘
key가 string안에 언제 처음 나오는지 알아낸다.
만약 key가 빈 문자열이라면 가장 처음을 반환한다.
string안에 들어있지 않다면 -1을 반환한다.
'''


def get_pi(key):
    pi = [0]
    j = 0
    for i in range(1,len(key)):
        while j > 0 and key[i] != key[j]: j = pi[j-1]
        if key[i] == key[j]:
            j += 1
            pi.append(j)
            if j == len(key):
                j = pi[j-1]
        else:
            pi.append(j)
    return pi

def kmp(string,key):
    if not key: return 0
    pi = get_pi(key)
    j = 0
    for i in range(len(string)):
        while j > 0 and string[i] != key[j]: j = pi[j-1]
        if string[i] == key[j]:
            j += 1
            if j == len(key):
                return i-len(key)+1
    return -1
