import random
F = 'Birth of the King · Lesson 2'

# ---------- maze: shepherds to Bethlehem ----------
def _maze(cols=11, rows=14, cell=38, seed=11):
    rnd = random.Random(seed)
    walls = {(c, r): {'N', 'S', 'E', 'W'} for c in range(cols) for r in range(rows)}
    seen = {(0, 0)}; stack = [(0, 0)]
    D = {'N': (0, -1, 'S'), 'S': (0, 1, 'N'), 'E': (1, 0, 'W'), 'W': (-1, 0, 'E')}
    while stack:
        c, r = stack[-1]
        nb = [(d, c + dx, r + dy, o) for d, (dx, dy, o) in D.items() if (c + dx, r + dy) in walls and (c + dx, r + dy) not in seen]
        if not nb: stack.pop(); continue
        d, nc, nr, o = rnd.choice(nb)
        walls[(c, r)].discard(d); walls[(nc, nr)].discard(o); seen.add((nc, nr)); stack.append((nc, nr))
    walls[(0, 0)].discard('W'); walls[(cols - 1, rows - 1)].discard('E')
    ox, oy = 150, 10
    seg = []
    for (c, r), w in walls.items():
        x, y = ox + c * cell, oy + r * cell
        if 'N' in w: seg.append(f'M{x} {y}h{cell}')
        if 'W' in w: seg.append(f'M{x} {y}v{cell}')
        if r == rows - 1 and 'S' in w: seg.append(f'M{x} {y+cell}h{cell}')
        if c == cols - 1 and 'E' in w: seg.append(f'M{x+cell} {y}v{cell}')
    W = ox + cols * cell + 122; H = oy * 2 + rows * cell
    g = f'<path d="{" ".join(seg)}" stroke="#1f2f5c" stroke-width="3.2" stroke-linecap="round" fill="none"/>'
    # start: the shepherds
    g += f'<image href="imgc/sk_shepherds.png" x="2" y="{oy-4}" width="142" height="142"/><text x="72" y="{oy+150}" text-anchor="middle" font-family="Inter" font-weight="800" font-size="10" fill="#1f2f5c">START</text>'
    g += ''
    # finish: a wooden sign that says Bethlehem
    ex, ey = ox + cols * cell, oy + (rows - 1) * cell
    sx, sy = ex + 10, ey - 22
    g += f'<path d="M{ex+2} {ey+cell*0.5} h6" stroke="#c9a24a" stroke-width="3" fill="none"/>'
    g += f'<rect x="{sx+47}" y="{sy+30}" width="8" height="62" fill="#d9c08a" stroke="#1f2f5c" stroke-width="2"/>'
    g += f'<path d="M{sx+4} {sy} h88 l12 16 l-12 16 h-88 z" fill="#f4e3b5" stroke="#1f2f5c" stroke-width="2.4" stroke-linejoin="round"/>'
    g += f'<text x="{sx+50}" y="{sy+20.5}" text-anchor="middle" font-family="Inter" font-weight="900" font-size="11.5" fill="#1f2f5c">BETHLEHEM</text>'
    g += f'<text x="{sx+52}" y="{sy-10}" text-anchor="middle" font-size="24" fill="#c9a24a">★</text>'
    g += f'<path d="M{sx+30} {sy+92} q21 -8 42 0" stroke="#1f2f5c" stroke-width="1.6" fill="none"/>'
    return f'<svg viewBox="0 0 {W} {H}" style="width:100%;display:block">{g}</svg>'

CUTS = '<div class="scissors"><b>✂</b> Color, cut on the dashed lines, and glue into the picture</div><div class="cuts">' + ''.join(
    f'<div><img src="imgc/{n}.png"></div>' for n in ['cut_mary', 'cut_joseph', 'cut_baby', 'cut_sheep', 'cut_lamb']) + '</div>'

PAGES = [
dict(t='opener', id='l2', img='l2_open', num=2, title='A King Is Born', ref='Luke 2:1–20 · Micah 4:8 · Micah 5:2'),
dict(t='plan', num=2, title='A King Is Born', bignum='2',
 passages='Luke 2:1–20; Micah 4:8; Micah 5:2; Genesis 35:19–21; John 1:29',
 objectives=['Where Yeshua was born, and why Bethlehem mattered', 'What Migdal Eder, the Tower of the Flock, was, and why it may have been the place of His birth',
             'How the shepherds learned of the Messiah’s birth', 'Why the swaddling cloths and manger were a special sign'],
 prayer='Lord, thank You for sending Yeshua, the Lamb of God, to be our Savior. Help us listen like the shepherds did, and share the good news with joy. In Yeshua’s name, amen.',
 materials='Bibles, pencils, crayons, scissors, glue, a map of Israel (optional), and copies of the Lesson 2 printable pages.',
 overview='Mary traveled with Joseph to Bethlehem, the hometown of King David. The town was crowded, and there was no room in the guest room. Right at the edge of Bethlehem stood Migdal Eder, the Tower of the Flock, where special shepherds cared for the lambs raised for temple sacrifices. Yeshua was born and laid in a manger, wrapped in swaddling cloths. That same night an angel appeared to the shepherds with the good news: “The Messiah is born!” The shepherds knew exactly what the sign meant. They hurried to see the baby, just as the angel said, and praised God for their newborn Savior.',
 dyk='Many Bible teachers believe Yeshua was born at a fall Appointed Time, possibly near the Day of Trumpets (Rosh Hashanah). In Israel, trumpets were blown when kings were announced!',
 flow=[('Read:', 'Migdal Eder: The Tower of the Flock'), ('Read:', 'The Shepherds of the Temple Flocks'),
       ('Activity:', 'Lay Him in the Manger (Cut and Paste) · The Tower of the Flock'),
       ('Read:', 'Heaven’s Army and the Shepherds · The Shepherds Come to See'), ('Activity:', 'Shepherds’ Maze'),
       ('Read:', 'When Was Yeshua Born?'), ('Activity:', 'Let’s See What You Remember · Birth of the King')]),

dict(t='illus', img='l2_tower', cap='Migdal Eder, the Tower of the Flock'),
dict(t='text', id='l2a', kicker='Lesson Two · Reading 1', title='Migdal Eder: The Tower of the Flock', bignum='2', foot=F,
 verse='And thou, O tower of the flock, the strong hold of the daughter of Zion, unto thee shall it come, even the first dominion', vref='Micah 4:8',
 read='Genesis 35:19–21 · Micah 4:8 · Micah 5:2 · Luke 2:8–12',
 paras=["Right at the edge of Bethlehem, in the fields just outside the town, stood a stone watchtower called **Migdal Eder**. In Hebrew, *Migdal Eder* means “Tower of the Flock.” It was so close to Bethlehem that the shepherds who worked there could walk into town in a few minutes.",
  "## Where Rachel Was Buried",
  "The Tower of the Flock first appears in the story of Jacob. When Jacob’s wife Rachel died, she “was buried in the way to Ephrath, which is Bethlehem,” and Jacob set up a pillar on her grave (Genesis 35:19–20). The very next verse says Jacob “spread his tent beyond the tower of Edar” (Genesis 35:21). *Edar* is the same Hebrew word as *Eder*. So from Israel’s earliest days, the Tower of the Flock stood right beside Bethlehem.",
  "## A Prophecy the Shepherds Knew",
  "Hundreds of years later, the prophet Micah spoke to the Tower of the Flock: “Unto thee shall it come, even the first dominion” (Micah 4:8). A few verses later he announced that the Ruler of Israel would come from Bethlehem (Micah 5:2). The shepherds of Migdal Eder knew these prophecies about their own tower. So when the angel spoke, they knew exactly where to look for the Messiah: right there in Bethlehem, near the Tower of the Flock.",
  "## Shepherd Language",
  "The angel said, “Ye shall find the babe wrapped in swaddling clothes, lying in a manger” (Luke 2:12). That was shepherd language! These were the very words these shepherds used every lambing season. God gave them a sign that only shepherds like them would fully understand.",
  "## What Was the Tower Like?",
  "Watchtowers like this were usually two stories tall. From the top, shepherds watched for wolves and thieves. The lower level was a sheltered place where ewes gave birth to their lambs."],
 notes=[('Ancient sources', 'The Mishnah (Shekalim 7:4) describes animals found in the area near Jerusalem as fit for temple offerings. The Targum on Genesis 35:21 calls Migdal Eder the place where “King Messiah will be revealed in the end of days.”'),
        ('Map it', 'Migdal Eder was a shepherding site at the edge of Bethlehem, not a separate town. See the small map in Reading 3.'),
        ('Ask', 'Why would God reveal His Son first to shepherds in a field full of lambs?')],
 callout=('Did You Know?', 'Today the fields just east of Bethlehem, near the town of Beit Sahour, are still called “Shepherds’ Field.” Archaeologists have found ancient caves and tower ruins there.')),

dict(t='illus', img='l2_lamb', cap='Wrapping a newborn temple lamb'),
dict(t='text', id='l2b', kicker='Lesson Two · Reading 2', title='The Shepherds of the Temple Flocks', bignum='2', foot=F,
 verse='She brought forth her firstborn son, and wrapped him in swaddling clothes, and laid him in a manger; because there was no room for them in the inn', vref='Luke 2:7',
 read='Luke 2:6–12 · John 1:29 · Luke 22:11–12',
 paras=["The shepherds near Bethlehem were not ordinary shepherds. Many Bible teachers believe they were specially trained shepherds who raised lambs for the temple in Jerusalem, especially the Passover lambs. These lambs had to be *without blemish*: perfect, with no cuts, broken bones, or spots.",
  "## Caring for a Newborn Lamb",
  "When a ewe was ready to give birth, the shepherds brought her into the lower room of the tower. As soon as a lamb was born, they wrapped it snugly in strips of cloth, **swaddling cloths**, so it would not hurt itself. Then they laid it in a stone **manger** to keep it calm, safe, and spotless until it could be checked.",
  "## “No Room in the Inn”",
  "The Greek word translated “inn” in Luke 2:7 is *kataluma*. It means a **guest room**. Luke uses the same word for the upper room of the Last Supper (Luke 22:11). For a real roadside inn he used a different word, *pandocheion* (Luke 10:34). So there was no room in the crowded guest room in Bethlehem.",
  "Where could a young mother go? Just at the edge of town stood a clean, sheltered birthing room made for spotless lambs, with a stone manger and swaddling cloths close at hand. This is one more reason many believe the lower room of Migdal Eder could be the place where Yeshua was born.",
  "## The Lamb of God",
  "Years later, John the Baptist saw Yeshua and cried out, “Behold the Lamb of God, which taketh away the sin of the world” (John 1:29). From His very first night, Yeshua’s mission was pointing to the cross."],
 notes=[('Word study', '*Kataluma:* guest room (Luke 2:7; 22:11).\n*Pandocheion:* roadside inn (Luke 10:34).'),
        ('Swaddling', 'Swaddling cloths picture purity and protection, the same care given to temple lambs. The manger pictures humility.'),
        ('Passover link', 'Read Exodus 12:5 and 1 Peter 1:19 together: “a lamb without blemish and without spot.”')],
 callout=('Did You Know?', 'Many mangers in Israel were carved from stone, not built of wood. Some ancient stone mangers can still be seen today.')),

dict(t='work', lesson=2, title='Lay Him in the Manger', kick='Cut and Paste', ins='Color the hay in the stone manger yellow. Then color the figures at the bottom of the page, cut them out, and glue them into the picture. Who goes in the manger?',
 blocks=[('img', 'c_manger_scene', 4.55), ('html', CUTS)]),
dict(t='work', lesson=2, title='The Tower of the Flock', sk='c_tower', skh=1.25, ins='Read “Migdal Eder” and “The Shepherds of the Temple Flocks,” then answer the questions.',
 blocks=[('qs', [('What does *Migdal Eder* mean in English?', 1), ('Which prophet spoke to the “tower of the flock”?', 1),
                 ('Where was Migdal Eder located?', 1), ('What were the lambs near Bethlehem raised for?', 1),
                 ('What did the shepherds wrap newborn lambs in? Where did they lay them?', 1),
                 ('Why was the angel’s sign so special to the shepherds?', 2),
                 ('Luke 2:7 says there was no room in the *kataluma*. What does *kataluma* mean?', 1),
                 ('Why might the lower room of Migdal Eder have been the place where Yeshua was born?', 2),
                 ('What did John the Baptist call Yeshua? (John 1:29)', 1)])]),

dict(t='illus', img='l2_angels', cap='“A multitude of the heavenly host”'),
dict(t='text', id='l2c', kicker='Lesson Two · Reading 3', title='Heaven’s Army and the Shepherds', bignum='2', foot=F,
 verse='And suddenly there was with the angel a multitude of the heavenly host praising God, and saying, Glory to God in the highest, and on earth peace, good will toward men', vref='Luke 2:13–14',
 read='Luke 2:8–20 · 1 Timothy 3:16',
 paras=["The night was quiet in the fields near the Tower of the Flock. Suddenly an angel of the Lord stood before the shepherds, and God’s glory shone all around them. They were terrified! But the angel said, “Fear not: for, behold, I bring you good tidings of great joy, which shall be to all people. For unto you is born this day in the city of David a Saviour, which is Christ the Lord.”",
  "## The Heavenly Army",
  "Then the sky filled with a *multitude of the heavenly host*. The word **host** means an army. Heaven’s army had come to honor their Commander, who had just entered the world as a baby! Together they were praising God with one voice: “Glory to God in the highest, and on earth peace, good will toward men.”",
  "## Angels Are God’s Messengers",
  "The word *angel* means “messenger.” In the Bible, angels deliver exactly the words God gives them. An angel announced John’s birth to Zechariah (Luke 1:11–17). Gabriel announced Yeshua’s birth to Mary (Luke 1:26–33). An angel announced His birth to the shepherds (Luke 2:9–14). And angels announced His resurrection at the empty tomb (Matthew 28:5–7).",
  "Paul wrote that God was “manifest in the flesh … seen of angels” (1 Timothy 3:16). The angels who worship God in heaven now saw His glory in the face of a newborn baby."],
 notes=[('Look closely', 'Luke says the angels were “praising God, and saying, Glory to God in the highest, and on earth peace, good will toward men” (Luke 2:13–14). Ask: Does the Bible say the angels *sang*? (It says they spoke praise. Singing is possible, but not stated.)'),
        ('Good news', 'The angel said the good news was “to all people”: a Saviour, Christ the Lord, born in the city of David (Luke 2:10–11). Ask: Who is this good news for? (Everyone, including you!)'),
        ('Commander', 'Yeshua is the Lord of hosts, the commander of heaven’s armies. Even as a baby, He was their King.')],
 callout=('Did You Know?', 'Gabriel, the angel who visited Zechariah and Mary, had also brought God’s messages to the prophet Daniel hundreds of years earlier (Daniel 8:16; 9:21).')),
dict(t='text', kicker='Lesson Two · Reading 3, continued', title='The Shepherds Come to See', bignum='2', foot=F,
 top=[('l2_shepherds', 'The shepherds find the baby', 'cover', 0.72), ('map_bethlehem', 'Bethlehem and Migdal Eder', 'cover', 1.5)], toph=2.45,
 paras=["As soon as the angels went back into heaven, the shepherds said to one another, “Let us now go even unto Bethlehem, and see this thing which is come to pass.” They did not have far to go. They hurried into town and found Mary and Joseph, and the baby lying in a manger, just as the angel had said.",
  "Then the shepherds told everyone what they had heard and seen, and all who heard it were amazed. Mary treasured these things and thought about them in her heart. The shepherds went back to their flocks, “glorifying and praising God.”",
  "## The Setting Was Not an Accident",
  "- **In Bethlehem,** the city of David, fulfilling the royal promise (Micah 5:2).",
  "- **At Migdal Eder,** where spotless lambs were born and protected (Micah 4:8).",
  "- **Announced first to shepherds** who knew what swaddling cloths and a manger meant (Luke 2:12).",
  "> “That the Messiah was to be born in Bethlehem was a settled conviction. Equally so was the belief that He was to be revealed from Migdal Eder.” (Alfred Edersheim, 1883)"],
 notes=[('Summary chart', '**Born in Bethlehem:** Micah 5:2 → Luke 2:4–7\n**Tower of the Flock:** Micah 4:8 → Luke 2:8–12\n**Sign of the lamb:** Luke 2:7, 12\n**Sacrificial Lamb:** Exodus 12; Isaiah 53 → John 1:29'),
        ('Edersheim', 'Alfred Edersheim was a 19th-century Jewish scholar who became a follower of Yeshua.')],
 callout=('Your Turn', 'The shepherds could not keep the good news to themselves. Who can you tell about Yeshua this week?')),

dict(t='work', lesson=2, title='Shepherds, Hurry to Bethlehem!', kick='Maze', ins='“Let us now go even unto Bethlehem, and see this thing which is come to pass” (Luke 2:15). Help the shepherds find the way from the fields to Bethlehem!',
 blocks=[('html', _maze()), ('q', 'Fill in the missing words: “For unto you is born this day in the city of ____________ a ____________, which is Christ the Lord.” (Luke 2:11)', 0)], skbot=('sk_star', 1.75)),
dict(t='illus', img='l2_fall', cap='Bethlehem in the fall feast season'),
dict(t='text', id='l2d', kicker='Lesson Two · Reading 4', title='When Was Yeshua Born?', bignum='2', foot=F,
 verse='And there were in the same country shepherds abiding in the field, keeping watch over their flock by night', vref='Luke 2:8',
 read='Luke 1:5, 24–36 · Luke 2:8 · Leviticus 23:23–43',
 paras=["The Bible does not give the date of Yeshua’s birth. But it does give clues, and Bible students have studied them for centuries. There are two main views.",
  "## Clues for a Fall Birth",
  "- **Shepherds in the fields.** In Judea, shepherds stayed out in the fields with their flocks at night from spring until early fall. The weather was mild enough to sleep outdoors.",
  "- **Zechariah’s temple service.** Luke records that Zechariah served in the priestly “course of Abijah” (Luke 1:5). Using the Hebrew calendar, his service falls in midsummer, John the Baptist’s birth near Passover, and Yeshua’s birth six months later, in the early fall.",
  "- **The feasts.** The fall feasts, Trumpets, the Day of Atonement, and Tabernacles (Sukkot), brought crowds of travelers. That would explain why there was no room! A Roman census would also make sense in a season when people were already traveling.",
  "## Clues for a Spring Birth",
  "- Some Bible scholars count Zechariah’s service differently, placing John’s birth in March and Yeshua’s around March or April.",
  "- Spring is lambing season, when shepherds kept watch day and night.",
  "- Some early Christian writers placed the birth in March or April.",
  "## What Matters Most",
  "Both views are possible, but calculations that use the Hebrew calendar point most strongly to the fall. What matters most is not the date, but that God kept His promise right on time."],
 notes=[('Hebrew calendar', 'The Hebrew calendar follows the moon and adds leap months. The feasts fall on fixed Hebrew dates. Using the modern calendar can shift the calculations.'),
        ('Tabernacles', 'John 1:14 says the Word “dwelt” among us. The Greek word means “tabernacled”!'),
        ('Keep it friendly', 'Let children hear both views. Christians who love the Bible hold either one.')],
 callout=('Did You Know?', 'During Sukkot (the Feast of Tabernacles), families lived in leafy booths for seven days to remember how God cared for Israel in the wilderness.')),

dict(t='work', lesson=2, title='Let’s See What You Remember', kick='Review', sk='sk_star', skh=0.85, ins='Look back at Luke 2:1–20, Micah 5:2, and the Lesson 2 readings.',
 blocks=[('part', 'Part 1 · Circle the best answer'),
         ('mc', [('Who ordered a census of the Roman Empire?', ['King Herod', 'Caesar Augustus', 'Pontius Pilate', 'King David']),
                 ('Why did Mary and Joseph travel to Bethlehem?', ['To visit friends', 'To register for the census', 'To escape King Herod', 'To buy a lamb']),
                 ('Which prophet said the Ruler of Israel would be born in Bethlehem?', ['Isaiah', 'Daniel', 'Jeremiah', 'Micah']),
                 ('Where did Mary lay her baby after He was born?', ['In a basket', 'In a manger', 'In a bed', 'In a boat']),
                 ('Who were the first people to hear the good news?', ['Priests', 'Kings', 'Shepherds', 'Soldiers']),
                 ('What did Mary do with all these things? (Luke 2:19)', ['Told everyone in town', 'Kept them and pondered them in her heart', 'Wrote them on a scroll']),
                 ('In Judea, shepherds stayed out in the fields at night …', ['only in winter', 'from spring until early fall', 'only on feast days']),
                 ('During which feast did families live in leafy booths for seven days?', ['Passover', 'Shavuot (Pentecost)', 'Sukkot (Tabernacles)'])]),
         ('part', 'Part 2 · Write your answer'),
         ('mc', [('What name did the angel Gabriel tell Mary to give her baby?', 1),
                 ('What did the angels say? (Luke 2:14)', 2),
                 ('What did the shepherds do after they saw the baby?', 1),
                 ('Name one clue that points to Yeshua being born in the fall.', 1),
                 ('What matters more than the exact date of Yeshua’s birth?', 1)], 9)]),
dict(t='work', lesson=2, title='Birth of the King', sk='sk_quill', skh=0.8, ins='Use your imagination! Write or draw your answer in each box.',
 blocks=[('grid4', ['Imagine you are a shepherd in the field. What would you say to the angel?', 'This miracle teaches that …',
                    'Draw a welcome sign for Bethlehem, the city of David.', 'If the story of Yeshua’s birth were a book, the cover would look like this …'], 6.6)]),
]
