import math
from django.shortcuts import render

# Create your views here.
MyArr=[]
clip=[]
area=0
xmm=[]
totalPoint=[]
view=300

def start(request):
    return render(request,'index.html')
def hello(request):
    return render(request,'line.html',{'name':'luigi'})

def cal(request):
    x1=request.GET['x1']
    y1=request.GET['y1']
    x2=request.GET['x2']
    y2=request.GET['y2']
    xmin=request.GET['Xmin']
    xmax=request.GET['Xmax']
    ymin=request.GET['Ymin']
    ymax=request.GET['Ymax']
    xmin=int(xmin);
    ymin=int(ymin);
    xmax=int(xmax);
    ymax=int(ymax);
    x1=int(x1);
    y1=int(y1);
    x2=int(x2);
    y2=int(y2);
    point="";
    scalePoint=[[xmin,xmax,ymin,ymax]]
    totalPoint=[[x1,y1,x2,y2]]
    sign1=signcond(x1,y1,xmin,xmax,ymin,ymax);
    print(sign1)
    sign2=signcond(x2,y2,xmin,xmax,ymin,ymax);
    print(sign2)

    clipping=cohen(sign1,sign2)

    if clipping=="Clipping Candidate":
        point=midpoint(x1,y1,x2,y2,xmin,xmax,ymin,ymax)
    
    areaX=int(view)/(int(xmax)-int(xmin))
    areaY=int(view)/(int(ymax)-int(ymin))

    line=liner(x1,x2,y1,y2)
    return render(request,'line.html',{'areaX':areaX,'areaY':areaY,'view':view ,'line':line,'cliping':clipping,'point':point,'p':totalPoint,'scalePoint':scalePoint})

def signcond(x,y,xmin,xmax,ymin,ymax):
    #หาพิกัดของจุดใดๆ ว่าอยู่ใน segmentในของ
    #ซึ่งจะมีทั้งหมด 9 regions
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
    #แปลงเป็น binary array ใช้ในการเทียบเลขบิทต่อไป
    return sign

def liner(x1,x2,y1,y2):
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
    return a+b

def midpoint(x1,y1,x2,y2,xmin,xmax,ymin,ymax):
    xx1=x1
    yy1=y1
    xx2=x2
    yy2=y2
    #วนรอบเพื่อหาจุดที่อยู่ใกล้เคียงกับเส้นขอบ
    #ในที่นี้จะวน 9 รอบ แล้วหารอบที่ใกล้เคียงกับขอบที่สุด
    #ทำ ณ จุด x1,y1
    for i in range(9):
        xm1=math.floor((x1+xx2)/2)
        ym1=math.floor((y1+yy2)/2)
        if xm1==xmin or xm1==xmax: break
        if ym1==ymin or ym1==ymax: break
        x1=xm1
        y1=ym1
    text1="("+str(xm1)+","+str(ym1)+")"

    #ทำ ณ จุด x2,y2
    for j in range(9):
        xm2=math.floor((xx1+xm1)/2)
        ym2=math.floor((yy1+ym1)/2)
        if xm2==xmin or xm2==xmax: break
        if ym2==ymin or ym2==ymax: break
        xm1=xm2
        ym1=ym2
    text2="("+str(xm2)+","+str(ym2)+")"

    if xx1==xm2 and yy1==ym2+1:
        text2=""
    if xx1==xm2+1 and yy1==ym2:
        text2=""
    if xx1==xm2 and yy1==ym2:
        text2=""
            
    res="midpoint: "+text1+text2

    return res

def enBinary(s):
    #แปลงเป็นเลขฐานสอง แล้วกลับค่า เพื่อคำนวณได้ง่ายขึ้น
    res=[0,0,0,0]
    res = [int(i) for i in list('{0:0b}'.format(s))]
    print(res) 
    res.reverse();
    return res

def cohen(s1,s2):
    #ทำให้จำนวนบิทเท่ากัน
    for j in range(3):
        if len(s1)>len(s2):
            s2.append(0);
            print(s2)
        elif len(s1)<len(s2):
            s1.append(0);
            print(s1)
    #เปรียบเทียบตัวบิทตัวต่อตัว
    for i in range(len(s1)):
        #เรารู้ว่าถ้า 1 เจอ 1 จะได้ 1 แล้ว visible ทันที
        if s1[i]==1 and s2[i]==1: 
            clipping="Invisible"
        #กรณีอื่นๆ ค่าบิทจะเป็น 0
        elif s1[i]==0 and s2[i]==0:
            clipping="Visible"
        else:
            clipping="Clipping Candidate"

    return clipping
