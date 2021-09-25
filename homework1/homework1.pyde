time=0;
wave=[];
maru=5;

def setup():
    global time,wave,n
    size(600,400)
    
def draw():
    global time,wave,n
    background(0)
    translate(200,200)
    x=0;
    y=0;
    for i in range(maru):
        prevx=x
        prevy=y
        n=i*2+1
        r=50*4/(n*PI)
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
    
    time+=0.05
    if len(wave)>250:
        wave.pop()
        
