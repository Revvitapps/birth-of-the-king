import sys
from PIL import Image
d=sys.argv[1]; out=sys.argv[2]; ns=[int(x) for x in sys.argv[3:]]
ims=[Image.open(f'{d}/p{n:03d}.png').convert('RGB') for n in ns]
w,h=ims[0].size; cols=min(4,len(ims)); rows=(len(ims)+cols-1)//cols
c=Image.new('RGB',(w*cols,h*rows),'white')
for i,im in enumerate(ims): c.paste(im,((i%cols)*w,(i//cols)*h))
c.save(out)
