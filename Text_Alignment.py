thickness = 5 #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).ljust(thickness*1)+(c*thickness).rjust(thickness*4))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).ljust(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).ljust(thickness*1)+(c*thickness).rjust(thickness*4))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).ljust(thickness)+c+(c*(thickness-i-1)).rjust(thickness)).rjust(width)(thickness*6))
