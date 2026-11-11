
from datetime import date
from pathlib import Path

TOPICS = [
    {
        "topic": "Yorker kya hoti hai?",
        "hook": "Kya tum jaante ho yorker ball itni dangerous kyun hoti hai?",
        "script": "Yorker ek aisi delivery hai jo batsman ke pairon ke paas pitch hoti hai. Isse powerful shot khelna mushkil ho sakta hai.",
        "visual": "Cricket pitch animation and ball illustration"
    },
    {
        "topic": "Powerplay kya hota hai?",
        "hook": "Cricket mein powerplay ka asli purpose kya hai?",
        "script": "Powerplay limited overs cricket ka ek special phase hai. Ismein fielding restrictions hoti hain, jisse batting aur bowling dono ki strategy badalti hai.",
        "visual": "Animated cricket field with fielders"
    },
    {
        "topic": "DRS kya hai?",
        "hook": "Umpire ka decision technology kaise badal sakti hai?",
        "script": "DRS ka full form Decision Review System hai. Is system se teams kuch umpire decisions ko review karne ki request kar sakti hain.",
        "visual": "Umpire review screen animation"
    },
    {
        "topic": "Wide aur no-ball",
        "hook": "Wide aur no-ball mein difference pata hai?",
        "script": "Wide aur no-ball dono alag types ki illegal deliveries hain. Inke rules alag hain aur dono par batting team ko extra run milta hai.",
        "visual": "Cricket umpire signals"
    },
    {
        "topic": "Swing bowling",
        "hook": "Cricket ball hawa mein direction kaise badalti hai?",
        "script": "Swing bowling mein bowler ball ko hawa mein movement karwane ki koshish karta hai. Isse batsman ke liye timing mushkil ho sakti hai.",
        "visual": "Animated swinging cricket ball"
    }
]

today = date.today()
item = TOPICS[(today.timetuple().tm_yday - 1) % len(TOPICS)]

output = f"""# Cricket Shorts - {today}

## Topic
{item['topic']}

## Hook
{item['hook']}

## Hindi Voiceover
{item['hook']}

{item['script']}

Cricket ke aur interesting facts ke liye channel ko subscribe karo!

## Video Visual
{item['visual']}

## YouTube Title
{item['topic']} 😱 | Cricket Facts #shorts

## Description
Aaj jaano cricket ka ek interesting topic!
Video pasand aaye to like aur subscribe karo.

## Hashtags
#Cricket #CricketFacts #Shorts #HindiCricket

## Editing Instructions
- Format: 9:16 vertical
- Duration: 20-30 seconds
- Add Hindi voiceover
- Use original graphics and animations
- Add subtitles and sound effects
"""

folder = Path("content")
folder.mkdir(exist_ok=True)

file = folder / f"short-{today}.md"
file.write_text(output, encoding="utf-8")

print(f"SUCCESS: Content created at {file}")
