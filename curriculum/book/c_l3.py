F = 'Birth of the King · Lesson 3'
NEWS = '''<div class="paper"><div class="ear"><div class="box">Price<br>One Lepton</div><div class="box">Today’s Weather<br>Clear skies · Bright star in the east!</div></div>
<div class="mast">The Judea Times</div>
<div class="dateline"><span>Vol. I · No. 1</span><span>Jerusalem, Judea</span><span>Matthew 2:1–8</span></div>
<div class="extra">★ EXTRA! EXTRA! ★</div><div class="head">Wise Men Seek a Newborn King!</div>
<div class="grid"><div class="col"><h5>Strange Star Seen in the East</h5><div class="by">By ______________, Staff Reporter</div>''' + ''.join('<div class="ln"></div>' for _ in range(6)) + '''
<div class="pic"><span>Draw your own picture for this story</span></div><div class="cap">Caption:<div class="ln"></div></div></div>
<div class="col"><h5>King Herod Calls a Secret Meeting</h5><div class="by">By ______________, Palace Reporter</div>''' + ''.join('<div class="ln"></div>' for _ in range(9)) + '''
<div class="side"><b>Interview Corner</b>If you could ask a Wise Man one question, what would it be?''' + ''.join('<div class="ln"></div>' for _ in range(2)) + '''</div>
<div class="ad"><b>WANTED</b>Directions to Bethlehem! Ask the chief priests.<br><i>(Micah 5:2)</i></div></div></div></div>'''
import random as _r
def _wordsearch(words, n=13, seed=3):
    rnd = _r.Random(seed); g = [[None]*n for _ in range(n)]; dirs = [(1,0),(0,1),(1,1)]
    for w in sorted(words, key=len, reverse=True):
        for _ in range(500):
            dx, dy = rnd.choice(dirs); x = rnd.randrange(n - (len(w)-1)*dx); y = rnd.randrange(n - (len(w)-1)*dy)
            if all(g[y+i*dy][x+i*dx] in (None, c) for i, c in enumerate(w)):
                for i, c in enumerate(w): g[y+i*dy][x+i*dx] = c
                break
        else: raise ValueError(w)
    A = 'ABCDEFGHIJKLMNOPRSTUWY'
    rows = ''.join('<tr>' + ''.join(f'<td>{c or rnd.choice(A)}</td>' for c in r) + '</tr>' for r in g)
    bank = ' · '.join(words)
    return f'<table class="wsearch">{rows}</table><div class="bank" style="text-align:center"><b>Find these words:</b> {bank}</div>'
WS = _wordsearch(['MAGI', 'STAR', 'HEROD', 'BETHLEHEM', 'PARTHIA', 'CAMEL', 'CARAVAN', 'SCRIBES', 'PROPHET', 'JERUSALEM', 'DANIEL', 'MICAH', 'KING', 'EAST'])


PAGES = [
dict(t='opener', id='l3', img='l3_open', num=3, title='Star in the Sky', ref='Matthew 2:1–8 · Numbers 24:17 · Micah 5:2'),
dict(t='plan', num=3, title='Star in the Sky', bignum='3',
 passages='Matthew 2:1–8; Numbers 24:17; Daniel 2:48; Daniel 9:24–27; Micah 5:2',
 objectives=['Who the Wise Men (Magi) were and where they came from', 'What the star may have been, and when the Magi came',
             'Who King Herod was, and why he was troubled by the news', 'How the chief priests knew where the Messiah would be born'],
 prayer='God of heaven and earth, You guided the Wise Men by a star and You guide us by Your Word. Help us seek Yeshua with our whole hearts. In His name, amen.',
 materials='Bibles, pencils, crayons, a map or atlas, and copies of the Lesson 3 printable pages.',
 overview='Far to the east, in the Parthian Empire, lived a group of powerful priest-scholars called Magi. They studied the stars and advised kings. When they saw a remarkable star rise, they knew the King of the Jews had been born, and they set out on a long journey to Jerusalem. King Herod was alarmed. He gathered the chief priests, learned that the Messiah would be born in Bethlehem, and secretly told the Magi to search for the child and report back. But God was already at work to protect His Son.',
 dyk='From Susa, an old royal city of Persia, the Magi may have traveled around 1,200 miles to reach Bethlehem. From the Parthian capital at Ctesiphon, the trip was about 700 to 900 miles, two to four months each way!',
 flow=[('Read:', 'Who Were the Magi?'), ('Activity:', 'Color the Wise Man · The Wise Men'), ('Read:', 'The Star: What Did They See?'),
       ('Read:', 'The Parthian Empire'), ('Activity:', 'Journey to Jerusalem'), ('Read:', 'Herod Is Troubled · Who Was King Herod?'),
       ('Activity:', 'Parthia and King Herod · The Judea Times · Word Search')]),

dict(t='illus', img='l3_magi', cap='Magi of the Parthian court'),
dict(t='text', id='l3a', kicker='Lesson Three · Reading 1', title='Who Were the Magi?', bignum='3', foot=F,
 verse='Behold, there came wise men from the east to Jerusalem, saying, Where is he that is born King of the Jews? for we have seen his star in the east', vref='Matthew 2:1–2',
 read='Matthew 2:1–2 · Daniel 2:48 · Numbers 24:17',
 paras=["Many songs call them “three kings,” but the Bible never says they were kings. Matthew calls them *magoi*, or **Magi**, a well-known group of priest-scholars from the lands east of Israel.",
  "## Priests, Scholars, and King-Makers",
  "The Magi first came from the Medes and Persians. They were experts in the stars, astrologers, and students of dreams, ancient writings, and the business of kings. At the time Yeshua was born, Persia was part of the **Parthian Empire**, the great rival of Rome. In Parthia, Magi sat on the king’s council. Together with the nobles, they had so much power that they could help choose a new king, or remove one. People called them *king-makers*.",
  "## Why Would They Care About a Jewish King?",
  "Hundreds of years earlier, the Jews were carried away to Babylon. One of them, **Daniel**, became “chief of the governors over all the wise men of Babylon” (Daniel 2:48). Daniel’s writings included a timetable for the coming Messiah (Daniel 9:24–27).",
  "Many Jewish families stayed in Babylon and Persia for centuries. They knew the prophecy of Balaam: “There shall come a Star out of Jacob, and a Sceptre shall rise out of Israel” (Numbers 24:17). For scholars who studied the sky, a prophecy about a star would catch their attention! Generations of Eastern scholars may have kept and passed on this knowledge."],
 notes=[('Key word', '*Magi* (Greek *magoi*) is where we get the word “magic,” but these men were not tricksters. They were respected priests and scholars.\n**Astronomy** is studying the sun, moon, stars, and planets as God made them. **Astrology** is the belief that the stars control or foretell people’s lives, which the Bible warns against (Deuteronomy 18:10–12). The Magi practiced both, yet God used the sky they studied to lead them to Yeshua.'),
        ('Daniel’s legacy', 'Daniel’s influence is a big reason many scholars believe Eastern Magi were expecting a Jewish King.'),
        ('Ask', 'The Magi traveled a long way to find Yeshua. What does that tell us about how much they wanted to see Him?')],
 callout=('Did You Know?', 'The Parthian royal council was called the *Megistanes*. Its members included royal family members, nobles, and the Magi.')),

dict(t='color', lesson=3, title='A Wise Man from the East', img='c_magus', caption='“We have seen his star in the east, and are come to worship him.” (Matthew 2:2)'),
dict(t='work', lesson=3, title='The Wise Men', sk='sk_starmap', skh=1.1, ins='Open your Bible and read Matthew 2:1–8. Then read “Who Were the Magi?” and answer the questions.',
 blocks=[('part', 'Part 1 · Circle the best answer'),
         ('mc', [('Who was king of Judea when Yeshua was born? (verse 1)', ['Caesar', 'Herod', 'David', 'Pilate']),
                 ('From where did the Wise Men come? (verse 1)', ['The west', 'Egypt', 'The east', 'Rome']),
                 ('What is another name for the Wise Men?', ['Pharisees', 'Levites', 'Scribes', 'Magi']),
                 ('Which empire ruled Persia when Yeshua was born?', ['The Parthian Empire', 'The Roman Empire', 'The Greek Empire']),
                 ('Which Hebrew prophet was chief over the wise men of Babylon?', ['Isaiah', 'Daniel', 'Jonah', 'Elijah'])]),
         ('part', 'Part 2 · Write your answer'),
         ('mc', [('What did the Wise Men say when they arrived in Jerusalem? (verse 2)', 2),
                 ('Why were the Magi called “king-makers”?', 2),
                 ('What did Numbers 24:17 say would come out of Jacob?', 1)], 6)]),

dict(t='illus', img='l3_star', cap='Following the star'),
dict(t='text', id='l3b', kicker='Lesson Three · Reading 2', title='The Star: What Did They See?', bignum='3', foot=F,
 verse='And, lo, the star, which they saw in the east, went before them, till it came and stood over where the young child was', vref='Matthew 2:9',
 read='Matthew 2:1–11, 16',
 paras=["What was the star the Magi saw? Matthew does not explain, but he gives us some clues.",
  "## What It Probably Was Not",
  "It was probably not a comet, because no recorded comet matches the time. And it was not an ordinary star sitting still above one house. Matthew says the star “went before them” and then “stood over where the young child was.” That sounds like God’s own guidance. Many believe the Magi first noticed an important sign in the sky, and then God guided them by a special light, like the glory cloud that led Israel in the wilderness, for the last part of their journey.",
  "## How Many Wise Men Were There?",
  "The Bible never says there were three. The number three comes from the three gifts: gold, frankincense, and myrrh. Important visitors from Parthia would never travel in a group of three! A royal delegation traveled with a large caravan of servants, guards, camels, and horses, possibly 80 to 100 people or more.",
  "## When Did They Come?",
  "The Magi did not visit the manger on the night Yeshua was born. Matthew calls Him a *young child* (Greek *paidion*), not a newborn baby. The Magi found Him in a **house** (Matthew 2:11). And Herod later ordered the death of boys “two years old and under,” based on when the star first appeared (Matthew 2:16). The Magi most likely arrived when Yeshua was between six months and two years old."],
 notes=[('Timeline', 'Yeshua’s birth: most likely 5 or 4 BC.\nMagi arrive: likely 6 to 18 months later.'),
        ('Nativity scenes', 'It is fine to enjoy nativity scenes! Just help children notice what the Bible actually says.'),
        ('Ask', 'Why do you think God used a star to lead people who studied the stars?')],
 callout=('Did You Know?', 'When the Magi saw the star again over Bethlehem, “they rejoiced with exceeding great joy” (Matthew 2:10). That is very great joy!')),

dict(t='text', id='l3c', kicker='Lesson Three · Reading 3', title='The Parthian Empire', bignum='3', foot=F,
 verse='When Herod the king had heard these things, he was troubled, and all Jerusalem with him', vref='Matthew 2:3',
 read='Matthew 2:1–3',
 top=[('map_magi_wide', 'The Magi’s likely route from Parthia', 'contain')], toph=2.75,
 paras=["Parthia was a vast empire that stretched across the lands we now call Iran and Iraq, southeast of the Caspian Sea. The Parthians ruled the East at the same time the Romans ruled the lands around the Mediterranean Sea.",
  "## Rome’s Great Rival",
  "Rome started many wars with Parthia, but it never conquered it. In fact, the Parthians defeated Roman armies many times. In 53 BC they crushed a Roman army at the Battle of Carrhae. And from 40 to 37 BC, Parthian forces even took control of Judea and Jerusalem for a short time! After that, Rome wanted peace with Parthia, and Roman officials knew that starting another war could cost them their jobs, or their lives.",
  "## The Magi’s Journey",
  "The Magi likely set out from the Parthian capital, **Seleucia–Ctesiphon**, on the Tigris River. They would have followed the trade routes of the Silk Road along the Euphrates River, turned south through **Damascus**, and come down to **Jerusalem**. The trip was about 700 to 900 miles and could take two to four months.",
  "So imagine the scene: a large group of powerful officials from Rome’s greatest enemy rides into Jerusalem asking, “Where is he that is born King of the Jews?” No wonder Herod was troubled!"],
 notes=[('Map it', 'Use the map above. Trace the route with your finger from Seleucia–Ctesiphon to Bethlehem.'),
        ('History', 'Parthia lasted from about 247 BC to AD 224, when it was replaced by the Sassanid Persians.'),
        ('Research', 'Older students can research facts about the Parthian Empire for the activity page.')]),

dict(t='work', lesson=3, title='Journey to Jerusalem', ins='Read the story below, then answer the questions. Color the Wise Man and his camel!',
 blocks=[('read', ["The Bible does not say how many Wise Men made the journey, but history suggests a large group of Parthian Magi traveled to Jerusalem to worship the Messiah. Before they left, they had to prepare gifts, take care of their business at home, load a caravan of camels and horses, and find soldiers to protect them. No wonder the long trip took months!",
                   "Why were these men from the East so interested in the Messiah? Daniel, a Hebrew prophet, had once been chief over the wise men of Babylon (Daniel 2:48). Many believe he shared God’s prophecies with them, and that later Magi passed this knowledge down for generations."]),
         ('qs', [('What did the Magi need to do before they traveled to Judea?', 2), ('Why do you think the Magi were interested in the Messiah?', 2),
                 ('What would you pack for a long journey to see the King?', 2)]),
         ('img', 'c_camel', 2.6)]),

dict(t='illus', img='l3_herod', cap='Herod meets the Magi'),
dict(t='text', id='l3d', kicker='Lesson Three · Reading 4', title='Herod Is Troubled', bignum='3', foot=F,
 verse='Go and search diligently for the young child; and when ye have found him, bring me word again, that I may come and worship him also', vref='Matthew 2:8',
 read='Matthew 2:3–8 · Micah 5:2',
 paras=["King Herod was a very suspicious ruler. Rome had made him king over Judea, and he was always afraid that someone would take his throne away. He had good reason to worry about Parthia: only a few years before, Parthia had defeated Rome and held Judea for a time.",
  "So when Parthian Magi arrived in Jerusalem asking for the one “born King of the Jews,” Herod heard it as a political threat. Were the Parthians planning to replace him with a new king? The Bible says Herod “was troubled, and all Jerusalem with him.”",
  "## Where Will the Messiah Be Born?",
  "Herod quickly called together the chief priests and teachers of the law. “Where should the Messiah be born?” he asked. They knew the answer from Micah’s prophecy: “In Bethlehem of Judaea.”",
  "## A Secret Meeting",
  "Then Herod met with the Magi secretly. He asked them exactly when the star had appeared. He sent them to Bethlehem and said, “Go and search diligently for the young child; and when ye have found him, bring me word again, that I may come and worship him also.”",
  "But Herod did not want to worship Yeshua at all. He wanted to destroy Him. Herod pretended to be friendly, but God saw his heart, and God was already protecting His Son."],
 notes=[('Discuss', 'The chief priests knew the Scripture, but they did not go to Bethlehem with the Magi. Ask: Is knowing about Yeshua the same as seeking Him?'),
        ('Herod’s fear', 'Herod was not from David’s family. Rome gave him the title “King of the Jews.” A true heir of David was a threat to him.')],
 callout=('Did You Know?', 'Bethlehem is only about six miles south of Jerusalem. The Magi were almost at the end of their long journey!')),
dict(t='text', kicker='Lesson Three · Reading 4, continued', title='Who Was King Herod?', bignum='3', foot=F,
 sidefig=('l5_herod', 'King Herod, old and afraid'),
 paras=["To understand why Herod was so troubled, it helps to know who he was. Here are the main points to remember:",
  "- **Made king by Rome.** Herod, often called **Herod the Great**, was named king of Judea by the Roman Senate in 40 BC. He was not from David’s family.",
  "- **A busy builder.** He built fortresses, palaces, theaters, and whole cities, including the port of **Caesarea**, the fortress-palace **Herodium**, and a palace on **Masada**. He also rebuilt the temple, partly to win the favor of the Jewish people.",
  "- **A cruel and fearful king.** Herod was so afraid of losing his throne that he killed members of his own family.",
  "- **“King of the Jews.”** Rome gave Herod this title. When Wise Men came asking for the one *born* King of the Jews, the old, sick king was not about to give it up.",
  "- **His end.** Herod died in about 4 BC, not long after his cruel order in Bethlehem. His son **Archelaus** ruled Judea after him (Matthew 2:22)."],
 notes=[('Contrast', 'Herod was given his title by Rome. Yeshua was born King (Matt. 2:2). Ask: What is the difference between the two kings?'),
        ('Herod’s family', 'Herod’s family came from Idumea (Edom), and his mother was Arabian.')],
 callout=('Did You Know?', 'Herod was buried at Herodium, the fortress-palace he built near Bethlehem. Archaeologists found what is believed to be his tomb in 2007.')),

dict(t='work', lesson=3, title='Parthia and King Herod', sk='c_herod', skh=1.3, ins='Read “The Parthian Empire,” “Herod Is Troubled,” and “Who Was King Herod?” Then answer the questions.',
 blocks=[('qs', [('Why do you think King Herod was troubled when the Wise Men arrived in Jerusalem? (Matthew 2:1–8)', 3),
                 ('Where did the chief priests say the Messiah would be born? Which prophet wrote it?', 1),
                 ('Who made Herod king of Judea?', 1), ('Name three things Herod built.', 1),
                 ('Who ruled Judea after Herod died? (Matthew 2:22)', 1), ('How was Herod different from King Yeshua?', 2)]),
         ('q', 'With an adult, use an atlas, encyclopedia, or the Internet to research the Parthian Empire. Write three facts below.', 0),
         ('html', '<ol class="qs">' + ''.join('<li><div class="ln"></div></li>' for _ in range(3)) + '</ol>')]),

dict(t='work', lesson=3, title='The Judea Times', kick='Be a Reporter', ins='You are a reporter in Jerusalem! Read Matthew 2:1–8. Write two news stories about what happened, then draw a picture for your front page.',
 blocks=[('html', NEWS)]),
dict(t='work', lesson=3, title='Star in the Sky Word Search', kick='Word Search', sk='sk_caravan', skh=0.9, ins='Find the words from Lesson 3 hidden in the puzzle. Words go across, down, or diagonally. Circle each one you find!',
 blocks=[('html', WS), ('q', 'Pick two words you found. Write a sentence about Lesson 3 using both words.', 2)]),
]
