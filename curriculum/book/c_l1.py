from c_common import *
from c_common import _hw, _maze, _wordsearch, _code
F = 'Beyond the Manger · Lesson 1'

PAGES = [
dict(t='opener', img='l1_open', num=1, title='The Promised King', ref='Matthew 1 · Luke 1:26–38 · Luke 2:1–5'),
dict(**{'t': 'plan',
 'num': 1,
 'title': 'The Promised King',
 'bignum': '1',
 'passages': 'Matthew 1:1–17; Luke 3:23–38; 2 Samuel 7:12–16. Prophecies: Isaiah 11:1–2; Jeremiah 23:5–6',
 'objectives': ['Tell why Matthew calls Yeshua the “Son of David”',
                'Name two prophets who promised a King from David’s family',
                'Explain the difference between the legal right and the blood right to the throne',
                'Fill in the main names of Yeshua’s family tree'],
 'prayer': 'Father God, thank You for keeping every promise You make. Open our ears and our hearts as we learn about the birth of Your Son, the King. In Yeshua’s name, amen.',
 'materials': 'Bibles, pencils, crayons or colored pencils, and copies of the Lesson 1 printable pages.',
 'overview': 'The story of the King does not begin in a manger. It begins with a promise. God told David that one of his sons would rule forever (2 Samuel 7:12–16), and the prophets held that promise in front of Israel for a '
             'thousand years. This lesson follows the promise through the family records. Matthew and Luke each record a family line, and together they show that Yeshua holds the throne by legal right through Joseph and by blood '
             'right through Mary. Before the first angel speaks, the family tree already says who this child will be.',
 'dyk': 'Matthew arranges Yeshua’s family line in three sets of fourteen generations (Matthew 1:17), and he names five women in a list that normally named only fathers.',
 'flow': [('Read:', 'The Promised King'), ('Read:', 'Two Family Lines'), ('Activity:', 'Color King David · Yeshua’s Family Tree')]}),

dict(t='illus', img='l1_david', cap='David, the shepherd boy from Bethlehem'),
dict(t='text', kicker='Lesson One · Reading 1', title='The Promised King: Son of David', bignum='1', foot=F,
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
dict(t='text', kicker='Lesson One · Reading 2', title='Two Family Lines: The Right to Be King', bignum='1', foot=F,
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

]
