import warnings; warnings.filterwarnings('ignore')
import geopandas as gpd, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from shapely.ops import unary_union
w=gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
land=unary_union(list(w.geometry))
INK='#1f2f5c'; GOLD='#c9a24a'
plt.rcParams['font.family']='Inter'
def base(ext,size,fill='#f3ead2',sea='#dbe7f0'):
    fig,ax=plt.subplots(figsize=size)
    ax.set_facecolor(sea)
    gpd.GeoSeries([land]).plot(ax=ax,color=fill,edgecolor=INK,linewidth=1.4)
    ax.set_xlim(ext[0],ext[1]); ax.set_ylim(ext[2],ext[3]); ax.set_aspect(1.15)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_edgecolor(INK); s.set_linewidth(2)
    return fig,ax
def town(ax,x,y,t,dx=0.25,dy=0.12,ha='left',size=10,bold=False):
    ax.plot(x,y,'o',ms=6,mfc='white',mec=INK,mew=1.8,zorder=5)
    if t: ax.text(x+dx,y+dy,t,fontsize=size,color=INK,ha=ha,fontweight='bold' if bold else 'normal',zorder=6)
def compass(ax,x,y,s=0.6):
    ax.annotate('',xy=(x,y+s),xytext=(x,y-s*0.2),arrowprops=dict(arrowstyle='-|>',color=INK,lw=2))
    ax.text(x,y+s*1.15,'N',ha='center',fontsize=12,fontweight='bold',color=INK)

# 1 Magi route
for kind in ['book','sheet']:
    fill='#f3ead2' if kind=='book' else 'white'; sea='#dbe7f0' if kind=='book' else 'white'
    fig,ax=base((31,51,26,38.5),(7,6.0),fill,sea)
    tig=[(42.7,37.1),(43.1,36.3),(43.6,35.0),(44.3,33.6),(45.4,32.5),(46.6,31.4),(47.5,30.9),(48.0,30.4)]
    eup=[(38.5,36.8),(38.2,35.9),(39.5,35.4),(40.9,34.4),(42.2,33.9),(43.6,33.0),(44.4,32.3),(45.6,31.3),(46.6,31.0),(47.5,30.9)]
    for r in (tig,eup): ax.plot(*zip(*r),color='#5b8db8',lw=1.6)
    ax.text(41.3,35.0,'Euphrates R.',fontsize=8,color='#3d6f99',rotation=-30,style='italic')
    ax.text(44.1,34.6,'Tigris R.',fontsize=8,color='#3d6f99',rotation=-50,style='italic')
    places=[(35.2,31.78,'Jerusalem',-0.2,0.25,'right'),(35.2,31.7,'Bethlehem',-0.2,-0.5,'right'),(36.3,33.5,'Damascus',0.25,0.1,'left'),
            (44.4,32.5,'Babylon',-0.25,-0.5,'right'),(44.6,33.1,'Seleucia–Ctesiphon\n(Parthian capital)',0.3,0.1,'left'),(48.25,32.19,'Susa',0.25,0.0,'left')]
    for x,y,t,dx,dy,ha in places: town(ax,x,y,t,dx,dy,ha,9.5,t in('Jerusalem','Bethlehem'))
    if kind=='book':
        rt=[(44.6,33.1),(42.5,34.6),(40.2,35.6),(38.2,36.1),(37.2,35.0),(36.3,33.5),(35.6,32.6),(35.2,31.78),(35.2,31.7)]
        ax.plot(*zip(*rt),color='#b33a2b',lw=2.6,ls=(0,(5,3)),zorder=4)
    ax.text(47.5,36.4,'PARTHIAN\nEMPIRE',fontsize=13,fontweight='bold',color=INK,ha='center',alpha=.75)
    ax.text(32.2,27.3,'EGYPT',fontsize=11,fontweight='bold',color=INK,alpha=.6,ha='center')
    ax.text(33.0,34.0,'Mediterranean\nSea',fontsize=10,color='#3d6f99',style='italic',ha='center')
    ax.text(34.0,37.6,'ROMAN EMPIRE',fontsize=10,fontweight='bold',color='#8a3326',alpha=.6,ha='center')
    ax.text(42,28.5,'ARABIAN DESERT',fontsize=9,color=INK,alpha=.5,ha='center')
    compass(ax,32.3,29.6,0.6)
    fig.savefig(f'book/img/map_magi_{kind}.png',dpi=220,bbox_inches='tight',pad_inches=0.02); plt.close(fig)

# 2 Escape to Egypt
for kind in ['book','sheet']:
    fill='#f3ead2' if kind=='book' else 'white'; sea='#dbe7f0' if kind=='book' else 'white'
    fig,ax=base((31.0,36.5,29.4,33.3),(6.4,6.6),fill,sea)
    ax.add_patch(Ellipse((35.58,32.82),0.13,0.2,color='#5b8db8',zorder=3))
    ax.add_patch(Ellipse((35.5,31.5),0.17,0.75,color='#5b8db8',zorder=3))
    jr=[(35.6,32.71),(35.57,32.4),(35.55,32.1),(35.53,31.86)]; ax.plot(*zip(*jr),color='#5b8db8',lw=1.6)
    nile=[(31.25,30.05),(31.15,29.5),(31.1,29.0)]; ax.plot(*zip(*nile),color='#5b8db8',lw=2)
    for a in [[(31.25,30.05),(30.95,30.55),(30.7,30.95)],[(31.25,30.05),(31.45,30.55),(31.65,30.95)]]: ax.plot(*zip(*a),color='#5b8db8',lw=1.6)
    pts={'Nazareth':(35.3,32.7),'Jerusalem':(35.23,31.78),'Bethlehem':(35.2,31.7),'Caesarea':(34.9,32.5),'Gaza':(34.45,31.5),'Jericho':(35.45,31.86)}
    for i,(t,(x,y)) in enumerate(pts.items()):
        if kind=='book':
            L={'Nazareth':(-0.08,0.06,'right'),'Jerusalem':(-0.12,0.1,'right'),'Bethlehem':(0.1,-0.17,'left'),'Caesarea':(-0.08,0.04,'right'),'Gaza':(-0.08,-0.1,'right'),'Jericho':(0.1,0.03,'left')}[t]
            town(ax,x,y,t,L[0],L[1],L[2],9.5,t in ('Nazareth','Bethlehem','Jerusalem'))
        else:
            town(ax,x,y,None); ox,oy={'Bethlehem':(-0.08,-0.16),'Jericho':(0.18,0.02)}.get(t,(-0.08,0.04)); ax.text(x+ox,y+oy,str(i+1),fontsize=10,fontweight='bold',color=INK,ha='right' if ox<0 else 'left')
    if kind=='sheet': ax.text(35.72,32.85,'7',fontsize=10,fontweight='bold',color=INK)
    if kind=='book':
        rt=[(35.3,32.7),(35.25,32.2),(35.23,31.78),(35.2,31.7),(34.8,31.3),(34.3,31.0),(33.3,30.8),(32.3,30.65),(31.4,30.35)]
        ax.plot(*zip(*rt),color='#b33a2b',lw=2.6,ls=(0,(5,3)),zorder=4)
        for t,(x,y) in {'GALILEE':(35.0,33.05),'JUDEA':(35.1,31.25),'PEREA':(36.0,32.1),'IDUMEA':(34.9,30.9)}.items():
            ax.text(x,y,t,fontsize=8.5,fontweight='bold',color=INK,alpha=.55,ha='center')
        ax.text(35.7,32.82,'Sea of\nGalilee',fontsize=7,color='#3d6f99',style='italic',ha='left',va='center')
        ax.text(35.7,31.35,'Dead\nSea',fontsize=7.5,color='#3d6f99',style='italic',ha='left')
        ax.text(31.9,29.9,'LAND OF\nEGYPT',fontsize=13,fontweight='bold',color=INK,ha='center',alpha=.75)
        ax.text(31.25,29.55,'Nile R.',fontsize=8,color='#3d6f99',style='italic')
    ax.text(33.0,32.4,'Mediterranean Sea',fontsize=11,color='#3d6f99',style='italic',ha='center')
    ax.text(33.8,30.0,'Sinai\nDesert',fontsize=9,color=INK,alpha=.5,ha='center')
    compass(ax,36.2,29.7,0.3)
    fig.savefig(f'book/img/map_escape_{kind}.png',dpi=220,bbox_inches='tight',pad_inches=0.02); plt.close(fig)

# 3 Africa outline
fig,ax=base((-20,56,-36,40),(6.2,6.6),'white','white')
ax.set_aspect(1.0)
fig.savefig('book/img/map_africa.png',dpi=200,bbox_inches='tight',pad_inches=0.02); plt.close(fig)
print('ok')
