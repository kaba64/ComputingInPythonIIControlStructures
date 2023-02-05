def calculate_modifier(STAB_in,Type_in,Critical_in,Other_in,Random_in):
    
    return (STAB_in*Type_in*Critical_in*Other_in*Random_in)

def calculate_damage(STAB_in,Type_in,Critical_in,Other_in,Random_in,Level_in, Attack_in,Defense_in,Base_in):
    
    Modifier = calculate_modifier(STAB_in,Type_in,Critical_in,Other_in,Random_in)
    a1 = (2.*Level_in+10.)/250.
    a2 = Attack_in/Defense_in
    return (a1*a2*Base_in+2.)*Modifier

#Below are some lines of code that will test your function.
#You can change the value of the variable to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 16.0
STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

print(calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base))
