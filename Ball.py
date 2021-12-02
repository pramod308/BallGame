class Ball:
    def __init__(self,canvas):
        self.canvas=canvas
        self.img=canvas.create_oval(75,75,50,50,fill='Lightgreen')
        self.x=10
        self.y=10
        self.hit_bottom=False
    def move(self,canvas):
        self.canvas.move(self.img,self.x,self.y)
        lp,tp,rp,bp=canvas.coords(self.img)
        if lp<=0 or rp>=450:
            self.x=-self.x
        if tp<=0:
            self.y=-self.y
        if bp>=390:
            self.hit_bottom=True
        
    def coord_s(self,canvas):
        pos=self.canvas.coords(self.img)
        return pos
        
    
