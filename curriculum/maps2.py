import warnings; warnings.filterwarnings('ignore')
import geopandas as gpd, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from shapely.geometry import box
NE = '/tmp/claude-0/-home-user/3a5c4b7d-4602-5541-b0fe-22f390b862a8/scratchpad/ne/'
OUT = '/tmp/claude-0/-home-user/3a5c4b7d-4602-5541-b0fe-22f390b862a8/scratchpad/book/img/'
land10 = gpd.read_file(NE + 'ne_10m_land.geojson')
land50 = gpd.read_file(NE + 'ne_50m_land.geojson')
lakes = gpd.read_file(NE + 'ne_10m_lakes.geojson')
rivers = gpd.read_file(NE + 'ne_10m_rivers_lake_centerlines.geojson')
INK = '#1f2f5c'; WATER = '#5b8db8'; WTXT = '#3d6f99'
plt.rcParams['font.family'] = 'Inter'

def clip(g, ext):
    b = box(ext[0] - 1, ext[2] - 1, ext[1] + 1, ext[3] + 1)
    return g[g.intersects(b)].clip(b)

def base(ext, size, land, fill, sea, lake_names=(), river_names=(), lw=1.4, rlw=1.6, aspect=1.18):
    fig, ax = plt.subplots(figsize=size)
    ax.set_facecolor(sea)
    clip(land, ext).plot(ax=ax, color=fill, edgecolor=INK, linewidth=lw, zorder=1)
    if lake_names:
        lk = lakes[lakes['name'].isin(lake_names)]
        clip(lk, ext).plot(ax=ax, color=sea if sea != 'white' else 'white', edgecolor=INK if sea == 'white' else WATER, linewidth=lw * 0.8, zorder=2)
    if river_names:
        rv = rivers[rivers['name'].isin(river_names)]
        clip(rv, ext).plot(ax=ax, color=(INK if sea == 'white' else WATER), linewidth=rlw, zorder=2)
    ax.set_xlim(ext[0], ext[1]); ax.set_ylim(ext[2], ext[3]); ax.set_aspect(aspect)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_edgecolor(INK); s.set_linewidth(2)
    return fig, ax

def town(ax, x, y, t, dx=0.25, dy=0.12, ha='left', size=10, bold=False, ms=6):
    ax.plot(x, y, 'o', ms=ms, mfc='white', mec=INK, mew=1.8, zorder=5)
    if t: ax.text(x + dx, y + dy, t, fontsize=size, color=INK, ha=ha, fontweight='bold' if bold else 'normal', zorder=6)

def compass(ax, x, y, s=0.6, r=0.085, fc=None):
    """full compass rose (N, E, S, W) centred near data point (x, y); r = radius as a fraction of the axes width"""
    import numpy as np
    from matplotlib.patches import Polygon, Circle
    fx, fy = ax.transAxes.inverted().transform(ax.transData.transform((x, y)))
    bb = ax.get_window_extent(); ry = r * bb.width / bb.height
    fx = min(max(fx, r * 1.65), 1 - r * 1.65); fy = min(max(fy, ry * 1.65), 1 - ry * 1.65)
    ia = ax.inset_axes([fx - r * 1.5, fy - ry * 1.5, r * 3, ry * 3], zorder=20)
    ia.set_xlim(-1.5, 1.5); ia.set_ylim(-1.5, 1.5); ia.set_aspect('equal'); ia.axis('off'); ia.patch.set_alpha(0)
    ia.add_patch(Circle((0, 0), 0.62, fc='none', ec=INK, lw=1.0))
    ia.add_patch(Circle((0, 0), 0.52, fc='none', ec=INK, lw=0.5))
    for k in range(4):                       # short diagonal points
        t = np.pi / 4 + k * np.pi / 2
        tip = (0.62 * np.cos(t), 0.62 * np.sin(t)); l = (0.16 * np.cos(t + np.pi / 2), 0.16 * np.sin(t + np.pi / 2))
        ia.add_patch(Polygon([tip, l, (-l[0], -l[1])], closed=True, fc='white', ec=INK, lw=0.8))
    for k in range(4):                       # long N E S W points, half dark, half light
        t = np.pi / 2 - k * np.pi / 2
        tip = (np.cos(t), np.sin(t)); l = (0.2 * np.cos(t + np.pi / 4 + np.pi / 2), 0.2 * np.sin(t + np.pi / 4 + np.pi / 2))
        a_ = (0.2 * np.cos(t + np.pi / 4), 0.2 * np.sin(t + np.pi / 4)); b_ = (0.2 * np.cos(t - np.pi / 4), 0.2 * np.sin(t - np.pi / 4))
        ia.add_patch(Polygon([tip, a_, (0, 0)], closed=True, fc=INK, ec=INK, lw=0.8))
        ia.add_patch(Polygon([tip, b_, (0, 0)], closed=True, fc='white', ec=INK, lw=0.8))
    for t_, (lx, ly) in {'N': (0, 1.27), 'E': (1.27, 0), 'S': (0, -1.27), 'W': (-1.27, 0)}.items():
        ia.text(lx, ly, t_, ha='center', va='center', fontsize=10 if t_ == 'N' else 8, fontweight='bold', color=INK)

def save(fig, name, dpi=220):
    fig.savefig(OUT + name + '.png', dpi=dpi, bbox_inches='tight', pad_inches=0.02); plt.close(fig)

# 1 Magi route (book, colored)
ext = (31, 51, 26, 38.5)
fig, ax = base(ext, (7, 6.0), land50, '#f3ead2', '#dbe7f0', ('Dead Sea', 'Sea of Galilee'), ('Tigris', 'Euphrates', 'Dicle', 'Firat', 'Al Furat', 'Shatt al Arab', 'Jordan', 'Nile', 'Damietta Branch', 'Rosetta Branch'))
ax.text(39.6, 35.1, 'Euphrates R.', fontsize=8, color=WTXT, rotation=-28, style='italic')
ax.text(43.5, 35.2, 'Tigris R.', fontsize=8, color=WTXT, rotation=-55, style='italic')
places = [(35.23, 31.78, 'Jerusalem', -0.2, 0.25, 'right'), (35.2, 31.7, 'Bethlehem', -0.2, -0.5, 'right'), (36.3, 33.5, 'Damascus', 0.25, 0.1, 'left'),
          (44.42, 32.54, 'Babylon', -0.25, -0.5, 'right'), (44.58, 33.09, 'Seleucia–Ctesiphon\n(Parthian capital)', 0.3, 0.1, 'left'), (48.25, 32.19, 'Susa', 0.25, 0.0, 'left')]
for x, y, t, dx, dy, ha in places: town(ax, x, y, t, dx, dy, ha, 9.5, t in ('Jerusalem', 'Bethlehem'))
rt = [(44.58, 33.09), (42.5, 34.6), (40.2, 35.6), (38.2, 36.1), (37.2, 35.0), (36.3, 33.5), (35.6, 32.6), (35.23, 31.78), (35.2, 31.7)]
ax.plot(*zip(*rt), color='#b33a2b', lw=2.6, ls=(0, (5, 3)), zorder=4)
ax.text(47.5, 36.4, 'PARTHIAN\nEMPIRE', fontsize=13, fontweight='bold', color=INK, ha='center', alpha=.75)
ax.text(32.2, 27.3, 'EGYPT', fontsize=11, fontweight='bold', color=INK, alpha=.6, ha='center')
ax.text(33.0, 34.0, 'Mediterranean\nSea', fontsize=10, color=WTXT, style='italic', ha='center')
ax.text(34.0, 37.6, 'ROMAN EMPIRE', fontsize=10, fontweight='bold', color='#8a3326', alpha=.6, ha='center')
ax.text(42, 28.5, 'ARABIAN DESERT', fontsize=9, color=INK, alpha=.5, ha='center')
ax.text(49.6, 28.9, 'Persian\nGulf', fontsize=9, color=WTXT, style='italic', ha='center')
compass(ax, 32.6, 29.9, r=0.07)
save(fig, 'map_magi_book')

# 1b Magi route wide (book, colored)
ext = (30.5, 51.5, 28.6, 37.6)
fig, ax = base(ext, (8.4, 3.6), land50, '#f3ead2', '#dbe7f0', ('Dead Sea', 'Sea of Galilee'), ('Tigris', 'Euphrates', 'Dicle', 'Firat', 'Al Furat', 'Shatt al Arab', 'Jordan', 'Nile', 'Damietta Branch', 'Rosetta Branch'))
ax.text(39.6, 35.1, 'Euphrates R.', fontsize=8, color=WTXT, rotation=-28, style='italic')
ax.text(43.5, 35.2, 'Tigris R.', fontsize=8, color=WTXT, rotation=-55, style='italic')
places = [(35.23, 31.78, 'Jerusalem', -0.2, 0.25, 'right'), (35.2, 31.7, 'Bethlehem', -0.2, -0.5, 'right'), (36.3, 33.5, 'Damascus', 0.25, 0.1, 'left'),
          (44.42, 32.54, 'Babylon', -0.25, -0.5, 'right'), (44.58, 33.09, 'Seleucia–Ctesiphon\n(Parthian capital)', 0.3, 0.1, 'left'), (48.25, 32.19, 'Susa', 0.25, 0.0, 'left')]
for x, y, t, dx, dy, ha in places: town(ax, x, y, t, dx, dy, ha, 9.5, t in ('Jerusalem', 'Bethlehem'))
rt = [(44.58, 33.09), (42.5, 34.6), (40.2, 35.6), (38.2, 36.1), (37.2, 35.0), (36.3, 33.5), (35.6, 32.6), (35.23, 31.78), (35.2, 31.7)]
ax.plot(*zip(*rt), color='#b33a2b', lw=2.6, ls=(0, (5, 3)), zorder=4)
ax.text(47.0, 35.9, 'PARTHIAN\nEMPIRE', fontsize=13, fontweight='bold', color=INK, ha='center', alpha=.75)
ax.text(31.8, 29.2, 'EGYPT', fontsize=11, fontweight='bold', color=INK, alpha=.6, ha='center')
ax.text(33.0, 34.0, 'Mediterranean\nSea', fontsize=10, color=WTXT, style='italic', ha='center')
ax.text(34.5, 36.9, 'ROMAN EMPIRE', fontsize=10, fontweight='bold', color='#8a3326', alpha=.6, ha='center')
ax.text(41, 30.0, 'ARABIAN DESERT', fontsize=9, color=INK, alpha=.5, ha='center')
ax.text(50.0, 29.3, 'Persian\nGulf', fontsize=9, color=WTXT, style='italic', ha='center')
compass(ax, 45.7, 30.0, r=0.05)
save(fig, 'map_magi_wide')

# 2 Escape to Egypt: book (answer map, colored) and sheet (coloring, numbered dots to label and connect)
ext = (30.0, 36.7, 29.0, 33.5)
LK = ('Sea of Galilee', 'Dead Sea'); RV = ('Jordan', 'Nile', 'Damietta Branch', 'Rosetta Branch')
stops = [('Bethlehem', 35.20, 31.70), ('Gaza', 34.46, 31.50), ('Egypt', 31.25, 30.10), ('Joppa', 34.75, 32.05), ('Caesarea', 34.89, 32.50), ('Nazareth', 35.30, 32.70)]
out_rt = [(35.20, 31.70), (34.85, 31.62), (34.46, 31.50), (34.2, 31.2), (33.3, 31.05), (32.4, 30.95), (31.6, 30.6), (31.25, 30.10)]
back_rt = [(31.25, 30.10), (31.7, 30.75), (32.5, 31.08), (33.4, 31.15), (34.3, 31.35), (34.46, 31.50), (34.62, 31.8), (34.75, 32.05), (34.89, 32.50), (35.05, 32.62), (35.30, 32.70)]
for kind in ['book', 'sheet']:
    if kind == 'book':
        fig, ax = base(ext, (6.4, 6.6), land10, '#f3ead2', '#dbe7f0', LK, RV)
        L = {'Bethlehem': (0.14, -0.26, 'left'), 'Gaza': (-0.14, 0.1, 'right'), 'Egypt': (0.15, -0.05, 'left'), 'Joppa': (-0.12, -0.02, 'right'), 'Caesarea': (-0.12, 0.0, 'right'), 'Nazareth': (0.17, 0.1, 'left')}
        for i, (t, x, y) in enumerate(stops): town(ax, x, y, f'{i+1} {t}', L[t][0], L[t][1], L[t][2], 9.5, True)
        town(ax, 35.23, 31.78, 'Jerusalem', 0.1, 0.14, 'left', 8.5)
        ax.plot(*zip(*out_rt), color='#b33a2b', lw=2.6, ls=(0, (5, 3)), zorder=4)
        ax.plot(*zip(*back_rt), color='#2b5fa8', lw=2.2, ls=(0, (2, 2)), zorder=4)
        ax.plot([30.25, 30.75], [33.2, 33.2], color='#b33a2b', lw=2.6, ls=(0, (5, 3))); ax.text(30.85, 33.2, 'Escape to Egypt (1 → 2 → 3)', fontsize=8.5, color=INK, va='center')
        ax.plot([30.25, 30.75], [32.95, 32.95], color='#2b5fa8', lw=2.2, ls=(0, (2, 2))); ax.text(30.85, 32.95, 'Trip home (3 → 2 → 4 → 5 → 6)', fontsize=8.5, color=INK, va='center')
        for t, (x, y) in {'JUDEA': (35.0, 31.05), 'GALILEE': (35.75, 33.15), 'IDUMEA': (35.0, 30.6)}.items():
            ax.text(x, y, t, fontsize=8.5, fontweight='bold', color=INK, alpha=.55, ha='center')
        ax.text(35.66, 30.98, 'Dead\nSea', fontsize=7.5, color=WTXT, style='italic', ha='left')
        ax.text(31.9, 29.5, 'LAND OF\nEGYPT', fontsize=11, fontweight='bold', color=INK, ha='center', alpha=.75)
        ax.text(31.35, 29.1, 'Nile R.', fontsize=8, color=WTXT, style='italic')
        ax.text(33.6, 29.9, 'Sinai\nDesert', fontsize=9, color=INK, alpha=.5, ha='center')
        ax.text(32.6, 32.3, 'Mediterranean Sea', fontsize=11, color=WTXT, style='italic', ha='center')
        compass(ax, 36.05, 29.62, r=0.085)
        save(fig, 'map_escape_book')
    else:
        fig, ax = base(ext, (6.4, 6.6), land10, 'white', 'white', LK, RV, lw=1.6, rlw=1.4)
        # (number offset, writing line start, end, y) per stop
        W = {'Bethlehem': (33.95, 35.08, 31.74), 'Gaza': (33.2, 34.33, 31.44), 'Egypt': (31.62, 32.75, 30.04),
             'Joppa': (33.5, 34.63, 32.02), 'Caesarea': (33.64, 34.77, 32.45), 'Nazareth': (34.05, 35.18, 32.76)}
        for i, (t, x, y) in enumerate(stops):
            ax.plot(x, y, 'o', ms=8, mfc=INK, mec=INK, zorder=5)
            x0, x1, ly = W[t]
            ax.text(x0 - 0.07, ly + 0.02, str(i + 1), fontsize=12, fontweight='bold', color=INK, ha='right', va='center', zorder=6)
            ax.plot([x0, x1], [ly, ly], color=INK, lw=1.1, zorder=6)
        ax.text(32.3, 32.75, 'Mediterranean Sea', fontsize=11, color=INK, style='italic', ha='center', alpha=.6)
        ax.text(33.6, 29.9, 'Sinai Desert', fontsize=9, color=INK, alpha=.5, ha='center')
        ax.text(31.0, 29.35, 'Nile River', fontsize=8, color=INK, alpha=.6, style='italic')
        compass(ax, 36.05, 29.62, r=0.085)
        save(fig, 'map_escape_sheet')

# 3 Journey: Nazareth to Bethlehem (coloring)
ext = (34.55, 36.05, 31.35, 33.0)
fig, ax = base(ext, (5.6, 6.2), land10, 'white', 'white', LK, ('Jordan',), lw=1.6, rlw=1.6)
road = [(35.30, 32.70), (35.42, 32.62), (35.52, 32.45), (35.55, 32.2), (35.53, 32.0), (35.44, 31.86), (35.33, 31.81), (35.23, 31.78), (35.20, 31.70)]
ax.plot(*zip(*road), color=INK, lw=3.4, ls=(0, (0.1, 2.6)), dash_capstyle='round', zorder=4)
J = {'Nazareth': (35.30, 32.70, -0.06, 0.05, 'right'), 'Jericho': (35.44, 31.86, 0.06, 0.02, 'left'), 'Jerusalem': (35.23, 31.78, -0.06, 0.03, 'right'), 'Bethlehem': (35.20, 31.70, -0.06, -0.01, 'right')}
for t, (x, y, dx, dy, ha) in J.items(): town(ax, x, y, t, dx, dy, ha, 11, t in ('Nazareth', 'Bethlehem'), ms=8)
ax.text(35.66, 32.85, 'Sea of\nGalilee', fontsize=8.5, color=INK, style='italic', ha='left', va='center', alpha=.8)
ax.text(35.62, 31.43, 'Dead\nSea', fontsize=8.5, color=INK, style='italic', ha='left', alpha=.8)
ax.text(35.63, 32.3, 'Jordan\nRiver', fontsize=8.5, color=INK, style='italic', ha='left', alpha=.8)
ax.text(34.74, 32.78, 'Mediterranean\nSea', fontsize=8, color=INK, style='italic', ha='center', alpha=.6)
ax.text(35.3, 32.93, 'GALILEE', fontsize=9, fontweight='bold', color=INK, alpha=.5, ha='center')
ax.text(34.95, 31.48, 'JUDEA', fontsize=9, fontweight='bold', color=INK, alpha=.5, ha='center')
ax.text(35.42, 32.72, '★ START', fontsize=9, fontweight='bold', color=INK, ha='center')
ax.text(35.20, 31.64, 'FINISH ★', fontsize=9, fontweight='bold', color=INK, ha='center')
compass(ax, 35.86, 31.56, r=0.085)
save(fig, 'map_journey')

# 4 Bethlehem area: Migdal Eder (book): painted bird's-eye base (Magica) with our own labels and compass rose
import matplotlib.image as mpimg, matplotlib.patheffects as pe
img = mpimg.imread('/tmp/claude-0/-home-user/3a5c4b7d-4602-5541-b0fe-22f390b862a8/scratchpad/dl/bmapB.png')
H_, W_ = img.shape[:2]
fig, ax = plt.subplots(figsize=(7.68, 5.12))
ax.imshow(img, extent=(0, 1, 0, 1), aspect=H_ / W_)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([])
for s_ in ax.spines.values(): s_.set_edgecolor(INK); s_.set_linewidth(2)
halo = [pe.withStroke(linewidth=3.2, foreground='white', alpha=.92)]
def lab(x, y, t, size=11, bold=True, ha='center', color=INK, style='normal'):
    ax.text(x, y, t, fontsize=size, fontweight='bold' if bold else 'normal', color=color, ha=ha, va='center', style=style, path_effects=halo, zorder=9, linespacing=1.05)
lab(0.66, 0.945, 'Jerusalem', 19)
lab(0.84, 0.865, 'Temple', 12, False, style='italic')
lab(0.245, 0.49, 'Bethlehem', 19)
lab(0.61, 0.585, 'Migdal Eder\n(Tower of the Flock)', 13.5)
lab(0.60, 0.30, 'shepherds’ fields', 12, False, color='#33501a', style='italic')
lab(0.82, 0.47, 'Herodium', 14.5)
lab(0.17, 0.27, 'road to Hebron', 11, False, color='#5a4a2a', style='italic')
lab(0.40, 0.77, 'road to Jerusalem', 11, False, color='#5a4a2a', style='italic')
lab(0.92, 0.63, 'Judean\nwilderness', 11.5, False, color='#6b5a3a', style='italic')
compass(ax, 0.90, 0.27, r=0.065)
fig.savefig(OUT + 'map_bethlehem.png', dpi=200, bbox_inches='tight', pad_inches=0.02); plt.close(fig)

# 5 Africa (larger)
fig, ax = base((-20, 56, -36, 40), (6.2, 6.4), land50, 'white', 'white', lw=1.2, aspect=1.0)
save(fig, 'map_africa', dpi=200)
print('maps ok')
