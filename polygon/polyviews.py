from django.shortcuts import render

# Create your views here.

coordinate=[]

def hello(request):
    return render(request,'polygon.html',{'name':'luigi'})

def addlist(request):
    MyArr=[]
    cond=[]
    Arr=[]
    Arr2=[]
    xmin=request.GET['xmin']
    ymin=request.GET['ymin']
    xmax=request.GET['xmax']
    ymax=request.GET['ymax']
    x1=request.GET['x1']
    y1=request.GET['y1']
    x2=request.GET['x2']
    y2=request.GET['y2']
    x3=request.GET['x3']
    y3=request.GET['y3']
    x4=request.GET['x4']
    y4=request.GET['y4']
    x5=request.GET['x5']
    y5=request.GET['y5']
    xmin=int(xmin)
    ymin=int(ymin)
    xmax=int(xmax)
    ymax=int(ymax)
    x1=int(x1)
    y1=int(y1)
    x2=int(x2)
    y2=int(y2)
    x3=int(x3)
    y3=int(y3)
    x4=int(x4)
    y4=int(y4)
    x5=int(x5)
    y5=int(y5)
    
    cond.append([xmin,ymin,xmax,ymin])#y=0
    cond.append([xmax,ymin,xmax,ymax])#x=10
    cond.append([xmax,ymax,xmin,ymax])#y=10
    cond.append([xmin,ymax,xmin,ymin])#x=0
    
    
    MyArr.append([x1,y1,x2,y2])
    MyArr.append([x2,y2,x3,y3])
    MyArr.append([x3,y3,x4,y4])
    MyArr.append([x4,y4,x5,y5])
    MyArr.append([x5,y5,x1,y1])

    print(MyArr)

    count=0
    
    for i in cond:
        for j in MyArr:
            c=orientation(i,j)
            if c!=[]:
                Arr.append(c)
            
    
        print(Arr)
        for k in Arr:
            for m in k:
                for n in m:
                    Arr2.append(n)
        MyArr=divide(Arr2)
        Arr2=[]
        Arr=[]
        print(MyArr)
    
    return render(request,'polygon.html',{'point':MyArr})

def divide(Arr):
    print(Arr)
    newArr=[]
    n2=[]
    o=0
    f=4
    arrLen=len(Arr)
    for j in range(f,arrLen):
        if f<=arrLen:
            for i in range(o,f):
                newArr.append(Arr[i])
            n2.append(newArr)
            newArr=[]
            o+=2
            f+=2
    n2.append([Arr[-2],Arr[-1],Arr[0],Arr[1]])
    print("n:{}".format(n2))    
    return n2

def orientation(cond,Arr):
    print("start")
    newPoint=[]
    x1=cond[0]
    y1=cond[1]
    x2=cond[2]
    y2=cond[3]
    px1=Arr[0]
    py1=Arr[1]
    px2=Arr[2]
    py2=Arr[3]
    
    print("px1:{}".format(px1))
    print("py1:{}".format(py1))
    print("px2:{}".format(px2))
    print("py2:{}".format(py2))

    c1=((x2-x1)*(py1-y1))-((y2-y1)*(px1-x1))
    c2=((x2-x1)*(py2-y1))-((y2-y1)*(px2-x1))
    print(c1)
    print(c2)
    
    if c1>=0:
        p1="p"
    else:
        p1="n"

    if c2>=0:
        p2="p"
    else:
        p2="n"
    
    clip=clipping(p1,p2)

    if px1==px2:
        x=px2
        y=y2
    else:
        m=(py2-py1)/(px2-px1)
        print("m:{}".format(m))
        print("clip:{}".format(clip))
        b1=py1-(m*px1);
        b2=py2-(m*px2);
        b1=int(b1)
        b2=int(b2)
        print("b1:{}".format(b1))
        print("b2:{}".format(b2))
        
        if b1==b2:
            if m>0:
                if y1==y2:
                    x=(y2-(b1))/m
                    y=y2
                else:
                    x=x2
                    y=(m*x2)+(b1)
            elif m<0:
                if y1==y2:
                    x=(y2-(b1))/m
                    y=y2
                else:
                    x=x2
                    y=(m*x2)+(b1)
            else:
                if y1==y2:
                    y=y2
                    x=px1
                    print(x1)
                    print(y2)
                else:
                    x=x2
                    y=py1
                    print(x2)
        else:
            x=0
            y=0
        
    

    if clip=="a":
        newPoint.append([px2,py2])
    elif clip=="c":
        newPoint.append([x,y])
    elif clip=="d":
        newPoint.append([x,y])
        newPoint.append([px2,py2])
    return newPoint

def clipping(p1,p2):
    if p1=="p" and p2=="p":
        clip="a"
    elif p1=="n" and p2=="n":
        clip="b"
    elif p1=="p" and p2=="n":
        clip="c"
    elif p1=="n" and p2=="p":
        clip="d"
    return clip