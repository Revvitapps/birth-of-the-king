F = 'Birth of the King · Lesson 1'
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
TREE = '<div class="tree" style="height:5.1in">' + ''.join(_parts) + '</div>'

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
 objectives=['Why Yeshua is called the “Son of David”', 'How Yeshua had both the legal right and the blood right to be King',
             'How Mary and Joseph learned God’s plan', 'Why Mary and Joseph traveled to Bethlehem'],
 prayer='Father God, thank You for keeping every promise You make. Open our ears and our hearts as we learn about the birth of Your Son, the King. In Yeshua’s name, amen.',
 materials='Bibles, pencils, crayons or colored pencils, and copies of the Lesson 1 printable pages.',
 overview='Long before Yeshua was born, God promised that a King would come from the family of David. The prophets Isaiah and Jeremiah wrote about this King hundreds of years ahead of time. In this lesson, children will discover how Yeshua belonged to David’s royal family through both Joseph and Mary. They will hear how the angel Gabriel visited Mary in the small village of Nazareth, how an angel spoke to Joseph in a dream, and why a Roman census sent the young couple on the road to Bethlehem, the city of David.',
 dyk='Yeshua fulfilled more than 300 prophecies from the Old Testament! Isaiah and Micah told about His birth hundreds of years before it happened (Isaiah 7:14; Micah 5:2).',
 flow=[('Read:', 'The Promised King'), ('Read:', 'Two Family Lines'), ('Activity:', 'Color King David · Yeshua’s Family Tree'),
       ('Read:', 'An Angel Visits Mary'), ('Read:', 'His Name Is Yeshua'), ('Activity:', 'Let’s Write Yeshua · Names of the King'),
       ('Read:', 'Life in Nazareth'), ('Activity:', 'Color a Man of Nazareth · Nazareth Village'), ('Read:', 'A Hebrew Wedding'),
       ('Activity:', 'Color the Bride and Groom · Wedding Questions'), ('Read:', 'The Census'), ('Activity:', 'Trace the Road to Bethlehem · A Census')]),

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
 paras=["The Bible gives us two family trees for Yeshua. Matthew 1 and Luke 3 list His ancestors, but the lists are different. Why? Together they show that Yeshua had the right to be King through **both sides** of His family.",
  "## The Legal Right: Joseph’s Line",
  "Matthew traces the family from Abraham to King David, and then through David’s son **Solomon**, the line of the kings, all the way to Joseph. Joseph was not Yeshua’s birth father, but by adopting Him, Joseph gave Yeshua the *legal* right to David’s throne.",
  "## The Blood Right: Mary’s Line",
  "Luke traces the family through David’s son **Nathan**. Many Bible teachers believe this is Mary’s family line. Through Mary, Yeshua was truly born from David’s family. He had the *blood* right to the throne, just as Isaiah promised.",
  "## Adopted Into His Family",
  "Here is good news for us: just as Yeshua was adopted into Joseph’s family, God adopts us into His family. “God sent forth his Son … that we might receive the adoption of sons” (Galatians 4:4–5). We who were far away are brought near “by the blood of Christ” (Ephesians 2:13).",
  "## Three Sets of Fourteen",
  "Matthew arranges the names into three groups of fourteen generations (Matthew 1:17). Matthew even lists some women with surprising stories, like Tamar, Rahab, Ruth, and Bathsheba, showing that God’s grace reaches everyone."],
 notes=[('Legal and Blood', '**Legal right:** Joseph, Solomon’s line (Jer. 23:5–6).\n**Blood right:** Mary, Nathan’s line (Isa. 11).'),
        ('Numbers', '“14” is often linked to deliverance and salvation; “3” to divine completeness. Three sets of fourteen cover Israel’s long seasons of hardship before the Deliverer came.'),
        ('Gospel link', 'We are adopted into God’s family (Gal. 4:4–5) and brought near by His blood (Eph. 2:13).')],
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
  "To His family and friends, the baby was called *Yehoshua*, or in its shorter form, **Yeshua**. The name means “God is salvation” or “God saves.” Every time someone called His name, they were saying what He came to do: “He shall save his people from their sins.”",
  "## A Hebrew Name",
  "Mary and Joseph were Hebrews, so it was natural for them to give their son a Hebrew name. Later, when the good news spread to people who spoke Greek, His name was written *Iēsous*. From there it came into Latin and, many centuries later, into English as *Jesus*. In fact, the letter “J” was not used in English until about 500 years ago!",
  "## Immanuel: God With Us",
  "Matthew tells us that all this happened to fulfill Isaiah’s prophecy: the virgin would have a son, and they would call Him *Immanuel*, which means “God with us” (Matthew 1:23). Yeshua is both. He is the God who saves, and the God who came to be with us."],
 notes=[('Name study', '*Yeshua* is the same name as *Joshua* in the Old Testament. Joshua led Israel into the Promised Land; Yeshua leads us into God’s kingdom.'),
        ('Joseph’s obedience', 'Joseph “did as the angel of the Lord had bidden him” (Matt. 1:24). Ask: How did Joseph show faith?'),
        ('Activity tip', 'Hebrew is read from right to left. Show the class before they try the writing page.')],
 callout=('Did You Know?', 'The name *Yeshua* appears in Hebrew as ישוע. It is made from four Hebrew letters: Yod, Shin, Vav, and Ayin.')),

dict(t='work', lesson=1, title='Let’s Write Yeshua!', ins='Yeshua’s name in Hebrew is made of four letters. Remember: Hebrew is read from RIGHT to LEFT. Trace the gray letters, then try writing the name on your own.',
 blocks=[('html', '<div class="letters"><div><div class="hl">י</div><div class="nm">Yod · Y</div></div><div><div class="hl">ש</div><div class="nm">Shin · SH</div></div><div><div class="hl">ו</div><div class="nm">Vav · U</div></div><div><div class="hl">ע</div><div class="nm">Ayin · A</div></div></div>'),
         ('html', _hw('heb', [('ישוע', 'solid'), ('ישוע', 'trace')]) + _hw('heb', [('ישוע', 'trace'), ('ישוע', 'trace')]) + _hw('heb', [])),
         ('html', '<div class="qt" style="margin-top:6px">Now write His name in English:</div>' + _hw('en', [('Yeshua', 'solid'), ('Yeshua', 'trace')]) + _hw('en', []) + _hw('en', []))]),
dict(t='work', lesson=1, title='Names of the King', cls='roomy', sk='sk_crown', ins='Read Matthew 1:21–23, Luke 1:32, and Matthew 1:1. Draw a line from each name to its meaning. Then answer the question.',
 blocks=[('html', '''<div class="match"><div class="mc">
<div class="mi"><b>1</b> Yeshua</div><div class="mi"><b>2</b> Immanuel</div><div class="mi"><b>3</b> Son of David</div><div class="mi"><b>4</b> Messiah (Christ)</div><div class="mi"><b>5</b> Son of the Most High</div></div>
<div class="mc"><div class="mi">God with us</div><div class="mi">The Anointed One, the chosen King</div><div class="mi">God saves</div><div class="mi">The Son of God</div><div class="mi">The King from David’s royal family</div></div></div>'''),
         ('q', 'Which name of the King is your favorite? Why?', 2),
         ('box', 'Draw a picture of the angel speaking to Joseph in his dream', 3.2, 'fill')]),

dict(t='illus', img='l1_nazareth', cap='The village of Nazareth'),
dict(t='text', id='l1e', kicker='Lesson One · Reading 5', title='Life in Nazareth', bignum='1', foot=F,
 verse='And he came and dwelt in a city called Nazareth: that it might be fulfilled which was spoken by the prophets, He shall be called a Nazarene', vref='Matthew 2:23',
 read='Luke 1:26 · Luke 2:39–40 · John 1:46',
 paras=["When Mary and Joseph were growing up, Nazareth was a small farming village in the hills of Galilee. Fewer than 200 people lived there. It was so small and unimportant that one man later asked, “Can there any good thing come out of Nazareth?” (John 1:46).",
  "## Homes and Gardens",
  "Most families in Nazareth had a strip of land where they grew vegetables. Their homes were built of mud brick or stone. A house usually had two or three rooms and an open courtyard. Life centered on the home. That is where families talked about the news, their faith, and the events of the day, often while they shared a meal.",
  "## Mealtimes",
  "Hebrew families usually ate two meals a day. The first was in the late morning or around midday, and the second was in the evening at home. Meals were simple: bread, lentil stew, fruit, and eggs. Families also enjoyed fish, goat meat, cheese, olives, and wine. Red meat was saved for special occasions. Instead of sitting on chairs at a table, people often reclined on cushions on the floor to eat.",
  "## God Chose a Humble Place",
  "God could have chosen a palace in Jerusalem. Instead, He chose a young woman from a tiny village and a carpenter who worked with his hands. God loves to do great things through humble people."],
 notes=[('Compare and share', 'Ask children to compare a day in Nazareth with their own day: food, homes, chores.'),
        ('“Nazarene”', 'The name Nazareth may come from the Hebrew word *netzer*, “branch.” It connects to Isaiah 11:1, the Branch from Jesse!'),
        ('Galilee', 'Nazareth was about 65 miles north of Jerusalem.')],
 callout=('Did You Know?', 'Archaeologists have found the remains of simple houses, olive presses, and stone water cisterns in Nazareth from the time of Yeshua.')),

dict(t='color', lesson=1, title='A Man of Nazareth', img='c_farmer', caption='Most families in Nazareth grew their own vegetables on a small strip of land.'),
dict(t='work', lesson=1, title='Nazareth Village', sk='sk_bread', ins='Read “Life in Nazareth” again, then answer the questions below.',
 blocks=[('qs', [('About how many people lived in Nazareth?', 1), ('Where did Hebrew families grow their own food?', 2),
                 ('What were Hebrew homes made of?', 1), ('What kinds of food did Hebrew families like to eat at mealtimes?', 2),
                 ('How did people sit when they ate a meal?', 1), ('Why do you think God chose a small village like Nazareth?', 2)]),
         ('box', 'Draw your favorite meal from Nazareth', 4.0, 'fill')]),

dict(t='illus', img='l1_wedding', cap='Signing the marriage contract'),
dict(t='text', kicker='Lesson One · Reading 6', title='A Hebrew Wedding', bignum='1', foot=F,
 verse='Then Joseph being raised from sleep did as the angel of the Lord had bidden him, and took unto him his wife', vref='Matthew 1:24',
 read='Matthew 1:18–25 · Luke 1:27',
 paras=["Weddings in ancient Israel were very different from weddings today. A Hebrew wedding happened in two big steps, often about a year apart.",
  "## Step One: The Betrothal",
  "In Hebrew tradition, the father of the groom often chose a bride for his son. The groom’s family and the bride’s father agreed on a bride price and signed a marriage contract called a **ketubah**. Once the ketubah was signed, the couple was legally husband and wife, but they did not live together yet. If they wanted to separate, they needed a divorce, and the groom would lose the price he had paid.",
  "## Step Two: The Wedding Feast",
  "During the waiting time, the groom prepared a home for his bride, often a room added onto his father’s house. When the groom’s father saw that everything was ready, he told his son to go and get his bride! The groom brought her home for a wedding feast that could last up to seven days. This final step was called the **nisuin**.",
  "## Mary and Joseph",
  "Mary and Joseph were in the first step, betrothed but not yet living together, when Mary was found to be expecting a baby. That is why Joseph was so troubled. After the angel explained God’s plan in a dream, Joseph took Mary to be his wife."],
 notes=[('A picture of Yeshua', 'Yeshua used wedding pictures when He spoke of His return: “I go to prepare a place for you” (John 14:2–3). Like a groom, He is preparing a home for His people.'),
        ('Key words', '*Ketubah:* marriage contract.\n*Nisuin:* the final wedding step when the bride is brought home.'),
        ('Discuss', 'Why was Joseph’s choice to obey God brave?')],
 callout=('Did You Know?', 'Joseph planned to end the betrothal quietly so Mary would not be shamed (Matthew 1:19). The Bible calls him “a just man.”')),

dict(t='color', lesson=1, title='The Bride and Groom', img='c_wedding', caption='A Hebrew wedding feast could last up to seven days!'),
dict(t='work', lesson=1, title='A Hebrew Wedding', sk='sk_wedding', ins='Read “A Hebrew Wedding” and Matthew 1:18–25. Answer the questions below.',
 blocks=[('qs', [('Who usually selected a bride for a young man?', 1), ('What was the marriage contract called?', 1),
                 ('What did the groom do while he waited for his wedding day?', 2),
                 ('What instruction did the groom’s father give when he saw everything was ready?', 2),
                 ('How long could a wedding feast last?', 1), ('What did Joseph do after the angel spoke to him in a dream?', 2)]),
         ('q', 'Yeshua said, “I go to prepare a place for you” (John 14:2). How is that like a Hebrew groom?', 2)]),

dict(t='illus', img='l1_census', cap='A decree from Caesar Augustus'),
dict(t='text', kicker='Lesson One · Reading 7', title='The Census', bignum='1', foot=F,
 verse='And it came to pass in those days, that there went out a decree from Caesar Augustus, that all the world should be taxed', vref='Luke 2:1',
 read='Luke 2:1–5 · Micah 5:2',
 paras=["Far away in the city of Rome, the emperor **Caesar Augustus** made a law. Everyone in the Roman Empire had to be counted in a census and registered for taxes. Each family had to go to its own hometown to sign up.",
  "Joseph belonged to the family of King David, and David’s hometown was **Bethlehem** in Judea. So Joseph had to leave Nazareth and travel south to Bethlehem, and he took Mary with him, even though her baby would soon be born.",
  "## A Long Journey",
  "The trip from Nazareth to Bethlehem was about 90 miles. Traveling on foot, perhaps with a donkey to carry supplies, it would have taken about a week. Many travelers followed the road along the Jordan River valley and then climbed up through the hills past Jerusalem.",
  "## God Was in Charge",
  "Caesar Augustus thought he was in control of the whole world. But God was using even an emperor’s law to keep His promise! Seven hundred years earlier, the prophet Micah had written that the Ruler of Israel would be born in Bethlehem (Micah 5:2). The census brought Mary and Joseph to exactly the right town at exactly the right time.",
  "As the fall season was about to begin, Mary and Joseph set out on the road to Bethlehem."],
 notes=[('God’s timing', 'Galatians 4:4 says God sent His Son “when the fulness of the time was come.” Ask: How did God use the census?'),
        ('Rulers', 'Caesar Augustus ruled Rome from 27 BC to AD 14. Quirinius governed Syria (Luke 2:2).'),
        ('Map it', 'Trace the route from Nazareth to Bethlehem on a map of Israel.')],
 callout=('Did You Know?', 'Bethlehem means “House of Bread.” The One who called Himself “the bread of life” (John 6:35) was born in the House of Bread!')),

dict(t='work', lesson=1, title='The Road to Bethlehem', kick='Color and Trace', ins='Mary and Joseph traveled about 90 miles from Nazareth to Bethlehem. Trace the dotted line with a crayon from START to FINISH to follow their journey. Color the water blue and the land green or brown. Then color Mary, Joseph, and the donkey!',
 blocks=[('img', 'map_journey', 6.9)]),
dict(t='work', lesson=1, title='A Census', ins='Open your Bible and read Luke 2:1–5. Answer the questions.',
 blocks=[('qs', [('Who was the Caesar who ordered a census? (verse 1)', 1), ('Who was governor of Syria at this time? (verse 2)', 1),
                 ('Why did Joseph go to Bethlehem to register for the census? (verse 4)', 2), ('Who did Joseph take with him? (verse 5)', 1),
                 ('About how far was it from Nazareth to Bethlehem?', 1), ('Which prophet said the Ruler of Israel would be born in Bethlehem?', 1)]),
         ('img', 'c_journey_fig', 2.6)]),
]
