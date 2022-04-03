

global i,j,circle1,circle2, circle3
i=0
j=0
rightSide=False
downSide=False


def setup():
    global mu,normalForce,i,j,circle1,circle2,circle3,waterPool1,waterPool2, waterPool3
    circle1 = Circle(204,159,203,5,2,PVector(600,50),PVector(0,0))
    circle2 = Circle(100,159,203,50,10,PVector(320,50),PVector(0,0))
    circle3 = Circle(204,0,203,20,5,PVector(20,50),PVector(0,0))
    waterPool1 = Liquid(200, 0, height/3, width, height/3, 0.48)
    waterPool2 = Liquid(100, 0, height/2, width, height/2, 10)
    waterPool3 = Liquid(50, 0, height/20, width, height/3, 0.1)
    
    size(640,800)
    background(128)
    noiseDetail(8,0.9)
    mu = 0.04
    normalForce = 1
    

def draw():
    background(0)
   # translate(width/2,height/2)
    global mu,normalForce,i,j,circle1,circle2,circle3
    waterPool1.display()
    waterPool2.display()
    waterPool3.display()
    
    friction = circle1.velocity.get()
    friction.mult(-1)
    friction.normalize()
    friction.mult(mu)
   
    if circle1.isInside(waterPool1):
        circle1.drag(waterPool1)
    circle1.applyForce(PVector(0,0.1*circle1.mass))
    circle1.move()
    circle1.display()
    circle1.checkEdges()
    if circle1.isInside(waterPool2):
        circle1.drag(waterPool2)
    circle1.applyForce(PVector(0,0.1*circle1.mass))
    circle1.move()
    circle1.display()
    circle1.checkEdges()
    if circle1.isInside(waterPool3):
        circle1.drag(waterPool3)
    circle1.applyForce(PVector(0,0.1*circle1.mass))
    circle1.move()
    circle1.display()
    circle1.checkEdges()
    
    friction = circle2.velocity.get()
    friction.mult(-1)
    friction.normalize()
    friction.mult(mu)
    
    if circle2.isInside(waterPool1):
        circle2.drag(waterPool1)
    circle2.applyForce(PVector(0,0.1*circle2.mass))
    circle2.move()
    circle2.display()
    circle2.checkEdges()
    if circle2.isInside(waterPool2):
        circle2.drag(waterPool2)
    circle2.applyForce(PVector(0,0.1*circle2.mass))
    circle2.move()
    circle2.display()
    circle2.checkEdges()
    if circle2.isInside(waterPool3):
        circle2.drag(waterPool3)
    circle2.applyForce(PVector(0,0.1*circle2.mass))
    circle2.move()
    circle2.display()
    circle2.checkEdges()
    if circle3.isInside(waterPool3):
        circle3.drag(waterPool3)
    circle3.applyForce(PVector(0,0.1*circle3.mass))
    circle3.move()
    circle3.display()
    circle3.checkEdges()
    
    friction = circle3.velocity.get()
    friction.mult(-1)
    friction.normalize()
    friction.mult(mu)
    if circle3.isInside(waterPool1):
        circle3.drag(waterPool1)
    circle3.applyForce(PVector(0,0.1*circle3.mass))
    circle3.move()
    circle3.display()
    circle3.checkEdges()
    if circle3.isInside(waterPool2):
        circle3.drag(waterPool2)
    circle3.applyForce(PVector(0,0.1*circle3.mass))
    circle3.move()
    circle3.display()
    circle3.checkEdges()

class Circle(object):
    def __init__(self,c1,c2,c3,diameter,mass,location,velocity):
        self.c = color(c1,c2,c3)
        self.location = location
        self.velocity = velocity
        self.diameter = diameter
        self.mass = mass
        self.acceleration = PVector(0,0)

    
    def display(self):
        stroke(self.c)
        fill(self.c)
        circle(self.location.x,
               self.location.y,self.diameter)
        
    def move(self):
        
        self.velocity.add(self.acceleration)
        self.location.add(self.velocity)
        self.acceleration.mult(0)

    def checkEdges(self):
        if (self.location.x > width-self.diameter/2):
            self.location.x = width-self.diameter/2
            self.velocity.x *=-1
        elif (self.location.x < self.diameter/2):
            self.location.x = self.diameter/2
            self.velocity.x *=-1
 
        if (self.location.y > height-self.diameter/2): 
            self.location.y = height-self.diameter/2
            self.velocity.y *=-1
        elif (self.location.y < self.diameter/2):
            self.location.y = self.diameter/2
            self.velocity.y *=-1

    def applyForce(self,force):
        realForce = PVector.div(force,self.mass)
        self.acceleration.add(realForce)
        
    def isInside(self,liquid):
        if self.location.x>liquid.x and self.location.x<liquid.x+liquid.width and self.location.y > liquid.y and self.location.y<liquid.y+liquid.height:
            return True
        else:
            return False
        
    def drag(self,liquid):
        speed = self.velocity.mag()
        dragMagnitude = liquid.coeff*speed*speed
        dragForce = self.velocity.get()
        dragForce.mult(-1)
        dragForce.normalize()
        dragForce.mult(dragMagnitude)
        self.applyForce(dragForce)

class Liquid(object):
    def __init__(self,c,x,y,width,height,coeff):

        self.c = color(c)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.coeff = coeff
        
    def display(self):
        noStroke()
        fill(self.c)
        rect(self.x,self.y,self.width,self.height)
        
