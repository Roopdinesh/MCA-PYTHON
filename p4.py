for row in range(7):
    for col in range(5):
        if( (col==3 and row<=6 or row==6 and col==4) or ((col>4 or row==6 and row==2 ) and(   row==6 and col==2))or
           ((  row==7 or row==3 or col==3) and (row>1 and row<6 and row==4 )  or (row==7 and  col>=0 and col<6) )):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
