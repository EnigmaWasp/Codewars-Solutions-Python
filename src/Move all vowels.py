def move_vowels(inp): 
    res=''
    vows=''
    for x in inp:
        if x in 'aeiou':
            vows+=x
        else:
            res+=x
    return res+vows
    pass 