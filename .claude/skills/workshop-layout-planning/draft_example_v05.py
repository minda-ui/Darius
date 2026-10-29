import sys, math
from PIL import Image, ImageDraw, ImageFont
src,out=sys.argv[1],sys.argv[2]
K=100/72.0                      # px per pt
O=(759.4,824.6); A=(-0.866,-0.5006); D=(0.5005,-0.866); MMPT=37.5
def P(x,y):                      # bay mm -> px
    return ((O[0]+(x*A[0]+y*D[0])/MMPT)*K, (O[1]+(x*A[1]+y*D[1])/MMPT)*K)
def T(px80):                     # 80-dpi trace px -> px
    return [(u*0.9*K, v*0.9*K) for u,v in px80]
im=Image.open(src).convert('RGBA'); ov=Image.new('RGBA',im.size,(0,0,0,0)); d=ImageDraw.Draw(ov)
F=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',s)
def rect(x0,y0,x1,y1,col,label,fill=60,dash=False,size=12,tcol=None):
    pts=[P(x0,y0),P(x1,y0),P(x1,y1),P(x0,y1)]
    d.polygon(pts,fill=col+(fill,),outline=col+(255,))
    cx=sum(p[0] for p in pts)/4; cy=sum(p[1] for p in pts)/4
    for i,line in enumerate(label.split('\n')):
        d.text((cx,cy+(i-(label.count('\n'))/2)*(size+3)),line,fill=(tcol or col)+(255,),font=F(size),anchor='mm')
def poly(pts,col,label,size=11):
    d.polygon(pts,fill=col+(35,),outline=col+(200,))
    cx=sum(p[0] for p in pts)/len(pts); cy=sum(p[1] for p in pts)/len(pts)
    d.text((cx,cy),label,fill=col+(230,),font=F(size),anchor='mm')
# removed wall (Unit 30 bay / workshop bay)
w=[(476.4*K,661.0*K),(569.5*K,500.4*K)]
d.line(w,fill=(255,255,255,255),width=7); d.line(w,fill=(200,30,30,200),width=2)
mx,my=(w[0][0]+w[1][0])/2,(w[0][1]+w[1][1])/2
d.text((mx-10,my),'wall removed',fill=(200,30,30,255),font=F(11),anchor='rm')
# unchanged machines (traced from owner's marks, approx)
poly(T([(190,60),(410,60),(410,290),(190,290)]),(40,120,200),'ASSEMBLY (racking removed)',12)
# new layout in the Unit 30 bay (mm from bottom-right inside corner; y = away from the bottom wall)
rect(150,150,4700,10300,(170,120,60),'TOOLS AND\nCONSTRUCTION\nMATERIALS\nSTORAGE\n(not workshop)',fill=55,size=12,tcol=(130,80,30))
# forklift aisle from the 2.4 m doors (top) to the rack face
rect(5000,3300,7650,9500,(0,90,220),'',fill=22)
ax,ay=P(6330,8800); bx2,by2=P(6330,3500)
d.line([(ax,ay),(bx2,by2)],fill=(0,90,220,230),width=4)
import math as _m
ang=_m.atan2(by2-ay,bx2-ax); L=16
d.polygon([(bx2,by2),(bx2-L*_m.cos(ang-0.4),by2-L*_m.sin(ang-0.4)),(bx2-L*_m.cos(ang+0.4),by2-L*_m.sin(ang+0.4))],fill=(0,90,220,230))
mx2,my2=P(6330,6600)
nt2='forklift aisle\nfrom roller shutter\nthrough 2.4 m doors'
bb=d.multiline_textbbox((mx2,my2),nt2,font=F(10),anchor='mm'); d.rectangle([bb[0]-3,bb[1]-2,bb[2]+3,bb[3]+2],fill=(255,255,255,220))
d.multiline_text((mx2,my2),nt2,fill=(0,90,220,255),font=F(10),anchor='mm')
dx,dy=P(6330,10300); d.text((dx,dy),'2.4 m double doors',fill=(0,90,220,255),font=F(10),anchor='mm')
rect(5195,150,7465,3150,(130,100,40),'PANEL RACK\n3000 x 2270\n5-6 shelves\nloaded from\nthe aisle',fill=90,size=10)
rect(7750,2550,12250,9050,(0,140,90),'F45 (moved)\n4500 x 6500\ncan shift left -\nwall is gone',fill=70,size=11)
rect(8000,0,12250,2250,(60,60,60),'',fill=40)
rect(8650,150,11820,1350,(90,90,90),'EXTRACTOR 3170 x 1200',fill=110,size=9)
qx,qy=P(10125,1850); d.text((qx,qy),'ACOUSTIC ROOM ~4.2 x 2.2 m',fill=(40,40,40,255),font=F(10),anchor='mm')
ex1=P(10200,150); ex2=P(10200,-900); d.line([ex1,ex2],fill=(0,150,200,255),width=5); d.text((ex2[0]+6,ex2[1]+4),'clean-air duct\nout through wall',fill=(0,120,170,255),font=F(10),anchor='la')
dr=[P(8000,1500),P(8000,2250)]; d.line(dr,fill=(255,255,255,255),width=5); d.text((dr[1][0]-4,dr[1][1]-4),'door?',fill=(40,40,40,255),font=F(9),anchor='rb')
# jib crane
cx,cy=P(7700,3300); r=4200/MMPT*K
d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=(220,0,140,220),width=2)
d.ellipse([cx-6,cy-6,cx+6,cy+6],fill=(220,0,140,255))
d.text((cx+8,cy+12),'jib post, reach 4.2 m',fill=(220,0,140,255),font=F(10),anchor='lm')
nx,ny=P(19500,12500)
nt='Compressor: stays in its\nown room (clean air)?\nor here - to decide'
bb=d.multiline_textbbox((nx,ny),nt,font=F(10),anchor='mm'); d.rectangle([bb[0]-4,bb[1]-3,bb[2]+4,bb[3]+3],fill=(255,255,255,235),outline=(200,30,30,255))
d.multiline_text((nx,ny),nt,fill=(200,30,30,255),font=F(10),anchor='mm')
# --- v0.5: F4, offcuts, Vitap on the Unit 31 side ---
rect(12800,3500,15600,5450,(200,120,0),'F4 in-feed\n2.8 m',fill=25,size=9)
rect(15600,4000,19800,4950,(200,120,0),'F4 4200',fill=110,size=11)
rect(19800,3500,22600,5450,(200,120,0),'F4 out-feed\n2.8 m',fill=25,size=9)
rect(12600,6800,15600,8000,(150,100,50),'OFFCUT RACK\n3000 x 1200',fill=90,size=9)
rect(23200,3700,28140,7410,(120,60,170),'',fill=25)
rect(24200,4700,27140,6410,(120,60,170),'VITAP\n2940 x 1710\n(stays ~)',fill=110,size=10)
def arrow2(p,q,col=(20,20,160)):
    import math
    d.line([p,q],fill=col+(230,),width=4); a=math.atan2(q[1]-p[1],q[0]-p[0]); L=14
    d.polygon([q,(q[0]-L*math.cos(a-0.4),q[1]-L*math.sin(a-0.4)),(q[0]-L*math.cos(a+0.4),q[1]-L*math.sin(a+0.4))],fill=col+(230,))
arrow2(P(11000,6000),P(13600,4700)); arrow2(P(20500,4500),P(23900,5300)); arrow2(P(25700,7300),P(27800,11000))
fx,fy=P(19000,2400); d.text((fx,fy),'board flow: rack > F45 > F4 > Vitap > assembly (trolleys / pallets after the saw)',fill=(20,20,160,255),font=F(10),anchor='mm')
# dimension of the bay
bx,by=P(6125,-2200); d.text((bx,by),'Unit 30 bay: 12.25 m along the bottom wall (from plan vectors)',fill=(60,60,60,255),font=F(10),anchor='mm')
d.text((30,30),'NEW LAYOUT - DRAFT v0.5 (Darius, 28/10/2026) - plan scale, +/-10 %, to check on site',fill=(20,20,20,255),font=F(16))
d.text((30,52),'Decided: storage opposite the 2.4 m doors (forklift via roller shutter), extractor along the bottom wall, F45 next to the rack, jib + vacuum lifter. No room for a white floor stack: the lifter picks from the rack.',fill=(60,60,60,255),font=F(11))
Image.alpha_composite(im,ov).convert('RGB').save(out)
