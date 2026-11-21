from c_common import *
from c_common import _hw, _maze, _wordsearch, _code
F = 'Beyond the Manger · Lesson 7'

PAGES = [
dict(t='opener', img='l5_open', num=7, title='Out of Egypt, Home to Nazareth', ref='Matthew 2:13–23 · Hosea 11:1 · Isaiah 11:1'),
dict(**{'t': 'plan',
 'num': 7,
 'title': 'Out of Egypt, Home to Nazareth',
 'bignum': '7',
 'passages': 'Matthew 2:13–23; Hosea 11:1; Jeremiah 31:15; Isaiah 11:1',
 'objectives': ['Explain why God sent the family to Egypt',
                'Show how Yeshua’s journey matches the journey of Israel',
                'Tell how God brought the family safely home to Nazareth',
                'Tell what kind of town Nazareth was and why that matters'],
 'prayer': 'Heavenly Father, thank You for watching over Yeshua and His family. Thank You that You watch over us too. Help us trust You and obey You quickly, like Joseph did. In Yeshua’s name, amen.',
 'materials': 'Bibles, pencils, crayons, an atlas or globe, and copies of the Lesson 7 printable pages.',
 'overview': 'Matthew 2 records three more dreams given to Joseph, and each one moves the family a step ahead of danger. The first sends them to Egypt by night, beyond Herod’s reach. Herod’s rage falls on Bethlehem, and Matthew '
             'hears in it Jeremiah’s words about Rachel weeping. After Herod’s death a second dream calls the family back to Israel, and a third turns them away from Judea toward Galilee. Matthew marks the moves with prophecy: '
             '“Out of Egypt have I called my son” and “He shall be called a Nazarene.” The lesson ends in Nazareth, a village the Old Testament never names, where the promised Branch grew up.',
 'dyk': 'Israel went down to Egypt as a family and came out as a nation God called “my son” (Exodus 4:22). Yeshua traveled the same road, and Matthew uses the same words for Him.',
 'flow': [('Read:', 'Flight to Egypt'),
          ('Activity:', 'Color the Escape · Arise and Flee'),
          ('Read:', 'Safe in Egypt, Home to Nazareth'),
          ('Activity:', 'Out of Egypt: Two Journeys · Map: The Escape Route'),
          ('Read:', 'Can Any Good Thing Come Out of Nazareth?'),
          ('Activity:', 'Color a Man of Nazareth · Come and See Nazareth · Joseph’s Four Dreams · From Promise to Nazareth')]}),

dict(t='illus', img='l5_flight', cap='The flight to Egypt'),
dict(t='text', kicker='Lesson Seven · Reading 1', title='Flight to Egypt', bignum='7', foot=F,
 verse='When he arose, he took the young child and his mother by night, and departed into Egypt', vref='Matthew 2:14',
 read='Matthew 2:13–18 · Hosea 11:1 · Jeremiah 31:15',
 paras=["After the Wise Men left, an angel of the Lord appeared to Joseph in a dream. “Arise, and take the young child and his mother, and flee into Egypt, and be thou there until I bring thee word: for Herod will seek the young child to destroy him.”",
  "Joseph did not wait until morning. He got up, took Yeshua and Mary, and left **that very night**. This was the third time Joseph obeyed God’s message in a dream, and each time he obeyed right away.",
  "## Why Egypt?",
  "Egypt was outside Herod’s kingdom, so Herod could not reach them there. It was also home to many Jewish families, especially in the great city of Alexandria. And God had a reason in His Word: the prophet Hosea had written, “Out of Egypt have I called my son” (Hosea 11:1). Long ago, God brought Israel out of Egypt. Now His own Son would come out of Egypt too.",
  "## Herod’s Anger",
  "When Herod realized the Wise Men had tricked him, he became furious. He ordered his soldiers to put to death every boy in and around Bethlehem who was two years old or younger. It was a terrible and cruel act, and Matthew says it fulfilled Jeremiah’s words about Rachel weeping for her children (Jeremiah 31:15).",
  "But Herod could not stop God’s plan. The young King was already safe in Egypt, protected by His Father in heaven."],
 notes=[('Handle with care', 'Be gentle when sharing Herod’s cruelty with young children. Focus on God’s protection and Joseph’s obedience.'),
        ('Provision', 'The gifts of the Magi likely paid for the trip and for living in Egypt. God provided before they even knew they needed it!'),
        ('Distance', 'From Bethlehem to the Nile delta was about 250 to 300 miles, a journey of two weeks or more.')],
 callout=('Did You Know?', 'Joseph is never quoted saying a single word in the Bible. But his actions showed great faith!')),

dict(t='color', lesson=7, title='The Escape to Egypt', img='c_flight', caption='“He took the young child and his mother by night, and departed into Egypt.” (Matthew 2:14)'),
dict(**{'t': 'work',
 'lesson': 7,
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
dict(t='illus', img='l5_egypt', cap='Safe beside the Nile'),
dict(t='text', kicker='Lesson Seven · Reading 2', title='Safe in Egypt, Home to Nazareth', bignum='7', foot=F,
 verse='And he came and dwelt in a city called Nazareth: that it might be fulfilled which was spoken by the prophets, He shall be called a Nazarene', vref='Matthew 2:23',
 read='Matthew 2:19–23 · Luke 2:39–40',
 paras=["Mary, Joseph, and young Yeshua stayed in Egypt until Herod died. Then, once again, an angel of the Lord appeared to Joseph in a dream: “Arise, and take the young child and his mother, and go into the land of Israel: for they are dead which sought the young child’s life.”",
  "Joseph got up and brought his family back. But when he heard that Herod’s son Archelaus was ruling Judea, he was afraid to go there. God warned him in another dream, so Joseph took the family north to Galilee, to their old hometown of **Nazareth**.",
  "## The Branch Grows Up",
  "Remember Isaiah’s promise of a *Branch* growing from the stump of Jesse? The name Nazareth may come from the Hebrew word *netzer*, “branch.” The promised Branch from David’s family grew up in the “Branch Town”! Luke says “the child grew, and waxed strong in spirit, filled with wisdom: and the grace of God was upon him” (Luke 2:40).",
  "## The King Has Come",
  "Look back at the whole story. God promised a King from David’s line. He sent Gabriel to Mary and an angel to Joseph. He used an emperor’s census to bring them to Bethlehem. He revealed the Lamb of God to shepherds at the Tower of the Flock, and led Wise Men from Parthia by a star. And He protected His Son from a jealous king.",
  "Every promise came true. The King has come, and He invites everyone to follow Him."],
 notes=[('Review', 'Use the “From Promise to Nazareth” page to review all seven lessons.'),
        ('Response', 'Give children a chance to pray and thank God for sending Yeshua. Invite anyone who wants to follow Yeshua to talk with you.')],
 callout=('Did You Know?', 'Joseph received four messages from God in dreams: Matthew 1:20; 2:13; 2:19–20; and 2:22. He obeyed every one!')),

dict(**{'t': 'work',
 'lesson': 7,
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
            ('html', '<div style="font-size:.95em;line-height:1.6;margin-top:6px">☐ <b>Map link:</b> Find Egypt on the Escape Route map on the next page and color it yellow.</div>')]}),
dict(t='work', lesson=7, title='The Escape Route', kick='Map It', ins='Read Matthew 2:13–23. Each dot on the map is a place on the family’s journey. Write the name of each place on the line next to its number. Then connect the dots: draw a line from 1 to 2 to 3 for the escape to Egypt. For the trip home, use another color and go from 3 back to 2, then on to 4, 5, and 6.',
 blocks=[('html', '<div class="routelist">' + ''.join(f'<div><b>{i}.</b>{t}</div>' for i, t in enumerate(['Bethlehem', 'Gaza', 'Egypt', 'Joppa', 'Caesarea', 'Nazareth'], 1)) + '</div>'),
         ('img', 'map_escape_sheet', 5.45),
         ('html', '<div class="ckey"><b style="font-family:Inter;font-size:.8em;color:#1f2f5c">COLOR THE MAP:</b><span><i style="background:#cfe3f3"></i>Water: blue</span><span><i style="background:#cfe8c4"></i>Land: green</span><span><i style="background:#ecdcb8"></i>Desert: brown</span></div>')]),
dict(t='illus', img='l1_nazareth', cap='The village of Nazareth'),
dict(**{'t': 'text',
 'id': 'l5n',
 'kicker': 'Lesson Seven · Reading 3',
 'title': 'Can Any Good Thing Come Out of Nazareth?',
 'bignum': '7',
 'foot': F,
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
 'notes': [('Key word', 'Isaiah 11:1 promises a “Branch” from Jesse’s roots. The Hebrew word is *netzer*. Many teachers believe the name Nazareth comes from the same word.'),
           ('Prophecy and fulfillment', 'Isaiah 53:2 → John 1:46. The Messiah would not look important. Nathanael’s question proves the prophecy true.'),
           ('Ask', 'Philip did not argue with Nathanael. He said, “Come and see.” Who could be invited to come and see Yeshua this week?')],
 'callout': ('Did You Know?', 'Nathanael changed his mind the same day. After meeting Yeshua he said, “Thou art the Son of God; thou art the King of Israel” (John 1:49).')}),

dict(t='color', lesson=7, title='A Man of Nazareth', img='c_farmer', caption='Families in Nazareth grew grain, olives and grapes on the hillsides.'),
dict(**{'t': 'work',
 'lesson': 7,
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

dict(t='work', lesson=7, title='Joseph’s Four Dreams', cls='roomy', sk='sk_dream', ins='God spoke to Joseph in four dreams, and Joseph obeyed every time! Look up each verse. Draw a line from the verse to what God told Joseph.',
 blocks=[('html', '''<div class="match"><div class="mc">
<div class="mi"><b>1</b> Matthew 1:20</div><div class="mi"><b>2</b> Matthew 2:13</div><div class="mi"><b>3</b> Matthew 2:19–20</div><div class="mi"><b>4</b> Matthew 2:22</div></div>
<div class="mc"><div class="mi">“Go into the land of Israel.”</div><div class="mi">Go to Galilee, not Judea.</div><div class="mi">“Fear not to take unto thee Mary thy wife.”</div><div class="mi">“Flee into Egypt.”</div></div></div>'''),
         ('q', 'How did Joseph respond every time God spoke to him?', 2),
         ('box', 'Draw one of Joseph’s dreams', 3.6, 'fill')]),
dict(**{'t': 'work',
 'lesson': 7,
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
