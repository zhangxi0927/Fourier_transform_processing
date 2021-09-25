class Fourierplay:
    def __init__(self,maru):
        self.maru=maru
    def create(self):
        if k1==1:
            self.maru+=1
        if k1==2:
            self.maru-=1
        if self.maru<2:
            self.maru=2
        x=0
        y=0
        for i in range(0,self.maru):
            prevx=x
            prevy=y
            # n=i*2+1
            # r=4/(n*PI)
            if k3==1:
                n=i*2+1
                r=50*4/(n*PI)
            if k3==2:
                n=i+1
                r=50* (2*(-1**(n+1)) / (n * PI))
            if k3==3:
                n=i*2+1
                r=(50 * 3) * (4 * (1 - (-1 ** n))/ ((PI ** 2) * (n ** 2)))
            
            x+=r*cos(n*time)
            y+=r*sin(n*time)

            stroke(255,100)
            noFill()
            ellipse(prevx,prevy,r*2,r*2)
            
            stroke(255)
            line(prevx,prevy,x,y)
        wave.insert(0,y)
        translate(200,0)
        line(x-200,y,0,y)
        
        beginShape()
        noFill()
        for i in range(len(wave)):
            vertex(i,wave[i])
        endShape()
    def deleteLine(self):
        if len(wave)>250:
            wave.pop()
            
    
def setup():
    global time,k1,wave,fourierplay,k2,interval,k3
    size(600,400)
    k1=0
    k2=0
    k3=1
    time=0
    interval=0.01
    wave=[]
    fourierplay=Fourierplay(2)

    
def draw():
    global time,interval
    background(0)
    textSize(20)
    fill(255)
    text("press 1,2,3 to control shape", 10, 30)
    fill(255)
    text("press UP and DOWN to control the number of circles", 10, 60)
    fill(255)
    text("press LEFT and RIGHT to control the speed", 10, 90)
    translate(200,200)
    fourierplay.create()
    time+=interval
    fourierplay.deleteLine()
    if k2==1:
        interval-=0.01
    if k2==2:
        interval+=0.01
    
        
def keyPressed():
    global k1,k2,k3
    if keyCode == UP:
        k1=1
    if keyCode == DOWN:
        k1=2
    if keyCode==LEFT:
        k2=1
    if keyCode==RIGHT:
        k2=2
    
def keyReleased():
    global k1,k2,k3
    if keyCode == UP:
        k1=0
    if keyCode == DOWN:
        k1=0
    if keyCode == LEFT:
        k2=0
    if keyCode == RIGHT:
        k2=0
    if key=='1':
        k3=1
    if key=='2':
        k3=2
    if key=='3':
        k3=3
