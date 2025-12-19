def sortCharcters(s):
    freq={}
    for char in s:
        freq[char]=freq.get(char,0)+1
    sortedChars=sorted(freq.items(),key=lamda x:(-x[1],x[0]))
    result=[char for char, count in sortCharcters]
    return result