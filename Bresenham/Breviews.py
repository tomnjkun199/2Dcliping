from django.shortcuts import render

Arr=[]
# Create your views here.
def hello (request):
    return render(request,'bresen.html',{'name':'luigi'})

def brealgo(request):
    NewArr=[]
    x1=int(request.GET['x1'])
    y1=int(request.GET['y1'])
    x2=int(request.GET['x2'])
    y2=int(request.GET['y2'])
    dx=x2-x1
    dy=y2-y1
    
    if abs(dx)>abs(dy):
        if (dx>0)!=(dy>0):
            print("case3")
            NewArr=originalBresenhamline(3,x1,-y1,x2,-y2)
            NewArr=flipArray(3,NewArr)
            print(NewArr)
        else:
            print("case1")
            NewArr=originalBresenhamline(1,x1,y1,x2,y2)
            print(NewArr)
    else:
        if (dx>0)!=(dy>0):
            print("case4")
            NewArr=originalBresenhamline(4,-y1,x1,-y2,x2)
            NewArr=flipArray(4,NewArr)  
            print(NewArr)   
        else:
            print("case2")
            NewArr=originalBresenhamline(2,y1,x1,y2,x2)
            print(NewArr)
                                
    return render(request,'bresen.html',{'point':NewArr})

def flipArray(case,a):
    Arr=a
    for i in Arr:
        if case==4:
            i[0]=-i[0]
            i[2]=-i[2]
        elif case==3:
            i[1]=-i[1]
            i[3]=-i[3]
    return Arr

def originalBresenhamline(case,x1,y1,x2,y2):
    Arr=[]
    dx=x2-x1
    dy=y2-y1
    d=(2*dy)-dx
    du=2*(dy-dx)
    dD=2*dy
    print("has been changed to ({},{})==> ({},{})".format(x1,y1,x2,y2))
    print("|dx| = {} |dy| = {}".format(dx,dy))
    x=x1
    y=y1
    print(x)
    print(x2)

    while x<x2:
        dp=d
        if d<0:
            d+= dD
            oldX=x
            oldY=y
            x+=1
            print("choose D, d= {} + ({}) = {} ==> ({},{}) ==> {}".format(dp,dD,d,x,y,PrintPixel(case,x,y)))
            Arr.append([oldX,oldY,x,y])
        else:
            d+=du
            oldX=x
            oldY=y
            x+=1
            y+=1
            print("choose U, d= {} + ({}) = {} ==> ({},{}) ==> {}".format(dp,du,d,x,y,PrintPixel(case,x,y)))
            Arr.append([oldX,oldY,x,y])
    return Arr

def PrintPixel(case,x,y):
    if case==1:
        str1="({},{})".format(x,y)
        return str1
    elif case==2:
        str1="({},{})".format(y,x)
        return str1
    elif case==3:
        str1="({},{})".format(x,-y)
        return str1
    elif case==4:
        str1="({},{})".format(y,-x)
        return str1   