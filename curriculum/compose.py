# bakes Mary/Joseph/donkey onto the journey map (run after maps2.py)
from PIL import Image, ImageChops
B='/tmp/claude-0/-home-user/3a5c4b7d-4602-5541-b0fe-22f390b862a8/scratchpad/book/'
m=Image.open(B+'img/map_journey.png').convert('RGB'); f=Image.open(B+'img/c_journey_fig.png').convert('RGB')
bb=ImageChops.difference(f,Image.new('RGB',f.size,'white')).convert('L').point(lambda v:255 if v>30 else 0).getbbox(); f=f.crop(bb)
w=int(m.width*0.34); f=f.resize((w,int(f.height*w/f.width)),Image.LANCZOS)
x,y=int(m.width*0.27),int(m.height*0.44)
reg=m.crop((x,y,x+f.width,y+f.height)); m.paste(ImageChops.multiply(reg,f),(x,y))
m.quantize(64,dither=Image.NONE).save(B+'imgc/map_journey.png',optimize=True)
