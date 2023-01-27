def flat_list(l):
    # input nested list is stored in l
    # Insert Code below
    sdl=[]
    for i in l:
        for j in i:
            sdl.append(j)

    
    # Insert Code Above
    # Return single-dimension list.
    return sdl

