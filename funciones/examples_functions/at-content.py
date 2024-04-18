def get_at_content(dna, num): 
    dna = dna.replace('N', '')
    length = len(dna) 
    a_count = dna.upper().count('A') 
    t_count = dna.upper().count('T') 
    at_content = (a_count + t_count) / length 
    return round(at_content, num)


print(get_at_content("ATCGGANNNNAT", 2))

