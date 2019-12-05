"""
Hangman. Made by Timothy.
Started on 12/4/19
Finished on 12/5/19
"""

import time
import random

six = """
*=====:
|     :
|
|
|
|_______
"""

five = """
*=====:
|     :
|     O
|
|
|_______
"""

four = """
*=====:
|     :
|     O
|     |
|
|_______
"""

three = """
*=====:
|     :
|     O
|    /|
|
|_______
"""

two = """
*=====:
|     :
|     O
|    /|\\
|
|_______
"""

one = """
*=====:
|     :
|     O
|    /|\\
|    / 
|_______
"""

dead = """
*=====:
|     :
|     O
|    /|\\
|    / \\
|_______
"""
frames = [dead, one, two, three, four, five, six]


def word(difficulty):
    words = "about, above, abuse, accept, accident, accuse, across, activist, actor, administration, admit, adult, advertise, advise, affect, afraid, after, again, against, agency, aggression, agree, agriculture, force, airplane, airport, album, alcohol, alive, almost, alone, along, already, although, always, ambassador, amend, ammunition, among, amount, anarchy, ancestor, ancient, anger, animal, anniversary, announce, another, answer, apologize, appeal, appear, appoint, approve, archeology, argue, around, arrest, arrive, artillery, assist, astronaut, astronomy, asylum, atmosphere, attach, attack, attempt, attend, attention, automobile, autumn, available, average, avoid, awake, award, balance, balloon, ballot, barrier, battle, beauty, because, become, before, begin, behavior, behind, believe, belong, below, betray, better, between, biology, black, blame, bleed, blind, block, blood, border, borrow, bottle, bottom, boycott, brain, brave, bread, break, breathe, bridge, brief, bright, bring, broadcast, brother, brown, budget, build, building, bullet, burst, business, cabinet, camera, campaign, cancel, cancer, candidate, capital, capture, career, careful, carry, catch, cause, ceasefire, celebrate, center, century, ceremony, chairman, champion, chance, change, charge, chase, cheat, cheer, chemicals, chemistry, chief, child, children, choose, circle, citizen, civilian, civil, rights, claim, clash, class, clean, clear, clergy, climate, climb, clock, close, cloth, clothes, cloud, coalition, coast, coffee, collapse, collect, college, colony, color, combine, command, comment, committee, common, communicate, community, company, compare, compete, complete, complex, compromise, computer, concern, condemn, condition, conference, confirm, conflict, congratulate, Congress, connect, conservative, consider, constitution, contact, contain, container, continent, continue, control, convention, cooperate, correct, corruption, cotton, count, country, court, cover, crash, create, creature, credit, crime, criminal, crisis, criticize, crops, cross, crowd, crush, culture, curfew, current, custom, customs, damage, dance, danger, daughter, debate, decide, declare, decrease, defeat, defend, deficit, define, degree, delay, delegate, demand, democracy, demonstrate, denounce, depend, deplore, deploy, depression, describe, desert, design, desire, destroy, detail, detain, develop, device, dictator, different, difficult, dinner, diplomat, direct, direction, disappear, disarm, disaster, discover, discrimination, discuss, disease, dismiss, dispute, dissident, distance, divide, doctor, document, dollar, donate, double, dream, drink, drive, drown, during, early, earth, earthquake, ecology, economy, education, effect, effort, either, elect, electricity, embassy, embryo, emergency, emotion, employ, empty, enemy, energy, enforce, engine, engineer, enjoy, enough, enter, environment, equal, equipment, escape, especially, establish, estimate, ethnic, evaporate, event, every, evidence, exact, examine, example, excellent, except, exchange, excuse, execute, exercise, exile, exist, expand, expect, expel, experience, experiment, expert, explain, explode, explore, export, express, extend, extra, extraordinary, extreme, extremist, factory, false, family, famous, father, favorite, federal, female, fence, fertile, field, fierce, fight, final, financial, finish, fireworks, first, float, flood, floor, flower, fluid, follow, force, foreign, forest, forget, forgive, former, forward, freedom, freeze, fresh, friend, frighten, front, fruit, funeral, future, gather, general, generation, genocide, gentle, glass, goods, govern, government, grain, grass, great, green, grind, ground, group, guarantee, guard, guerrilla, guide, guilty, happen, happy, harvest, headquarters, health, heavy, helicopter, hijack, history, holiday, honest, honor, horrible, horse, hospital, hostage, hostile, hotel, house, however, human, humor, hunger, hurry, husband, identify, ignore, illegal, imagine, immediate, immigrant, import, important, improve, incident, incite, include, increase, independent, individual, industry, infect, inflation, influence, inform, information, inject, injure, innocent, insane, insect, inspect, instead, instrument, insult, intelligence, intelligent, intense, interest, interfere, international, Internet, intervene, invade, invent, invest, investigate, invite, involve, island, issue, jewel, joint, judge, justice, kidnap, knife, knowledge, labor, laboratory, language, large, laugh, launch, learn, leave, legal, legislature, letter, level, liberal, light, lightning, limit, liquid, listen, literature, little, local, lonely, loyal, machine, magazine, major, majority, manufacture, march, market, marry, material, mathematics, matter, mayor, measure, media, medicine, member, memorial, memory, mental, message, metal, method, microscope, middle, militant, military, militia, mineral, minister, minor, minority, minute, missile, missing, mistake, model, moderate, modern, money, month, moral, morning, mother, motion, mountain, mourn, movement, movie, murder, music, mystery, narrow, nation, native, natural, nature, necessary, negotiate, neighbor, neither, neutral, never, night, noise, nominate, normal, north, nothing, nowhere, nuclear, number, object, observe, occupy, ocean, offensive, offer, office, officer, official, often, operate, opinion, oppose, opposite, oppress, orbit, order, organize, other, overthrow, paint, paper, parachute, parade, pardon, parent, parliament, partner, party, passenger, passport, patient, peace, people, percent, perfect, perform, period, permanent, permit, person, persuade, physical, physics, picture, piece, pilot, place, planet, plant, plastic, please, plenty, point, poison, police, policy, politics, pollute, popular, population, position, possess, possible, postpone, poverty, power, praise, predict, pregnant, present, president, press, pressure, prevent, price, prison, private, prize, probably, problem, process, produce, profession, professor, profit, program, progress, project, promise, propaganda, property, propose, protect, protest, prove, provide, public, publication, publish, punish, purchase, purpose, quality, question, quick, quiet, radar, radiation, radio, railroad, raise, reach, react, ready, realistic, reason, reasonable, rebel, receive, recent, recession, recognize, record, recover, reduce, reform, refugee, refuse, register, regret, reject, relations, release, religion, remain, remains, remember, remove, repair, repeat, report, represent, repress, request, require, rescue, research, resign, resist, resolution, resource, respect, responsible, restaurant, restrain, restrict, result, retire, return, revolt, right, river, rocket, rough, round, rubber, rural, sabotage, sacrifice, sailor, satellite, satisfy, school, science, search, season, second, secret, security, seeking, seize, Senate, sense, sentence, separate, series, serious, serve, service, settle, several, severe, shake, shape, share, sharp, sheep, shell, shelter, shine, shock, shoot, short, should, shout, shrink, sickness, signal, silence, silver, similar, simple, since, single, sister, situation, skeleton, skill, slave, sleep, slide, small, smash, smell, smoke, smooth, social, soldier, solid, solve, sound, south, space, speak, special, speech, speed, spend, spill, spirit, split, sport, spread, spring, square, stand, start, starve, state, station, statue, steal, steam, steel, stick, still, stone, store, storm, story, stove, straight, strange, street, stretch, strike, strong, structure, struggle, study, stupid, subject, submarine, substance, substitute, subversion, succeed, sudden, suffer, sugar, suggest, suicide, summer, supervise, supply, support, suppose, suppress, surface, surplus, surprise, surrender, surround, survive, suspect, suspend, swallow, swear, sweet, sympathy, system, target, taste, teach, technical, technology, telephone, telescope, television, temperature, temporary, tense, terrible, territory, terror, terrorist, thank, theater, theory, there, these, thick, thing, think, third, threaten, through, throw, tired, today, together, tomorrow, tonight, torture, total, touch, toward, trade, tradition, traffic, tragic, train, transport, transportation, travel, treason, treasure, treat, treatment, treaty, trial, tribe, trick, troops, trouble, truce, truck, trust, under, understand, unite, universe, university, unless, until, urgent, usual, vacation, vaccine, valley, value, vegetable, vehicle, version, victim, victory, video, village, violate, violence, visit, voice, volcano, volunteer, wages, waste, watch, water, wealth, weapon, weather, weigh, welcome, wheat, wheel, where, whether, which, while, white, whole, willing, window, winter, withdraw, without, witness, woman, wonder, wonderful, world, worry, worse, worth, wound, wreck, wreckage, write, wrong, yellow, yesterday, young"
    words_list = words.lower().split(", ")
    give = words_list[random.randint(1, len(words_list) + 1)]
    if difficulty <= 0:
        while len(give) > 6:
            give = words_list[random.randint(1, len(words_list))]
    elif difficulty == 1:
        while not 6 < len(give) < 9:
            give = words_list[random.randint(1, len(words_list))]
    elif difficulty >= 2:
        while len(give) < 9:
            give = words_list[random.randint(1, len(words_list))]
    return give


def search(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def add_margin():
    for i in range(200):
        print("")


# animation when game starts
def introduction():
    for life in reversed(frames):
        add_margin()
        print(life)
        time.sleep(.35)


def hangman(rand_word):
    rand_word.lower()
    # start off with 6 lives
    lives = 6
    rand_word_length = len(rand_word)
    rand_word_char = list(rand_word)
    printed_string = "_" * rand_word_length
    spaced_printed_string = "_ " * rand_word_length
    already_guessed = []
    guessed_letter = ""
    guessed_correctly = False
    add_margin()
    # loop until out of lives or guessed the word
    while lives > 0:
        # make sure player entered a single letter before moving on
        while True:
            try:
                if guessed_correctly:
                    add_margin()
                    guessed_correctly = False
                print(frames[lives])
                print(spaced_printed_string)
                guessed_letter = (input(">>>"))
                # check if guessed_letter is int
                val = int(guessed_letter)
                add_margin()
                print("You can only use single letters")
            except ValueError:
                # check if guessed_letter is a single character
                if len(guessed_letter) == 1:
                    guessed_letter.lower()
                    # check if it was already guessed
                    if guessed_letter in already_guessed:
                        add_margin()
                        print("You've already guessed that letter")
                        pass
                    else:
                        already_guessed.append(guessed_letter)
                        break
                else:
                    add_margin()
                    print("You can only use single letters")
                    pass
        # check if guessed_letter is in rand_word
        if guessed_letter in rand_word_char:
            # find all indexes of guessed_letter in rand_word
            indexes_in_word = search(rand_word, guessed_letter)
            # put guessed_letter in those indexes
            for index in indexes_in_word:
                # change it into list so that characters can be replaced
                printed_string = list(printed_string)
                printed_string[index] = guessed_letter
                printed_string = "".join(printed_string)
                guessed_correctly = True
        else:
            lives -= 1
            add_margin()
            # check if player loses
            if lives == 0:
                # player loses. end loop
                add_margin()
                print("YOU LOSE")
                print(dead)
                # show word
                print(" ".join(rand_word))
                print()
                break
        # add spaces between all characters in printed_string
        spaced_printed_string = " ".join(printed_string)
        # check if all letters are guessed
        if printed_string.find("_") == -1:
            # player wins. end loop
            add_margin()
            print("YOU WIN")
            print(frames[lives])
            # show word
            print(" ".join(rand_word))
            print()
            break


while True:
    try:
        introduction()
        time.sleep(.8)
        add_margin()

        print("HANGMAN")
        print(dead)
        # print("Press CTRL + C to quit ")
        start = " "
        while start != "" and start != "quit":
            print("Press ENTER to start ")
            print('Type "Quit" to quit ')
            start = input(">>>")
            start = start.strip()
            start = start.lower()

        if start == "quit":
            print("Quitting...")
            break

        diff = 3
        while not diff == 0 and not diff == 1 and not diff == 2:
            try:
                print("Choose a difficulty between 0-2 ")
                diff = int((input(">>>")))
            except ValueError:
                pass

        playing = True
        while playing:
            hangman(word(diff))
            print("")
            play_again = 2
            # make sure player entered 0 or 1
            while not play_again == 0 and not play_again == 1:
                try:
                    print("Play again? (0 = main menu, 1 = play again)")
                    play_again = int(input(">>>"))
                    if play_again == 0:
                        playing = False
                    if play_again == 1:
                        pass
                except ValueError:
                    pass

    except KeyboardInterrupt:
        print("Quitting...")
