import math
from django.shortcuts import render

# Create your views here.
MyArr=[]
clip=[]
area=0
xmin=0
xmax=0
ymin=0
ymax=0
xmm=[]
totalPoint=[]
view=300

def hello(request):
    return render(request,'index.html',{'name':'luigi'})

def cal(request):
    x1=request.GET['x1']
    y1=request.GET['y1']
    x2=request.GET['x2']
    y2=request.GET['y2']
    xmin=request.GET['Xmin']
    xmax=request.GET['Xmax']
    ymin=request.GET['Ymin']
    ymax=request.GET['Ymax']
    x1=int(x1);
    y1=int(y1);
    x2=int(x2);
    y2=int(y2);
    point="";
    scalePoint=[[xmin,xmax,ymin,ymax]]
    totalPoint=[[x1,y1,x2,y2]]
    sign1=signcond(x1,y1);
    print(sign1)
    sign2=signcond(x2,y2);
    print(sign2)

    clipping=cohen(sign1,sign2)

    if clipping=="Clipping Candidate":
        point=midpoint(x1,y1,x2,y2)

    if x1==x2:
        a="y="+str(x1)
        b=" "
    elif y1==y2:
        a="x="+str(y1)
        b=" "
    else:
        a=(y2-y1)/(x2-x1)
        b=((-a)*x1)+y1

        if a > 0 or a < 0:
            a="y="+str(a)+"x"
        elif a == 0:
            a="y="+"0"

        if b > 0:
            b="+"+str(b)
        elif b == 0:
            b=" "
        else:
            b=str(b)
    
    areaX=int(view)/(int(xmax)-int(xmin))
    areaY=int(view)/(int(ymax)-int(ymin))

    line=a+b
    return render(request,'index.html',{'areaX':areaX,'areaY':areaY,'view':view ,'line':line,'cliping':clipping,'point':point,'p':totalPoint,'scalePoint':scalePoint})

def signcond(x,y):
    if x<xmin and y>ymax: s=9
    elif y>ymax: s=8
    elif x>xmax and y>ymax: s=10
    elif x<xmin: s=1
    elif x>xmax: s=2
    elif x<xmin and y<ymin: s=5
    elif y<ymin: s=4
    elif x>xmax and y<ymin: s=6
    else: s=0
    sign=enBinary(s)
    return sign

def midpoint(x1,y1,x2,y2):
    xx1=x1
    yy1=y1
    xx2=x2
    yy2=y2

    for i in range(9):
        xm1=math.floor((x1+xx2)/2)
        ym1=math.floor((y1+yy2)/2)
        if xm1==xmin or xm1==xmax: break
        if ym1==ymin or ym1==ymax: break
        x1=xm1
        y1=ym1
    text1="("+str(xm1)+","+str(ym1)+")"

    for j in range(9):
        xm2=math.floor((xx1+xm1)/2)
        ym2=math.floor((yy1+ym1)/2)
        if xm2==xmin or xm2==xmax: break
        if ym2==ymin or ym2==ymax: break
        xm1=xm2
        ym1=ym2
    text2="("+str(xm2)+","+str(ym2)+")"
    res="midpoint: "+text2+"and"+text1
    return res

def enBinary(s):
    res=[0,0,0,0]
    res = [int(i) for i in list('{0:0b}'.format(s))]
    res.reverse(); 
    return res

def cohen(s1,s2):
    buffer=0
    for j in range(3):
        if len(s1)>len(s2):
            s2.append(0);
            print(s2)
        elif len(s1)<len(s2):
            s1.append(0);
            print(s1)
    
    for i in range(len(s1)):
        if s1[i]==1 and s2[i]==1:
            clipping="Invisible"
            buffer+=1
        elif s1[i]==0 and s2[i]==0 and buffer==0:
            clipping="Visible"
        else:
            clipping="Clipping Candidate"
            buffer+=1
    return clipping
