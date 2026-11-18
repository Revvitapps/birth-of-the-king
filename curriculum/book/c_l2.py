from c_common import *
from c_common import _hw, _maze, _wordsearch, _code
F = 'Beyond the Manger · Lesson 2'

PAGES = [
dict(t='opener', img='l1_angel', num=2, title='The Announcement', ref='Luke 1:26–38 · Matthew 1:18–25 · Isaiah 7:14'),
dict(**{'t': 'plan',
 'num': 2,
 'title': 'The Announcement',
 'bignum': '2',
 'passages': 'Luke 1:26–38; Matthew 1:18–25. Prophecy: Isaiah 7:14',
 'objectives': ['Retell how Mary and Joseph each heard God’s plan', 'Explain what the name Yeshua means and where it comes from', 'Describe what a betrothal was in Israel', 'Tell how Yeshua is like a bridegroom'],
 'prayer': 'Father God, thank You that You speak and that Your word can be trusted. Give us hearts like Mary and Joseph, ready to say yes to You. In Yeshua’s name, amen.',
 'materials': 'Bibles, pencils, crayons or colored pencils, and copies of the Lesson 2 printable pages.',
 'overview': 'God announced the King before He sent Him. Gabriel carried the news to Mary in Nazareth: her son would sit on David’s throne, and His kingdom would never end. Mary answered with trust. Joseph heard the same news in '
             'a dream, along with the name the child must carry. That name, Yeshua, says what He came to do. Mary and Joseph were betrothed, bound to each other by covenant but not yet living as husband and wife. Seeing how a '
             'marriage was made in Israel shows what Joseph risked when he obeyed. It also gives a picture Yeshua later used for Himself: the Bridegroom who goes to prepare a place and comes back for His bride.',
 'dyk': 'Gabriel’s words to Mary repeat God’s promise to David almost line by line. Compare Luke 1:32–33 with 2 Samuel 7:12–16.',
 'flow': [('Read:', 'An Angel Visits Mary'),
          ('Read:', 'His Name Is Yeshua'),
          ('Activity:', 'Let’s Write Yeshua · Names of the King'),
          ('Read:', 'Betrothed: A Promise Before the Wedding'),
          ('Activity:', 'Color the Bride and Groom · The Bridegroom’s Promise')]}),

dict(t='illus', img='l1_angel', cap='Nazareth, Galilee'),
dict(t='text', kicker='Lesson Two · Reading 1', title='An Angel Visits Mary', bignum='2', foot=F,
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
dict(t='text', kicker='Lesson Two · Reading 2', title='His Name Is Yeshua', bignum='2', foot=F,
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

dict(t='work', lesson=2, title='Let’s Write Yeshua!', ins='Yeshua’s name in Hebrew has four letters. Hebrew runs the opposite way from English, so start at the right side and move left. Trace the gray letters, then write the name on your own.',
 blocks=[('html', '<div class="letters"><div><div class="hl">י</div><div class="nm">Yod · Y</div></div><div><div class="hl">ש</div><div class="nm">Shin · SH</div></div><div><div class="hl">ו</div><div class="nm">Vav · U</div></div><div><div class="hl">ע</div><div class="nm">Ayin · A</div></div></div>'),
         ('html', _hw('heb', [('ישוע', 'solid'), ('ישוע', 'trace')]) + _hw('heb', [('ישוע', 'trace'), ('ישוע', 'trace')]) + _hw('heb', [])),
         ('html', '<div class="qt" style="margin-top:6px">Now write His name in English:</div>' + _hw('en', [('Yeshua', 'solid'), ('Yeshua', 'trace')]) + _hw('en', []) + _hw('en', []))]),
dict(t='work', lesson=2, title='Names of the King', cls='roomy', sk='sk_crown', ins='Read Matthew 1:21–23, Luke 1:32, and Matthew 1:1. Draw a line from each name to its meaning. Then answer the question.',
 blocks=[('html', '''<div class="match"><div class="mc">
<div class="mi"><b>1</b> Yeshua</div><div class="mi"><b>2</b> Immanuel</div><div class="mi"><b>3</b> Son of David</div><div class="mi"><b>4</b> Messiah (Christ)</div><div class="mi"><b>5</b> Son of the Most High</div></div>
<div class="mc"><div class="mi">God with us</div><div class="mi">The Anointed One, the chosen King</div><div class="mi">God saves</div><div class="mi">The Son of God</div><div class="mi">The King from David’s royal family</div></div></div>'''),
         ('q', 'Which name of the King is your favorite? Why?', 2),
         ('box', 'Draw a picture of the angel speaking to Joseph in his dream', 3.2, 'fill')]),

dict(t='illus', img='l1_wedding', cap='A promise made before the wedding'),
dict(**{'t': 'text',
 'id': 'l1f',
 'kicker': 'Lesson Two · Reading 3',
 'title': 'Betrothed: A Promise Before the Wedding',
 'bignum': '2',
 'foot': F,
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

dict(t='color', lesson=2, title='The Bride and Groom', img='c_wedding', caption='When the groom brought his bride home, the families feasted for a week. (Judges 14:12)'),
dict(**{'t': 'work',
 'lesson': 2,
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

]
