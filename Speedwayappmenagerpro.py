import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Symulator Żużlowy PRO 2026", layout="wide")
st.title("🏁 Symulator Meczów Żużlowych - Sezon 2026")

# 1. Baza Klubów
druzyny_pge = {
    "PRES Grupa Deweloperska Toruń": {
        "seniorzy": ["Patryk Dudek", "Robert Lambert", "Mikkel Michelsen", "Emil Sajfutdinow"],
        "u24": ["Norick Bloedorn"],
        "juniorzy": ["Antoni Kawczyński", "Mikołaj Duchiński", "Mateusz Affelt", "Bartosz Derek", "Robert Downar", "Nicolai Heiselberg", "Wiktor Jasiński II", "Dominik Łakomy", "Oskar Rumiński", "Ksawery Słomski"]
    },
    "Orlen Oil Motor Lublin": {
        "seniorzy": ["Bartosz Zmarzlik", "Fredrik Lindgren", "Kacper Woryna", "Martin Vaculik", "Josh Pickering"],
        "u24": ["Mateusz Cierniak"],
        "juniorzy": ["Bartosz Bańbor", "Bartosz Jaworski", "Dawid Cepielik", "Sven Cerjak", "Paweł Czaus", "Dawid Grzeszczyk", "Michał Psiuk", "Karol Szmyd"]
    },
    "Betard Sparta Wrocław": {
        "seniorzy": ["Artiom Łaguta", "Maciej Janowski", "Daniel Bewley", "Brady Kurtz"],
        "u24": ["Bartłomiej Kowalski", "Francis Gusts"],
        "juniorzy": ["Mikkel Andersen", "Filip Kumaszka", "Krystian Gręda", "Rafał Grzędziński", "Paweł Sitek"]
    },
    "Bayersystem GKM Grudziądz": {
        "seniorzy": ["Max Fricke", "Maksym Drabik", "Wadim Tarasienko", "Michael Jepsen Jensen"],
        "u24": ["Kacper Łobodziński"],
        "juniorzy": ["Kevin Małkiewicz", "Bastian Pedersen", "Jan Przanowski", "Beau Bailey", "Kevin Iwański-Helt", "Damian Miller", "Kacper Szarszewski", "Oliver Nielsen"]
    },
    "Stelmet Falubaz Zielona Góra": {
        "seniorzy": ["Leon Madsen", "Dominik Kubera", "Andrzej Lebiediew", "Przemysław Pawlicki"],
        "u24": ["Michał Curzytek"],
        "juniorzy": ["Damian Ratajczak", "Oskar Hurysz", "William Cairns", "Eryk Farański", "Slater Lightcap", "Mitchell McDiarmid", "Villads Pedersen", "Bartosz Rudolf", "Rafał Sękowski", "Kacper Witrykus"]
    },
    "Krono-Plast Włókniarz Częstochowa": {
        "seniorzy": ["Rohan Tungate", "Jaimon Lidsey", "Mads Hansen", "Jakub Miśkowiak"],
        "u24": ["Sebastian Szostak"],
        "juniorzy": ["Franciszek Karczewski", "Szymon Ludwiczak", "Paweł Caban", "Alan Ciurzyński", "James Pearson", "Dawid Rozpędek", "Bartosz Śmigielski"]
    },
    "Gezet Stal Gorzów": {
        "seniorzy": ["Anders Thomsen", "Jack Holder", "Paweł Przedpełski", "Marcel Szymko", "Wiktor Trofimov", "Timo Lahti", "Adrian Gała"],
        "u24": ["Mathias Pollestad"],
        "juniorzy": ["Oskar Paluch", "Adam Bednar", "Hubert Jabłoński", "Denis Andrzejczak", "Dominik Baryłka", "Oskar Chatłas", "Igor Kordun", "Sebastian Mayland", "Kewin Nycz", "Andreas Olsen"]
    },
    "Fogo Unia Leszno": {
        "seniorzy": ["Janusz Kołodziej", "Piotr Pawlicki", "Grzegorz Zengota", "Ben Cook", "Andreas Johansson"],
        "u24": ["Keynan Rew", "Janusz Kołodziej"],
        "juniorzy": ["Nazar Parnicki", "Kacper Mania", "Marcel Juskowiak", "Krystian Buczyński", "Filip Gano", "Emil Konieczny", "Maksymilian Kostera", "Krzysztof Skorczyk", "Kuba Wojtyńka", "Jakub Żurek"]
    }
}

druzyny_metalkas = {
    "Energa Wybrzeże Gdańsk": {
        "seniorzy": ["Jacob Thorssell", "Timo Lahti", "Tim Sørensen", "Krystian Pieszczek",],
        "u24": ["Mateusz Bartkowiak", "Miłosz Wysocki", "Casper Henriksson"],
        "juniorzy": ["Jan Przanowski", "Eryk Kamiński", "Niklas Holm Jakobsen", "Kacper Warduliński", "Mikołaj Krok", "Jakub Redzimski", "Jakub Malina"]
    },
    "Abramczyk Polonia Bydgoszcz": {
        "seniorzy": ["Szymon Woźniak", "Kai Huckenbeck", "Aleksandr Łoktajew", "Krzysztof Buczkowski", "Tom Brennan", "Janusz Kołodziej"],
        "u24": [],
        "juniorzy": ["Maksymilian Pawełczak", "Kacper Andrzejewski", "Adam Putkowski", "Jan Rompkowski"]
    },
    "H.Skrzydlewska Orzeł Łódź": {
        "seniorzy": ["Marcin Nowak", "Oliver Berntzon", "Zach Cook", "Szymon Szlauderbach"],
        "u24": ["Villads Nagel", "Dan Thompson"],
        "juniorzy": ["Krzysztof Lewandowski", "Jakub Orgacki", "Tomasz Szeląg", "Seweryn Orgacki"]
    },
    "Cellfast Wilki Krosno": {
        "seniorzy": ["Jason Doyle", "Tobiasz Musielak", "Robert Chmiel", "Luke Becker"],
        "u24": [],
        "juniorzy": ["Szymon Bańdur", "Jakub Woźnik", "Radosław Kowalski", "Szymon Wieszczak", "Arkadiusz Kopeć", "Miłosz Duda"]
    },
    "Dakar Development Stal Rzeszów": {
        "seniorzy": ["Rasmus Jensen", "Andreas Lyager", "Mateusz Szczepaniak", "Oskar Fajfer"],
        "u24": ["Anders Rowe"],
        "juniorzy": ["Krzysztof Sadurski", "Franciszek Majewski", "Bartosz Curzytek", "Adrian Przybyło", "Kryspin Jarosz"]
    },
    "Moonfin Magnus Ostrów Wlkp.": {
        "seniorzy": ["Tai Woffinden", "Chris Holder", "Gleb Czugunow", "Frederik Jakobsen", "Krystian Pieszczek"],
        "u24": ["Jakub Krawczyk", "Kacper Wierzbicki"],
        "juniorzy": ["Filip Seniuk", "Marcel Kowolik", "Nikodem Mikołajczyk", "Nikodem Łuczak", "Tobiasz Potasznik", "Gracjan Szostak"]
    },
    "Polonia Piła": {
        "seniorzy": ["Wiktor Jasiński", "Adrian Cyfer", "Norbert Kościuch", "Matias Nielsen", "Kyle Howarth", "Mikkel Sørensen"],
        "u24": ["Benjamin Basso", "Wiliam Drejer"],
        "juniorzy": ["Emil Maroszek", "Tobiasz Jakub Musielak", "Kacper Teska", "Krystian Buczyński", "Błażej Wypior", "Mateo Rossi"]
    },
    "Hunters PSŻ Poznań": {
        "seniorzy": ["Ryan Douglas", "Dimitri Bergé", "Niels Kristian Iversen", "Bartosz Smektała"],
        "u24": ["Kacper Pludra"],
        "juniorzy": ["Kacper Teska", "Kamil Witkowski", "Mateusz Latała", "Antoni Mencel", "Cooper Rushen"]
    },
    "INNPRO ROW Rybnik": {
        "seniorzy": ["Jan Kvech", "Nicolai Klindt", "Patryk Wojdyło", "Jakub Jamróg"],
        "u24": ["Jesper Knudsen"],
        "juniorzy": ["Jakub Żurek", "Kacper Tkocz", "Paweł Wyczyszczok", "Roch Wujec"]
    }
}

druzyny_klz = {
    "Ultrapur Start Gniezno": {
        "seniorzy": ["Adam Ellis", "Sam Masters", "Norbert Krakowiak", "Kevin Fajfer"],
        "u24": ["Kevin Juhl Pedersen"],
        "juniorzy": ["Slater Lightcap", "Anže Grmek", "Patryk Budniak", "Alex Martin", "Robert Roszak", "Mateusz Latała", "Jacob Jensen", "Adrian Kierzek", "Mateusz Malinowski", "Maksymilian Kabaciński"]
    },
    "Optibet Lokomotiv Daugavpils": {
        "seniorzy": ["David Bellego", "Daniił Kołodinski", "Jewgienij Kostygow", "Oleg Michaiłow", "Nick Morris", "Jonas Knudsen"],
        "u24": ["Drew Kemp", "Nikita Kaulin", "Esben Hjerrild"],
        "juniorzy": ["Artjoms Juhno", "Damir Filimonow", "Emil Rimicans", "Dmitrij Reuka"]
    },
    "Trans HL Devils Landshut": {
        "seniorzy": ["Kim Nilsson", "Erik Riss", "Charles Wright", "Kevin Wölbert", "Michele Paco Castagna", "Lukas Fienhage"],
        "u24": ["Leon Flint"],
        "juniorzy": ["Mario Häusl", "Janek Konzack", "Tyler Haupt", "Hannah Grunwald"]
    },
    "OK Bedmet Kolejarz Opole": {
        "seniorzy": ["Václav Milík", "Oskar Polis", "Jonas Jeppesen", "Hubert Łęgowik", "Matic Ivačič", "Mathias Thörnblom"],
        "u24": [],
        "juniorzy": ["James Pearson", "Oskar Stępień", "Oskar Rumiński", "Dawid Rozpędek", "Dastin Łukaszczyk", "Sebastian Madej"]
    },
    "Autona Unia Tarnów": {
        "seniorzy": ["Marko Lewiszyn", "Richard Lawson", "Nicolai Klindt", "Jesse Mustonen", "Stanisław Mielniczuk", "Mitchell Cluff", "Paweł Miesiąc"],
        "u24": ["Dawid Rempała", "Kacper Łobodziński", "Fraser Bowes", "Michael West"],
        "juniorzy": ["Luke Harrison", "Jakub Breński", "Jędrzej Chmura", "Leon Szlegiel", "Szymon Machura"]
    },
    "Śląsk Świętochłowice": {
        "seniorzy": ["Mateusz Tonder", "Wiktor Trofimow", "Adrian Gała", "Tomasz Orwat", "Filip Hjelmland", "Bartosz Szymura"],
        "u24": ["Kacper Mateusz Grzelak", "Matteo Boncinelli", "Rune Thorst", "Bastian Borke", "Sebastian Kössler", "Andrij Rozaliuk"],
        "juniorzy": ["Luke Harrison", "Jakub Breński", "Jędrzej Chmura", "Leon Szlegiel", "Szymon Machura"]
    }
}

wszystkie_druzyny = {**druzyny_pge, **druzyny_metalkas, **druzyny_klz}

# Lista wszystkich klubów dostępnych w symulatorze
kluby_lista = list(wszystkie_druzyny.keys())

# 2. Baza OVR
reczne_ovr = {
    
    # Start Gniezno
    "Adam Ellis": 78, "Sam Masters": 77, "Norbert Krakowiak": 77, "Kevin Fajfer": 73,
    "Slater Lightcap": 73, "Kevin Juhl Pedersen": 70, "Anže Grmek": 68, "Patryk Budniak": 67,
    "Alex Martin": 66, "Robert Roszak": 64, "Mateusz Latała": 63, "Jacob Jensen": 62,
    "Adrian Kierzek": 61, "Mateusz Malinowski": 61, "Maksymilian Kabaciński": 60,

    # Lokomotiv Daugavpils
    "David Bellego": 79, "Daniił Kołodinski": 75, "Jewgienij Kostygow": 73, "Oleg Michaiłow": 72,
    "Drew Kemp": 69, "Nick Morris": 68, "Nikita Kaulin": 67, "Artjoms Juhno": 66,
    "Esben Hjerrild": 65, "Jonas Knudsen": 65, "Damir Filimonow": 62, "Emil Rimicans": 60,
    "Dmitrij Reuka": 60,

    # Landshut Devils
    "Kim Nilsson": 81, "Erik Riss": 76, "Charles Wright": 75, "Leon Flint": 74,
    "Kevin Wölbert": 73, "Michele Paco Castagna": 70, "Lukas Fienhage": 65, "Mario Häusl": 63,
    "Janek Konzack": 63, "Tyler Haupt": 61, "Hannah Grunwald": 60,

    # Kolejarz Opole
    "Václav Milík": 77, "Oskar Polis": 77, "James Pearson": 72, "Jonas Jeppesen": 68,
    "Hubert Łęgowik": 67, "Matic Ivačič": 66, "Mathias Thörnblom": 65, "Oskar Stępień": 64,
    "Oskar Rumiński": 63, "Dawid Rozpędek": 61, "Dastin Łukaszczyk": 61, "Sebastian Madej": 60,

    # Unia Tarnów
    "Marko Lewiszyn": 79, "Dawid Rempała": 73, "Richard Lawson": 72, "Jesse Mustonen": 69,
    "Stanisław Mielniczuk": 68, "Mitchell Cluff": 66, "Fraser Bowes": 65, "Michael West": 63,
    "Paweł Miesiąc": 63, "Jakub Juda": 60, "Maksym Zientara": 60, "Filip Bęczkowski": 60,

    # Energa Wybrzeże Gdańsk
    "Jacob Thorssell": 82, "Tim Sørensen": 79, "Mateusz Bartkowiak": 76,
    "Miłosz Wysocki": 76, "Krystian Pieszczek": 74, "Casper Henriksson": 74,
    "Jan Przanowski": 70, "Eryk Kamiński": 68, "Niklas Holm Jakobsen": 66, "Kacper Warduliński": 64,
    "Mikołaj Krok": 63, "Jakub Redzimski": 62, "Jakub Malina": 60,

    # Śląsk Świętochłowice
    "Mateusz Tonder": 80, "Wiktor Trofimow": 71, "Kacper Mateusz Grzelak": 67,
    "Tomasz Orwat": 66, "Matteo Boncinelli": 66, "Rune Thorst": 65, "Bastian Borke": 65,
    "Filip Hjelmland": 64, "Sebastian Kössler": 64, "Andrij Rozaliuk": 63,
    "Bartosz Szymura": 62, "Luke Harrison": 62, "Jakub Breński": 61,
    "Jędrzej Chmura": 60, "Leon Szlegiel": 60, "Szymon Machura": 60,
        
    # PGE Ekstraliga
    "Patryk Dudek": 90, "Robert Lambert": 92, "Mikkel Michelsen": 87, "Emil Sajfutdinow": 89, "Norick Bloedorn": 80,
    "Antoni Kawczyński": 79, "Mikołaj Duchiński": 71, "Mateusz Affelt": 60, "Bartosz Derek": 60, "Robert Downar": 60,
    "Nicolai Heiselberg": 60, "Wiktor Jasiński II": 60, "Dominik Łakomy": 60, "Ksawery Słomski": 60,
    "Bartosz Zmarzlik": 95, "Fredrik Lindgren": 87, "Kacper Woryna": 89, "Martin Vaculik": 87, "Mateusz Cierniak": 83,
    "Bartosz Bańbor": 79, "Bartosz Jaworski": 60, "Dawid Cepielik": 60, "Sven Cerjak": 70, "Paweł Czaus": 60,
    "Dawid Grzeszczyk": 61, "Michał Psiuk": 60, "Karol Szmyd": 60, "Artiom Łaguta": 92, "Maciej Janowski": 88,
    "Daniel Bewley": 87, "Brady Kurtz": 93, "Bartłomiej Kowalski": 82, "Francis Gusts": 79, "Marcel Kowolik": 74,
    "Nikodem Mikołajczyk": 73, "Mikkel Andersen": 76, "Filip Kumaszka": 62, "Krystian Gręda": 60, "Rafał Grzędziński": 60,
    "Max Fricke": 91, "Maksym Drabik": 87, "Wadim Tarasienko": 87, "Michael Jepsen Jensen": 88, "Kacper Łobodziński": 67,
    "Kevin Małkiewicz": 79, "Bastian Pedersen": 77, "Beau Bailey": 69, "Kevin Iwański-Helt": 60,
    "Damian Miller": 60, "Kacper Szarszewski": 60, "Leon Madsen": 91, "Dominik Kubera": 88, "Andrzej Lebiediew": 86,
    "Przemysław Pawlicki": 89, "Michał Curzytek": 69, "Damian Ratajczak": 81, "Oskar Hurysz": 76, "William Cairns": 70,
    "Eryk Farański": 60, "Mitchell McDiarmid": 74, "Villads Pedersen": 60, "Bartosz Rudolf": 60,
    "Rafał Sękowski": 60, "Kacper Witrykus": 60, "Rohan Tungate": 82, "Jaimon Lidsey": 85, "Mads Hansen": 84,
    "Jakub Miśkowiak": 83, "Sebastian Szostak": 71, "Franciszek Karczewski": 65, "Szymon Ludwiczak": 71, "Paweł Caban": 60,
    "Alan Ciurzyński": 66, "Bartosz Śmigielski": 60, "Anders Thomsen": 91,
    "Jack Holder": 93, "Paweł Przedpełski": 85, "Marcel Szymko": 64, "Mathias Pollestad": 82, "Oskar Paluch": 82,
    "Adam Bednar": 81, "Hubert Jabłoński": 63, "Denis Andrzejczak": 60, "Dominik Baryłka": 60, "Oskar Chatłas": 60,
    "Igor Kordun": 74, "Sebastian Mayland": 61, "Kewin Nycz": 60, "Andreas Olsen": 60, "Janusz Kołodziej": 87,
    "Piotr Pawlicki": 90, "Grzegorz Zengota": 86, "Ben Cook": 89, "Keynan Rew": 81, "Nazar Parnicki": 84,
    "Kacper Mania": 79, "Marcel Juskowiak": 60, "Timo Lahti": 80, "Krystian Buczyński": 60, "Filip Gano": 69, "Emil Konieczny": 72,
    "Maksymilian Kostera": 60, "Cooper Rushen": 73, "Krzysztof Skorczyk": 60, "Kuba Wojtyńka": 60, "Jakub Żurek": 74, "Wiktor Trofimov": 79, "Josh Pickering": 78,

    # Metalkas 2. Ekstraliga
    "Szymon Woźniak": 86, "Kai Huckenbeck": 85, "Aleksandr Łoktajew": 84, "Krzysztof Buczkowski": 85, "Tom Brennan": 75,
    "Wiktor Przyjemski": 85, "Maksymilian Pawełczak": 84, "Kacper Andrzejewski": 75, "Adam Putkowski": 60, "Jan Rompkowski": 60,
    "Marcin Nowak": 81, "Oliver Berntzon": 78, "Zach Cook": 79, "Szymon Szlauderbach": 79, "Villads Nagel": 81,
    "Dan Thompson": 74, "Kacper Halkiewicz": 70, "Krzysztof Lewandowski": 68, "Jakub Orgacki": 60, "Tomasz Szeląg": 60, "Seweryn Orgacki": 60,
    "Jason Doyle": 86, "Tobiasz Musielak": 80, "Robert Chmiel": 78, "Luke Becker": 81, "Radosław Kowalski": 74,
    "Szymon Bańdur": 70, "Jakub Woźnik": 64, "Szymon Wieszczak": 60, "Arkadiusz Kopeć": 60, "Miłosz Duda": 61,
    "Rasmus Jensen": 85, "Oskar Fajfer": 81, "Andreas Lyager": 78, "Mateusz Szczepaniak": 78, "Anders Rowe": 72,
    "Krzysztof Sadurski": 73, "Franciszek Majewski": 74, "Bartosz Curzytek": 60, "Adrian Przybyło": 60, "Kryspin Jarosz": 60,
    "Tai Woffinden": 78, "Chris Holder": 75, "Gleb Czugunow": 79, "Frederik Jakobsen": 83, "Jakub Krawczyk": 75,
    "Filip Seniuk": 71, "Paweł Sitek": 75, "Nikodem Łuczak": 60, "Tobiasz Potasznik": 60, "Gracjan Szostak": 65,
    "Benjamin Basso": 81, "Wiktor Jasiński": 79, "Norbert Kościuch": 78, "Matias Nielsen": 78, "Adrian Cyfer": 76,
    "Wiliam Drejer": 70, "Kacper Teska": 74, "Emil Maroszek": 66, "Tobiasz Jakub Musielak": 69, "Błażej Wypior": 60,
    "Ryan Douglas": 87, "Dimitri Bergé": 81, "Niels Kristian Iversen": 78, "Bartosz Smektała": 80, "Kacper Pludra": 75,
    "Kamil Witkowski": 73, "Jan Kvech": 86, "Nicolai Klindt": 84, "Patryk Wojdyło": 82,
    "Jakub Jamróg": 80, "Jesper Knudsen": 74, "Kacper Tkocz": 71, "Paweł Wyczyszczok": 67, "Roch Wujec": 60, "Philip Helstrom Bangs": 79, "Adrian Gała": 77, 
    "Antoni Mencel": 75, "Kyle Howarth": 77, "Krystian Pieszczek": 77, "Kacper Wierzbicki": 84, "Mikkel Sørensen": 81, "Andreas Johansson": 83, "Mateo Rossi": 67,
    "Oliver Nielsen": 72
}

def oblicz_ovr_ze_sredniej(nazwisko):
    return reczne_ovr.get(nazwisko, 60)

def generuj_statystyki_zawodnikow():
    baza = {}
    for klub, sklad in wszystkie_druzyny.items():
        for kat in ["seniorzy", "u24", "juniorzy"]:
            for z in sklad[kat]:
                ovr_val = oblicz_ovr_ze_sredniej(z)
                odchylenie = random.randint(-2, 2)
                st_val = max(50, min(99, ovr_val + odchylenie))
                dys_val = max(50, min(99, ovr_val - odchylenie))
                forma_dnia = random.randint(-3, 3)
                
                baza[z] = {
                    "start": st_val, 
                    "dystans": dys_val, 
                    "ovr": ovr_val, 
                    "forma": forma_dnia,
                    "rola": "junior" if kat == "juniorzy" else "senior"
                }
    return baza

def generuj_komentarz_sf(uczestnicy, zdarzenia):
    if zdarzenia:
        zdarz_tekst = " ".join(zdarzenia)
        opisy_zdarzen = [
            f"Co za dramatyczne wydarzenia! {zdarz_tekst}",
            f"Jankowski aż wstał z wrażenia! {zdarz_tekst}",
            f"Sędzia przerywa bieg! {zdarz_tekst}",
            f"Niesamowite zamieszanie na torze. {zdarz_tekst}"
        ]
        return random.choice(opisy_zdarzen)

    if not uczestnicy:
        return "Bieg bez historii — nikt nie dojechał do mety."

    zwyciezca = uczestnicy[0]['nazwisko']
    drugi = uczestnicy[1]['nazwisko'] if len(uczestnicy) > 1 else None
    trzeci = uczestnicy[2]['nazwisko'] if len(uczestnicy) > 2 else None
    czwarty = uczestnicy[3]['nazwisko'] if len(uczestnicy) > 3 else None

    roznica = uczestnicy[0]['sila'] - uczestnicy[1]['sila'] if drugi else 100

    if drugi and uczestnicy[0]['druzyna'] == uczestnicy[1]['druzyna']:
        scenariusze_51 = [
            f"🔥 **Pojedynek parowy perfekcyjny!** {zwyciezca} i {drugi} wystrzelili spod taśmy i nie dali rywalom najmniejszych szans. Podwójna wygrana!",
            f"🚀 **Para jak z żelaza!** {zwyciezca} prowadził bieg, a {drugi} mądrze blokował ataki rywali na dystansie. 5:1!",
            f"💥 **Nokaut!** Pokaz jazdy parą w wykonaniu duetu {zwyciezca} - {drugi}. Rywale oglądali tylko plecy i spaliny!"
        ]
        return random.choice(scenariusze_51)

    if drugi and trzeci and uczestnicy[0]['druzyna'] != uczestnicy[1]['druzyna'] and uczestnicy[1]['druzyna'] == uczestnicy[2]['druzyna']:
        scenariusze_remis = [
            f"⚖️ **Remis po twardej walce!** {zwyciezca} pewnie wygrywa bieg, ale {drugi} i {trzeci} dowożą cenne punkty dla swojej drużyny.",
            f"🎯 **Samotny jastrząb!** {zwyciezca} uciekł reszcie stawki, lecz para rywali ({drugi}, {trzeci}) kontrolowała sytuację na dalszych pozycjach."
        ]
        return random.choice(scenariusze_remis)

    if drugi and roznica < 1.5:
        scenariusze_styk = [
            f"😱 **NIESAMOWITE!** {zwyciezca} wyprzedza zawodnika {drugi} dosłownie na kresce! Różnica wyniosła centymetry!",
            f"⚔️ **Walka łokcie w łokcie!** {drugi} prowadził przez 3,5 okrążenia, ale {zwyciezca} pikowaniem pod łokieć wyrywa 3 punkty na ostatniej prostej!",
            f"🔥 **Co za mijanka!** {zwyciezca} zaryzykował, wszedł szeroko w ostatni łuk i przy samej bandzie przemknął obok {drugi}!"
        ]
        return random.choice(scenariusze_styk)

    if roznica > 6.0:
        scenariusze_dominacja = [
            f"⚡ **Błyskawica od startu!** {zwyciezca} zdemolował rywali na dojeździe do pierwszego łuku i wygrał z przewagą prostej.",
            f"🎯 **Poza zasięgiem!** {zwyciezca} założył całą stawkę na pierwszym łuku i dopisał pewne 3 punkty.",
            f"👑 **Profesor toru!** {zwyciezca} dopasował przełożenia idealnie — nikt nie był w stanie podjąć z nim walki."
        ]
        return random.choice(scenariusze_dominacja)

    scenariusze_walka = [
        f"🏍️ **Zacięty bieg!** {zwyciezca} mądrze obierał ścieżki na torze i utrzymał prowadzenie przed atakami, które przypuszczał {drugi}.",
        f"💨 **Kąśliwe ataki na dystansie!** {drugi} szukał prędkości pod bandą, ale {zwyciezca} zamknął bramę na trzecim okrążeniu i dowiózł trójkę.",
        f"🏁 **Twarda walka o punkty!** {zwyciezca} wygrywa start, a z tyłu {trzeci} zacięcie walczył z zawodnikiem {czwarty if czwarty else 'rywali'}."
    ]
    return random.choice(scenariusze_walka)

if 'baza_zawodnikow' not in st.session_state:
    st.session_state.baza_zawodnikow = generuj_statystyki_zawodnikow()

st.sidebar.header("⚙️ Konfiguracja Meczu")

if 'gospodarz_bieżący' not in st.session_state or st.session_state.gospodarz_bieżący not in kluby_lista:
    st.session_state.gospodarz_bieżący = kluby_lista[0]
if 'gosc_bieżący' not in st.session_state or st.session_state.gosc_bieżący not in kluby_lista:
    st.session_state.gosc_bieżący = kluby_lista[1]

wybrany_gospodarz = st.sidebar.selectbox("🏠 Gospodarz (Czerwony/Niebieski)", kluby_lista, index=kluby_lista.index(st.session_state.gospodarz_bieżący), key="gospodarz_bieżący")
wybrany_gosc = st.sidebar.selectbox("✈️ Gość (Biały/Żółty)", kluby_lista, index=kluby_lista.index(st.session_state.gosc_bieżący), key="gosc_bieżący")
wybrana_pogoda = st.sidebar.selectbox("🌤️ Warunki atmosferyczne:", ["☀️ Słonecznie i ciepło", "⛅ Lekkie zachmurzenie", "🌬️ Wietrznie", "🌧️ Deszcz (Mżawka)", "🌩️ Burza / Ulewa"])

tab_kadry, tab_taktyka, tab_mecz = st.tabs(["👥 1. Wybór Drużyn i Kadry", "📣 2. Odprawa Taktyczna", "🏎️ 3. Centrum Meczowe"])

kadra_gosp_klub = wszystkie_druzyny[wybrany_gospodarz]["seniorzy"] + wszystkie_druzyny[wybrany_gospodarz]["u24"] + wszystkie_druzyny[wybrany_gospodarz]["juniorzy"]
kadra_gosc_klub = wszystkie_druzyny[wybrany_gosc]["seniorzy"] + wszystkie_druzyny[wybrany_gosc]["u24"] + wszystkie_druzyny[wybrany_gosc]["juniorzy"]

def get_ovr_info(nazwisko):
    dane = st.session_state.baza_zawodnikow.get(nazwisko, {"ovr": 60, "forma": 0})
    ovr = dane.get("ovr", 60)
    forma = dane.get("forma", 0)
    znak = f"+{forma}" if forma > 0 else str(forma)
    return f"{ovr} (Forma: {znak})"

program_zawodow = [
    {"bieg": 1,  "A": 1,  "B": 9,  "C": 3,  "D": 11, "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},
    {"bieg": 2,  "A": 6,  "B": 14, "C": 7,  "D": 15, "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},
    {"bieg": 3,  "A": 10, "B": 2,  "C": 12, "D": 4,  "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}},
    {"bieg": 4,  "A": 13, "B": 5,  "C": 14, "D": 6,  "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}},
    {"bieg": 5,  "A": 3,  "B": 9,  "C": 4,  "D": 10, "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},
    {"bieg": 6,  "A": 11, "B": 1,  "C": 12, "D": 7,  "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}},
    {"bieg": 7,  "A": 2,  "B": 13, "C": 5,  "D": 15, "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},
    {"bieg": 8,  "A": 10, "B": 4,  "C": 11, "D": 6,  "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}},
    {"bieg": 9,  "A": 1,  "B": 9,  "C": 2,  "D": 12, "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},
    {"bieg": 10, "A": 14, "B": 3,  "C": 13, "D": 5,  "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}},
    {"bieg": 11, "A": 4,  "B": 13, "C": 1,  "D": 9,  "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},
    {"bieg": 12, "A": 15, "B": 7,  "C": 10, "D": 3,  "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}},
    {"bieg": 13, "A": 5,  "B": 11, "C": 2,  "D": 12, "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},
    {"bieg": 14, "A": 3,  "B": 11, "C": 4,  "D": 12, "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},
    {"bieg": 15, "A": 1,  "B": 9,  "C": 2,  "D": 10, "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},
]

with tab_kadry:
    st.header(f"Składy Meczowe: {wybrany_gospodarz} vs {wybrany_gosc}")
    col_gosp, col_gosc = st.columns(2)
    
    if 'aktualny_gospodarz' not in st.session_state or st.session_state.aktualny_gospodarz != wybrany_gospodarz:
        st.session_state.aktualny_gospodarz = wybrany_gospodarz
        wszyscy_g = kadra_gosp_klub
        st.session_state.sklad_gospodarze = {
            1: wszyscy_g[0] if len(wszyscy_g) > 0 else "",
            2: wszyscy_g[1] if len(wszyscy_g) > 1 else "",
            3: wszyscy_g[2] if len(wszyscy_g) > 2 else "",
            4: wszyscy_g[3] if len(wszyscy_g) > 3 else "",
            5: wszyscy_g[4] if len(wszyscy_g) > 4 else wszyscy_g[0],
            6: wszyscy_g[5] if len(wszyscy_g) > 5 else wszyscy_g[0],
            7: wszyscy_g[6] if len(wszyscy_g) > 6 else wszyscy_g[0],
            8: wszyscy_g[7] if len(wszyscy_g) > 7 else wszyscy_g[0]
        }

    if 'aktualny_gosc' not in st.session_state or st.session_state.aktualny_gosc != wybrany_gosc:
        st.session_state.aktualny_gosc = wybrany_gosc
        wszyscy_go = kadra_gosc_klub
        st.session_state.sklad_goscie = {
            9: wszyscy_go[0] if len(wszyscy_go) > 0 else "",
            10: wszyscy_go[1] if len(wszyscy_go) > 1 else "",
            11: wszyscy_go[2] if len(wszyscy_go) > 2 else "",
            12: wszyscy_go[3] if len(wszyscy_go) > 3 else "",
            13: wszyscy_go[4] if len(wszyscy_go) > 4 else wszyscy_go[0],
            14: wszyscy_go[5] if len(wszyscy_go) > 5 else wszyscy_go[0],
            15: wszyscy_go[6] if len(wszyscy_go) > 6 else wszyscy_go[0],
            16: wszyscy_go[7] if len(wszyscy_go) > 7 else wszyscy_go[0]
        }

    with col_gosp:
        st.subheader(f"🏠 {wybrany_gospodarz} (🔴🔵)")
        for nr in range(1, 6):
            wybory = [z for z in kadra_gosp_klub if z not in list(st.session_state.sklad_gospodarze.values()) or st.session_state.sklad_gospodarze[nr] == z]
            st.session_state.sklad_gospodarze[nr] = st.selectbox(
                f"Nr {nr} (Senior / U24)", 
                wybory, 
                index=wybory.index(st.session_state.sklad_gospodarze[nr]) if st.session_state.sklad_gospodarze[nr] in wybory else 0, 
                format_func=lambda z: f"{z} (OVR: {get_ovr_info(z)})", 
                key=f"g_{nr}"
            )
        for nr in range(6, 9):
            wybory = [z for z in kadra_gosp_klub if z not in list(st.session_state.sklad_gospodarze.values()) or st.session_state.sklad_gospodarze[nr] == z]
            label = f"Nr {nr} (Rezerwa Zwykła 🔄)" if nr == 8 else f"Nr {nr} (Junior 👦)"
            st.session_state.sklad_gospodarze[nr] = st.selectbox(
                label, 
                wybory, 
                index=wybory.index(st.session_state.sklad_gospodarze[nr]) if st.session_state.sklad_gospodarze[nr] in wybory else 0, 
                format_func=lambda z: f"{z} (OVR: {get_ovr_info(z)})", 
                key=f"g_{nr}"
            )
            
    with col_gosc:
        st.subheader(f"✈️ {wybrany_gosc} (⚪🟡)")
        for nr in range(9, 14):
            wybory = [z for z in kadra_gosc_klub if z not in list(st.session_state.sklad_goscie.values()) or st.session_state.sklad_goscie[nr] == z]
            st.session_state.sklad_goscie[nr] = st.selectbox(
                f"Nr {nr} (Senior / U24)", 
                wybory, 
                index=wybory.index(st.session_state.sklad_goscie[nr]) if st.session_state.sklad_goscie[nr] in wybory else 0, 
                format_func=lambda z: f"{z} (OVR: {get_ovr_info(z)})", 
                key=f"gosc_{nr}"
            )
        for nr in range(14, 17):
            wybory = [z for z in kadra_gosc_klub if z not in list(st.session_state.sklad_goscie.values()) or st.session_state.sklad_goscie[nr] == z]
            label = f"Nr {nr} (Rezerwa Zwykła 🔄)" if nr == 16 else f"Nr {nr} (Junior 👦)"
            st.session_state.sklad_goscie[nr] = st.selectbox(
                label, 
                wybory, 
                index=wybory.index(st.session_state.sklad_goscie[nr]) if st.session_state.sklad_goscie[nr] in wybory else 0, 
                format_func=lambda z: f"{z} (OVR: {get_ovr_info(z)})", 
                key=f"gosc_{nr}"
            )

with tab_taktyka:
    st.title("🛠️ Ustawienia Taktyczne Menedżerów")
    st.info("📣 **PRZERWA / ODPRAWA TAKTYCZNA:** Odprawa przedmeczowa")
    
    col_tak_gosp, col_tak_gosc = st.columns(2)
    with col_tak_gosp:
        st.subheader(f"🏠 Gospodarz ({wybrany_gospodarz})")
        st.selectbox("📐 Przygotowanie Nawierzchni:", ["⚖️ Tor Neutralny", "🧱 Tor Twardy", "🚜 Tor Przyczepny"], key="przygotowanie_toru_gosp")
        st.selectbox("🔥 Styl Jazdy Drużyny:", ["Standardowe nastawienie", "Agresywne (większe ryzyko)", "Defensywne (bezpieczne)"], key="styl_jazdy_gosp")
        st.selectbox("🔧 Sprzęt / Tuner:", ["🔧 Silnik Niezawodny (0% defektu)", "🚀 Silnik Ekstra Mocny (+2 siły, wyższy defekt)"], key="sprzet_gosp")

    with col_tak_gosc:
        st.subheader(f"✈️ Gość ({wybrany_gosc})")
        st.selectbox("🔥 Styl Jazdy Drużyny:", ["Standardowe nastawienie", "Agresywne (większe ryzyko)", "Defensywne (bezpieczne)"], key="styl_jazdy_gosc")
        st.selectbox("🔧 Sprzęt / Tuner:", ["🔧 Silnik Niezawodny (0% defektu)", "🚀 Silnik Ekstra Mocny (+2 siły, wyższy defekt)"], key="sprzet_gosc")

with tab_mecz:
    st.header("Panel Symulacji Meczowej")
    
    def reset_stats():
        st.session_state.current_heat = 0
        st.session_state.score_gosp = 0
        st.session_state.score_gosc = 0
        st.session_state.match_history = []
        st.session_state.starts_count = {nr: 0 for nr in list(range(1, 17))}
        st.session_state.rider_heats = {nr: [] for nr in list(range(1, 17))}
        st.session_state.rider_bonuses = {nr: 0 for nr in list(range(1, 17))}
        st.session_state.kontuzjowani = set()
        st.session_state.mecz_przerwany = False
        st.session_state.decyzja_o_przerwaniu_podjeta = False
        st.session_state.baza_zawodnikow = generuj_statystyki_zawodnikow()

    if 'current_heat' not in st.session_state or 'rider_heats' not in st.session_state or len(st.session_state.rider_heats.keys()) < 16 or 'kontuzjowani' not in st.session_state:
        reset_stats()

    col_top1, col_top2 = st.columns([4, 1])
    with col_top2:
        if st.button("🔄 Resetuj Mecz"):
            reset_stats()
            st.rerun()

    typ_toru = st.session_state.get("przygotowanie_toru_gosp", "⚖️ Tor Neutralny")
    if "Twardy" in typ_toru:
        waga_startu, waga_dystansu = 0.8, 0.2
    elif "Neutralny" in typ_toru:
        waga_startu, waga_dystansu = 0.5, 0.5
    else:
        waga_startu, waga_dystansu = 0.3, 0.7

    roznica = st.session_state.score_gosp - st.session_state.score_gosc
    st.markdown(f"### 📊 Aktualny Wynik: {wybrany_gospodarz} **{st.session_state.score_gosp} : {st.session_state.score_gosc}** {wybrany_gosc} | Pogoda: {wybrana_pogoda}")

    if st.session_state.kontuzjowani:
        st.warning(f"⚠️ **Zawodnicy niezdolni do jazdy (kontuzje):** {', '.join([str(nr) for nr in st.session_state.kontuzjowani])}")

    if st.session_state.current_heat == 8 and wybrana_pogoda == "🌩️ Burza / Ulewa" and not st.session_state.get('decyzja_o_przerwaniu_podjeta', False):
        st.warning("⚠️ Nad stadionem przeszła gwałtowna burza! Sędzia wstrzymał zawody po 8. biegu z powodu złych warunków torowych.")
        col_przerw1, col_przerw2 = st.columns(2)
        with col_przerw1:
            if st.button("🔴 Przerwij mecz i zalicz wynik (min. 8 biegów)"):
                st.session_state.mecz_przerwany = True
                st.session_state.decyzja_o_przerwaniu_podjeta = True
                st.rerun()
        with col_przerw2:
            if st.button("🟢 Czekamy na poprawę pogody – jedziemy dalej"):
                st.session_state.decyzja_o_przerwaniu_podjeta = True
                st.rerun()

    if st.session_state.get('mecz_przerwany', False):
        st.error(f"🛑 **MECZ PRZERWANY PRZEZ SĘDZIEGO PO 8 BIEGACH!** Wynik końcowy: {wybrany_gospodarz} {st.session_state.score_gosp}:{st.session_state.score_gosc} {wybrany_gosc}")
    elif st.session_state.current_heat < 15:
        heat_data = program_zawodow[st.session_state.current_heat]
        nr_b = heat_data["bieg"]
        kaski_map = heat_data["kaski"]
        
        st.divider()
        st.subheader(f"🚀 Bieg {nr_b} / 15")

        taktyczna_gosp = roznica <= -6
        taktyczna_gosc = roznica >= 6

        def get_pkt_sum(nr):
            starty = st.session_state.rider_heats.get(nr, [])
            s_pkt = 0
            for s in starty:
                if s.startswith("3"): s_pkt += 3
                elif s.startswith("2"): s_pkt += 2
                elif s.startswith("1"): s_pkt += 1
            return s_pkt + st.session_state.rider_bonuses.get(nr, 0)

        def buduj_opcje_gosp(prog_nr, wykluczone_numery=[]):
            opcje = []
            if nr_b in [14, 15]:
                dostępni = [nr for nr in range(1, 9) if nr not in st.session_state.kontuzjowani and st.session_state.starts_count[nr] < 5 and nr not in wykluczone_numery]
                dostępni.sort(key=lambda nr: get_pkt_sum(nr), reverse=True)
                return dostępni if dostępni else [prog_nr]

            if nr_b == 2:
                juniorzy = [6, 7, 8]
                if prog_nr in juniorzy and prog_nr not in st.session_state.kontuzjowani and st.session_state.starts_count[prog_nr] < 5:
                    opcje.append(prog_nr)
                for r_nr in juniorzy:
                    if r_nr not in opcje and r_nr not in st.session_state.kontuzjowani and st.session_state.starts_count[r_nr] < 5:
                        opcje.append(r_nr)
                res = [nr for nr in opcje if nr not in wykluczone_numery]
                return res if res else [prog_nr]

            if prog_nr not in st.session_state.kontuzjowani and st.session_state.starts_count[prog_nr] < 5:
                opcje.append(prog_nr)
            
            rezerwy_gosp = [8, 6, 7]
            for r_nr in rezerwy_gosp:
                if r_nr not in opcje and r_nr not in st.session_state.kontuzjowani and st.session_state.starts_count[r_nr] < 5:
                    opcje.append(r_nr)

            if taktyczna_gosp:
                for nr in range(1, 6):
                    if nr not in opcje and nr not in st.session_state.kontuzjowani and st.session_state.starts_count[nr] < 5:
                        opcje.append(nr)

            if prog_nr in st.session_state.kontuzjowani:
                for nr in range(1, 8):
                    if nr not in opcje and nr not in st.session_state.kontuzjowani and st.session_state.starts_count[nr] < 5:
                        opcje.append(nr)

            res = [nr for nr in opcje if nr not in wykluczone_numery]
            return res if res else [prog_nr]

        def buduj_opcje_gosc(prog_nr, wykluczone_numery=[]):
            opcje = []
            if nr_b in [14, 15]:
                dostępni = [nr for nr in range(9, 17) if nr not in st.session_state.kontuzjowani and st.session_state.starts_count[nr] < 5 and nr not in wykluczone_numery]
                dostępni.sort(key=lambda nr: get_pkt_sum(nr), reverse=True)
                return dostępni if dostępni else [prog_nr]

            if nr_b == 2:
                juniorzy = [14, 15, 16]
                if prog_nr in juniorzy and prog_nr not in st.session_state.kontuzjowani and st.session_state.starts_count[prog_nr] < 5:
                    opcje.append(prog_nr)
                for r_nr in juniorzy:
                    if r_nr not in opcje and r_nr not in st.session_state.kontuzjowani and st.session_state.starts_count[r_nr] < 5:
                        opcje.append(r_nr)
                res = [nr for nr in opcje if nr not in wykluczone_numery]
                return res if res else [prog_nr]

            if prog_nr not in st.session_state.kontuzjowani and st.session_state.starts_count[prog_nr] < 5:
                opcje.append(prog_nr)
            
            rezerwy_gosc = [16, 14, 15]
            for r_nr in rezerwy_gosc:
                if r_nr not in opcje and r_nr not in st.session_state.kontuzjowani and st.session_state.starts_count[r_nr] < 5:
                    opcje.append(r_nr)

            if taktyczna_gosc:
                for nr in range(9, 14):
                    if nr not in opcje and nr not in st.session_state.kontuzjowani and st.session_state.starts_count[nr] < 5:
                        opcje.append(nr)

            if prog_nr in st.session_state.kontuzjowani:
                for nr in range(9, 16):
                    if nr not in opcje and nr not in st.session_state.kontuzjowani and st.session_state.starts_count[nr] < 5:
                        opcje.append(nr)

            res = [nr for nr in opcje if nr not in wykluczone_numery]
            return res if res else [prog_nr]

        cols = st.columns(4)
        wybrane_numery = []
        wybrani_zawodnicy = {}

        for i, pole in enumerate(["A", "B", "C", "D"]):
            prog_nr = heat_data[pole]
            kask = kaski_map[pole]
            czy_gospodarz = kask in ["🔴", "🔵"]
            
            with cols[i]:
                if czy_gospodarz:
                    opcje = buduj_opcje_gosp(prog_nr, wybrane_numery)
                    sklad = st.session_state.sklad_gospodarze
                else:
                    opcje = buduj_opcje_gosc(prog_nr, wybrane_numery)
                    sklad = st.session_state.sklad_goscie
                
                wybrany_nr = st.selectbox(
                    f"{kask} Pole {pole} (Program: Nr {prog_nr})",
                    opcje,
                    format_func=lambda x: f"Nr {x} - {sklad[x]} ({get_ovr_info(sklad[x])})",
                    key=f"h_{nr_b}_{pole}"
                )
                wybrane_numery.append(wybrany_nr)
                wybrani_zawodnicy[pole] = {
                    "kask": kask,
                    "pole": pole,
                    "nr": wybrany_nr,
                    "nazwisko": sklad[wybrany_nr],
                    "druzyna": "gosp" if czy_gospodarz else "gosc"
                }

        col_btn1, col_btn2 = st.columns([1, 4])
        with col_btn1:
            if st.button("🏁 Jedź Bieg"):
                uczestnicy = list(wybrani_zawodnicy.values())
                ukończyli = []
                zdarzenia = []
                
                for u in uczestnicy:
                    zaw = st.session_state.baza_zawodnikow[u['nazwisko']]
                    sila = (zaw['start'] * waga_startu) + (zaw['dystans'] * waga_dystansu) + zaw['forma']
                    sila += random.uniform(-5.0, 5.0)
                    
                    takt_sprzet = st.session_state.get(f"sprzet_{u['druzyna']}", "")
                    szansa_defekt = 0.02
                    if "Ekstra Mocny" in takt_sprzet:
                        sila += 2.0
                        szansa_defekt = 0.08
                        
                    u['sila'] = sila
                    
                    los_zdarzenie = random.random()
                    if los_zdarzenie < szansa_defekt:
                        zdarzenia.append(f"💨 Defekt sprzętu: {u['nazwisko']}!")
                        u['wynik_litera'] = "D"
                        u['sila'] = -100
                    elif los_zdarzenie < szansa_defekt + 0.03:
                        zdarzenia.append(f"💥 Upadek: {u['nazwisko']}!")
                        u['wynik_litera'] = "U"
                        u['sila'] = -200
                        if random.random() < 0.2:
                            st.session_state.kontuzjowani.add(u['nr'])
                            zdarzenia.append(f"🚑 {u['nazwisko']} niezdolny do dalszej jazdy!")
                    elif los_zdarzenie < szansa_defekt + 0.05:
                        zdarzenia.append(f"🚫 Wykluczenie: {u['nazwisko']}!")
                        u['wynik_litera'] = "W"
                        u['sila'] = -300
                    else:
                        u['wynik_litera'] = None
                        
                uczestnicy.sort(key=lambda x: x['sila'], reverse=True)
                
                punkty = [3, 2, 1, 0]
                wyniki_biegu_gosp = 0
                wyniki_biegu_gosc = 0
                
                for i, u in enumerate(uczestnicy):
                    st.session_state.starts_count[u['nr']] += 1
                    
                    if u['wynik_litera']:
                        pkt = 0
                        zapis = u['wynik_litera']
                    else:
                        pkt = punkty[i]
                        bonus = False
                        if pkt == 2 and uczestnicy[0]['druzyna'] == u['druzyna']:
                            bonus = True
                        elif pkt == 1 and (uczestnicy[0]['druzyna'] == u['druzyna'] or uczestnicy[1]['druzyna'] == u['druzyna']):
                            bonus = True
                        
                        zapis = f"{pkt}*" if bonus else str(pkt)
                        if bonus:
                            st.session_state.rider_bonuses[u['nr']] += 1
                            
                    st.session_state.rider_heats[u['nr']].append(zapis)
                    
                    if u['druzyna'] == "gosp":
                        wyniki_biegu_gosp += pkt
                    else:
                        wyniki_biegu_gosc += pkt
                        
                st.session_state.score_gosp += wyniki_biegu_gosp
                st.session_state.score_gosc += wyniki_biegu_gosc
                
                sklasyfikowani = [u for u in uczestnicy if not u['wynik_litera']]
                komentarz = generuj_komentarz_sf(sklasyfikowani, zdarzenia)
                
                st.session_state.match_history.append({
                    "bieg": nr_b,
                    "wynik_biegu": f"{wyniki_biegu_gosp}:{wyniki_biegu_gosc}",
                    "szczegoly": ", ".join([f"{u['nazwisko']} ({u['kask']}) - {st.session_state.rider_heats[u['nr']][-1]}" for u in uczestnicy]),
                    "komentarz": komentarz
                })
                
                st.session_state.current_heat += 1
                st.rerun()

    # 📊 HISTORIA BIEGÓW I SCOREBOARD
    if st.session_state.match_history:
        st.divider()
        st.subheader("📜 Historia Biegów i Komentarz Live")
        for hist in reversed(st.session_state.match_history):
            with st.expander(f"Bieg {hist['bieg']} | Wynik: {hist['wynik_biegu']}", expanded=(hist['bieg'] == st.session_state.current_heat)):
                st.markdown(f"**Kolejność na mecie:** {hist['szczegoly']}")
                st.info(f"🎙️ {hist['komentarz']}")

    st.divider()
    st.subheader("📋 Tabela Punktowa Zawodników")

    def generuj_tabele_wynikow(sklad_dict):
        dane = []
        for nr, zawodnik in sklad_dict.items():
            if not zawodnik: 
                continue
                
            starty = st.session_state.rider_heats.get(nr, [])
            suma_pkt = 0
            bonusy = st.session_state.rider_bonuses.get(nr, 0)
            biegi_str = []
            
            for s in starty:
                s_str = str(s)
                biegi_str.append(s_str)
                if s_str.startswith("3"): suma_pkt += 3
                elif s_str.startswith("2"): suma_pkt += 2
                elif s_str.startswith("1"): suma_pkt += 1
                
            dane.append({
                "Nr": nr,
                "Zawodnik": zawodnik,
                "Pkt": suma_pkt,
                "Bon": bonusy,
                "Razem": f"{suma_pkt}+{bonusy}",
                "Biegi": ", ".join(biegi_str) if biegi_str else "-"
            })
            
        return pd.DataFrame(dane)

    col_tab_gosp, col_tab_gosc = st.columns(2)

    with col_tab_gosp:
        st.markdown(f"**🏠 {wybrany_gospodarz}**")
        df_gosp = generuj_tabele_wynikow(st.session_state.sklad_gospodarze)
        st.dataframe(df_gosp, hide_index=True, use_container_width=True)

    with col_tab_gosc:
        st.markdown(f"**✈️ {wybrany_gosc}**")
        df_gosc = generuj_tabele_wynikow(st.session_state.sklad_goscie)
        st.dataframe(df_gosc, hide_index=True, use_container_width=True)
