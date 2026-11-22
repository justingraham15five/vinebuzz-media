from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys
SRC='../2026-11-website-chicken-skins-popup/TripleSSnack-MuttJeff-ChickenSkinsFlyer-WebsitePopup_20261120v1.jpg'
F='/usr/share/fonts/truetype/google-fonts/ofl/'
ANTON=F+'anton/Anton-Regular.ttf'; MONT=F+'montserrat/Montserrat[wght].ttf'
CREAM=(242,238,227); BLACK=(0,0,0); WHITE=(255,255,255)
fly=Image.open(SRC).convert('RGB')
def mont(sz,w=800):
    f=ImageFont.truetype(MONT,sz)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
def ctext(d,y,txt,font,fill,W,track=0):
    if track:
        widths=[d.textlength(c,font=font) for c in txt]; tw=sum(widths)+track*(len(txt)-1); x=(W-tw)/2
        for c,w in zip(txt,widths): d.text((x,y),c,font=font,fill=fill); x+=w+track
    else:
        tw=d.textlength(txt,font=font); d.text(((W-tw)/2,y),txt,font=font,fill=fill)
def make(W,H,fh,top,head,kick,bot1,bot2,out,hs,ks,bs):
    im=Image.new('RGB',(W,H),BLACK)
    # subtle vignette texture: cream radial glow behind flyer
    glow=Image.new('L',(W,H),0); gd=ImageDraw.Draw(glow)
    gd.ellipse((W*0.1,H*0.2,W*0.9,H*0.85),fill=60); glow=glow.filter(ImageFilter.GaussianBlur(120))
    im.paste(Image.new('RGB',(W,H),(60,56,48)),(0,0),glow)
    d=ImageDraw.Draw(im)
    # thin cream frame
    m=22; d.rectangle((m,m,W-m,H-m),outline=CREAM,width=3)
    # header
    hf=ImageFont.truetype(ANTON,hs); kf=mont(ks,700); b1=mont(bs,800); b2=mont(int(bs*0.82),600)
    hb=d.textbbox((0,0),head,font=hf); kb=d.textbbox((0,0),kick,font=kf)
    total=(kb[3])+18+(hb[3])+34+fh+12+34+bs+14+int(bs*0.82)+8
    y=(H-total)//2
    ctext(d,y,kick,kf,CREAM,W,track=6); y+=kb[3]+18
    ctext(d,y,head,hf,WHITE,W); y+=hb[3]+34
    # flyer, uniform scale
    fw=int(fly.width*fh/fly.height); f=fly.resize((fw,fh),Image.LANCZOS)
    x=(W-fw)//2
    sh=Image.new('L',(W,H),0); ImageDraw.Draw(sh).rectangle((x+10,y+18,x+fw+10,y+fh+18),fill=170)
    sh=sh.filter(ImageFilter.GaussianBlur(18)); im.paste(BLACK,(0,0),sh)
    d=ImageDraw.Draw(im)
    b=6; d.rectangle((x-b,y-b,x+fw+b-1,y+fh+b-1),fill=CREAM)
    im.paste(f,(x,y)); y+=fh+b+34
    ctext(d,y,bot1,b1,CREAM,W); y+=bs+14
    ctext(d,y,bot2,b2,WHITE,W)
    im.save(out,optimize=True); print(out,im.size)
D='20261122v1'
make(1080,1350,880,62,'CHICKEN SKINS ARE HERE','NEW FROM MUTT & JEFF',"Now at local convenience stores & Jet Stores","Triple S Snacks · triplessnacks.com",f'TripleSSnack-MuttJeff-ChickenSkinsFlyer-FacebookPost_{D}.png',96,26,30)
make(1080,1350,880,62,'CHICKEN SKINS ARE HERE','NEW FROM MUTT & JEFF',"Now at local convenience stores & Jet Stores","Triple S Snacks · triplessnacks.com",f'TripleSSnack-MuttJeff-ChickenSkinsFlyer-InstagramPost_{D}.png',96,26,30)
make(1200,1200,800,52,'CHICKEN SKINS ARE HERE','NEW FROM MUTT & JEFF',"Now at local convenience stores & Jet Stores","Triple S Snacks · triplessnacks.com",f'TripleSSnack-MuttJeff-ChickenSkinsFlyer-LinkedInPost_{D}.png',80,24,28)
make(1080,1920,980,230,'CHICKEN SKINS ARE HERE','NEW FROM MUTT & JEFF',"Now at local convenience stores & Jet Stores","Triple S Snacks · triplessnacks.com",f'TripleSSnack-MuttJeff-ChickenSkinsFlyer-Story-FacebookInstagram_{D}.png',100,28,34)
