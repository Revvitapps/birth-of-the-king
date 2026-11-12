import json
C=("Warm, painterly children's Bible storybook illustration, full-page portrait. Historically accurate 1st-century Judea; Middle-Eastern people with olive and brown skin. "
   "Rich but gentle colors (deep navy, warm gold, terracotta, cream), soft gouache and watercolor texture, classic picture-book quality, reverent and joyful mood. No text, no letters, no words, no borders.")
M="Mary is a young Hebrew woman with dark hair under a cream and soft-blue linen head covering. "
J="Joseph is a young bearded Hebrew carpenter in a brown tunic and striped wool cloak. "
color={
"cover":"A starry night over the small hill town of Bethlehem, flat-roofed stone houses glowing with lamplight, one brilliant star shining above. In the foreground hills, a stone watchtower (the Tower of the Flock) with sheep resting around it and a shepherd with a staff. Keep the upper third of the image as open deep-blue night sky with soft stars (space for a title).",
"front":"An ancient Hebrew scroll unrolled on a wooden table beside a clay oil lamp, a quill and inkpot, a small olive branch; through a window, the hills of Judea at golden hour. Still life, warm candlelight.",
"l1_open":"The prophet Isaiah, an older bearded Hebrew man in simple robes, writing on a scroll by lamplight in a stone room in ancient Jerusalem, looking upward with hope as soft golden light falls on the scroll.",
"l1_david":"Young David, a shepherd boy with reddish-brown hair, sitting on a rock playing a wooden lyre on the green hills outside Bethlehem, sheep grazing around him, a small golden crown resting beside him on the rock as a hint that he will be king.",
"l1_jesse":"Symbolic illustration of Isaiah 11:1: an old cut tree stump on a Judean hillside with a fresh green shoot and a new branch with leaves and a single white blossom growing from it, glowing with soft morning light, a royal golden crown faintly in the sky light above, olive trees and Bethlehem in the distance.",
"l1_dream":J+"Joseph asleep on a straw mat in his simple Nazareth home at night while a gentle angel in soft golden light stands near him speaking in a dream; moonlight through the window, carpentry tools on the wall.",
"l1_nazareth":"The small village of Nazareth in Galilee on a hillside: simple stone and mud-brick houses with flat roofs and courtyards, families tending small vegetable gardens, a woman carrying a water jar, a man with a donkey, olive trees, children playing, morning light.",
"l1_wedding":"An ancient Hebrew betrothal: two fathers seated at a low table signing a marriage contract scroll (a ketubah) with a reed pen, while a young man and a young woman stand shyly to the side with their mothers, inside a stone courtyard with lamps and a woven rug.",
"l1_census":"A Roman herald in a red cloak and helmet standing on steps in a Galilean town square, holding an unrolled decree from Caesar Augustus and announcing it to a crowd of villagers; "+J+"listens with "+M+"beside him.",
"l2_open":M+J+"Mary rides a small grey donkey while Joseph leads it along a rocky road through the Judean hills at sunset; the hill town of Bethlehem is visible ahead.",
"l2_tower":"Migdal Eder, the Tower of the Flock: a two-story ancient stone watchtower standing in the shepherds' fields outside Bethlehem at dusk, a stone sheepfold around its base, flocks of white sheep and young lambs grazing, shepherds with staffs, Bethlehem on a distant hill.",
"l2_fall":"Bethlehem in early autumn: harvest season, leafy booths (sukkot) made of branches on flat rooftops, grape vines and baskets of figs and pomegranates, pilgrims arriving with donkeys, sheep in the nearby fields, warm golden evening light, a thin new moon.",
"l2_birth":M+J+"Inside the lower level of a simple stone family house in Bethlehem at night, where the animals are kept: Mary lays her newborn baby, wrapped in white swaddling cloths, in a carved stone manger filled with straw; Joseph kneels beside her holding an oil lamp; a donkey and an ox nearby; stairs lead up to a crowded upper living area.",
"l2_lamb":"A Levitical shepherd at night in the lower room of a stone watchtower, gently wrapping a newborn white lamb in strips of swaddling cloth and laying it in a stone manger with straw, lit by an oil lamp; other sheep resting nearby.",
"l2_angels":"Shepherds in the fields near Bethlehem at night, startled and shielding their eyes as a radiant angel appears in the sky, and behind him a vast heavenly host of angels arrayed like a shining army with light and wings filling the sky, praising God; sheep in the foreground.",
"l2_shepherds":M+J+"Humble shepherds kneeling in wonder before the newborn baby lying in a stone manger in the lower room of a Bethlehem house, a young shepherd boy holding a lamb, warm lamplight.",
"l3_open":"Wise men (Parthian magi) in rich Persian robes and tall felt caps standing on the rooftop of an observatory in an ancient Persian city at night, studying the sky with scrolls and an astrolabe, one pointing at a bright new star.",
"l3_magi":"The court of the Parthian Empire: a group of distinguished magi, priest-scholars and nobles in embroidered Persian robes and tall caps, gathered around a table of star charts and scrolls in a grand hall with carved columns, debating; one holds an old scroll of Daniel's prophecy.",
"l3_star":"A long caravan of Parthian magi with dozens of camels, horses, servants and armed guards traveling through desert hills under a brilliant guiding star at twilight.",
"l3_herod":"Old King Herod, an anxious, grey-bearded king in rich purple robes seated on a throne in his marble palace in Jerusalem, meeting with richly dressed Parthian magi; his scribes and chief priests unroll scrolls nearby; Roman-style columns and guards.",
"l3_temple":"Herod's Temple in Jerusalem seen from the Mount of Olives: a gleaming white and gold temple on a vast stone platform with great walls and colonnades, crowds of pilgrims on the steps, the city around it, morning light.",
"l3_simeon":M+J+"Inside the temple courts in Jerusalem: old Simeon, a white-bearded man, holds the baby joyfully and lifts his eyes to heaven; elderly Anna, a prophetess in simple robes, raises her hands in praise; Mary and Joseph stand nearby, Joseph holding a small cage with two turtledoves; tall stone columns and sunlight.",
"l4_open":"A large group of Parthian magi on camels and horses with servants and guards approaching the walls and gates of Jerusalem along a dusty road; the temple is visible above the walls; late afternoon light.",
"l4_worship":M+J+"Inside a simple stone house in Bethlehem: richly robed Parthian magi bow down low before the young child Jesus, a toddler about one and a half years old in a white tunic, sitting on Mary's lap; the magi offer an open chest of gold, a vessel of frankincense and a jar of myrrh; Joseph stands behind; warm lamplight.",
"l4_gifts":"Still life of the three gifts of the magi on an embroidered Persian cloth: an open carved wooden chest overflowing with gold coins and gold objects, a bowl of pale amber frankincense resin with a thin curl of fragrant smoke rising, and an alabaster jar with reddish-brown myrrh resin; soft warm light.",
"l4_home":"The Parthian magi and their caravan quietly leaving Bethlehem at dawn by a different road through the hills, looking back at the town, the morning sky glowing pink and gold; peaceful mood.",
"l5_open":J+"An angel in soft light wakes Joseph in the night inside the house in Bethlehem, urgently pointing toward the south, while Mary sleeps with the toddler Jesus beside her.",
"l5_flight":M+J+"The family fleeing to Egypt by night: Joseph leads a donkey carrying Mary holding the toddler Jesus, crossing a moonlit desert with palm trees and distant dunes, stars above.",
"l5_house":"A cutaway view of a typical 1st-century Israelite stone house: a flat roof made of branches and straw covered in clay, an upstairs living space with sleeping mats, a ground-level kitchen with clay oven, a stable area with a donkey and goat and a stone manger, and an open courtyard; a family going about its day.",
"l5_herod":"Old King Herod, grey-bearded and sick, looking angry and fearful in his luxurious palace, gripping the arms of his throne as he gives orders to Roman-style soldiers; a model of his fortress Herodium in the background; dramatic but not violent.",
"l5_egypt":M+J+"The family resting safely in Egypt beside the Nile River: palm trees, reeds, a small mud-brick house, Mary holding the young child Jesus on her lap while Joseph works at a carpentry bench, ancient Egyptian temples and pyramids far in the distance, peaceful golden light.",
}
L=("Black and white coloring book page for children ages 6 to 12: clean, bold, smooth black outlines only, no shading, no gray tones, no hatching, no color, pure white background, large simple shapes that are easy to color, historically accurate 1st-century Middle East. No text, no letters, no words, no border. ")
line={
"c_david":"Young King David as a shepherd boy playing a lyre, sitting on a rock with two sheep beside him.",
"c_farmer":"A Hebrew man from Nazareth in a tunic and head covering, carrying a basket of vegetables, with a small house and olive tree behind him.",
"c_wedding":"A Hebrew bride in a long veil and a groom in a robe and head covering standing together under a canopy, holding hands.",
"c_caesar":"Caesar Augustus, Roman emperor, in a toga and laurel wreath, pointing at an unrolled scroll decree.",
"c_tower":"Migdal Eder, an ancient two-story stone watchtower in a field with a stone sheep pen, sheep and lambs, a shepherd with a staff.",
"c_manger":"A carved stone manger filled with straw, with a baby wrapped in swaddling cloths lying in it, a small lamb resting beside it.",
"c_shepherd":"A shepherd boy with a staff holding a lamb, looking up in wonder at an angel in the night sky with stars.",
"c_mary":"Mary holding the newborn baby Jesus wrapped in swaddling cloths, Joseph standing beside her with a lamp, a donkey behind them.",
"c_magus":"A Parthian wise man (magus) standing tall in long embroidered Persian robes and a tall rounded cap, holding a scroll, pointing up at a star.",
"c_temple":"Herod's Temple in Jerusalem: a large temple building with columns on a big stone platform with steps and walls, a few pilgrims.",
"c_simeon":"Old Simeon with a long beard holding baby Jesus in the temple, elderly Anna beside him raising her hands in praise, a column behind.",
"c_herodmagi":"King Herod on his throne talking to two Parthian wise men in tall caps, a scribe holding a scroll.",
"c_camel":"A wise man in Persian robes riding a camel carrying bags and a treasure chest, a big star above.",
"c_worship":"Three wise men kneeling and bowing before the young child Jesus sitting on Mary's lap inside a simple house, gifts on the floor.",
"c_gifts":"Three gifts: an open treasure chest of gold coins, a bowl of frankincense with curling smoke, and a jar of myrrh, on a cloth.",
"c_house":"Side cutaway view of an ancient Israelite two-story stone house: flat roof of branches and straw, upstairs living room, kitchen with clay oven, stable with a donkey and a manger, courtyard with a gate.",
"c_flight":"Joseph leading a donkey carrying Mary and young child Jesus through the desert, palm trees and a star.",
"c_herod":"King Herod, an old king with a beard and crown, sitting on a throne holding a scepter, with columns behind.",
"c_pharaoh":"An ancient Egyptian king (pharaoh) wearing a striped royal headdress and holding a crook and flail, standing beside the Nile with a pyramid and palm tree.",
}
calls=[]
for k,v in color.items(): calls.append((k,{"modelId":"gpt-image-2-text","size":"1024x1536","quality":"High","output_format":"PNG","n":1,"prompt":v+" "+C}))
for k,v in line.items(): calls.append((k,{"modelId":"gpt-image-2-text","size":"1024x1536","quality":"High","output_format":"PNG","n":1,"prompt":L+v}))
json.dump(calls,open('calls.json','w'))
print(len(calls))
for i in range(0,len(calls),20):
    json.dump({"calls":[{"tool":"generate","input":c[1]} for c in calls[i:i+20]]},open(f'batch{i//20}.json','w'))
    print(i//20,[c[0] for c in calls[i:i+20]])
