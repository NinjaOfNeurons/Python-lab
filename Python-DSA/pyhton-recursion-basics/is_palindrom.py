def pland(i,j, ch):
    if(i>=j):
        print("true")
        return 

    if(ch[i] == ch[j]):
        pland(i+1,j-1,ch)
    else:
        print("false")
        




ch = "madam"
print(pland(i=0, j=len(ch)- 1, ch=ch))