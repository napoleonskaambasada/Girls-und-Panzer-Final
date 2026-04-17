from flask import Flask, render_template

app = Flask(__name__)

main_schools = [
    {
        "name": "Ōarai Girls' Academy",
        "tank": "Panzer IV Ausf. H",
        "commander": "Miho Nishizumi",
        "image": "images/Oarai.jpg",
        "overview": "A diverse and resilient school located on a massive Academy Ship based in Ibaraki Prefecture. Once a powerhouse, its Sensha-dō program was abolished and only recently revived in a desperate bid to win the National Championship and save the school from being decommissioned by the Ministry of Education. It serves as the ultimate underdog story, bringing together students from various clubs and backgrounds.",
        "tactics": "Mastered the art of 'Active Defense' and unconventional improvisation. Because their fleet is a 'museum' of mismatched tanks, they use the specific strengths of each—like the Duck Team's agility for baiting or the Hippo Team's sniping—to execute complex, multi-layered traps. They excel in urban warfare and utilizing environmental hazards to neutralize the numerical and technological superiority of their opponents.",
        "weapons": "The most diverse arsenal in the series: the Panzer IV (the flagship), the 38(t) which was later converted to a Hetzer, the Type 89B I-Go, the M3 Lee, the StuG III Ausf. F, the Renault B1 bis, the heavy Tiger (P), the Type 3 Chi-Nu, and the Mark IV Landship.",
        "characters": "Led by the Anglerfish Team (Miho Nishizumi, Saori Takebe, Hana Isuzu, Yukari Akiyama, and Mako Reizei). Key support comes from the Student Council (Anzu, Momo, Yuzu), the History Club (Hippo Team), and the Automotive Club (Leopon Team) who maintain the tanks.",
        "trivia": "Unlike schools that represent a single nation's spirit, Ōarai represents the town of Ōarai itself. The school's logo is a stylized 'Ō' character. In the real world, the city of Ōarai holds an annual 'Anglerfish Festival' that attracts over 100,000 fans of the series."
    },
    {
        "name": "Kuromorimine Girls Academy",
        "tank": "Tiger I",
        "commander": "Maho Nishizumi",
        "image": "images/Kuromorimine.jpg",
        "overview": "The 'Black Forest Peak' Academy is a prestigious institution from Kumamoto that defines German-style efficiency. They held a legendary nine-year winning streak in the National Tournament. The school operates with a military-grade hierarchy and a 'win at all costs' mentality that values the legacy of the Nishizumi Style above individual sentiment.",
        "tactics": "They employ 'Schwerpunkt' (Center of Gravity) doctrine, using heavy armor to punch through enemy lines at their weakest point. Their formation is usually a 'V' or 'W' shape designed to maximize frontal armor deflection. They rely on the 'Iron Wall' strategy—advancing slowly and methodically while letting their superior long-range 88mm guns pick off targets before the enemy can get into range.",
        "weapons": "A terrifying lineup of German heavyweights: Tiger I, Tiger II (King Tiger), Panther G, Jagdpanther, Jagdtiger, Elefant, and the 188-ton Panzer VIII Maus. They also utilize Panzer III Ausf. J for scouting and command roles.",
        "characters": "Maho Nishizumi, the stoic and dutiful commander; Erika Itsumi, her aggressive and fiercely loyal vice-commander; and Koume Akaboshi, a survivor of the accident that led to Miho's departure from the school.",
        "trivia": "The school's philosophy is rooted in the 'Nishizumi Style,' a fictional martial art of tankery. Their Academy Ship is modeled after the German aircraft carrier Graf Zeppelin. Many students are rumored to come from long lines of professional Sensha-dō families."
    },
    {
        "name": "Pravda High School",
        "tank": "T-34/85",
        "commander": "Katyusha",
        "image": "images/Pravda.jpg",
        "overview": "A Soviet-themed powerhouse from the snowy regions of Aomori. Pravda is famous for its extreme discipline and its ability to operate in the harshest winter conditions. They emphasize the collective over the individual, often singing traditional songs like 'Katyusha' or 'Polyushko-polye' as they march into battle.",
        "tactics": "Specialists in 'Deep Battle' operations. They often use a small force (usually led by Katyusha) as a 'golden' bait to lure enemies into a vast, snowy encirclement. Once trapped, their heavy hitters like the IS-2 and KV-2 provide high-explosive suppression while waves of T-34s overwhelm the enemy from all sides in a war of attrition.",
        "weapons": "Soviet-inspired armor including the ubiquitous T-34/76 and T-34/85, the IS-2 heavy tank, the KV-2 'Gigant' (known for its massive 152mm howitzer), and the BM-13 Katyusha rocket launchers (used for ceremonies).",
        "characters": "Katyusha, the 'Great Little Dictator' who demands respect; Nonna, her calm and deadly accurate vice-commander who acts as a mother figure; and Nina and Alina, the hardworking loaders of the KV-2.",
        "trivia": "Pravda students are known to eat Russian cuisine like borscht and pirozhki. The name 'Pravda' means 'Truth' in Russian. Katyusha is so dedicated to her image that she refuses to walk on the ground when she can be carried on Nonna’s shoulders to look taller.",
        "trivia": "The school has a 'Great Purge' system where students who fail are sent to 'Siberia' (a cold, remote part of the ship) for remedial training."
    },
    {
        "name": "St. Gloriana Girls' College",
        "tank": "Churchill",
        "commander": "Darjeeling",
        "image": "images/Gloriana.jpg",
        "overview": "An elite British-themed school based in Yokohama. St. Gloriana is the epitome of high-society elegance and sportsmanship. They treat Sensha-dō as a refined art form rather than a brutal sport, maintaining a strict code of conduct that demands composure regardless of the chaos on the battlefield.",
        "tactics": "They utilize a 'Hammer and Anvil' strategy. The slow, heavily armored Churchill and Matilda II tanks act as the immovable 'anvil,' absorbing fire and maintaining a steady line. Meanwhile, the 'hammer' consists of high-speed Crusader tanks that flank and harass the enemy rear. They prioritize accuracy while moving, a feat achieved through intense training.",
        "weapons": "Exclusively British vehicles: the Churchill Mk. VII (Infantry Tank), Matilda II Mk. III/IV, the high-speed Crusader Mk. III, and the Cromwell (seen in the films). Their command vehicle is always stocked with high-end tea sets.",
        "characters": "Darjeeling, the commander who speaks in philosophical quotes and proverbs; Orange Pekoe, her soft-spoken loader and tactical observer; Assam, the expert gunner who calculates trajectories; and Rosehip, the speed-obsessed outlier of the group.",
        "trivia": "St. Gloriana is the only school Miho Nishizumi has never defeated in a fair 1v1 school match. They have a tradition of gifting a tea set to any opponent who truly impresses them in battle. Their Academy Ship resembles the HMS Ark Royal."
    },
    {
        "name": "Saunders University High School",
        "tank": "M4 Sherman",
        "commander": "Kay",
        "image": "images/Saunders.jpg",
        "overview": "A wealthy American-themed school that boasts the largest inventory of tanks in the world. Based on a carrier modeled after the USS Nimitz, Saunders values freedom, fair play, and massive logistics. They are known for being the friendliest school, treating their opponents with genuine hospitality and respect.",
        "tactics": "They fight using 'Material Supremacy.' By fielding a unified fleet of Shermans, they have interchangeable parts and synchronized speeds, allowing for highly efficient maneuvers. They use radio interception and aerial reconnaissance (via balloons and transport planes) to know the enemy's position at all times, then overwhelm them with sheer volume of fire.",
        "weapons": "A massive fleet of M4 Shermans, including the M4A1 (76mm), the standard M4, and the specialized British-modified Sherman Firefly used for its superior anti-tank capabilities.",
        "characters": "Kay, the energetic and optimistic commander; Alisa, the manipulative radio operator and strategist; and Naomi, the cool-headed ace gunner who rarely misses a shot.",
        "trivia": "Saunders is so wealthy that they fly in their own steak and burger catering for away matches. Despite Alisa’s tendency to cheat using radio bugs, Kay strictly forbids it, believing that a victory without 'Fair Play' is no victory at all."
    },
    {
        "name": "Anzio High School",
        "tank": "Carro Veloce CV.33",
        "commander": "Chiyomi Anzai",
        "image": "images/Anzio.jpg",
        "overview": "An Italian-themed school that, while low on funds, is the highest in spirit. Anzio is more of a traveling festival than a military academy. They are beloved by fans and other schools alike for their infectious energy and their ability to turn every match into a giant pasta party.",
        "tactics": "They rely on 'Operation Macaroni'—a mix of high-speed swarming and theatrical deception. Using their tiny, ultra-fast CV.33 tankettes, they perform reconnaissance and 'distraction' maneuvers. They are famous for using smoke screens and cardboard silhouettes to make their small force look like a massive division.",
        "weapons": "Italian armor including the CV.33 (L3/33) Tankette, the Semovente 75/18 assault gun, and their 'heavy' tank, the P40. They also utilize the Carro Armato M13/40.",
        "characters": "Chiyomi Anzai (known as 'Anchovy' or 'Duce'), the charismatic leader; Carpaccio, the disciplined and skillful vice-commander; and Pepperoni, the energetic impulsive chef and driver.",
        "trivia": "The school is perpetually in debt because they prioritize buying top-tier pasta makers and ingredients over tank upgrades. Anchovy is actually one of the most capable leaders in the series, managing to keep a massive student body happy with almost zero resources."
    },
    {
        "name": "Chi-Ha-Tan Academy",
        "tank": "Type 97 Chi-Ha",
        "commander": "Kinuyo Nishi",
        "image": "images/Chihatan.jpg",
        "overview": "A school that embodies the 'Showa' era spirit of Japan. Chi-Ha-Tan is deeply traditional, emphasizing honor, courage, and perseverance. While they were historically seen as a 'first-round exit' team due to their rigidness, they have recently undergone a tactical revolution.",
        "tactics": "Historically, they only knew how to 'Charge' (Banzai) regardless of the odds. After training with Ōarai, they developed 'The Art of Not Charging,' which includes camouflage, jungle guerrilla warfare, and amphibious landings. They now use their light tanks to bait enemies into crossfires before delivering a 'Calculated Charge.'",
        "weapons": "Imperial Japanese Army tanks: the Type 97 Chi-Ha (old and new turret versions), the Type 95 Ha-Go light tank, and the Type 2 Ka-Mi amphibious tank which can shed its pontoons for land combat.",
        "characters": "Kinuyo Nishi, the polite and honorable commander; Fukuda, the young strategist who realized the folly of blind charging; and Tamada and Hosomi, the aggressive spearheads of the charge.",
        "trivia": "The students are so conditioned to charge that they often have to use code words to avoid accidentally triggering a suicide run. Their Academy Ship is modeled after the Akagi aircraft carrier."
    },
    {
        "name": "Jatkosota High School",
        "tank": "BT-42",
        "commander": "Mika",
        "image": "images/Jaktosota.jpg",
        "overview": "A mysterious Finnish-themed school known for its independence and survivalist skills. Jatkosota (named after the Continuation War) operates on a shoestring budget, often 'acquiring' supplies from other schools. They are considered the most dangerous 'wild card' school because their movements are completely unpredictable.",
        "tactics": "They utilize 'Sissi' (guerrilla) tactics and extreme mobility. Their signature move is the 'Säkkijärven polkka,' where they use high-speed drifting and precision driving to circle heavier tanks. They are famous for the ability to drive their BT-42 even after losing its tracks, running on the road wheels alone.",
        "weapons": "A scavenged arsenal including the iconic BT-42 (a BT-7 chassis with a British 4.5-inch howitzer), the T-34/85, and the StuG III Ausf. G.",
        "characters": "Mika, the kantele-playing philosopher who 'borrowed' her way to the top; Aki, the sensible observer; and Mikko, arguably the best driver in the entire Sensha-dō world.",
        "trivia": "The school has a long-standing 'rivalry' with Pravda, mostly because Jatkosota keeps stealing Pravda's tanks and food. Mika’s hat is based on the Finnish 'Väinämöinen' style, and she often quotes the wind when asked difficult questions."
    },
    {
        "name": "BC Freedom Academy",
        "tank": "Renault FT-17",
        "commander": "Marie",
        "image": "images/BC.jpg",
        "overview": "A French-themed academy that is a powder keg of internal politics. It was formed by the merger of two rival schools: the 'Escalator' school (wealthy, aristocratic) and the 'Examination' school (diligent, scholarship-based). The students spend as much time fighting each other as they do the enemy.",
        "tactics": "Their primary strategy is the 'False Schism.' They fake a heated internal argument over radio frequencies to trick the enemy into thinking they are disorganized. When the enemy moves in to capitalize on the chaos, BC Freedom executes a perfect, unified pincer movement known as the 'Cidre' formation.",
        "weapons": "An elegant mix of French armor: the legendary Renault FT-17 (command tank), the Somua S35 for medium combat, and the heavy ARL 44 which provides unexpected long-range firepower.",
        "characters": "Marie, the cake-loving, swan-like commander who remains calm during riots; Oshida, the hot-headed leader of the Escalator faction; and Andou, the sharp-tongued leader of the Examination faction.",
        "trivia": "Marie is never seen without a piece of cake, even in a tank. The school's internal conflict is a direct parody of the French Revolution and the historical tensions between the French classes. Their Academy Ship is modeled after the French carrier Béarn."
    }
]

 
minor_schools = [
    {
        "name": "Maginot Girls' Academy",
        "tank": "SOMUA S35",
        "commander": "Éclair",
        "image": "images/maginot.jpg",
        "overview": "A French-themed school that follows the rigid, defensive military doctrines of pre-WWII France. They are famous for their high-quality education and culinary arts, but their Sensha-dō team has historically struggled with a lack of flexibility, often sticking to traditional 'trench warfare' mindsets.",
        "tactics": "They utilize a 'Static Defense' doctrine, favoring heavy, slow-moving lines and well-fortified positions. While they are difficult to displace once dug in, they often struggle against high-mobility opponents who can bypass their 'Maginot Line' of heavy tanks.",
        "weapons": "Primarily French armor, featuring the Char B1 bis, SOMUA S35, and Renault R35. They prioritize thick armor over speed.",
        "characters": "Éclair (Commander), a hardworking leader trying to modernize the school's outdated tactics, and Fondue (Vice-Commander).",
        "trivia": "The school is named after the historical Maginot Line. In the manga, they have a fierce but respectful rivalry with Ōarai and were one of the first schools to practice with them."
    },
    {
        "name": "Bonple High School",
        "tank": "7TP",
        "commander": "Jajka",
        "image": "images/bonple.jpg",
        "overview": "A Polish-themed school known for its incredible tenacity and aggressive scouting. Despite having mostly light tanks, their students possess a 'cavalry spirit' that makes them punch far above their weight class.",
        "tactics": "They specialize in 'Winged Hussar' charges—high-speed, daring maneuvers designed to shock and confuse the enemy. They use light tanks to draw the enemy into narrow terrain before performing a synchronized, aggressive strike.",
        "weapons": "Light Polish tanks, specifically the 7TP (twin-turret and single-turret variants) and the TKS Tankette.",
        "characters": "Jajka (Overall Commander), a fierce and loud leader, and Uszka (Vice-Commander).",
        "trivia": "They are famous for their 'Bigos' (Polish hunter's stew). Jajka has a personal rivalry with Shizuka Tsuruki from the Tatenashi High School."
    },
    {
        "name": "Blue Division High School",
        "tank": "Panzer II",
        "commander": "El",
        "image": "images/bluedivision.jpg",
        "overview": "A Spanish-themed school that brings a fiery, passionate energy to Sensha-dō. They are known for their flamboyant style and their specialized, chef-designed field rations.",
        "tactics": "Mobile guerrilla warfare. They prefer close-quarters combat and use their light Panzers to swarm isolated enemies. They are highly adaptable in rugged, mountainous terrain.",
        "weapons": "German-derived armor used during the Spanish Civil War, such as the Panzer I, Panzer II, and Verdeja 1.",
        "characters": "El (Commander), a charismatic leader who speaks with passion, and Viridiana (Vice-Commander).",
        "trivia": "The school uniform is modeled after the Spanish Legion. They are widely considered to have the best catering on any Academy Ship, specializing in paella."
    },
    {
        "name": "Count High School",
        "tank": "KV-2",
        "commander": "Count",
        "image": "images/count.jpg",
        "overview": "A Romanian-themed school that plays into the gothic and 'vampiric' aesthetics of its theme. They are mysterious and often play matches during the evening or in foggy conditions.",
        "tactics": "Ambush-heavy tactics. They prefer to stay hidden in fog or forests, using their heavy KV-2 to deliver a single, devastating 'death blow' to unsuspecting enemies.",
        "weapons": "A mix of Soviet lend-lease and German tanks, most notably the KV-2 and Panzer IV G.",
        "characters": "The Commander, known only as 'Count,' who wears a cape and maintains a theatrical persona.",
        "trivia": "The school ship's architecture is modeled after Bran Castle (Dracula's Castle) in Transylvania."
    },
    {
        "name": "Waffle Academy",
        "tank": "TKS Tankette",
        "commander": "Unknown",
        "image": "images/waffle.jpg",
        "overview": "A Belgian-themed school that focuses on small, high-quality detachments. They are often overlooked due to their size, but they are experts in defensive engineering and narrow-pathway maneuvers.",
        "tactics": "They utilize 'Box-in' tactics, using their small TKS tankettes to hide in spots where larger tanks cannot go, waiting for the perfect moment to disable the enemy's tracks or vision blocks.",
        "weapons": "Primarily Belgian and Polish light armor, most notably the TKS Tankette (20mm version) and the Vickers T-15.",
        "characters": "While their commander rarely appears in the anime, they are known for having a highly disciplined and polite student body.",
        "trivia": "As the name suggests, they are famous for their waffles. They have a long-standing cooperative agreement with St. Gloriana for tea-and-dessert events."
    },
    {
        "name": "Kebab High School",
        "tank": "Renault R35",
        "commander": "Bosporus",
        "image": "images/kebak.jpg",
        "overview": "A Turkish-themed school that excels in desert and arid environment training. They have a reputation for being extremely hospitable to guests but fierce and unwavering on the battlefield.",
        "tactics": "They use 'Sandstorm' tactics, utilizing high-speed maneuvers to kick up dust and debris, obscuring the enemy's view while they move into a flanking position.",
        "weapons": "A mix of older French and German tanks, including the Renault R35 and the Panzer III Ausf. N.",
        "characters": "Commander Bosporus, known for her strategic patience and love for traditional Turkish coffee.",
        "trivia": "The school's Academy Ship is designed to resemble the architecture of Istanbul, featuring a large dome in the center of the student district."
    },
    {
        "name": "Bellwall Academy",
        "tank": "T-44",
        "commander": "Emi Nakasuga",
        "image": "images/Bellwall.jpg",
        "overview": "A German-Soviet hybrid themed school that arose from a complex history. They are extremely serious and treat Sensha-dō as a rigorous academic and physical discipline.",
        "tactics": "A blend of Blitzkrieg speed and Soviet endurance. They use high-tier tanks to strike hard and fast, refusing to yield ground even when outnumbered.",
        "weapons": "Powerful mid-to-late war vehicles like the Panther and the high-performance Soviet T-44.",
        "characters": "Emi Nakasuga, a cold but brilliant tactician who has a personal history with Maho Nishizumi.",
        "trivia": "The school's name is a reference to the Berlin Wall. They are known for their incredibly high academic standards."
    },
    {
        "name": "Gregor High School",
        "tank": "Panzer 38(t)",
        "commander": "Kafka",
        "image": "images/Gregor.jpg",
        "overview": "A Czechoslovakian-themed school that prides itself on precision engineering and technical maintenance. Their tanks are often in better condition than those of much wealthier schools.",
        "tactics": "They focus on 'Clockwork' coordination—highly synchronized movements where every tank moves as part of a single larger machine to maximize coverage.",
        "weapons": "Almost exclusively Czechoslovakian designs, mainly the Panzer 38(t) and the Panzer 35(t).",
        "characters": "Commander Kafka, a quiet, introspective leader who is often found in the maintenance bays helping the mechanics.",
        "trivia": "The school was named after the famous writer Franz Kafka. Their school motto is 'Metamorphosis through discipline.'"
    },
    {
        "name": "Gilbert High School",
        "tank": "M26 Pershing",
        "commander": "Jinko Yoshinaga",
        "image": "images/Gilbert.jpg",
        "overview": "A prestigious school that mimics the United States military academies. Unlike the fun-loving Saunders, Gilbert High is defined by strict discipline and a 'perfectionist' approach to Sensha-dō. They are known for producing high-tier tactical officers.",
        "tactics": "They favor 'Combined Arms' precision. They don't just overwhelm with numbers; they use M26 Pershings as heavy anchors while light elements perform highly coordinated flanking maneuvers. Their discipline allows them to maintain perfect formations even under heavy fire.",
        "weapons": "High-performance American armor including the M26 Pershing, M4A3E8 'Easy Eight' Shermans, and the M24 Chaffee.",
        "characters": "Jinko Yoshinaga, a strict and formidable commander who values results above all else, and Emi Nakasuga (who attended before moving to Bellwall).",
        "trivia": "In the 'Little Army' manga, Gilbert High is portrayed as a rival that pushed Miho and her childhood friends to their absolute limits. Their training sessions are rumored to be as difficult as university-level matches."
    },
    {
        "name": "Koala Forest Academy",
        "tank": "AC.I Sentinel",
        "commander": "Koala",
        "image": "images/Koala.jpg",
        "overview": "An Australian-themed school known for its laid-back atmosphere and unique leadership structure. While they are relaxed outside of combat, they are surprisingly disciplined once the hatches are closed.",
        "tactics": "They use 'Bushcraft' tactics, excelling at camouflage and long-range harassment. They often wait patiently for the enemy to make a mistake before counter-attacking with their sturdy Sentinels.",
        "weapons": "Australian-produced tanks like the AC.I Sentinel and various British lend-lease vehicles like the Matilda II.",
        "characters": "The 'Commander' is an actual Koala who 'decides' tactics based on which leaf it eats; the human vice-commander, Wallaby, interprets these as strategic commands.",
        "trivia": "The students are experts at survival training. The school is one of the few to operate a tank designed and built in its representative country (the Sentinel)."
    },
    {
        "name": "Maple High School",
        "tank": "Light Tank Mk VIB",
        "commander": "Trout",
        "image": "images/Maple.jpg",
        "overview": "A Canadian-themed school known for its rugged endurance and specialty in forest combat. They are extremely polite off the field but become incredibly aggressive once a match begins.",
        "tactics": "Specialists in 'Timber' ambushes. They use the natural cover of forests and heavy foliage to hide their light tanks, striking the enemy's side armor at point-blank range.",
        "weapons": "British-derived light armor, including the Light Tank Mk VIB and the Ram II medium tank.",
        "characters": "Commander Trout, a master of wilderness survival, and her vice-commander, Maple.",
        "trivia": "They are the only school that produces its own high-grade maple syrup, which they often trade with Saunders for mechanical parts."
    },
    {
        "name": "Tategoto High School",
        "tank": "Type 95 Ha-Go",
        "commander": "Aung",
        "image": "images/tategoto.jpg",
        "overview": "A Myanmar-themed school (formerly Burma) that emphasizes spiritual discipline and endurance. They are often seen as the 'gentle' school, but they possess a quiet, unbreakable resolve.",
        "tactics": "They use 'Jungle Ghost' tactics, utilizing heavy camouflage and silent movement to get within point-blank range of the enemy before striking.",
        "weapons": "Japanese-made light tanks used during the Burma campaign, specifically the Type 95 Ha-Go and Type 97 Chi-Ha.",
        "characters": "Commander Aung, a calm and meditative leader who rarely raises her voice.",
        "trivia": "Tategoto means 'Harp' in Japanese, a reference to the film 'The Burmese Harp.' The students are known for playing music to relax before a match."
    },
    {
        "name": "Tatenashi High School",
        "tank": "Type 97 Te-Ke",
        "commander": "Shizuka Tsuruki",
        "image": "images/Tatenashi.jpg",
        "overview": "A traditional Japanese school that specializes in 'Tankathlon' (unregulated, light-tank-only street matches). They are the primary focus of the 'Ribbon no Musha' manga series.",
        "tactics": "Psychological and reckless warfare. Shizuka, the 'Centipede Commander,' uses terrifying, unpredictable movements to make her single light tank seem like a ghostly legion. They ignore traditional rules to achieve victory.",
        "weapons": "Primarily the Type 97 Te-Ke tankette and other light Japanese vehicles.",
        "characters": "Shizuka Tsuruki, a girl who believes she is a reincarnated samurai, and Rin Matsukaze, her loyal driver.",
        "trivia": "Shizuka often enters a trance-like state in battle where she 'sees' the battlefield as a traditional Japanese painting."
    },
    {
        "name": "Viggen High School",
        "tank": "Strv m/40",
        "commander": "Semla",
        "image": "images/Viggen.jpg",
        "overview": "A Swedish-themed school that focuses on mountainous and cold-weather operations. They are smaller than Viking Fisheries but have a reputation for high-tech maintenance and extremely reliable equipment.",
        "tactics": "Specialists in 'Hull-Down' defense. They use the excellent gun depression of their Swedish tanks to fire from behind ridges, exposing as little of their tank as possible to the enemy.",
        "weapons": "Swedish-made armor, primarily the Stridsvagn m/40 and the m/42 Lago.",
        "characters": "Semla, a tactical commander who is often seen consulting complex topographical maps before a match.",
        "trivia": "The school is named after the Saab 37 Viggen fighter jet. They are famous for their fika (coffee breaks), which they take very seriously regardless of the situation."
    },
    {
        "name": "West Kureouji Grona Academy",
        "tank": "Black Prince",
        "commander": "Kiri Shiratori",
        "image": "images/Grona.jpg",
        "overview": "A high-class British-themed school that rivals St. Gloriana in prestige but focuses on late-war, heavy industrial doctrine. They are quite wealthy and pride themselves on fielding rare 'experimental' vehicles.",
        "tactics": "They utilize 'Heavy Infantry Tank' doctrine. They deploy the Black Prince to act as an indestructible mobile fortress, slowly crawling forward while absorbing all incoming fire to protect their lighter cruisers.",
        "weapons": "Rare British heavy armor including the A43 Black Prince and various Churchill variants.",
        "characters": "Kiri Shiratori, a refined commander who views Sensha-dō as a high-stakes game of chess.",
        "trivia": "They often hold joint 'tea parties' with St. Gloriana, though there is a subtext of intense social competition between the two schools."
    },
    {
        "name": "Yogurt Academy",
        "tank": "CV.33",
        "commander": "Sofia",
        "image": "images/Yogurt.jpg",
        "overview": "A Bulgarian-themed school that focuses on light-weight, high-speed hit-and-run tactics. They are often invited to exhibition matches because of their unique, energetic fighting style.",
        "tactics": "They employ 'Swarm' tactics, using a high number of very cheap tankettes to overwhelm a single target's ability to aim and reload.",
        "weapons": "Light Italian and German armor, primarily the Carro Veloce CV.33 and the Panzer 38(t).",
        "characters": "Commander Sofia, an energetic leader who is also a champion in rhythmic gymnastics.",
        "trivia": "They claim to have the healthiest students in the Federation due to their mandatory diet of Bulgarian yogurt and honey."
    },
    {
        "name": "Neutral High School",
        "tank": "No Tank (Observer)",
        "commander": "Senjyu",
        "image": "images/Natural.jpg",
        "overview": "A unique school that models itself after Switzerland. True to their name, they rarely participate in active combat, instead serving as the official mediators and observers for the Sensha-dō Federation.",
        "tactics": "When they do fight, they use 'Alpine Fortress' tactics—occupying high ground and forcing the enemy to attack into a heavily fortified bottleneck.",
        "weapons": "Typically they use Panzerwagen 39 (LTH) and other Swiss-operated light vehicles.",
        "characters": "Commander Senjyu, a fair-minded and observant leader who is often called upon to judge disputes between schools.",
        "trivia": "Because of their neutrality, their Academy Ship is considered a safe haven where students from rival schools can meet and socialize without conflict."
    }

]

higher_education = [
    {
        "name": "All-Stars University Team",
        "tank": "Centurion Mk.I",
        "commander": "Alice Shimada",
        "image": "images/Stars.jpg",
        "overview": "The absolute pinnacle of Sensha-dō in Japan. This is a hand-picked team of the best university-level players, organized to face professional and international threats. They possess unlimited resources and the most advanced technology allowed by the Federation.",
        "tactics": "They use the 'Shimada Style,' which emphasizes terrifyingly precise individual skill combined with overwhelming mathematical strategy. Unlike high schools that use specific themes, the All-Stars use a 'Combined Arms' approach where every tank is a specialized counter to the enemy's strengths.",
        "weapons": "Late-war and post-war monsters, including the Centurion Mk.I, the T28 Super Heavy Tank, the M26 Pershing, and the Karl-Gerät 040 siege mortar.",
        "characters": "Alice Shimada, the child prodigy commander; the 'Big Three' vice-commanders (Azumi, Megumi, and Rumi).",
        "trivia": "Alice Shimada is the heir to the Shimada Style, the only rival to the Nishizumi Style. She is also an obsessed fan of 'Boko the Bear,' much like Miho Nishizumi."
    }
]


theater_items = {
    "main": [
        {"title": "Girls und Panzer (Main Series)", "image": "images/main_series.jpg", "link": "/watch"}
    ],
    "specials": [
        {"title": "This is the Real Anzio Battle!", "image": "images/anzio_ova.jpg", "link": "/theater/anzio"},
        {"title": "Alice War!", "image": "images/alice_war.jpg", "link": "/theater/alice"},
        {"title": "Taiyaki War!", "image": "images/taiyaki_war.jpg", "link": "/theater/taiyaki"}
    ]
}

main_series_episodes = [
    {
        "number": 1, 
        "title": "Tankery, Here It Is!", 
        "file": "ep1.mp4", 
        "desc": "Miho Nishizumi transfers to Oarai Girls Academy to escape Tankery, but the student council has other plans."
    },
    {
        "number": 2, 
        "title": "Tankery is Real!", 
        "file": "ep2.mp4", 
        "desc": "The newly formed teams set out to find the school's abandoned tanks and begin their first practice."
    },
    {
        "number": 3, 
        "title": "I'm Taking This Match!", 
        "file": "ep3.mp4", 
        "desc": "Oarai engages in an exhibition match against the heavy hitters of St. Gloriana Girls' College."
    },
    {
        "number": 4, 
        "title": "The Commander Does Her Best!", 
        "file": "ep4.mp4", 
        "desc": "As the national tournament begins, Oarai faces the Saunders University High School and their overwhelming numbers."
    },
    {
        "number": 5, 
        "title": "The Sherman Corps!", 
        "file": "ep5.mp4", 
        "desc": "The battle against Saunders intensifies as Miho uses clever tactics to counter their radio interception."
    },
    {
        "number": 6, 
        "title": "The First Round Reaches Its Climax!", 
        "file": "ep6.mp4", 
        "desc": "With their backs against the wall, the Ankou team attempts a daring high-stakes maneuver to take down the Saunders flagship."
    },
    {
        "number": 7, 
        "title": "Next is Anzio!", 
        "file": "ep7.mp4", 
        "desc": "While preparing for the next round, the girls take a break to explore the school ship and strengthen their bonds."
    },
    {
        "number": 8, 
        "title": "Pravda is Here!", 
        "file": "ep8.mp4", 
        "desc": "Oarai faces the defending champions, Pravda Girls' High School, in a brutal winter landscape."
    },
    {
        "number": 9, 
        "title": "Desperate Situation!", 
        "file": "ep9.mp4", 
        "desc": "Trapped in a church and surrounded by Pravda's tanks, the Oarai teams must find a way to break the siege before time runs out."
    },
    {
        "number": 10, 
        "title": "Classmates!", 
        "file": "ep10.mp4", 
        "desc": "The finals against Kuromorimine begins. Miho must face her sister, Maho, and the formidable Black Forest Peak doctrine."
    },
    {
        "number": 11, 
        "title": "The Battle is Fierce!", 
        "file": "ep11.mp4", 
        "desc": "Oarai struggles against the heavy German armor of Kuromorimine, leading to a dangerous rescue mission in the river."
    },
    {
        "number": 12, 
        "title": "The Battle We Can't Withdraw From!", 
        "file": "ep12.mp4", 
        "desc": "The final showdown. In a city-wide chase, Miho and Maho engage in a one-on-one duel to decide the fate of Oarai Academy."
    }
]

theater_items["finale"] = [
    {"title": "Girls und Panzer: das Finale", "image": "images/finale_poster.jpg", "link": "/theater/finale"}
]

theater_items["movies"] = [
    {"title": "Der Film", "image": "images/der_film.jpg", "link": "/theater/movie"}
]

finale_episodes = [
    {
        "number": 1, 
        "title": "Das Finale - Part 1", 
        "file": "finale1.mp4", 
        "desc": "Oarai Academy faces a new crisis, leading to the creation of the Shark Team and a battle against BC Freedom."
    },
    {
        "number": 2, 
        "title": "Das Finale - Part 2", 
        "file": "finale2.mp4", 
        "desc": "The battle against BC Freedom concludes, and the winter tournament continues against the spirited Chi-Ha-Tan Academy."
    },
    {
        "number": 3, 
        "title": "Das Finale - Part 3", 
        "file": "finale3.mp4", 
        "desc": "The jungle warfare reaches its peak! Afterward, Oarai prepares for a chilling match against Jatkosota High School."
    },
    {
        "number": 4, 
        "title": "Das Finale - Part 4", 
        "file": "finale4.mp4", 
        "desc": "Trapped in the snow, Oarai must fight without their commander after a devastating ambush by the White Witch."
    },
    {
        "number": 5, 
        "title": "Das Finale - Part 5", 
        "file": "finale5.mp4", 
        "desc": "The semifinals reach a boiling point as the remaining schools fight for a spot in the ultimate championship match."
    },
    {
        "number": 6, 
        "title": "Das Finale - Part 6", 
        "file": "finale6.mp4", 
        "desc": "The grand finale of the Sensha-do saga. One final battle to decide the future of the academy and the legend of the Nishizumi style."
    }
]

season1_ovas = [
    {"number": 1, "title": "Water War", "file": "s1_ova1.mp4", "desc": "The girls pick out swimsuits and enjoy a day at the pool."},
    {"number": 2, "title": "Survival War", "file": "s1_ova2.mp4", "desc": "The teams go camping and learn about field rations."},
    {"number": 3, "title": "School Ship War", "file": "s1_ova3.mp4", "desc": "A deep dive into how the massive school ships actually function."},
    {"number": 4, "title": "Anglerfish War", "file": "s1_ova4.mp4", "desc": "The girls practice the legendary Anglerfish Dance."},
    {"number": 5, "title": "Snow War", "file": "s1_ova5.mp4", "desc": "Yukari and Erwin go on a scouting mission in the snow."},
    {"number": 6, "title": "Banquet War", "file": "s1_ova6.mp4", "desc": "A celebration following the tournament victory."}
]

finale_ovas = [
    {
        "number": 1, 
        "title": "Radish War!", 
        "file": "finale_ova2.mp4", 
        "desc": "The Das Finale Part 2 special featuring the continuation of the peaceful yet competitive school life."
    },
    {
        "number": 2, 
        "title": "Daikon War!", 
        "file": "finale_ova3.mp4", 
        "desc": "The Das Finale Part 3 special. Agricultural conflict reaches new heights at Oarai."
    },
    {
        "number": 3, 
        "title": "The Jotunheim Trio", 
        "file": "finale_ova4.mp4", 
        "desc": "The Das Finale Part 4 special focusing on the mysterious trio from Jatkosota High School."
    }
]

@app.route("/theater/season1-specials")
def s1_specials():
    return render_template("specials.html", episodes=season1_ovas)

@app.route("/theater/radish-war")
def radish_war():
    return render_template("ova_radish.html", 
                           title="Radish War!", 
                           file="finale_ova2.mp4", 
                           desc="The Das Finale Part 2 special.")

@app.route("/theater/daikon-war")
def daikon_war():
    return render_template("ova_daikon.html", 
                           title="Daikon War!", 
                           file="finale_ova3.mp4", 
                           desc="The Das Finale Part 3 special.")

@app.route("/theater/jotunheim")
def jotunheim():
    return render_template("ova_jotunheim.html", 
                           title="The Jotunheim Trio", 
                           file="finale_ova4.mp4", 
                           desc="The Das Finale Part 4 special.")

@app.route("/theater")
def theater():
    return render_template("theater.html", items=theater_items)

@app.route("/theater/anzio")
def anzio():
    return render_template("ova1.html")

@app.route("/theater/alice")
def alice():
    return render_template("ova2.html")

@app.route("/theater/taiyaki")
def taiyaki():
    return render_template("ova3.html")

@app.route("/theater/finale")
def finale_page():
    return render_template("dasfinale.html", episodes=finale_episodes)

@app.route("/theater/movie")
def movie():
    movie_data = {
        "title": "Girls und Panzer der Film",
        "file": "der_film.mp4",
        "desc": "Oarai Academy faces decommission once again. To save their school, they must team up with their former rivals to face a formidable University All-Stars team led by the prodigy Alice Shimada."
    }
    return render_template("movie.html", movie=movie_data)

@app.route("/")
def intro():
    return render_template("intro.html")

@app.route("/schools")
def home():
    return render_template(
        "index.html",
        main_schools=main_schools,
        minor_schools=minor_schools,
        higher_education=higher_education
    )

@app.route("/school/<int:id>")
def school_page(id):
    all_schools = main_schools + minor_schools + higher_education
    try:
        school = all_schools[id]
        return render_template("school.html", school=school)
    except IndexError:
        return "School not found", 404
    

@app.route("/watch")
def watch():
    return render_template("watch.html", episodes=main_series_episodes)

if __name__ == "__main__":
    app.run(debug=True)