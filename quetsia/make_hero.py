from PIL import Image, ImageDraw, ImageFont
D="/root/.claude/skills/synced/e7b1a9cc-668f-48ae-b130-9180486d38f7_489e7ff2-4d2b-4c65-8f4d-520bed08f918/canvas-design/canvas-fonts/"
S=2; W,H=2400*S,1400*S
BG=(0,0,0); GOLD=(63,203,127); LINE=(153,132,216); DIM=(80,80,80)
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
cols,rows=22,11
mx,my=140*S,170*S
gx=(W-2*mx)/(cols-1); gy=(H-2*my)/(rows-1)
r=11*S
for j in range(rows):
    for i in range(cols):
        x=mx+i*gx; y=H-my-j*gy
        t=(i/(cols-1))-(j/(rows-1))*0.0   # progress to the right
        thr=(j+1)/rows*cols*0.9           # diagonal staircase
        step=i-j*1.6
        if step<-2: d.ellipse([x-r,y-r,x+r,y+r],outline=DIM,width=2*S)
        elif step<4: 
            k=(step+2)/6
            c=tuple(int(DIM[n]+(LINE[n]-DIM[n])*k) for n in range(3))
            d.ellipse([x-r,y-r,x+r,y+r],outline=c,width=2*S)
        elif step<5: d.ellipse([x-r,y-r,x+r,y+r],fill=LINE)
        else: d.ellipse([x-r,y-r,x+r,y+r],fill=GOLD)
f=lambda n,s:ImageFont.truetype(D+n,s*S)
d.text((mx,70*S),"MÉTODO QUETSIA",font=f("InstrumentSans-Regular.ttf",26),fill=LINE)
d.text((W-mx,70*S),"PERGUNTAR  ·  ESCUTAR  ·  CONDUZIR",font=f("InstrumentSans-Regular.ttf",22),fill=DIM,anchor="ra")
d.text((mx,H-95*S),"DA DÚVIDA AO SIM",font=f("InstrumentSans-Regular.ttf",22),fill=DIM)
d.text((W-mx,H-95*S),"● CONDUZIR",font=f("InstrumentSans-Regular.ttf",22),fill=GOLD,anchor="ra")
im.resize((W//S,H//S),Image.LANCZOS).save("static/hero.png",optimize=True)
