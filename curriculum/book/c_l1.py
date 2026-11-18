F = 'Beyond the Manger · Lesson 1'
def _n(x,y,t,g=False):
    return f'<div class="nd{' given' if g else ''}" style="left:{x}in;top:{y}in">{t}</div>'
def _v(x,y1,y2): return f'<div style="position:absolute;left:{x-0.01}in;top:{y1}in;width:0.02in;height:{y2-y1}in;background:#1f2f5c"></div>'
def _h(y,x1,x2): return f'<div style="position:absolute;top:{y-0.01}in;left:{x1}in;width:{x2-x1}in;height:0.02in;background:#1f2f5c"></div>'
_C, _L, _R = 2.95, 1.225, 4.675
_parts = [_n(2.325,0,'Abraham',True), _v(_C,0.42,0.6), _n(2.325,0.6,"Abraham's son"), _v(_C,1.02,1.2), _n(2.325,1.2,"Ruth's husband"),
          _v(_C,1.62,1.8), _n(2.325,1.8,"David's father"), _v(_C,2.22,2.4), _n(2.325,2.4,'King David',True),
          _v(_C,2.82,3.0), _h(3.0,_L,_R), _v(_L,3.0,3.2), _v(_R,3.0,3.2),
          _n(0.6,3.2,"David's son (Matthew)"), _n(4.05,3.2,"David's son (Luke)"), _v(_L,3.62,3.85), _v(_R,3.62,3.85),
          _n(0.6,3.85,'Legal father'), _n(4.05,3.85,'Mother'), _v(_L,4.27,4.45), _v(_R,4.27,4.45), _h(4.45,_L,_R), _v(_C,4.45,4.6),
          _n(2.325,4.6,'Yeshua',True),
          '<div style="position:absolute;left:0.35in;top:2.62in;width:1.75in;font-family:Inter;font-size:7.5pt;color:#c9a24a;font-weight:800;text-align:center">LEGAL RIGHT · MATTHEW 1</div>',
          '<div style="position:absolute;left:3.8in;top:2.62in;width:1.75in;font-family:Inter;font-size:7.5pt;color:#c9a24a;font-weight:800;text-align:center">BLOOD RIGHT · LUKE 3</div>']
TREE = '<div class="tree" style="height:5.1in"><img class="treesk" src="imgc/sk_tree.png">' + ''.join(_parts) + '</div>'

def _hw(kind, words):
    """handwriting guide row as SVG: words = list of (text, style) where style in solid|trace|''"""
    W, H = 566, 92
    if kind == 'heb':
        top, mid, base, fs, fam = 16, 46, 76, 84, 'DejaVu Sans'
    else:
        top, mid, base, fs, fam = 26, 39, 74, 64, 'Inter'
    g = f'<line x1="0" y1="{top}" x2="{W}" y2="{top}" stroke="#9aa0ae" stroke-width="1.3"/>'
    g += f'<line x1="0" y1="{mid}" x2="{W}" y2="{mid}" stroke="#b9bdc8" stroke-width="1.1" stroke-dasharray="6 5"/>'
    g += f'<line x1="0" y1="{base}" x2="{W}" y2="{base}" stroke="#5d6372" stroke-width="1.6"/>'
    xs = [W / 4, 3 * W / 4] if len(words) == 2 else [W / 2]
    for (t, st), x in zip(words, xs):
        if not t: continue
        col = '#1f2f5c' if st == 'solid' else '#c3c8d3'
        extra = ' direction="rtl" unicode-bidi="bidi-override"' if False else ''
        g += f'<text x="{x}" y="{base}" text-anchor="middle" font-family="{fam}" font-size="{fs}" fill="{col}">{t}</text>'
    return f'<svg class="hw" viewBox="0 0 {W} {H}" style="height:{H/96:.2f}in">{g}</svg>'


PAGES = [
dict(t='opener', id='l1', img='l1_open', num=1, title='The Promised King', ref='Matthew 1 · Luke 1:26–38 · Luke 2:1–5'),
dict(t='plan', num=1, title='The Promised King', bignum='1',
 passages='Matthew 1:1–25; Luke 1:26–38; Luke 2:1–5. Prophecies: Isaiah 7:14; Isaiah 11:1–2; Jeremiah 23:5–6',
 objectives=['Tell why Matthew calls Yeshua the “Son of David”',
 'Explain the difference between the legal right and the blood right to the throne',
 'Retell how Mary and Joseph each heard God’s plan',
 'Show how a Roman census fulfilled Micah 5:2'],
 prayer='Father God, thank You for keeping every promise You make. Open our ears and our hearts as we learn about the birth of Your Son, the King. In Yeshua’s name, amen.',
 materials='Bibles, pencils, crayons or colored pencils, and copies of the Lesson 1 printable pages.',
 overview='The story of the King does not begin in a manger. It begins with a promise. God told David that one of his sons would rule forever (2 Samuel 7:12–16), and the prophets held that promise in front of Israel for a thousand years. This lesson follows the promise to its doorstep. Matthew and Luke each record a family line, and together they show that Yeshua holds the throne by legal right through Joseph and by blood right through Mary. Gabriel carries the announcement to Mary in Nazareth. An angel settles Joseph’s fears in a dream. Then a decree from Rome moves the couple to Bethlehem, the very town Micah had named.',
 dyk='Matthew arranges Yeshua’s family line in three sets of fourteen generations (Matthew 1:17), and he names five women in a list that normally named only fathers.',
 flow=[('Read:', 'The Promised King'),
 ('Read:', 'Two Family Lines'),
 ('Activity:', 'Color King David · Yeshua’s Family Tree'),
 ('Read:', 'An Angel Visits Mary'),
 ('Read:', 'His Name Is Yeshua'),
 ('Activity:', 'Let’s Write Yeshua · Names of the King'),
 ('Read:', 'Betrothed: A Promise Before the Wedding'),
 ('Activity:', 'Color the Bride and Groom · The Bridegroom’s Promise'),
 ('Read:', 'The Census'),
 ('Activity:', 'Trace the Road to Bethlehem · Counted by Caesar')]),

dict(t='illus', img='l1_david', cap='David, the shepherd boy from Bethlehem'),
dict(t='text', id='l1a', kicker='Lesson One · Reading 1', title='The Promised King: Son of David', bignum='1', foot=F,
 verse='Behold, the days come, saith the LORD, that I will raise unto David a righteous Branch, and a King shall reign and prosper', vref='Jeremiah 23:5',
 read='Matthew 1:1 · 2 Samuel 7:12–16 · Isaiah 11:1–2',
 paras=["Long ago, God made a promise to King David, the shepherd boy from Bethlehem who became Israel’s greatest king. God told David that one of his descendants would sit on his throne, and that this King’s kingdom would last forever (2 Samuel 7:12–16).",
  "For hundreds of years, God’s people waited. The prophets kept the promise alive. Jeremiah said God would raise up a “righteous Branch” for David. Isaiah said a shoot would grow from the stump of Jesse, David’s father, and the Spirit of the Lord would rest on Him (Isaiah 11:1–2).",
  "## Waiting for a King",
  "By the time Yeshua was born, Israel was ruled by Rome. Many people were looking for a warrior king who would drive out the Romans with an army. The Pharisees, who carefully kept the Torah, believed they were protecting God’s ways. But God’s King came in a way almost no one expected: as a baby, born to a humble family.",
  "## “Son of David”",
  "Matthew begins his Gospel with these words: “Jesus Christ, the son of David, the son of Abraham.” Calling Yeshua the *Son of David* was a bold announcement. It was a title for the Messiah, the promised King. Matthew wanted every reader to know that Yeshua was the One God had promised."],
 notes=[('Ask the class', 'What kind of king do you think people were hoping for? How is Yeshua different?'),
        ('Fulfilled prophecy', 'Yeshua fulfilled more than 300 Old Testament prophecies. Have children find Jeremiah 23:5–6 and Isaiah 11:1–2 in their Bibles.'),
        ('Key word', '*Messiah* (Hebrew) and *Christ* (Greek) both mean “Anointed One,” the chosen King.')],
 callout=('Did You Know?', 'Jesse, David’s father, lived in Bethlehem. That is why Isaiah calls the coming King a shoot from “the stem of Jesse.”')),

dict(t='illus', img='l1_jesse', cap='“A rod out of the stem of Jesse” · Isaiah 11:1'),
dict(t='text', id='l1b', kicker='Lesson One · Reading 2', title='Two Family Lines: The Right to Be King', bignum='1', foot=F,
 verse='And there shall come forth a rod out of the stem of Jesse, and a Branch shall grow out of his roots', vref='Isaiah 11:1',
 read='Matthew 1:1–17 · Luke 3:23–38',
 paras=["The Bible gives two family trees for Yeshua. Matthew 1 and Luke 3 list His ancestors, but the lists are different. Why? Together they show that Yeshua had the right to be King through **both sides** of His family.",
  "## The Legal Right: Joseph’s Line",
  "Matthew traces the family from Abraham to King David, and then through David’s son **Solomon**, the line of the kings, all the way to Joseph. Joseph was not Yeshua’s birth father, but by adopting Him, Joseph gave Yeshua the *legal* right to David’s throne.",
  "## The Blood Right: Mary’s Line",
  "Luke traces the family through David’s son **Nathan**. Many Bible teachers believe this is Mary’s family line. Through Mary, Yeshua was truly born from David’s family. He had the *blood* right to the throne, just as Isaiah promised.",
  "## Adopted Into His Family",
  "Here is good news: just as Yeshua was adopted into Joseph’s family, God adopts all who believe into His family. “God sent forth his Son … that we might receive the adoption of sons” (Galatians 4:4–5). Those who were far away are brought near “by the blood of Christ” (Ephesians 2:13).",
  "## Three Sets of Fourteen",
  "Matthew arranges the names into three groups of fourteen generations (Matthew 1:17). Matthew even lists some women with surprising stories, like Tamar, Rahab, Ruth, and Bathsheba, showing that God’s grace reaches everyone."],
 notes=[('Legal and Blood', '**Legal right:** Joseph, Solomon’s line (Jer. 23:5–6).\n**Blood right:** Mary, Nathan’s line (Isa. 11).'),
        ('Numbers', '“14” is often linked to deliverance and salvation; “3” to divine completeness. Three sets of fourteen cover Israel’s long seasons of hardship before the Deliverer came.'),
        ('Gospel link', 'Believers are adopted into God’s family (Gal. 4:4–5) and brought near by His blood (Eph. 2:13).')],
 callout=('Did You Know?', 'Luke’s list goes all the way back to Adam, “which was the son of God” (Luke 3:38). There were about 2,000 years from Abraham to Yeshua.')),

dict(t='color', lesson=1, title='King David', img='c_david', caption='God promised that a King from David’s family would reign forever. (2 Samuel 7:16)'),
dict(t='work', lesson=1, title='Yeshua’s Family Tree', ins='Read Matthew 1:1–17 and Luke 3:23–38. Use the word bank to fill in the empty boxes of Yeshua’s family tree.',
 blocks=[('bank', ['Isaac', 'Boaz', 'Jesse', 'Solomon', 'Nathan', 'Joseph', 'Mary']), ('html', TREE),
         ('q', 'Through which son of David did Joseph’s family line come?', 1), ('q', 'Through which son of David did Mary’s family line come?', 1), ('q', 'How did Yeshua get the legal right to be King? How did He get the blood right?', 2)]),

dict(t='illus', img='l1_angel', cap='Nazareth, Galilee'),
dict(t='text', id='l1c', kicker='Lesson One · Reading 3', title='An Angel Visits Mary', bignum='1', foot=F,
 verse='Behold, a virgin shall conceive, and bear a son, and shall call his name Immanuel', vref='Isaiah 7:14',
 read='Luke 1:26–38 · Matthew 1:18–25',
 paras=["In the hill country of Galilee sat a little village called Nazareth. In this quiet place lived a young woman named Mary, who was promised in marriage to a carpenter named Joseph.",
  "One day God sent the angel Gabriel to Mary. “Greetings, you who are highly favored! The Lord is with you,” he said. Mary was troubled, but Gabriel told her not to be afraid. She would have a baby boy, the Son of the Most High, and she was to call Him *Yeshua*. “The Lord God shall give unto him the throne of his father David,” Gabriel said, “and of his kingdom there shall be no end” (Luke 1:32–33).",
  "“How can this be?” Mary asked. Gabriel explained that the Holy Spirit would come upon her, so the child would be called the Son of God. “For with God nothing shall be impossible.” Mary answered with a trusting heart: “Behold the handmaid of the Lord; be it unto me according to thy word.”",
  "## Joseph’s Dream",
  "When Joseph learned that Mary was expecting a baby, he was worried and did not know what to do. Then an angel spoke to him in a dream: the baby was from the Holy Spirit, and He would save His people from their sins. Joseph woke up, obeyed God, and took Mary to be his wife."],
 notes=[('Before you begin', 'Open in prayer, asking God to prepare the children’s hearts to be open and ready to receive understanding of today’s lesson.'),
        ('“Son of David”', 'Gabriel’s words point straight back to God’s promise to David. Ask: which promise from Reading 1 is coming true?'),
        ('Mary’s faith', 'Mary did not understand everything, but she trusted God. Ask: When is it hard to trust God?')],
 callout=('Did You Know?', ['This would not be the only time God would speak to Joseph through a dream! God spoke to him in four dreams in all (Matthew 1:20; 2:13; 2:19–20; 2:22).', 'The Hebrew word for salvation is ישועה (*yeshu’ah*), which means deliverance or rescue. It comes from the root ישע (Y-Sh-A), meaning to save or rescue. Listen closely: it sounds just like His name, *Yeshua*!'])),

dict(t='illus', img='l1_dream', cap='An angel speaks to Joseph in a dream'),
dict(t='text', id='l1d', kicker='Lesson One · Reading 4', title='His Name Is Yeshua', bignum='1', foot=F,
 verse='And she shall bring forth a son, and thou shalt call his name JESUS: for he shall save his people from their sins', vref='Matthew 1:21',
 read='Matthew 1:20–25 · Isaiah 49:6',
 paras=["In Bible times, a name was more than a label. It often told something about who a person was or what God would do through them. So when the angel told Joseph what to name the baby, the name carried a message.",
  "Mary and Joseph did not choose this name. Heaven chose it! In Hebrew, the name is **Yeshua**. This is a shorter form of *Yehoshua* (Joshua). It is made up from two Hebrew words: “Yah,” a shortened form of Yahweh, the personal name of God, and the verb “Yasha,” meaning to deliver, save or rescue. Put together, the meaning is “God is Salvation.” The angel even explained it: “for he shall save his people from their sins.”",
  "- **Yah** (יָה): a shortened form of Yahweh, the personal name of God.",
  "- **Yasha** (יָשַׁע): a verb meaning to deliver, save, or rescue.",
  "## From Yeshua to Jesus",
  "How did Yeshua become “Jesus”? The New Testament was written in Greek. Greek has no “sh” sound, and Greek names for men end in “s,” so Yeshua was written *Iēsous*. Latin kept it as *Iesus*. The first King James Bible, printed in 1611, still spelled it “Iesus.” The letter J came later. The spelling changed. The Person and the meaning never did.",
  "## Immanuel: God With Us",
  "Matthew explains that all this happened to fulfill Isaiah’s prophecy: the virgin would have a son, and they would call Him *Immanuel*, which means “God with us” (Matthew 1:23). Yeshua is both. He is the God who saves, and the God who came to be with His people."],
 notes=[('Name study', '*Yeshua* is the same name as *Joshua* in the Old Testament. Joshua led Israel into the Promised Land; Yeshua leads His people into God’s kingdom.'),
        ('Joseph’s obedience', 'Joseph “did as the angel of the Lord had bidden him” (Matt. 1:24). Ask: How did Joseph show faith?'),
        ('Activity tip', 'Hebrew is written and read from the right side of the page to the left. Show the class before they try the writing activity.')],
 callout=('Did You Know?', 'The name *Yeshua* appears in Hebrew as ישוע. It is made from four Hebrew letters: Yod, Shin, Vav, and Ayin.')),

dict(t='work', lesson=1, title='Let’s Write Yeshua!', ins='Yeshua’s name in Hebrew has four letters. Hebrew runs the opposite way from English, so start at the right side and move left. Trace the gray letters, then write the name on your own.',
 blocks=[('html', '<div class="letters"><div><div class="hl">י</div><div class="nm">Yod · Y</div></div><div><div class="hl">ש</div><div class="nm">Shin · SH</div></div><div><div class="hl">ו</div><div class="nm">Vav · U</div></div><div><div class="hl">ע</div><div class="nm">Ayin · A</div></div></div>'),
         ('html', _hw('heb', [('ישוע', 'solid'), ('ישוע', 'trace')]) + _hw('heb', [('ישוע', 'trace'), ('ישוע', 'trace')]) + _hw('heb', [])),
         ('html', '<div class="qt" style="margin-top:6px">Now write His name in English:</div>' + _hw('en', [('Yeshua', 'solid'), ('Yeshua', 'trace')]) + _hw('en', []) + _hw('en', []))]),
dict(t='work', lesson=1, title='Names of the King', cls='roomy', sk='sk_crown', ins='Read Matthew 1:21–23, Luke 1:32, and Matthew 1:1. Draw a line from each name to its meaning. Then answer the question.',
 blocks=[('html', '''<div class="match"><div class="mc">
<div class="mi"><b>1</b> Yeshua</div><div class="mi"><b>2</b> Immanuel</div><div class="mi"><b>3</b> Son of David</div><div class="mi"><b>4</b> Messiah (Christ)</div><div class="mi"><b>5</b> Son of the Most High</div></div>
<div class="mc"><div class="mi">God with us</div><div class="mi">The Anointed One, the chosen King</div><div class="mi">God saves</div><div class="mi">The Son of God</div><div class="mi">The King from David’s royal family</div></div></div>'''),
         ('q', 'Which name of the King is your favorite? Why?', 2),
         ('box', 'Draw a picture of the angel speaking to Joseph in his dream', 3.2, 'fill')]),

dict(t='illus', img='l1_wedding', cap='A promise made before the wedding'),
dict(**{'t': 'text',
 'id': 'l1f',
 'kicker': 'Lesson One · Reading 5',
 'title': 'Betrothed: A Promise Before the Wedding',
 'bignum': '1',
 'foot': 'Beyond the Manger · Lesson 1',
 'verse': 'When as his mother Mary was espoused to Joseph, before they came together, she was found with child of the Holy Ghost',
 'vref': 'Matthew 1:18',
 'read': 'Matthew 1:18–25 · Genesis 29:27 · John 14:2–3 · Revelation 19:7',
 'paras': ['Matthew says Mary was “espoused” to Joseph. That is betrothal, and in Israel a betrothal was far more than an engagement. To understand what Joseph faced, it helps to see how the Bible describes a marriage being '
           'made.',
           'A covenant came first. The two families agreed together, and the groom’s side gave a bride price, or “dowry” (Genesis 34:12; Exodus 22:16–17). From that day the couple belonged to each other by covenant. A covenant '
           'is a binding and unbreakable commitment. Scripture already calls a betrothed woman a “wife” (Deuteronomy 22:23–24). That is why Matthew calls Joseph “her husband” before the wedding, and why ending a betrothal took a '
           'divorce (Matthew 1:19).',
           'Then came the waiting. The bride stayed in her father’s house and made herself ready. The groom went home to prepare a place for her. Neither knew the exact day the waiting would end.',
           'When all was ready, the groom came for his bride with his friends, often at night, and the bride’s companions met him with burning lamps (Matthew 25:1–10). He brought her to his home, and the families feasted for a '
           'week (Genesis 29:27; Judges 14:12).',
           'Mary and Joseph were in the waiting period. The covenant was made, but Joseph had not yet brought Mary home. Then Mary was found to be with child. Joseph was a just man, and he was also a kind one. He planned to end '
           'the betrothal quietly. God stopped him with a dream, and Joseph “took unto him his wife” (Matthew 1:24).',
           '**Why it matters.** Yeshua used this same picture for Himself. “I go to prepare a place for you. And if I go and prepare a place for you, I will come again, and receive you unto myself” (John 14:2–3). He is the '
           'Bridegroom. His people are in the waiting, making themselves ready. The story ends with a feast: “the marriage of the Lamb is come, and his wife hath made herself ready” (Revelation 19:7).'],
 'notes': [('Key words', 'Later Jewish teachers named the two steps *erusin* (the betrothal) and *nisuin* (the bringing home). The written marriage contract is called a *ketubah*.'),
           ('Picture and fulfillment', 'Covenant made → the cross.\nThe waiting → today.\nThe groom returns → John 14:3.\nThe feast → Revelation 19:7–9.'),
           ('Discuss', 'Joseph obeyed before he understood everything. What made that hard? What made it right?')],
 'callout': ('Did You Know?', 'Yeshua’s first miracle took place at a wedding feast in Cana, only a few miles from Nazareth (John 2:1–11).')}),

dict(t='color', lesson=1, title='The Bride and Groom', img='c_wedding', caption='When the groom brought his bride home, the families feasted for a week. (Judges 14:12)'),
dict(**{'t': 'work',
 'lesson': 1,
 'title': 'The Bridegroom’s Promise',
 'sk': 'sk_wedding',
 'skh': 1.5,
 'ins': 'Read “Betrothed: A Promise Before the Wedding” and Matthew 1:18–25. Answer the questions below.',
 'blocks': [('qs',
             [('What word does Matthew 1:18 use for Mary and Joseph’s promise to marry?', 1),
              ('Why does Matthew call Joseph “her husband” before the wedding?', 2),
              ('What did the groom do during the waiting time? What did the bride do?', 2),
              ('How did the bride’s companions greet the groom when he came? (Matthew 25:1)', 1),
              ('How many days did a wedding feast last? (Judges 14:12)', 1),
              ('What did Joseph do after the angel spoke to him? (Matthew 1:24)', 2)]),
            ('q', 'Read John 14:2–3 and Revelation 19:7. How is Yeshua like a bridegroom?', 3)]}),

dict(t='illus', img='l1_census', cap='A decree from Caesar Augustus'),
dict(t='text', kicker='Lesson One · Reading 6', title='The Census', bignum='1', foot=F,
 verse='And it came to pass in those days, that there went out a decree from Caesar Augustus, that all the world should be taxed', vref='Luke 2:1',
 read='Luke 2:1–5 · Micah 5:2',
 paras=["Far away in the city of Rome, the emperor **Caesar Augustus** made a law. Everyone in the Roman Empire had to be counted in a census and registered for taxes. Each family had to go to its own hometown to sign up.",
  "Joseph belonged to the family of King David, and David’s hometown was **Bethlehem** in Judea. So Joseph had to leave Nazareth and travel south to Bethlehem, and he took Mary with him, even though her baby would soon be born.",
  "## A Long Journey",
  "The trip from Nazareth to Bethlehem was about 90 miles. Traveling on foot, perhaps with a donkey to carry supplies, it would have taken about a week. Many travelers followed the road along the Jordan River valley and then climbed up through the hills past Jerusalem.",
  "## God Was in Charge",
  "Caesar Augustus thought he was in control of the whole world. But God was using even an emperor’s law to keep His promise! Seven hundred years earlier, the prophet Micah had written that the Ruler of Israel would be born in Bethlehem (Micah 5:2). The census brought Mary and Joseph to exactly the right town at exactly the right time.",
  "So with the baby’s birth only weeks away, Joseph and Mary packed what they could carry and started south."],
 notes=[('God’s timing', 'Galatians 4:4 says God sent His Son “when the fulness of the time was come.” Ask: How did God use the census?'),
        ('Rulers', 'Caesar Augustus ruled Rome from 27 BC to AD 14. Quirinius governed Syria (Luke 2:2).'),
        ('Map it', 'Trace the route from Nazareth to Bethlehem on a map of Israel.')],
 callout=('Did You Know?', 'Bethlehem means “House of Bread.” The One who called Himself “the bread of life” (John 6:35) was born in the House of Bread!')),

dict(t='work', lesson=1, title='The Road to Bethlehem', kick='Color and Trace', ins='Mary and Joseph traveled about 90 miles from Nazareth to Bethlehem. Trace the dotted line with a crayon from START to FINISH to follow their journey. Color the water blue and the land green or brown. Then color Mary, Joseph, and the donkey!',
 blocks=[('img', 'map_journey', 6.9)]),
dict(**{'t': 'work',
 'lesson': 1,
 'title': 'Counted by Caesar',
 'ins': 'Open your Bible to Luke 2:1–5. Find each answer in the verse shown.',
 'blocks': [('qs',
             [('Verse 1 names the ruler who sent out the decree. Who was he?', 1),
              ('Who was governor of Syria at this time? (verse 2)', 1),
              ('Which town did Joseph’s family line take him to, and why that town? (verse 4)', 2),
              ('Who made the journey with Joseph? (verse 5)', 1),
              ('About how far was it from Nazareth to Bethlehem?', 1),
              ('Which prophet said the Ruler of Israel would be born in Bethlehem?', 1)]),
            ('img', 'c_journey_fig', 2.6)]}),
]
