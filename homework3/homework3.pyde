# pip install numpy
import json
def setup():
    global trainX,trainY,fourierX,fourierY,time,path,skip,dt,mode,col
    size(800,600)
    trainX=[]
    trainY=[]
    time=0
    path=[]
    skip=5
    mode=3
    col=255

    
def draw():
    global trainX,trainY,fourierX,fourierY,time,path,skip,dt,mode,col
    background(0)
    textSize(20)
    fill(255)
    text("press 1,2,3,4 to control shape", 10, 30)
    
    if mode==1:
        trainX=[]
        trainY=[]
        preload("kiwi.json")
    if mode==2:
        trainX=[]
        trainY=[]
        preload("hilbert.json")
    if mode==3:
        trainX=[]
        trainY=[]
        preload("heart.json")
    if mode==4:
        trainX=[]
        trainY=[]
        preload("pentagram.json")

    
    
    vx=epiCycles(width/2,100,0,fourierX)
    vy=epiCycles(100,height/2,HALF_PI,fourierY)
    v=PVector(vx.x,vy.y)
    path.insert(0,v)
    line(vx.x,vx.y,v.x,v.y)
    line(vy.x,vy.y,v.x,v.y)
    
    beginShape()
    noFill()
    stroke(col,255-col,100)
    print(len(path))
    for i in range(len(path)):
        vertex(path[i].x,path[i].y)
    endShape()
    
    dt=TWO_PI/len(fourierY)
    time+=dt
        
    if time>=TWO_PI:
        time=0
        path=[]
        col=col-50
        if(col<=0):
            col=255


def preload(path):
    global trainX,trainY,fourierX,fourierY,dt
    loadJson(path)
    # loadTxt("datas.txt")
    fourierX=dft(trainX)
    fourierY=dft(trainY)
    sortArray(fourierX)
    sortArray(fourierY)
    dt=TWO_PI/len(fourierY)
        
def epiCycles(x,y,rotation,fourier):
    for i in range(len(fourier)):
        prevx=x
        prevy=y
        freq=fourier[i][0]
        radius=fourier[i][1]
        phase=fourier[i][2]
        x+=radius*cos(freq*time+rotation+phase)
        y+=radius*sin(freq*time+rotation+phase)
        stroke(255,100)
        noFill()
        ellipse(prevx,prevy,radius*2,radius*2)
        stroke(255)
        line(prevx,prevy,x,y)
    vec=PVector(x,y)
    return vec
        
def loadJson(path):
    global trainX,trainY,skip
    file=open(path)
    fileJson=json.load(file)
    trainX=[[0]*1]*(len(fileJson)/skip)
    trainY=[[0]*1]*(len(fileJson)/skip)
    for i in range(len(fileJson)/skip):
        trainX[i]=fileJson[i*skip]['x']
        trainY[i]=fileJson[i*skip]['y']

def loadTxt(path):
    global trainX,trainY,fourierX,fourierY,time,skip,dt
    file=open(path,"r")
    filTxt=file.readlines()
    # trainX=[[0]*1]*len(filTxt)
    # trainY=[[0]*1]*len(filTxt)
    trainX=[]
    trainY=[]
    for fields in filTxt:
        fields=fields.strip();
        fields=fields.strip("[]");
        fields=fields.split(",");
        trainX.append(float(fields[0]))
        trainY.append(float(fields[1]))

    
def dft(x):
    N=len(x)
    X=[[0]*3]*N
    for k in range(N):
        re=0
        im=0
        for n in range(N):
            phi=(TWO_PI*k*n)/N
            re+=x[n]*cos(phi)
            im-=x[n]*sin(phi)
        re=re/N
        im=im/N
        freq=k
        amp=sqrt(re*re+im*im)
        phase=atan2(im,re)
        X[k]=[freq,amp,phase]
    return X


def sortArray(arr):
    n=len(arr)
    for i in range(1,n-1):
        for j in range(n-i):
            if arr[j][1]<arr[j+1][1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        
def keyPressed():
    global mode,time,path
    if key=='1':
        mode=1
        path=[]
        time=0
    if key=='2':
        mode=2
        path=[]
        time=0
    if key=='3':
        mode=3
        path=[]
        time=0
    if key=='4':
        mode=4
        path=[]
        time=0
