F = 'Beyond the Manger · Lesson 5'
SEQ = [('An angel appears to Mary.', ''), ('The Roman emperor orders everyone to register for a census.', ''),
       ('Mary and Joseph travel to Bethlehem.', ''), ('Yeshua is born in Bethlehem.', ''), ('An angel appears to shepherds in the fields.', ''),
       ('Yeshua is presented at the temple (Leviticus 12; Exodus 13).', ''), ('The Wise Men see a star and travel to Jerusalem to meet King Herod.', ''),
       ('The Wise Men bow down and worship Yeshua.', ''), ('The Wise Men return to their country by another way.', ''), ('Joseph and his family escape to Egypt.', '')]
ORDER = [5, 9, 2, 10, 4, 1, 3, 8, 6, 7]  # scrambled display order (indexes into SEQ, 1-based)
SEQ_HTML = ''.join(f'<div class="seq"><div class="bx"></div><b style="font-family:Inter;color:#c9a24a">{chr(65+i)}.</b> {SEQ[k-1][0]}</div>' for i, k in enumerate(ORDER))

PAGES = [
dict(t='opener', id='l5', img='l5_open', num=5, title='Out of Egypt', ref='Matthew 2:13–23 · Hosea 11:1'),
dict(t='plan', num=5, title='Out of Egypt', bignum='5',
 passages='Matthew 2:13–23; Hosea 11:1; Jeremiah 31:15; Isaiah 11:1',
 objectives=['Describe an ordinary home in Israel using clues from Scripture',
 'Explain why God sent the family to Egypt',
 'Show how Yeshua’s journey matches the journey of Israel',
 'Tell how God brought the family safely home to Nazareth'],
 prayer='Heavenly Father, thank You for watching over Yeshua and His family. Thank You that You watch over us too. Help us trust You and obey You quickly, like Joseph did. In Yeshua’s name, amen.',
 materials='Bibles, pencils, crayons, an atlas or globe, and copies of the Lesson 5 printable pages.',
 overview='Matthew 2 records three more dreams given to Joseph, and each one moves the family a step ahead of danger. The first sends them to Egypt by night, beyond Herod’s reach. Herod’s rage falls on Bethlehem, and Matthew hears in it Jeremiah’s words about Rachel weeping. After Herod’s death a second dream calls the family back to Israel, and a third turns them away from Judea toward Galilee. Matthew marks the moves with prophecy: “Out of Egypt have I called my son” and “He shall be called a Nazarene.” The lesson begins inside the kind of house where the Magi found the child, and it ends with the promised Branch growing up in Nazareth.',
 dyk='Israel went down to Egypt as a family and came out as a nation God called “my son” (Exodus 4:22). Yeshua traveled the same road, and Matthew uses the same words for Him.',
 flow=[('Read:', 'Under an Israelite Roof'),
 ('Activity:', 'Color an Israelite House · Inside the House'),
 ('Read:', 'Can Any Good Thing Come Out of Nazareth?'),
 ('Activity:', 'Color a Man of Nazareth · Come and See Nazareth'),
 ('Read:', 'Flight to Egypt'),
 ('Activity:', 'Color the Escape · Arise and Flee'),
 ('Activity:', 'Out of Egypt: Two Journeys · Joseph’s Four Dreams'),
 ('Read:', 'Safe in Egypt, Home to Nazareth'),
 ('Activity:', 'Map: The Escape Route · From Promise to Nazareth')]),

dict(t='illus', img='l5_house', cap='Inside an Israelite house'),
dict(**{'t': 'text',
 'id': 'l5a',
 'kicker': 'Lesson Five · Reading 1',
 'title': 'Under an Israelite Roof',
 'bignum': '5',
 'foot': 'Beyond the Manger · Lesson 5',
 'verse': 'And when they were come into the house, they saw the young child with Mary his mother',
 'vref': 'Matthew 2:11',
 'read': 'Matthew 2:11 · Deuteronomy 22:8 · Mark 2:1–4 · Luke 15:8',
 'paras': ['Notice one word in Matthew 2:11: *house*. The shepherds found a baby in a manger. The Wise Men found a young child in a house. Time had passed, and the family had settled in Bethlehem. Scripture never describes that '
           'house, but the Bible is full of clues about what an ordinary home in Israel was like.',
           '**1. One lamp lit the whole house.** Yeshua said a lamp on a stand “giveth light unto all that are in the house” (Matthew 5:15). Most homes had one main room. A whole family slept there together (Luke 11:7). The room '
           'was dim enough that a woman who lost a coin had to light a lamp and sweep to find it (Luke 15:8).',
           '**2. The roof was a room.** Roofs were flat, reached by outside steps. God’s law required a low wall around the edge so no one would fall (Deuteronomy 22:8). Peter went up on a roof to pray (Acts 10:9). The roof '
           'itself was made of beams, branches and packed earth, which is how four friends could dig through one to lower a man down to Yeshua (Mark 2:4).',
           '**3. Guests had an upper room.** Some homes had a small room built on top. A family in Shunem built one for the prophet Elisha, with a bed, a table, a stool and a lamp (2 Kings 4:10). This is the kind of “guest room” '
           'that was already full on the night Yeshua was born.',
           '**4. The animals were close.** A family’s donkey or ox was kept in a stall and led out to water each morning (Luke 13:15). A manger held the feed.',
           '**5. Work happened in the courtyard.** There the women ground grain for the day’s bread (Matthew 24:41) and baked it in a clay oven.',
           '**Why it matters.** The King of kings did not grow up in a palace. He lived in a home like this one, with one lamp, a flat roof and bread baked each morning. When He taught, He talked about lamps, lost coins and '
           'houses built on rock, because He had lived among them.'],
 'notes': [('Compare', 'Manger (Luke 2:16) and house (Matthew 2:11). Ask: What does this show about when the Wise Men came?'),
           ('God’s Word at the door', 'Deuteronomy 6:9 told Israel to write God’s words on the doorposts of the house. A Hebrew home was marked by Scripture from the doorway in.'),
           ('Ask', 'Which of Yeshua’s stories happen inside a house?')],
 'callout': ('Did You Know?', 'After the winter rains, families packed their roofs flat again with a heavy stone roller so the rain would not leak through.')}),

dict(t='color', lesson=5, title='An Israelite House', img='c_house', caption='Color the house. Then name its parts on the next page.'),
dict(**{'t': 'work',
 'lesson': 5,
 'title': 'Inside the House',
 'sk': 'sk_oven',
 'ins': 'Read “Under an Israelite Roof.” Each clue comes from a Bible verse. Write the part of the house it describes. Then answer the questions.',
 'blocks': [('bank', ['flat roof', 'upper room', 'main room', 'stall', 'courtyard']),
            ('html',
             '<table class="tbl"><tr><th style="width:60%">Clue from Scripture</th><th>Part of the house</th></tr><tr><td>One lamp gave light to everyone in it (Matthew 5:15)</td><td class="blank"></td></tr><tr><td>It needed a '
             'low wall so no one would fall (Deuteronomy 22:8)</td><td class="blank"></td></tr><tr><td>A family built one for Elisha, with a bed and a table (2 Kings 4:10)</td><td class="blank"></td></tr><tr><td>The ox and the '
             'donkey were kept here (Luke 13:15)</td><td class="blank"></td></tr><tr><td>Grain was ground here for the day’s bread (Matthew 24:41)</td><td class="blank"></td></tr></table>'),
            ('qs',
             [('Where did the shepherds find Yeshua? Where did the Wise Men find Him? (Luke 2:16; Matthew 2:11)', 2),
              ('What does that show about when the Wise Men came?', 2),
              ('How is this house like your home? How is it different?', 2)])]}),

dict(t='illus', img='l1_nazareth', cap='The village of Nazareth'),
dict(**{'t': 'text',
 'id': 'l5n',
 'kicker': 'Lesson Five · Reading 2',
 'title': 'Can Any Good Thing Come Out of Nazareth?',
 'bignum': '5',
 'foot': 'Beyond the Manger · Lesson 5',
 'verse': 'And Nathanael said unto him, Can there any good thing come out of Nazareth? Philip saith unto him, Come and see',
 'vref': 'John 1:46',
 'read': 'Luke 1:26 · John 1:45–46 · Luke 4:16 · Isaiah 11:1',
 'paras': ['The Old Testament names hundreds of towns in Israel. Nazareth is not one of them. No king was born there. No prophet preached there. No battle was won there. When God chose a hometown for His Son, He chose a place '
           'the Scriptures had never mentioned.',
           '**A village off the main road.** Nazareth sat on a ridge in the hills of lower Galilee, about fifteen miles from the Sea of Galilee. Below it stretched the wide Jezreel Valley, where armies and traders passed. About '
           'four miles away stood Sepphoris, a busy city. Nazareth itself was only a farming village. Even its neighbors looked down on it. When Nathanael, who came from nearby Cana, heard where Yeshua was from, he asked, “Can '
           'there any good thing come out of Nazareth?”',
           '**Hands that worked.** Families in Nazareth grew grain, olives and grapes on the hillsides, and the village shared a spring for its water. Joseph was a *tekton*, the word translated “carpenter” (Matthew 13:55). It '
           'means a builder, a man who worked with wood and stone. Yeshua learned that trade beside him, and the neighbors later called Him “the carpenter” (Mark 6:3).',
           '**A home filled with Scripture.** Nazareth had a synagogue, and Luke says it was Yeshua’s custom to be there every Sabbath (Luke 4:16). In a Hebrew home, God’s words were taught to children at the table, on the road, '
           'at bedtime and at sunrise (Deuteronomy 6:6–7). The King grew up hearing the very Scriptures that spoke about Him.',
           '**Why it matters.** Isaiah said the Messiah would grow up “as a root out of a dry ground” (Isaiah 53:2), with nothing impressive to draw a crowd. Nazareth was that dry ground. God “hath chosen the weak things of the '
           'world to confound the things which are mighty” (1 Corinthians 1:27). No one is from a place too small for God to use.'],
 'notes': [('Key word', 'Isaiah 11:1 promises a “Branch” from Jesse’s roots. The Hebrew word is *netzer*. Many teachers believe the name Nazareth comes from the same word. Watch for this again at the end of this lesson.'),
           ('Prophecy and fulfillment', 'Isaiah 53:2 → John 1:46. The Messiah would not look important. Nathanael’s question proves the prophecy true.'),
           ('Ask', 'Philip did not argue with Nathanael. He said, “Come and see.” Who could be invited to come and see Yeshua this week?')],
 'callout': ('Did You Know?', 'Nathanael changed his mind the same day. After meeting Yeshua he said, “Thou art the Son of God; thou art the King of Israel” (John 1:49).')}),

dict(t='color', lesson=5, title='A Man of Nazareth', img='c_farmer', caption='Families in Nazareth grew grain, olives and grapes on the hillsides.'),
dict(**{'t': 'work',
 'lesson': 5,
 'title': 'Come and See Nazareth',
 'ins': 'Read “Can Any Good Thing Come Out of Nazareth?” again, then answer the questions below.',
 'blocks': [('qs',
             [('How many times is Nazareth named in the Old Testament?', 1),
              ('What did Nathanael ask when he heard where Yeshua was from? (John 1:46)', 2),
              ('What kind of work did Joseph do? What does the word *tekton* mean?', 2),
              ('Where did Yeshua go every Sabbath? (Luke 4:16)', 1),
              ('What does the Hebrew word *netzer* mean? Which verse in Isaiah uses it?', 2),
              ('Why do you think God chose a small village like Nazareth?', 2)]),
            ('box', 'Draw Joseph and Yeshua at work', 3.4, 'fill')]}),

dict(t='illus', img='l5_flight', cap='The flight to Egypt'),
dict(t='text', id='l5b', kicker='Lesson Five · Reading 3', title='Flight to Egypt', bignum='5', foot=F,
 verse='When he arose, he took the young child and his mother by night, and departed into Egypt', vref='Matthew 2:14',
 read='Matthew 2:13–18 · Hosea 11:1 · Jeremiah 31:15',
 paras=["After the Wise Men left, an angel of the Lord appeared to Joseph in a dream. “Arise, and take the young child and his mother, and flee into Egypt, and be thou there until I bring thee word: for Herod will seek the young child to destroy him.”",
  "Joseph did not wait until morning. He got up, took Yeshua and Mary, and left **that very night**. This was the third time Joseph obeyed God’s message in a dream, and each time he obeyed right away.",
  "## Why Egypt?",
  "Egypt was outside Herod’s kingdom, so Herod could not reach them there. It was also home to many Jewish families, especially in the great city of Alexandria. And God had a reason in His Word: the prophet Hosea had written, “Out of Egypt have I called my son” (Hosea 11:1). Long ago, God brought Israel out of Egypt. Now His own Son would come out of Egypt too.",
  "## Herod’s Anger",
  "When Herod realized the Wise Men had tricked him, he became furious. He ordered his soldiers to kill all the boys in Bethlehem and the nearby area who were two years old and under. It was a terrible and cruel act, and Matthew says it fulfilled Jeremiah’s words about Rachel weeping for her children (Jeremiah 31:15).",
  "But Herod could not stop God’s plan. The young King was already safe in Egypt, protected by His Father in heaven."],
 notes=[('Handle with care', 'Be gentle when sharing Herod’s cruelty with young children. Focus on God’s protection and Joseph’s obedience.'),
        ('Provision', 'The gifts of the Magi likely paid for the trip and for living in Egypt. God provided before they even knew they needed it!'),
        ('Distance', 'From Bethlehem to the Nile delta was about 250 to 300 miles, a journey of two weeks or more.')],
 callout=('Did You Know?', 'Joseph is never quoted saying a single word in the Bible. But his actions showed great faith!')),

dict(t='color', lesson=5, title='The Escape to Egypt', img='c_flight', caption='“He took the young child and his mother by night, and departed into Egypt.” (Matthew 2:14)'),
dict(**{'t': 'work',
 'lesson': 5,
 'title': 'Arise and Flee',
 'sk': 'sk_pyramids',
 'ins': 'Open your Bible to Matthew 2:13–23. Find each answer in the verse shown.',
 'blocks': [('qs',
             [('How did God’s warning reach Joseph? (verse 13)', 1),
              ('Where was the family told to go, and what danger were they escaping? (verse 13)', 2),
              ('When did Joseph leave? (verse 14)', 1),
              ('What event ended the family’s stay in Egypt? (verse 15)', 1),
              ('Which prophet wrote, “Out of Egypt have I called my son”?', 1),
              ('What did Herod do when he found out the Magi had tricked him? (verse 16)', 2),
              ('Where did the family live when they came back? (verse 23)', 1)]),
            ('box', 'Draw how God kept Yeshua safe', 2.6, 'fill')]}),
dict(**{'t': 'work',
 'lesson': 5,
 'cls': 'roomy',
 'title': 'Out of Egypt: Two Journeys',
 'sk': 'sk_pyramids',
 'ins': 'Long before Yeshua was born, the people of Israel made a journey to Egypt and back. Matthew shows that Yeshua walked the same road. Look up the verses. Draw a line from what happened to Israel to what happened to '
        'Yeshua.',
 'blocks': [('html',
             '<div class="match"><div class="mc"><div class="part" style="margin:0 0 6px">What happened to Israel</div><div class="mi"><b>1</b> <span>Jacob’s family went down to Egypt to stay alive (Genesis '
             '46:3–4)</span></div><div class="mi"><b>2</b> <span>A cruel king ordered Hebrew baby boys killed (Exodus 1:22)</span></div><div class="mi"><b>3</b> <span>God called Israel “my son” (Exodus 4:22)</span></div><div '
             'class="mi"><b>4</b> <span>God brought His people up out of Egypt (Exodus 12:51)</span></div></div><div class="mc"><div class="part" style="margin:0 0 6px">What happened to Yeshua</div><div class="mi">A cruel king '
             'ordered the baby boys of Bethlehem killed (Matthew 2:16)</div><div class="mi">God called the family back to the land of Israel (Matthew 2:19–21)</div><div class="mi">Joseph took the child down to Egypt to keep Him '
             'alive (Matthew 2:13–14)</div><div class="mi">“Out of Egypt have I called my son” (Matthew 2:15)</div></div></div>'),
            ('q', '**Write your answer:** Hosea 11:1 was first written about the people of Israel. Why does Matthew say it is also about Yeshua?', 4),
            ('html', '<div style="font-size:.95em;line-height:1.6;margin-top:6px">☐ <b>Map link:</b> Find Egypt on the Escape Route map later in this lesson and color it yellow.</div>')]}),
dict(t='work', lesson=5, title='Joseph’s Four Dreams', cls='roomy', sk='sk_dream', ins='God spoke to Joseph in four dreams, and Joseph obeyed every time! Look up each verse. Draw a line from the verse to what God told Joseph.',
 blocks=[('html', '''<div class="match"><div class="mc">
<div class="mi"><b>1</b> Matthew 1:20</div><div class="mi"><b>2</b> Matthew 2:13</div><div class="mi"><b>3</b> Matthew 2:19–20</div><div class="mi"><b>4</b> Matthew 2:22</div></div>
<div class="mc"><div class="mi">“Go into the land of Israel.”</div><div class="mi">Go to Galilee, not Judea.</div><div class="mi">“Fear not to take unto thee Mary thy wife.”</div><div class="mi">“Flee into Egypt.”</div></div></div>'''),
         ('q', 'How did Joseph respond every time God spoke to him?', 2),
         ('box', 'Draw one of Joseph’s dreams', 3.6, 'fill')]),
dict(t='illus', img='l5_egypt', cap='Safe beside the Nile'),
dict(t='text', id='l5c', kicker='Lesson Five · Reading 4', title='Safe in Egypt, Home to Nazareth', bignum='5', foot=F,
 verse='And he came and dwelt in a city called Nazareth: that it might be fulfilled which was spoken by the prophets, He shall be called a Nazarene', vref='Matthew 2:23',
 read='Matthew 2:19–23 · Luke 2:39–40',
 paras=["Mary, Joseph, and young Yeshua stayed in Egypt until Herod died. Then, once again, an angel of the Lord appeared to Joseph in a dream: “Arise, and take the young child and his mother, and go into the land of Israel: for they are dead which sought the young child’s life.”",
  "Joseph got up and brought his family back. But when he heard that Herod’s son Archelaus was ruling Judea, he was afraid to go there. God warned him in another dream, so Joseph took the family north to Galilee, to their old hometown of **Nazareth**.",
  "## The Branch Grows Up",
  "Remember Isaiah’s promise of a *Branch* growing from the stump of Jesse? The name Nazareth may come from the Hebrew word *netzer*, “branch.” The promised Branch from David’s family grew up in the “Branch Town”! Luke says “the child grew, and waxed strong in spirit, filled with wisdom: and the grace of God was upon him” (Luke 2:40).",
  "## The King Has Come",
  "Look back at the whole story. God promised a King from David’s line. He sent Gabriel to Mary and an angel to Joseph. He used an emperor’s census to bring them to Bethlehem. He revealed the Lamb of God to shepherds at the Tower of the Flock, and led Wise Men from Parthia by a star. And He protected His Son from a jealous king.",
  "Every promise came true. The King has come, and He invites everyone to follow Him."],
 notes=[('Review', 'Use the “From Promise to Nazareth” page to review all five lessons.'),
        ('Response', 'Give children a chance to pray and thank God for sending Yeshua. Invite anyone who wants to follow Yeshua to talk with you.')],
 callout=('Did You Know?', 'Joseph received four messages from God in dreams: Matthew 1:20; 2:13; 2:19–20; and 2:22. He obeyed every one!')),

dict(t='work', lesson=5, title='The Escape Route', kick='Map It', ins='Read Matthew 2:13–23. Each dot on the map is a place on the family’s journey. Write the name of each place on the line next to its number. Then connect the dots: draw a line from 1 to 2 to 3 for the escape to Egypt. For the trip home, use another color and go from 3 back to 2, then on to 4, 5, and 6.',
 blocks=[('html', '<div class="routelist">' + ''.join(f'<div><b>{i}.</b>{t}</div>' for i, t in enumerate(['Bethlehem', 'Gaza', 'Egypt', 'Joppa', 'Caesarea', 'Nazareth'], 1)) + '</div>'),
         ('img', 'map_escape_sheet', 5.45),
         ('html', '<div class="ckey"><b style="font-family:Inter;font-size:.8em;color:#1f2f5c">COLOR THE MAP:</b><span><i style="background:#cfe3f3"></i>Water: blue</span><span><i style="background:#cfe8c4"></i>Land: green</span><span><i style="background:#ecdcb8"></i>Desert: brown</span></div>')]),
dict(**{'t': 'work',
 'lesson': 5,
 'kick': 'Review',
 'title': 'From Promise to Nazareth',
 'ins': 'These twelve moments tell the whole story of the King, but they are mixed up. Write the numbers 1 to 12 in the boxes to put them in order. Use Matthew 1–2 and Luke 1–2 to check.',
 'blocks': [('html',
             '<div class="seqrow"><div class="sq"><div class="seq"><div class="bx"></div><b style="font-family:Inter;color:#c9a24a">A.</b> Mary wraps her newborn son and lays Him in a manger.</div><div class="seq"><div '
             'class="bx"></div><b style="font-family:Inter;color:#c9a24a">B.</b> Herod dies, and an angel calls the family back to Israel.</div><div class="seq"><div class="bx"></div><b '
             'style="font-family:Inter;color:#c9a24a">C.</b> Gabriel brings God’s message to Mary in Nazareth.</div><div class="seq"><div class="bx"></div><b style="font-family:Inter;color:#c9a24a">D.</b> The Magi kneel before '
             'the young child and open their treasures.</div><div class="seq"><div class="bx"></div><b style="font-family:Inter;color:#c9a24a">E.</b> God promises David a King whose throne will last forever.</div><div '
             'class="seq"><div class="bx"></div><b style="font-family:Inter;color:#c9a24a">F.</b> Simeon holds the child in the temple, and Anna gives thanks.</div><div class="seq"><div class="bx"></div><b '
             'style="font-family:Inter;color:#c9a24a">G.</b> The family settles in Nazareth, and the child grows strong.</div><div class="seq"><div class="bx"></div><b style="font-family:Inter;color:#c9a24a">H.</b> Caesar’s '
             'decree puts Joseph and Mary on the road to Bethlehem.</div><div class="seq"><div class="bx"></div><b style="font-family:Inter;color:#c9a24a">I.</b> Joseph leaves for Egypt by night with Mary and the '
             'child.</div><div class="seq"><div class="bx"></div><b style="font-family:Inter;color:#c9a24a">J.</b> A dream tells Joseph to take Mary home as his wife.</div><div class="seq"><div class="bx"></div><b '
             'style="font-family:Inter;color:#c9a24a">K.</b> A star brings the Magi to Jerusalem, and Herod is troubled.</div><div class="seq"><div class="bx"></div><b style="font-family:Inter;color:#c9a24a">L.</b> Shepherds '
             'near the Tower of the Flock hear the angel and hurry to find the child.</div></div><img src="imgc/sk_scroll.png" style="width:1.7in"></div>'),
            ('q', 'Which moment shows most clearly that God keeps His promises? Tell why.', 2),
            ('box', 'Draw that moment', 2.2, 'fill')]}),
]
