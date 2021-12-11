import numpy
table = numpy.zeros((3,3))      # table.
p1 = numpy.array([1,1,1])       # result for player 1.
p2 = numpy.array([2,2,2])       # result for player 2.

def d_check(a):     # function for checking diagonal (\).
    comp = table.diagonal() == a
    eq = comp.all()
    if eq == True and a.all() == p1.all():
        return True
    if eq == True and a.all() == p2.all():
        return True

def fd_check(a):        #function for checking second diagonal (/).
    comp = numpy.fliplr(table).diagonal() == a
    eq = comp.all()
    if eq == True and a.all() == p1.all():
        return True
    if eq == True and a.all() == p2.all():
        return True


def row(a):     #function for checking rows.
    for i in range(3):
        comp = table[i, :] == a
        eq = comp.all()
        if eq == True and a.all() == p1.all():
            return True
            break

        if eq == True and a.all() == p2.all():
            return True
            break


def column(a):      #function for checking columns.
    for i in range(3):
        comp = table[:, i] == a
        eq = comp.all()
        if eq == True and a.all() == p1.all():
            return True
            break

        if eq == True and a.all() == p2.all():
            return True
            break

print(table)
x1,y1 = map(int,input().split())  #round 1 for user 2
table[x1,y1]=1
print(table)


for i in range(4):
    x, y = map(int, input().split())
    table[x,y] = 2                  #the input of user 1
    print(table)
    x1,y1 = map(int,input().split())
    table[x1,y1]=1
    print(table)
    if i >= 1:                      # The MainLoop of the program!
        if d_check(p1) == True:
            print('p1 wins ')
            break
        if d_check(p2) == True:
            print('p2 wins ')
            break


        if fd_check(p1) == True:
            print('p1 wins ')
            break
        if fd_check(p2) == True:
            print('p2 wins ')
            break


        if row(p1) == True:
            print('p1 wins ')
            break
        
        if row(p2) == True:
            print('p2 wins ')
            break

        if column(p1) == True:
            print('p1 wins ')
            break
        
        if column(p2) == True:
            print('p2 wins ')
            break
print('tie')      

