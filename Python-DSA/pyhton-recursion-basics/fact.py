def fact(i,facto):
    if i == 1:
        print(facto)
        return 
    facto = facto * i  
    fact(i-1,facto)
    

print(fact(count=3,facto=1))
