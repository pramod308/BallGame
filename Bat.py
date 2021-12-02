class Bat:
    def __init__(self,canvas):
        self.canvas=canvas
        self.img=canvas.create_rectangle(150,360,250,355,fill="blue")
        self.x=15
    def moveLeft(self):
        lp,tp,rp,bp=self.canvas.coords(self.img)
        if lp>0:
            self.canvas.move(self.img,-self.x,0)
    def moveRight(self):
        lp,tp,rp,bp=self.canvas.coords(self.img)
        if rp<=430:
            self.canvas.move(self.img,self.x,0)
    def coord_s(self,canvas):
        pos=self.canvas.coords(self.img)
        return pos
    
