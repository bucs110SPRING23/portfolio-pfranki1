def star_pyramid(lines):
    for i in range(1,lines+1):
        print("*"*i)
    
def rstar_pyramid(lines):
    for i in range(lines, 0, -1):
        print("*"*i)

#(start, stop, *)

height=int(input("Enter pyramid height:"))

star_pyramid(height)
rstar_pyramid(height)
