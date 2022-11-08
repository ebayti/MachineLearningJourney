import math

## Troll 
sensTroll= 12 /(12+112+83)
specTroll= (23+77+92+17) /(23+77+92+17+102+93)

print("Troll sensitivity is " + str(round(sensTroll,2)) )
print("Troll specificity is " + str(round(specTroll,2) ))

## Gore 
sensGore= 23/(23+102+92)
specGore= (12+93+83+17)/(12+93+83+17+112+77)

print("Gore sensitivity is "+ str(round(sensGore,2)) )
print("Gore specificity is "+ str(round(specGore,2)) )

## Cool as ice
sensCAI= 17/ (17+77+93)
specCAI= (12+102+112+23)/ (12+102+112+23+83+92)

print("Cool as Ice sensitivity is "+ str(round(sensCAI,2)) )
print("Cool as Ice specificity is "+ str(round(specCAI,2)) )