def first_non_repeating_char(s):
    char_counts = {}
    
    for i in range(len(s)):
        if s[i] not in char_counts:
            char_counts[s[i]] = 1
        
    else:
        char_counts[s[i]] += 1
    
    for i in char_counts:
        if char_counts[i] == 1:
            return s.index(i)
            
    return -1


if __name__ == "__main__":
    s = "loveleetcode"
    index = first_non_repeating_char(s)
    print(index)
