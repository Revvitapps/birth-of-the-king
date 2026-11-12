F = 'Birth of the King · Lesson 4'
MATCH = '''<div class="match"><div class="mc">
<div class="mi"><b>1</b> Gold</div><div class="mi"><b>2</b> Frankincense</div><div class="mi"><b>3</b> Myrrh</div></div>
<div class="mc"><div class="mi">A sweet-smelling resin burned in worship. It shows Yeshua is our High Priest.</div>
<div class="mi">An ointment used in burial. It points to Yeshua’s death for our sins.</div>
<div class="mi">A treasure fit for royalty. It shows Yeshua is the King.</div></div></div>'''
def _code(msg):
    out = []
    for word in msg.split():
        cells = ''.join(f'<div class="cc"><div class="cl"></div><div class="cn">{ord(ch)-64}</div></div>' for ch in word)
        out.append(f'<div class="cw">{cells}</div>')
    return '<div class="code">' + ''.join(out) + '</div>'
KEY = '<table class="ckeytbl"><tr>' + ''.join(f'<td><b>{chr(65+i)}</b><br>{i+1}</td>' for i in range(13)) + '</tr><tr>' + ''.join(f'<td><b>{chr(65+i)}</b><br>{i+1}</td>' for i in range(13, 26)) + '</tr></table>'

PAGES = [
dict(t='opener', id='l4', img='l4_open', num=4, title='The Wise Men Worship the King', ref='Matthew 2:9–12 · Luke 2:21–38'),
dict(t='plan', num=4, title='The Wise Men Worship the King', bignum='4',
 passages='Matthew 2:9–12; Psalm 72:10–11; Isaiah 60:6; John 19:39; Hebrews 4:14–16; Romans 12:1; Luke 2:21–38; Exodus 13:2, 12; Leviticus 12',
 objectives=['What happened when the Wise Men met Yeshua', 'What the gifts of gold, frankincense, and myrrh mean',
             'Why the Wise Men did not go back to King Herod', 'What gift we can bring to the King',
             'How Yeshua was presented at the temple, and who Simeon and Anna were'],
 prayer='King Yeshua, the Wise Men bowed down and worshiped You. We want to worship You too. Show us how to give You our very best, our hearts and our lives. Amen.',
 materials='Bibles, pencils, crayons, and copies of the Lesson 4 printable pages. Optional: a small piece of gold-colored jewelry, frankincense, or myrrh to show the class.',
 overview='The Wise Men left King Herod and followed the star to Bethlehem. When they saw it stop over the place where the young child was, they were filled with joy. Entering the house, they saw Yeshua with His mother Mary, and they bowed down and worshiped Him. Opening their treasures, they gave Him gifts of gold, frankincense, and myrrh, gifts that announced who He is: King, High Priest, and Suffering Savior. But God warned the Wise Men in a dream not to return to Herod, so they went home to their own country another way. The lesson closes at the temple in Jerusalem, where Mary and Joseph presented Yeshua to the Lord, and faithful Simeon and Anna recognized Him as the promised Savior.',
 dyk='Herod’s family came from Idumea (the land of Edom), and his mother was an Arabian princess. He was not from David’s family. Rome gave him the title “King of the Jews,” not the Jewish people.',
 flow=[('Read:', 'They Bowed Down and Worshiped Him'), ('Read:', 'The Gifts: Gold, Frankincense, and Myrrh'),
       ('Activity:', 'Color the Gifts · Gifts for the King · My Gift to the King'),
       ('Read:', 'The Temple in Jerusalem'), ('Activity:', 'Color the Temple · Temple in Jerusalem'),
       ('Read:', 'Presented at the Temple'), ('Activity:', 'Color Simeon and Anna · Presentation at the Temple')]),

dict(t='illus', img='l4_worship', cap='“They saw the young child with Mary his mother”'),
dict(t='text', id='l4a', kicker='Lesson Four · Reading 1', title='They Bowed Down and Worshiped Him', bignum='4', foot=F,
 verse='And when they were come into the house, they saw the young child with Mary his mother, and fell down, and worshipped him', vref='Matthew 2:11',
 read='Matthew 2:9–12 · Psalm 72:10–11',
 paras=["The Wise Men left Herod’s palace and took the short road south to Bethlehem. Then they saw the star again, going ahead of them, until it stopped over the place where the young child was. “They rejoiced with exceeding great joy!”",
  "## Kings Bow Before the King",
  "Remember who these men were: powerful officials from the Parthian Empire, rich and important *king-makers* who could help put a ruler on the throne. Yet when they came into the simple house and saw the young child with His mother Mary, they **fell down and worshiped Him**. They knew they were in the presence of a King far greater than any king on earth.",
  "## Treasures for a King",
  "Then they opened their treasures. Eastern visitors brought rich gifts to great rulers: gold, fine cloth, carved vessels, rare spices. The Bible names three of their gifts: **gold, frankincense, and myrrh**. These gifts were worth a great fortune, and they likely paid for the family’s sudden journey to Egypt and their life there.",
  "## Home Another Way",
  "That night, God warned the Wise Men in a dream not to go back to Herod. So they obeyed God and “departed into their own country another way.” Herod’s plan had failed, and the young King was safe in God’s hands."],
 notes=[('Prophecy', 'Psalm 72:11: “All kings shall fall down before him.” Isaiah 60:6: “They shall bring gold and incense.”'),
        ('Notice', 'The Magi worshiped Yeshua, not Mary. Ask: What does it mean to worship?'),
        ('Obedience', 'The Wise Men obeyed God rather than the king. Ask: Why was that brave?')],
 callout=('Did You Know?', 'Matthew says “the young child with Mary his mother.” Joseph may have been working that day, but God provided for the family through these gifts!')),

dict(t='illus', img='l4_gifts', cap='Gold, frankincense, and myrrh'),
dict(t='text', id='l4b', kicker='Lesson Four · Reading 2', title='The Gifts: Gold, Frankincense, and Myrrh', bignum='4', foot=F,
 verse='And when they had opened their treasures, they presented unto him gifts; gold, and frankincense, and myrrh', vref='Matthew 2:11',
 read='Matthew 2:11 · Exodus 30:34–38 · Hebrews 4:14–16',
 paras=["When you look deeply into the gifts mentioned in Matthew 2, you quickly realize they were not simply offerings of honor, but a prophetic proclamation. *Gold. Frankincense. Myrrh.*",
  "Matthew tells us that the Magi fell down and worshiped Him, and then, opening their treasures, they offered Him gifts. Each gift announced something essential about who Yeshua is and what His first coming would accomplish.",
  "## Gold: The King",
  "Gold has always spoken the language of royalty. Throughout Scripture it is linked with kingship, authority, and enduring worth (1 Kings 10:18–25; Psalm 21:3). By offering gold, the Magi proclaimed that Yeshua was born a King. Not one who would seize power later, but one who held authority from the very beginning. Even before Yeshua preached a sermon or performed a miracle, the gold declared what Pilate would later question and the cross would surprisingly affirm: “Jesus of Nazareth the King of the Jews” (John 19:19).",
  "## Frankincense: The High Priest",
  "Frankincense belonged to worship. In Israel it was reserved for sacred use, burned on the altar and mixed into the holy incense as an offering pleasing to the Lord (Exodus 30:34–38; Leviticus 2:1–2). The psalmist describes prayer rising to God “as incense” (Psalm 141:2), and Revelation links incense with the prayers of the saints before God’s throne (Revelation 5:8).",
  "By offering frankincense, the Magi acknowledged that Yeshua was not only royal but holy, the One through whom true worship would be made possible (John 4:21–24). Frankincense quietly announces that He would be our **High Priest**, the One who stands between God and people (Hebrews 4:14–16)."],
 notes=[('Show and tell', 'If you can, let children smell frankincense. It is a hardened tree sap that smells sweet when burned.'),
        ('Practical value', 'These were standard royal gifts from the East. They likely funded the family’s escape to Egypt.')],
 callout=('Did You Know?', 'Frankincense and myrrh both come from the sap of small, thorny trees that grow in Arabia and East Africa.')),

dict(t='text', kicker='Lesson Four · Reading 2, continued', title='Myrrh, and What Gift Can I Bring?', bignum='4', foot=F,
 verse='I beseech you therefore, brethren, by the mercies of God, that ye present your bodies a living sacrifice, holy, acceptable unto God', vref='Romans 12:1',
 read='Mark 15:23 · John 19:39 · Isaiah 53:3–5 · Mark 10:45',
 sidefig=('l4_home', '“They departed into their own country another way”'),
 paras=["## Myrrh: The Suffering Savior",
  "Myrrh brings a quiet, serious note into the story. It was used as a medicine (Mark 15:23), but also, importantly, for burial. After Yeshua’s crucifixion, Nicodemus brought “a mixture of myrrh and aloes, about an hundred pound weight” to prepare His body for burial (John 19:39).",
  "The presence of myrrh at Yeshua’s birth points ahead to His death. It reminds us that His mission included suffering from the very beginning. Isaiah spoke of a Servant who would be “wounded for our transgressions” (Isaiah 53:5), and Yeshua said He came “to give his life a ransom for many” (Mark 10:45). Myrrh stands as a quiet witness that the cradle was always moving toward the cross.",
  "## A Complete Testimony",
  "Together, the gifts tell the whole story. **Gold** proclaims Him King. **Frankincense** proclaims Him Priest. **Myrrh** proclaims Him the Suffering Savior. The Magi did not preach sermons. They offered gifts, and those gifts spoke clearly.",
  "## What Gift Can I Bring?",
  "This leads me to a deeply personal question. If His first coming was marked by gifts that proclaimed who He is, what about His second coming? What gift can I offer Him? Will He be delighted if the gift I bring is how I lived the life He gave me: how I served, how I obeyed, how I submitted to His Word?",
  "Perhaps the most meaningful offering we can bring is not something placed before Him, but a life faithfully lived for Him."],
 notes=[('Talk about it', 'What are some ways children can give their lives to Yeshua this week? (Kindness, obedience, prayer, telling others.)'),
        ('Connect', 'Romans 12:1 uses the same word *present* that Luke 2:22 uses for Yeshua at the temple (Reading 4).')],
 callout=('Your Turn', 'Use the “My Gift to the King” page to write or draw the gift you want to give Yeshua with your life.')),

dict(t='color', lesson=4, title='Gifts for the King', img='c_gifts', caption='“They presented unto him gifts; gold, and frankincense, and myrrh.” (Matthew 2:11)'),
dict(t='work', lesson=4, title='Gifts for the King', cls='roomy', sk='sk_chest', ins='Draw a line from each gift to what it tells us about Yeshua. Then answer the questions.',
 blocks=[('html', MATCH), ('qs', [('What did the Wise Men do before they gave their gifts? (Matthew 2:11)', 1),
                                    ('How might the gifts have helped Mary, Joseph, and Yeshua?', 1),
                                    ('Myrrh was used for burial. What did it point to in Yeshua’s life?', 1)]),
         ('box', 'Draw a gift you would bring to the King', 3.4, 'fill')]),

dict(t='work', lesson=4, title='My Gift to the King', sk='sk_heartgift', ins='The Wise Men gave Yeshua treasures. The best gift we can give Him is a life lived for Him (Romans 12:1). Write or draw your answers.',
 blocks=[('box', 'Draw yourself bringing a gift to King Yeshua', 2.9),
         ('q', 'Three ways I can serve Yeshua this week:', 0), ('html', '<ol class="qs">' + ''.join('<li><div class="ln"></div></li>' for _ in range(3)) + '</ol>'),
         ('q', 'Write a short prayer giving your life to the King:', 4)]),

dict(t='illus', img='l3_temple', cap='Herod’s Temple in Jerusalem'),
dict(t='text', id='l3e', kicker='Lesson Four · Reading 3', title='The Temple in Jerusalem', bignum='4', foot=F,
 verse='And when the days of her purification according to the law of Moses were accomplished, they brought him to Jerusalem, to present him to the Lord', vref='Luke 2:22',
 read='Luke 2:22–24 · 1 Kings 6 · Ezra 3',
 paras=["The temple in Jerusalem was the center of Hebrew life in Bible times. It was the place where God’s people came to worship, pray, and bring their offerings.",
  "## Three Temples in One Place",
  "King **Solomon**, David’s son, built the first temple in the tenth century BC to house the Ark of the Covenant. Hundreds of years later, the Babylonians destroyed it, stole its treasures, and burned what was left. When the Jews returned from exile, they built a second temple in the days of Zerubbabel and Ezra, and Nehemiah rebuilt the city walls.",
  "## Herod’s Great Project",
  "King Herod made the second temple much larger and more beautiful. One reason was to hold the huge crowds of pilgrims who came to Jerusalem for the three pilgrimage feasts: **Passover**, **Shavuot** (Pentecost), and **Sukkot** (Tabernacles). The historian Josephus says 10,000 workers labored on the project, and building the enormous retaining walls took years. The finished platform was as big as about two dozen football fields!",
  "People could enter the temple courtyards, but only priests went inside the temple building itself. The temple was also the meeting place of the **Sanhedrin**, the highest Jewish court in the days of Roman rule. The Romans destroyed this temple in AD 70.",
  "When the time came for the purification required by the Torah, Joseph and Mary brought baby Yeshua here to present Him to God."],
 notes=[('Set the scene', 'Use this reading to help children picture where Mary and Joseph brought Yeshua in Luke 2:22–38.'),
        ('Distance', 'Bethlehem was only about six miles from the temple, an easy trip for Mary and Joseph.'),
        ('Ask', 'Why do you think God wanted His people to have one central place of worship?')],
 callout=('Did You Know?', 'Some of the massive stones in Herod’s retaining walls weigh hundreds of tons. You can still see them today at the Western Wall in Jerusalem.')),

dict(t='color', lesson=4, title='The Temple', img='c_temple', caption='Herod made the temple bigger and more beautiful than ever.'),
dict(t='work', lesson=4, title='Temple in Jerusalem', sk='sk_menorah', ins='Read “The Temple in Jerusalem,” then answer the questions.',
 blocks=[('qs', [('Which king built the first temple in Jerusalem?', 1), ('What was the first temple built to house?', 1),
                 ('Who destroyed the first temple?', 1), ('Name the three pilgrimage feasts that brought crowds to Jerusalem.', 2),
                 ('What was the Sanhedrin?', 1), ('Who destroyed Herod’s temple, and in what year?', 1)]),
         ('box', 'Draw something you would see at the temple', 3.4, 'fill')]),

dict(t='illus', img='l3_simeon', cap='Simeon and Anna meet the Messiah'),
dict(t='text', id='l3f', kicker='Lesson Four · Reading 4', title='Presented at the Temple', bignum='4', foot=F,
 verse='For mine eyes have seen thy salvation, which thou hast prepared before the face of all people', vref='Luke 2:30–31',
 read='Luke 2:21–38 · Exodus 13:2, 12 · Romans 12:1',
 paras=["When Yeshua was eight days old, He was circumcised and officially given the name Yehoshua, or Yeshua. About forty days after His birth, Mary and Joseph took Him to the temple, obeying the Law of Moses. Every firstborn son belonged to the Lord (Exodus 13:2, 12), and Mary brought an offering for her purification: “a pair of turtledoves, or two young pigeons,” the gift of a family that could not afford a lamb (Leviticus 12:8).",
  "## To “Present” Him",
  "Luke says they came “to present him to the Lord.” To *present* means to fully hand over, to offer as a gift to God. Paul uses the same word in Romans 12:1: “present your bodies a living sacrifice.” Just as Yeshua was presented to God, we can dedicate ourselves to Him, once and for all, forever!",
  "## Simeon",
  "Simeon was a righteous and devout man in Jerusalem, known for his deep knowledge of God and his gift of understanding the times. He was waiting for “the consolation of Israel.” *Consolation* means comfort, encouragement, and help. The Holy Spirit had promised Simeon he would see the Messiah before he died. When he took baby Yeshua in his arms, he blessed God: “Mine eyes have seen thy salvation!” Simeon said, “*Behold*,” a word full of wonder and amazement.",
  "## Anna",
  "Anna was a prophetess from the tribe of Asher. She was 84 years old, a widow who never left the temple grounds, worshiping God with fasting and prayer night and day. She gave thanks and told everyone who was waiting for redemption about the child."],
 notes=[('Word study', '*Present* (Luke 2:22; Rom. 12:1): to hand over completely as an offering to God.\n*Behold:* shock, amazement, wonder.\n*Consolation:* comfort, encouragement, support.'),
        ('Humble offering', 'Two birds were the offering of the poor. The King of kings grew up in a humble family.'),
        ('Apply', 'Romans 12:1: what does it look like to give ourselves to God?')],
 callout=('Did You Know?', 'Simeon’s name comes from the Hebrew word *shama*, “to hear.” Simeon listened to the Holy Spirit and was in the right place at the right time.')),

dict(t='color', lesson=4, title='Simeon and Anna', img='c_simeon', caption='“Mine eyes have seen thy salvation.” (Luke 2:30)'),
dict(t='work', lesson=4, title='Presentation at the Temple', cls='roomy', sk='sk_doves', ins='Read Exodus 13:2, 12 and Luke 2:21–38. Draw a line from each name to the right clue. Then circle the best answer for each question.',
 blocks=[('html', '''<div class="match"><div class="mc">
<div class="mi"><b>1</b> Gabriel</div><div class="mi"><b>2</b> Simeon</div><div class="mi"><b>3</b> Anna</div><div class="mi"><b>4</b> Two turtledoves</div><div class="mi"><b>5</b> Jerusalem</div></div>
<div class="mc"><div class="mi">A prophetess, 84 years old, from the tribe of Asher</div><div class="mi">The city where the temple stood</div><div class="mi">The angel who told Mary to name her son Yeshua</div><div class="mi">The offering of a family who could not afford a lamb</div><div class="mi">Said, “Mine eyes have seen thy salvation”</div></div></div>'''),
         ('mc', [('On which day was Yeshua circumcised?', ['The first day', 'The third day', 'The eighth day', 'The fortieth day']),
                 ('Why did Mary and Joseph present Yeshua at the temple?', ['Every firstborn son belonged to the Lord', 'To pay a Roman tax', 'To make Him a priest']),
                 ('What had the Holy Spirit promised Simeon?', ['He would be high priest', 'He would see the Lord’s Christ before he died', 'He would visit Bethlehem']),
                 ('What did Anna do at the temple?', ['Sold doves', 'Worshiped with fasting and prayer night and day', 'Guarded the gate']),
                 ('What does it mean to “present” yourself to God? (Romans 12:1)', ['To give yourself completely to Him as a living sacrifice', 'To dress up for church', 'To bring Him money'])])]),
]
