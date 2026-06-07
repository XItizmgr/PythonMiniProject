import random
subjects = [
    "Elon Musk",
    "Taylor Swift",
    "Cristiano Ronaldo",
    "Lionel Messi",
    "Bill Gates",
    "Mark Zuckerberg",
    "Sundar Pichai",
    "Tim Cook",
    "MrBeast",
    "Virat Kohli",
    "Shah Rukh Khan",
    "Tom Cruise",
    "Dwayne Johnson",
    "Emma Watson",
    "Keanu Reeves",
    "Narendra Modi",
    "Barack Obama",
    "Donald Trump",
    "Greta Thunberg",
    "Mukesh Ambani"
]
actions = [
    "launches",
    "buys",
    "sells",
    "discovers",
    "creates",
    "accidentally deletes",
    "invests in",
    "announces",
    "bans",
    "adopts",
    "builds",
    "finds",
    "tests",
    "reveals",
    "promotes",
    "upgrades",
    "opens",
    "closes",
    "wins",
    "loses"
]
objects = [
    "a flying bicycle",
    "a secret AI project",
    "a colony on Mars",
    "a giant pizza factory",
    "a robot army",
    "a talking refrigerator",
    "a million-dollar sandwich",
    "a new social media app",
    "a time machine",
    "a smart toothbrush",
    "a virtual zoo",
    "a gold-plated laptop",
    "a moon hotel",
    "a self-driving skateboard",
    "a floating city",
    "a 100-foot burger",
    "a gaming spaceship",
    "a digital pet dinosaur",
    "a solar-powered umbrella",
    "a chocolate-powered car"
]
while True:
    subject = random.choice(subjects)
    action= random.choice(actions)
    object = random.choice(objects)
    print(f'Beaking News : {subject} {action} {object}')
    user_input = input("\n Do u want to create another headline ? (yes/no):").strip().lower()
    if user_input == "no":
        break
    
print("Have a good day with the news ")