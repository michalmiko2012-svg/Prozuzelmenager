import streamlit as st
import random
import pandas as pd


# ============================================================
# KONFIGURACJA
# ============================================================

st.set_page_config(
    page_title="Symulator Żużlowy PRO 2026",
    layout="wide"
)

st.title("🏁 Symulator Żużlowy PRO 2026")


# ============================================================
# 1. LISTA DRUŻYN
# ============================================================

druzyny_pge = [
    "PRES Grupa Deweloperska Toruń",
    "Orlen Oil Motor Lublin",
    "Betard Sparta Wrocław",
    "Bayersystem GKM Grudziądz",
    "Stelmet Falubaz Zielona Góra",
    "Krono-Plast Włókniarz Częstochowa",
    "Gezet Stal Gorzów",
    "Fogo Unia Leszno"
]

druzyny_metalkas = [
    "Energa Wybrzeże Gdańsk",
    "Abramczyk Polonia Bydgoszcz",
    "H.Skrzydlewska Orzeł Łódź",
    "Cellfast Wilki Krosno",
    "Dakar Development Stal Rzeszów",
    "Moonfin Magnus Ostrów Wlkp.",
    "Polonia Piła",
    "Hunters PSŻ Poznań",
    "INNPRO ROW Rybnik"
]

druzyny_klz = [
    "Ultrapur Start Gniezno",
    "Optibet Lokomotiv Daugavpils",
    "Trans HL Devils Landshut",
    "OK Bedmet Kolejarz Opole",
    "Autona Unia Tarnów",
    "Śląsk Świętochłowice"
]

kluby_lista = (
    druzyny_pge
    + druzyny_metalkas
    + druzyny_klz
)


# ============================================================
# 2. POGODA
# ============================================================

LISTA_POGODY = [
    "☀️ Słonecznie i ciepło",
    "⛅ Lekkie zachmurzenie",
    "🌬️ Wietrznie",
    "🌧️ Deszcz (Mżawka)",
    "🌩️ Burza / Ulewa"
]


def losuj_pogode():
    return random.choice(LISTA_POGODY)


# ============================================================
# 3. FUNKCJE DRUŻYNOWE
# ============================================================

def pobierz_ovr(nr, gospodarze=True):
    if gospodarze:
        return st.session_state.sklad_gospodarze_ovr.get(nr, 60)

    return st.session_state.sklad_goscie_ovr.get(nr, 60)


def pobierz_zawodnika(nr, gospodarze=True):
    if gospodarze:
        return st.session_state.sklad_gospodarze.get(nr, "")

    return st.session_state.sklad_goscie.get(nr, "")


def get_ovr_info(nr, gospodarze=True):
    zawodnik = pobierz_zawodnika(nr, gospodarze)
    ovr = pobierz_ovr(nr, gospodarze)

    if not zawodnik:
        return "-"

    return f"{zawodnik} (OVR: {ovr})"


def generuj_statystyki_zawodnikow():
    baza = {}

    for nr in range(1, 9):

        nazwisko = st.session_state.sklad_gospodarze.get(nr, "")
        ovr = st.session_state.sklad_gospodarze_ovr.get(nr, 60)

        if nazwisko:

            odchylenie = random.randint(-2, 2)

            baza[f"g_{nr}"] = {
                "nazwisko": nazwisko,
                "ovr": ovr,
                "start": max(50, min(99, ovr + odchylenie)),
                "dystans": max(50, min(99, ovr - odchylenie)),
                "forma": random.randint(-3, 3),
                "rola": "junior" if nr in [6, 7] else "senior"
            }

    for nr in range(9, 17):

        nazwisko = st.session_state.sklad_goscie.get(nr, "")
        ovr = st.session_state.sklad_goscie_ovr.get(nr, 60)

        if nazwisko:

            odchylenie = random.randint(-2, 2)

            baza[f"gosc_{nr}"] = {
                "nazwisko": nazwisko,
                "ovr": ovr,
                "start": max(50, min(99, ovr + odchylenie)),
                "dystans": max(50, min(99, ovr - odchylenie)),
                "forma": random.randint(-3, 3),
                "rola": "junior" if nr in [14, 15] else "senior"
            }

    return baza


def generuj_komentarz_sf(uczestnicy, zdarzenia):

    if zdarzenia:

        tekst = " ".join(zdarzenia)

        return random.choice([
            f"Co za dramatyczne wydarzenia! {tekst}",
            f"Sędzia przerywa bieg! {tekst}",
            f"Niesamowite zamieszanie na torze. {tekst}",
            f"Na torze dzieje się bardzo dużo! {tekst}"
        ])

    if not uczestnicy:
        return "Bieg bez historii."

    zwyciezca = uczestnicy[0]["nazwisko"]
    drugi = uczestnicy[1]["nazwisko"] if len(uczestnicy) > 1 else None

    roznica = (
        uczestnicy[0]["sila"] - uczestnicy[1]["sila"]
        if drugi
        else 100
    )

    if (
        drugi
        and uczestnicy[0]["druzyna"] == uczestnicy[1]["druzyna"]
    ):

        return random.choice([
            f"🔥 Pojedynek parowy perfekcyjny! {zwyciezca} i {drugi} wygrywają podwójnie.",
            f"🚀 Para jak z żelaza! {zwyciezca} prowadził, a {drugi} kontrolował rywali.",
            f"💥 Nokaut! Świetna jazda duetu {zwyciezca} - {drugi}."
        ])

    if drugi and roznica < 1.5:

        return random.choice([
            f"😱 NIESAMOWITE! {zwyciezca} wygrywa z {drugim} dosłownie na kresce!",
            f"⚔️ Walka łokcie w łokcie! {zwyciezca} wyrywa zwycięstwo!",
            f"🔥 Co za mijanka! {zwyciezca} atakuje do samej mety!"
        ])

    if roznica > 6:

        return random.choice([
            f"⚡ Błyskawica od startu! {zwyciezca} odjechał rywalom.",
            f"🎯 Poza zasięgiem! {zwyciezca} był zdecydowanie najlepszy.",
            f"👑 Profesor toru! {zwyciezca} idealnie dopasował sprzęt."
        ])

    return random.choice([
        f"🏍️ Zacięty bieg! {zwyciezca} utrzymał prowadzenie.",
        f"💨 Kąśliwe ataki na dystansie! {zwyciezca} dowozi zwycięstwo.",
        f"🏁 Twarda walka o punkty! {zwyciezca} wygrywa bieg."
    ])


# ============================================================
# 4. PROGRAM MECZU DRUŻYNOWEGO
# ============================================================

program_zawodow = [

    {"bieg": 1, "A": 1, "B": 9, "C": 3, "D": 11,
     "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},

    {"bieg": 2, "A": 6, "B": 14, "C": 7, "D": 15,
     "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},

    {"bieg": 3, "A": 10, "B": 2, "C": 12, "D": 4,
     "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}},

    {"bieg": 4, "A": 13, "B": 5, "C": 14, "D": 6,
     "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}},

    {"bieg": 5, "A": 3, "B": 9, "C": 4, "D": 10,
     "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},

    {"bieg": 6, "A": 11, "B": 1, "C": 12, "D": 7,
     "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}},

    {"bieg": 7, "A": 2, "B": 13, "C": 5, "D": 15,
     "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},

    {"bieg": 8, "A": 10, "B": 4, "C": 11, "D": 6,
     "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}},

    {"bieg": 9, "A": 1, "B": 9, "C": 2, "D": 12,
     "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},

    {"bieg": 10, "A": 14, "B": 3, "C": 13, "D": 5,
     "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}},

    {"bieg": 11, "A": 4, "B": 13, "C": 1, "D": 9,
     "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},

    {"bieg": 12, "A": 15, "B": 7, "C": 10, "D": 3,
     "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}},

    {"bieg": 13, "A": 5, "B": 11, "C": 2, "D": 12,
     "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},

    {"bieg": 14, "A": 3, "B": 11, "C": 4, "D": 12,
     "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}},

    {"bieg": 15, "A": 1, "B": 9, "C": 2, "D": 10,
     "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}
    }
]


# ============================================================
# 5. INICJALIZACJA MECZU
# ============================================================

def inicjalizuj_sklad():

    if "sklad_gospodarze" not in st.session_state:
        st.session_state.sklad_gospodarze = {
            nr: "" for nr in range(1, 9)
        }

    if "sklad_goscie" not in st.session_state:
        st.session_state.sklad_goscie = {
            nr: "" for nr in range(9, 17)
        }

    if "sklad_gospodarze_ovr" not in st.session_state:
        st.session_state.sklad_gospodarze_ovr = {
            nr: 60 for nr in range(1, 9)
        }

    if "sklad_goscie_ovr" not in st.session_state:
        st.session_state.sklad_goscie_ovr = {
            nr: 60 for nr in range(9, 17)
        }


inicjalizuj_sklad()


# ============================================================
# 6. FUNKCJE RAPORTU
# ============================================================

def raport_meczu():

    tekst = []

    tekst.append("🏁 RAPORT MECZU ŻUŻLOWEGO")
    tekst.append("=" * 50)
    tekst.append(
        f"{st.session_state.mecz_gospodarz} "
        f"{st.session_state.score_gosp}:"
        f"{st.session_state.score_gosc} "
        f"{st.session_state.mecz_gosc}"
    )

    tekst.append(
        f"Pogoda: {st.session_state.get('pogoda_mecz', '-')}"
    )

    tekst.append("")
    tekst.append("BIEG PO BIEGU")
    tekst.append("-" * 50)

    for hist in st.session_state.get("match_history", []):

        tekst.append(
            f"Bieg {hist['bieg']}: "
            f"{hist['wynik_biegu']}"
        )

        tekst.append(
            f"  {hist['szczegoly']}"
        )

        tekst.append(
            f"  Komentarz: {hist['komentarz']}"
        )

    tekst.append("")
    tekst.append("PUNKTY ZAWODNIKÓW")
    tekst.append("-" * 50)

    for sklad, prefix in [
        (st.session_state.sklad_gospodarze, "GOSPODARZ"),
        (st.session_state.sklad_goscie, "GOŚĆ")
    ]:

        tekst.append(prefix)

        for nr, zawodnik in sklad.items():

            if not zawodnik:
                continue

            biegi = st.session_state.rider_heats.get(nr, [])

            pkt = 0

            for wynik in biegi:

                if str(wynik).startswith("3"):
                    pkt += 3
                elif str(wynik).startswith("2"):
                    pkt += 2
                elif str(wynik).startswith("1"):
                    pkt += 1

            bonus = st.session_state.rider_bonuses.get(nr, 0)

            tekst.append(
                f"{nr}. {zawodnik}: "
                f"{pkt}+{bonus} "
                f"({', '.join(map(str, biegi))})"
            )

    return "\n".join(tekst)


# ============================================================
# 7. ZAWODY INDYWIDUALNE
# ============================================================

def inicjalizuj_zawody_indywidualne():

    if "indi_zawodnicy" not in st.session_state:

        st.session_state.indi_zawodnicy = {
            nr: {
                "name": "",
                "ovr": 60,
                "narodowosc": "Polska",
                "status": "Senior"
            }
            for nr in range(1, 19)
        }

    if "indi_heat" not in st.session_state:
        st.session_state.indi_heat = 0

    if "indi_stage" not in st.session_state:
        st.session_state.indi_stage = "main"

    if "indi_history" not in st.session_state:
        st.session_state.indi_history = []

    if "indi_points" not in st.session_state:
        st.session_state.indi_points = {
            nr: 0 for nr in range(1, 19)
        }

    if "indi_baza" not in st.session_state:
        st.session_state.indi_baza = {}

    if "indi_pogoda" not in st.session_state:
        st.session_state.indi_pogoda = "☀️ Słonecznie i ciepło"

    if "indi_format" not in st.session_state:
        st.session_state.indi_format = "🌍 SGP — Grand Prix"

    if "indi_finished" not in st.session_state:
        st.session_state.indi_finished = False

    if "indi_lcq" not in st.session_state:
        st.session_state.indi_lcq = {
            "LCQ1": [],
            "LCQ2": []
        }

    if "indi_finalists" not in st.session_state:
        st.session_state.indi_finalists = []

    if "indi_final_result" not in st.session_state:
        st.session_state.indi_final_result = []

    if "indi_starty" not in st.session_state:
        st.session_state.indi_starty = {
            nr: [] for nr in range(1, 19)
        }


inicjalizuj_zawody_indywidualne()


# ============================================================
# 8. FORMATY INDYWIDUALNE
# ============================================================

FORMATY_INDYWIDUALNE = [
    "🌍 SGP — Grand Prix",
    "🇵🇱 IMP — Indywidualne Mistrzostwa Polski",
    "🏆 Złoty Kask"
]


def reset_indywidualnych():

    st.session_state.indi_heat = 0
    st.session_state.indi_stage = "main"

    st.session_state.indi_history = []

    st.session_state.indi_points = {
        nr: 0 for nr in range(1, 19)
    }

    st.session_state.indi_starty = {
        nr: [] for nr in range(1, 19)
    }

    st.session_state.indi_baza = {}

    st.session_state.indi_finished = False

    st.session_state.indi_lcq = {
        "LCQ1": [],
        "LCQ2": []
    }

    st.session_state.indi_finalists = []
    st.session_state.indi_final_result = []

    st.session_state.indi_pogoda = losuj_pogode()


def aktywni_zawodnicy():

    return [
        nr
        for nr, dane in st.session_state.indi_zawodnicy.items()
        if dane["name"].strip()
    ]


def generuj_indi_baze():

    baza = {}

    for nr in aktywni_zawodnicy():

        dane = st.session_state.indi_zawodnicy[nr]

        ovr = dane["ovr"]

        odchylenie = random.randint(-2, 2)

        baza[nr] = {
            "start": max(50, min(99, ovr + odchylenie)),
            "dystans": max(50, min(99, ovr - odchylenie)),
            "forma": random.randint(-3, 3)
        }

    st.session_state.indi_baza = baza


# ============================================================
# 9. TABELA 20-BIEGOWA INDYWIDUALNA
# ============================================================

TABELA_20 = [
    (1, 9, 13, 5),
    (14, 6, 2, 10),
    (11, 3, 15, 7),
    (4, 12, 8, 16),

    (9, 1, 5, 13),
    (6, 14, 10, 2),
    (3, 11, 7, 15),
    (12, 4, 16, 8),

    (1, 10, 13, 6),
    (14, 2, 5, 11),
    (7, 3, 15, 12),
    (4, 16, 8, 9),

    (13, 7, 1, 15),
    (2, 12, 10, 5),
    (11, 8, 6, 3),
    (4, 9, 14, 16),

    (1, 11, 5, 15),
    (13, 2, 7, 10),
    (6, 12, 3, 14),
    (8, 16, 9, 4)
]


# ============================================================
# 10. SIŁA ZAWODNIKA INDYWIDUALNEGO
# ============================================================

def sila_indi(nr):

    dane = st.session_state.indi_zawodnicy[nr]

    if nr not in st.session_state.indi_baza:
        st.session_state.indi_baza[nr] = {
            "start": dane["ovr"],
            "dystans": dane["ovr"],
            "forma": 0
        }

    baza = st.session_state.indi_baza[nr]

    pogoda = st.session_state.indi_pogoda

    if "Twardy" in st.session_state.get(
        "indi_tor",
        "⚖️ Tor Neutralny"
    ):

        waga_startu = 0.8
        waga_dystansu = 0.2

    elif "Przyczepny" in st.session_state.get(
        "indi_tor",
        "⚖️ Tor Neutralny"
    ):

        waga_startu = 0.3
        waga_dystansu = 0.7

    else:

        waga_startu = 0.5
        waga_dystansu = 0.5

    kara = 0

    if "Wietrznie" in pogoda:
        kara = 1

    elif "Deszcz" in pogoda:
        waga_startu *= 0.9
        waga_dystansu *= 1.1
        kara = 1

    elif "Burza" in pogoda:
        waga_startu *= 0.85
        waga_dystansu *= 1.05
        kara = 2

    sila = (
        baza["start"] * waga_startu
        + baza["dystans"] * waga_dystansu
        + baza["forma"]
        - kara
    )

    sila += random.uniform(-5, 5)

    return sila


# ============================================================
# 11. SYMULACJA BIEGU INDYWIDUALNEGO
# ============================================================

def symuluj_bieg_indi(numery, nazwa_biegu):

    uczestnicy = []

    for nr in numery:

        if nr not in st.session_state.indi_zawodnicy:
            continue

        dane = st.session_state.indi_zawodnicy[nr]

        if not dane["name"].strip():
            continue

        uczestnicy.append({
            "nr": nr,
            "name": dane["name"],
            "ovr": dane["ovr"],
            "sila": sila_indi(nr),
            "status": None,
            "pkt": 0
        })

    zdarzenia = []

    for zawodnik in uczestnicy:

        los = random.random()

        if los < 0.025:

            zawodnik["status"] = "D"
            zawodnik["sila"] = -100

            zdarzenia.append(
                f"💨 Defekt: {zawodnik['name']}"
            )

        elif los < 0.055:

            zawodnik["status"] = "U"
            zawodnik["sila"] = -200

            zdarzenia.append(
                f"💥 Upadek: {zawodnik['name']}"
            )

        elif los < 0.075:

            zawodnik["status"] = "W"
            zawodnik["sila"] = -300

            zdarzenia.append(
                f"🚫 Wykluczenie: {zawodnik['name']}"
            )

    uczestnicy.sort(
        key=lambda x: x["sila"],
        reverse=True
    )

    punkty = [3, 2, 1, 0]

    for i, zawodnik in enumerate(uczestnicy):

        if zawodnik["status"] is None:

            zawodnik["pkt"] = punkty[i] if i < 4 else 0

        else:

            zawodnik["pkt"] = 0

    for zawodnik in uczestnicy:

        nr = zawodnik["nr"]

        st.session_state.indi_points[nr] += zawodnik["pkt"]

        st.session_state.indi_starty[nr].append(
            zawodnik["pkt"]
            if zawodnik["status"] is None
            else zawodnik["status"]
        )

    wynik = []

    for i, zawodnik in enumerate(uczestnicy):

        pozycja = i + 1

        if zawodnik["status"]:

            wynik.append(
                f"{pozycja}. "
                f"{zawodnik['name']} "
                f"({zawodnik['status']}) - 0"
            )

        else:

            wynik.append(
                f"{pozycja}. "
                f"{zawodnik['name']} - "
                f"{zawodnik['pkt']}"
            )

    st.session_state.indi_history.append({
        "bieg": nazwa_biegu,
        "wynik": wynik,
        "zdarzenia": zdarzenia
    })


# ============================================================
# 12. KLASYFIKACJA INDYWIDUALNA
# ============================================================

def klasyfikacja_indi():

    zawodnicy = aktywni_zawodnicy()

    dane = []

    for nr in zawodnicy:

        starty = st.session_state.indi_starty.get(nr, [])

        pkt = st.session_state.indi_points.get(nr, 0)

        zwyciestwa = sum(
            1
            for x in starty
            if str(x) == "3"
        )

        drugie = sum(
            1
            for x in starty
            if str(x) == "2"
        )

        trzecie = sum(
            1
            for x in starty
            if str(x) == "1"
        )

        dane.append({
            "Nr": nr,
            "Zawodnik": st.session_state.indi_zawodnicy[nr]["name"],
            "OVR": st.session_state.indi_zawodnicy[nr]["ovr"],
            "Kraj": st.session_state.indi_zawodnicy[nr]["narodowosc"],
            "Pkt": pkt,
            "3": zwyciestwa,
            "2": drugie,
            "1": trzecie,
            "Starty": len(starty),
            "Biegi": ", ".join(map(str, starty))
        })

    df = pd.DataFrame(dane)

    if not df.empty:

        df = df.sort_values(
            by=["Pkt", "3", "2", "1"],
            ascending=[False, False, False, False]
        ).reset_index(drop=True)

        df.insert(
            0,
            "Poz.",
            range(1, len(df) + 1)
        )

    return df


# ============================================================
# 13. RAPORT ZAWODÓW INDYWIDUALNYCH
# ============================================================

def raport_indi():

    tekst = []

    tekst.append("🏁 RAPORT ZAWODÓW INDYWIDUALNYCH")
    tekst.append("=" * 55)

    tekst.append(
        f"Format: {st.session_state.indi_format}"
    )

    tekst.append(
        f"Pogoda: {st.session_state.indi_pogoda}"
    )

    tekst.append("")

    tekst.append("BIEGI")
    tekst.append("-" * 55)

    for hist in st.session_state.indi_history:

        tekst.append(
            f"\n{hist['bieg']}"
        )

        for wynik in hist["wynik"]:

            tekst.append(
                f"  {wynik}"
            )

        if hist["zdarzenia"]:

            for zdarzenie in hist["zdarzenia"]:

                tekst.append(
                    f"  {zdarzenie}"
                )

    tekst.append("")
    tekst.append("KLASYFIKACJA")
    tekst.append("-" * 55)

    df = klasyfikacja_indi()

    for _, row in df.iterrows():

        tekst.append(
            f"{row['Poz.']}. "
            f"{row['Zawodnik']} — "
            f"{row['Pkt']} pkt"
        )

    return "\n".join(tekst)


# ============================================================
# 14. OBSŁUGA FAZY SGP
# ============================================================

def uruchom_sgp():

    if st.session_state.indi_heat < 20:

        indeks = st.session_state.indi_heat

        obsada = TABELA_20[indeks]

        obsada = [
            nr
            for nr in obsada
            if nr in aktywni_zawodnicy()
        ]

        if len(obsada) < 4:

            st.error(
                "Do pełnej obsady SGP potrzebnych jest 16 zawodników."
            )

            return

        st.subheader(
            f"🚦 Bieg {indeks + 1} / 20"
        )

        cols = st.columns(4)

        for i, nr in enumerate(obsada):

            with cols[i]:

                st.markdown(
                    f"**{i + 1}. "
                    f"{st.session_state.indi_zawodnicy[nr]['name']}**"
                )

                st.caption(
                    f"OVR {st.session_state.indi_zawodnicy[nr]['ovr']}"
                )

        if st.button(
            "🏁 Jedź bieg",
            key=f"indi_sgp_heat_{indeks}",
            use_container_width=True
        ):

            symuluj_bieg_indi(
                obsada,
                f"Bieg {indeks + 1}"
            )

            st.session_state.indi_heat += 1

            st.rerun()

        return

    # --------------------------------------------------------
    # PO 20 BIEGACH
    # --------------------------------------------------------

    df = klasyfikacja_indi()

    st.subheader(
        "📊 Klasyfikacja po 20 biegach"
    )

    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True
    )

    if st.session_state.indi_stage == "main":

        if len(df) < 16:

            st.error(
                "SGP wymaga dokładnie 16 zawodników."
            )

            return

        top10 = list(
            df["Nr"].head(10)
        )

        top2 = top10[:2]

        pozostali = top10[2:]

        random.shuffle(pozostali)

        lcq1 = pozostali[:4]
        lcq2 = pozostali[4:8]

        st.session_state.indi_lcq["LCQ1"] = lcq1
        st.session_state.indi_lcq["LCQ2"] = lcq2

        st.session_state.indi_finalists = top2.copy()

        st.session_state.indi_stage = "lcq"

        st.rerun()

    if st.session_state.indi_stage == "lcq":

        st.subheader(
            "🔥 Last Chance Qualifiers"
        )

        lcq = st.session_state.indi_lcq

        for nazwa, lista in [
            ("LCQ1", lcq["LCQ1"]),
            ("LCQ2", lcq["LCQ2"])
        ]:

            st.markdown(f"### {nazwa}")

            cols = st.columns(4)

            for i, nr in enumerate(lista):

                with cols[i]:

                    st.write(
                        f"{i + 1}. "
                        f"{st.session_state.indi_zawodnicy[nr]['name']}"
                    )

            if st.button(
                f"🏁 Jedź {nazwa}",
                key=f"jedz_{nazwa}"
            ):

                temp_start = dict(
                    st.session_state.indi_starty
                )

                temp_points = dict(
                    st.session_state.indi_points
                )

                historia_before = len(
                    st.session_state.indi_history
                )

                symuluj_bieg_indi(
                    lista,
                    nazwa
                )

                hist = st.session_state.indi_history[-1]

                zwyciezca_name = hist["wynik"][0]

                zwyciezca = None

                for nr in lista:

                    if (
                        st.session_state.indi_zawodnicy[nr]["name"]
                        in zwyciezca_name
                    ):

                        zwyciezca = nr
                        break

                if zwyciezca is not None:
                    st.session_state.indi_finalists.append(
                        zwyciezca
                    )

                if nazwa == "LCQ2":

                    st.session_state.indi_stage = "sgp_final"

                st.rerun()


    elif st.session_state.indi_stage == "sgp_final":

        st.subheader("🏆 FINAŁ SGP")

        finalisci = st.session_state.indi_finalists[:4]

        if len(finalisci) < 4:

            st.warning(
                "Finał wymaga czterech zawodników."
            )

            return

        cols = st.columns(4)

        for i, nr in enumerate(finalisci):

            with cols[i]:

                st.write(
                    f"{i + 1}. "
                    f"{st.session_state.indi_zawodnicy[nr]['name']}"
                )

        if st.button(
            "🏁 Jedź FINAŁ",
            key="sgp_final"
        ):

            symuluj_bieg_indi(
                finalisci,
                "FINAŁ SGP"
            )

            st.session_state.indi_stage = "finished"
            st.session_state.indi_finished = True

            st.rerun()


# ============================================================
# 15. OBSŁUGA IMP
# ============================================================

def uruchom_imp():

    if st.session_state.indi_heat < 20:

        indeks = st.session_state.indi_heat

        obsada = TABELA_20[indeks]

        if len(aktywni_zawodnicy()) < 16:

            st.error(
                "IMP wymaga 16 zawodników."
            )

            return

        st.subheader(
            f"🚦 Bieg {indeks + 1} / 20"
        )

        cols = st.columns(4)

        for i, nr in enumerate(obsada):

            with cols[i]:

                st.write(
                    f"{i + 1}. "
                    f"{st.session_state.indi_zawodnicy[nr]['name']}"
                )

        if st.button(
            "🏁 Jedź bieg",
            key=f"imp_heat_{indeks}",
            use_container_width=True
        ):

            symuluj_bieg_indi(
                obsada,
                f"Bieg {indeks + 1}"
            )

            st.session_state.indi_heat += 1

            st.rerun()

        return

    df = klasyfikacja_indi()

    st.subheader(
        "📊 Klasyfikacja po 20 biegach"
    )

    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True
    )

    if st.session_state.indi_stage == "main":

        top6 = list(
            df["Nr"].head(6)
        )

        st.session_state.imp_semifinal = top6

        st.session_state.indi_stage = "imp_semifinal"

        st.rerun()

    elif st.session_state.indi_stage == "imp_semifinal":

        zawodnicy = st.session_state.imp_semifinal

        st.subheader(
            "🔥 Półfinał IMP"
        )

        cols = st.columns(4)

        for i, nr in enumerate(zawodnicy[:4]):

            with cols[i]:

                st.write(
                    f"{i + 1}. "
                    f"{st.session_state.indi_zawodnicy[nr]['name']}"
                )

        if st.button(
            "🏁 Jedź półfinał IMP",
            key="imp_semi"
        ):

            symuluj_bieg_indi(
                zawodnicy[:4],
                "Półfinał IMP"
            )

            hist = st.session_state.indi_history[-1]

            zwyciezca = None
            drugi = None

            for nr in zawodnicy[:4]:

                name = st.session_state.indi_zawodnicy[nr]["name"]

                if name in hist["wynik"][0]:
                    zwyciezca = nr

                if len(hist["wynik"]) > 1:
                    if name in hist["wynik"][1]:
                        drugi = nr

            finalisci = [
                zawodnicy[0],
                zawodnicy[1]
            ]

            if zwyciezca is not None:
                finalisci.append(zwyciezca)

            if drugi is not None:
                finalisci.append(drugi)

            finalisci = list(dict.fromkeys(finalisci))[:4]

            st.session_state.imp_finalisci = finalisci

            st.session_state.indi_stage = "imp_final"

            st.rerun()

    elif st.session_state.indi_stage == "imp_final":

        finalisci = st.session_state.imp_finalisci

        st.subheader(
            "🏆 FINAŁ IMP"
        )

        cols = st.columns(4)

        for i, nr in enumerate(finalisci):

            with cols[i]:

                st.write(
                    f"{i + 1}. "
                    f"{st.session_state.indi_zawodnicy[nr]['name']}"
                )

        if st.button(
            "🏁 Jedź FINAŁ IMP",
            key="imp_final"
        ):

            symuluj_bieg_indi(
                finalisci,
                "FINAŁ IMP"
            )

            st.session_state.indi_stage = "finished"
            st.session_state.indi_finished = True

            st.rerun()


# ============================================================
# 16. OBSŁUGA ZŁOTEGO KASKU
# ============================================================

def uruchom_zloty_kask():

    if len(aktywni_zawodnicy()) < 16:

        st.error(
            "Złoty Kask wymaga 16 zawodników."
        )

        return

    if st.session_state.indi_heat < 20:

        indeks = st.session_state.indi_heat

        obsada = TABELA_20[indeks]

        st.subheader(
            f"🚦 Bieg {indeks + 1} / 20"
        )

        cols = st.columns(4)

        for i, nr in enumerate(obsada):

            with cols[i]:

                st.write(
                    f"{i + 1}. "
                    f"{st.session_state.indi_zawodnicy[nr]['name']}"
                )

        if st.button(
            "🏁 Jedź bieg",
            key=f"zk_heat_{indeks}",
            use_container_width=True
        ):

            symuluj_bieg_indi(
                obsada,
                f"Bieg {indeks + 1}"
            )

            st.session_state.indi_heat += 1

            st.rerun()

        return

    st.subheader(
        "🏆 KONIEC ZAWODÓW — ZŁOTY KASK"
    )

    df = klasyfikacja_indi()

    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True
    )

    if not st.session_state.indi_finished:

        if len(df) >= 2:

            pierwsze = df.iloc[0]
            drugie = df.iloc[1]

            if pierwsze["Pkt"] == drugie["Pkt"]:

                st.warning(
                    "Remis na pierwszym miejscu. "
                    "Możesz rozegrać bieg dodatkowy."
                )

                if st.button(
                    "🏁 Bieg dodatkowy o Złoty Kask",
                    key="zk_runoff"
                ):

                    numery = [
                        int(pierwsze["Nr"]),
                        int(drugie["Nr"])
                    ]

                    symuluj_bieg_indi(
                        numery,
                        "Bieg dodatkowy"
                    )

                    st.session_state.indi_finished = True

                    st.rerun()

            else:

                st.session_state.indi_finished = True


# ============================================================
# 17. GŁÓWNY SIDEBAR
# ============================================================

st.sidebar.header(
    "⚙️ Konfiguracja"
)


# ============================================================
# 18. WYBÓR DRUŻYN
# ============================================================

if (
    "gospodarz_bieżący" not in st.session_state
    or st.session_state.gospodarz_bieżący not in kluby_lista
):

    st.session_state.gospodarz_bieżący = kluby_lista[0]


if (
    "gosc_bieżący" not in st.session_state
    or st.session_state.gosc_bieżący not in kluby_lista
):

    st.session_state.gosc_bieżący = kluby_lista[1]


wybrany_gospodarz = st.sidebar.selectbox(
    "🏠 Gospodarz",
    kluby_lista,
    index=kluby_lista.index(
        st.session_state.gospodarz_bieżący
    ),
    key="gospodarz_bieżący"
)


wybrany_gosc = st.sidebar.selectbox(
    "✈️ Gość",
    kluby_lista,
    index=kluby_lista.index(
        st.session_state.gosc_bieżący
    ),
    key="gosc_bieżący"
)


# ============================================================
# 19. POGODA MECZU
# ============================================================

tryb_pogody_mecz = st.sidebar.selectbox(
    "🌤️ Pogoda meczu",
    [
        "☀️ Słonecznie i ciepło",
        "⛅ Lekkie zachmurzenie",
        "🌬️ Wietrznie",
        "🌧️ Deszcz (Mżawka)",
        "🌩️ Burza / Ulewa",
        "🎲 Losowa pogoda"
    ],
    key="wybor_pogody_mecz"
)


if tryb_pogody_mecz == "🎲 Losowa pogoda":

    if (
        "pogoda_mecz" not in st.session_state
        or st.session_state.get("wylosowana_pogoda_przelaczona")
        is not True
    ):

        st.session_state.pogoda_mecz = losuj_pogode()
        st.session_state.wylosowana_pogoda_przelaczona = True

else:

    st.session_state.pogoda_mecz = tryb_pogody_mecz
    st.session_state.wylosowana_pogoda_przelaczona = False


wybrana_pogoda = st.session_state.pogoda_mecz


# ============================================================
# 20. RESET MECZU PO ZMIANIE DRUŻYN
# ============================================================

if (
    st.session_state.get("mecz_gospodarz")
    != wybrany_gospodarz
    or
    st.session_state.get("mecz_gosc")
    != wybrany_gosc
):

    st.session_state.mecz_gospodarz = wybrany_gospodarz
    st.session_state.mecz_gosc = wybrany_gosc

    st.session_state.current_heat = 0
    st.session_state.score_gosp = 0
    st.session_state.score_gosc = 0
    st.session_state.match_history = []

    st.session_state.starts_count = {
        nr: 0 for nr in range(1, 17)
    }

    st.session_state.rider_heats = {
        nr: [] for nr in range(1, 17)
    }

    st.session_state.normal_starts_count = {
        nr: 0 for nr in range(1, 17)
    }

    st.session_state.rt_count = {
        nr: 0 for nr in range(1, 17)
    }

    st.session_state.zz_count = {
        nr: 0 for nr in range(1, 17)
    }

    st.session_state.rider_bonuses = {
        nr: 0 for nr in range(1, 17)
    }

    st.session_state.kontuzjowani = set()

    st.session_state.zz_gosp = None
    st.session_state.zz_gosc = None

    st.session_state.mecz_przerwany = False
    st.session_state.decyzja_o_przerwaniu_podjeta = False

    st.session_state.sklad_gospodarze = {
        nr: "" for nr in range(1, 9)
    }

    st.session_state.sklad_goscie = {
        nr: "" for nr in range(9, 17)
    }

    st.session_state.sklad_gospodarze_ovr = {
        nr: 60 for nr in range(1, 9)
    }

    st.session_state.sklad_goscie_ovr = {
        nr: 60 for nr in range(9, 17)
    }

    st.session_state.baza_zawodnikow = {}

    st.rerun()


# ============================================================
# 21. GŁÓWNE ZAKŁADKI
# ============================================================

tab_kadry, tab_taktyka, tab_mecz, tab_indi = st.tabs(
    [
        "👥 1. Kadry",
        "📣 2. Taktyka",
        "🏎️ 3. Mecz Drużynowy",
        "🏆 4. Zawody Indywidualne"
    ]
)


# ============================================================
# 22. KADRY
# ============================================================

with tab_kadry:

    st.header(
        f"{wybrany_gospodarz} vs {wybrany_gosc}"
    )

    st.info(
        "Wpisz ręcznie dowolnych zawodników oraz ich OVR."
    )

    col_gosp, col_gosc = st.columns(2)

    with col_gosp:

        st.subheader(
            f"🏠 {wybrany_gospodarz}"
        )

        for nr in range(1, 9):

            if nr <= 5:
                typ = "Senior / U24"
            elif nr in [6, 7]:
                typ = "Junior"
            else:
                typ = "Rezerwa"

            st.markdown(
                f"**Nr {nr} — {typ}**"
            )

            c1, c2 = st.columns([3, 1])

            with c1:

                st.session_state.sklad_gospodarze[nr] = st.text_input(
                    f"Zawodnik {nr}",
                    value=st.session_state.sklad_gospodarze.get(
                        nr,
                        ""
                    ),
                    key=f"manual_gosp_name_{nr}",
                    placeholder="Imię i nazwisko"
                )

            with c2:

                st.session_state.sklad_gospodarze_ovr[nr] = st.number_input(
                    f"OVR {nr}",
                    min_value=1,
                    max_value=99,
                    value=int(
                        st.session_state.sklad_gospodarze_ovr.get(
                            nr,
                            60
                        )
                    ),
                    key=f"manual_gosp_ovr_{nr}"
                )

    with col_gosc:

        st.subheader(
            f"✈️ {wybrany_gosc}"
        )

        for nr in range(9, 17):

            if nr <= 13:
                typ = "Senior / U24"
            elif nr in [14, 15]:
                typ = "Junior"
            else:
                typ = "Rezerwa"

            st.markdown(
                f"**Nr {nr} — {typ}**"
            )

            c1, c2 = st.columns([3, 1])

            with c1:

                st.session_state.sklad_goscie[nr] = st.text_input(
                    f"Zawodnik {nr}",
                    value=st.session_state.sklad_goscie.get(
                        nr,
                        ""
                    ),
                    key=f"manual_gosc_name_{nr}",
                    placeholder="Imię i nazwisko"
                )

            with c2:

                st.session_state.sklad_goscie_ovr[nr] = st.number_input(
                    f"OVR {nr}",
                    min_value=1,
                    max_value=99,
                    value=int(
                        st.session_state.sklad_goscie_ovr.get(
                            nr,
                            60
                        )
                    ),
                    key=f"manual_gosc_ovr_{nr}"
                )

    st.divider()

    if st.button(
        "🔄 Wylosuj statystyki zawodników",
        use_container_width=True
    ):

        st.session_state.baza_zawodnikow = (
            generuj_statystyki_zawodnikow()
        )

        st.success(
            "Statystyki zostały wygenerowane."
        )


# ============================================================
# 23. TAKTYKA
# ============================================================

with tab_taktyka:

    st.header(
        "📣 Odprawa Taktyczna"
    )

    c1, c2 = st.columns(2)

    with c1:

        st.subheader(
            f"🏠 {wybrany_gospodarz}"
        )

        st.selectbox(
            "Tor",
            [
                "⚖️ Tor Neutralny",
                "🧱 Tor Twardy",
                "🚜 Tor Przyczepny"
            ],
            key="przygotowanie_toru_gosp"
        )

        st.selectbox(
            "Styl jazdy",
            [
                "Standardowe nastawienie",
                "Agresywne",
                "Defensywne"
            ],
            key="styl_jazdy_gosp"
        )

        st.selectbox(
            "Sprzęt",
            [
                "🔧 Silnik Niezawodny",
                "🚀 Silnik Ekstra Mocny"
            ],
            key="sprzet_gosp"
        )

    with c2:

        st.subheader(
            f"✈️ {wybrany_gosc}"
        )

        st.selectbox(
            "Styl jazdy",
            [
                "Standardowe nastawienie",
                "Agresywne",
                "Defensywne"
            ],
            key="styl_jazdy_gosc"
        )

        st.selectbox(
            "Sprzęt",
            [
                "🔧 Silnik Niezawodny",
                "🚀 Silnik Ekstra Mocny"
            ],
            key="sprzet_gosc"
        )


# ============================================================
# 24. MECZ DRUŻYNOWY
# ============================================================

with tab_mecz:

    st.header(
        "🏎️ Centrum Meczowe"
    )

    if "current_heat" not in st.session_state:

        st.session_state.current_heat = 0

        st.session_state.score_gosp = 0
        st.session_state.score_gosc = 0

        st.session_state.match_history = []

        st.session_state.rider_heats = {
            nr: [] for nr in range(1, 17)
        }

        st.session_state.normal_starts_count = {
            nr: 0 for nr in range(1, 17)
        }

        st.session_state.rt_count = {
            nr: 0 for nr in range(1, 17)
        }

        st.session_state.zz_count = {
            nr: 0 for nr in range(1, 17)
        }

        st.session_state.rider_bonuses = {
            nr: 0 for nr in range(1, 17)
        }

        st.session_state.kontuzjowani = set()

        st.session_state.baza_zawodnikow = (
            generuj_statystyki_zawodnikow()
        )

    st.info(
        f"🌤️ Pogoda: **{wybrana_pogoda}**"
    )

    st.markdown(
        f"## {wybrany_gospodarz} "
        f"**{st.session_state.score_gosp}:"
        f"{st.session_state.score_gosc}** "
        f"{wybrany_gosc}"
    )

    if st.button(
        "📋 Skopiuj cały raport meczu",
        use_container_width=True
    ):

        raport = raport_meczu()

        st.code(
            raport,
            language="text"
        )

        st.info(
            "Raport znajduje się powyżej i można go skopiować."
        )

    st.divider()

    if st.session_state.current_heat < 15:

        heat = program_zawodow[
            st.session_state.current_heat
        ]

        st.subheader(
            f"🚦 Bieg {heat['bieg']} / 15"
        )

        kaski = heat["kaski"]

        uczestnicy = []

        for pole in ["A", "B", "C", "D"]:

            nr = heat[pole]

            czy_gosp = kaski[pole] in ["🔴", "🔵"]

            nazwa = pobierz_zawodnika(
                nr,
                czy_gosp
            )

            ovr = pobierz_ovr(
                nr,
                czy_gosp
            )

            if nazwa:

                uczestnicy.append({
                    "nr": nr,
                    "nazwisko": nazwa,
                    "ovr": ovr,
                    "kask": kaski[pole],
                    "druzyna": (
                        "gosp"
                        if czy_gosp
                        else "gosc"
                    ),
                    "sila": (
                        ovr
                        + random.uniform(-5, 5)
                    )
                })

        if len(uczestnicy) == 4:

            if st.button(
                "🏁 Jedź Bieg",
                use_container_width=True
            ):

                for u in uczestnicy:

                    if (
                        "Ekstra Mocny"
                        in st.session_state.get(
                            f"sprzet_{u['druzyna']}",
                            ""
                        )
                    ):

                        u["sila"] += 2

                uczestnicy.sort(
                    key=lambda x: x["sila"],
                    reverse=True
                )

                punkty = [3, 2, 1, 0]

                gosp_pkt = 0
                gosc_pkt = 0

                szczegoly = []

                for i, u in enumerate(uczestnicy):

                    pkt = punkty[i]

                    if u["druzyna"] == "gosp":
                        gosp_pkt += pkt
                    else:
                        gosc_pkt += pkt

                    st.session_state.rider_heats[
                        u["nr"]
                    ].append(
                        str(pkt)
                    )

                    st.session_state.normal_starts_count[
                        u["nr"]
                    ] += 1

                    szczegoly.append(
                        f"{u['nazwisko']} "
                        f"({u['kask']}) - {pkt}"
                    )

                st.session_state.score_gosp += gosp_pkt
                st.session_state.score_gosc += gosc_pkt

                komentarz = generuj_komentarz_sf(
                    uczestnicy,
                    []
                )

                st.session_state.match_history.append({
                    "bieg": heat["bieg"],
                    "wynik_biegu": (
                        f"{gosp_pkt}:{gosc_pkt}"
                    ),
                    "szczegoly": ", ".join(
                        szczegoly
                    ),
                    "komentarz": komentarz
                })

                st.session_state.current_heat += 1

                st.rerun()

        else:

            st.warning(
                "Aby przeprowadzić mecz, wpisz zawodników "
                "w wymagane pola."
            )

    else:

        st.success(
            f"🏁 KONIEC MECZU! "
            f"{wybrany_gospodarz} "
            f"{st.session_state.score_gosp}:"
            f"{st.session_state.score_gosc} "
            f"{wybrany_gosc}"
        )

        if st.session_state.match_history:

            st.subheader(
                "📜 Historia biegów"
            )

            for hist in reversed(
                st.session_state.match_history
            ):

                with st.expander(
                    f"Bieg {hist['bieg']} — "
                    f"{hist['wynik_biegu']}"
                ):

                    st.write(
                        hist["szczegoly"]
                    )

                    st.info(
                        hist["komentarz"]
                    )

    st.divider()

    st.subheader(
        "📊 Tabela punktowa"
    )

    tabela = []

    for nr in range(1, 17):

        nazwa = pobierz_zawodnika(
            nr,
            nr <= 8
        )

        if not nazwa:
            continue

        biegi = st.session_state.rider_heats.get(
            nr,
            []
        )

        pkt = 0

        for wynik in biegi:

            if str(wynik).startswith("3"):
                pkt += 3

            elif str(wynik).startswith("2"):
                pkt += 2

            elif str(wynik).startswith("1"):
                pkt += 1

        tabela.append({
            "Nr": nr,
            "Zawodnik": nazwa,
            "OVR": pobierz_ovr(
                nr,
                nr <= 8
            ),
            "Pkt": pkt,
            "Biegi": ", ".join(
                map(str, biegi)
            ),
            "Starty": len(biegi)
        })

    if tabela:

        st.dataframe(
            pd.DataFrame(tabela),
            hide_index=True,
            use_container_width=True
        )


# ============================================================
# 25. ZAWODY INDYWIDUALNE — PANEL
# ============================================================

with tab_indi:

    st.header(
        "🏆 Zawody Indywidualne"
    )

    st.info(
        "Wybierz format zawodów. Każdy format ma własny schemat."
    )

    wybrany_format = st.selectbox(
        "🏆 Format zawodów",
        FORMATY_INDYWIDUALNE,
        key="indi_format"
    )

    # --------------------------------------------------------
    # OPIS FORMATU
    # --------------------------------------------------------

    if wybrany_format == "🌍 SGP — Grand Prix":

        st.markdown(
            """
### 🌍 SGP — Grand Prix

- 16 zawodników
- 20 biegów rundy zasadniczej
- dwóch najlepszych po 20 biegach trafia bezpośrednio do finału
- miejsca 3–10 trafiają do dwóch LCQ
- zwycięzcy LCQ awansują do finału
- finał rozstrzyga zwycięzcę rundy
            """
        )

    elif wybrany_format == "🇵🇱 IMP — Indywidualne Mistrzostwa Polski":

        st.markdown(
            """
### 🇵🇱 IMP

- 16 zawodników w turnieju finałowym
- 20 biegów turnieju głównego
- półfinał
- finał
- końcowa klasyfikacja turnieju jest ustalana zgodnie z kolejnością
  po turnieju głównym oraz wynikami półfinału i finału
            """
        )

    else:

        st.markdown(
            """
### 🏆 Złoty Kask

- 16 zawodników
- 2 miejsca rezerwowe przygotowane w panelu
- 20 biegów
- klasyfikacja na podstawie zdobytych punktów
- przy remisie na pierwszym miejscu możliwość rozegrania biegu dodatkowego
            """
        )

    # --------------------------------------------------------
    # POGODA
    # --------------------------------------------------------

    tryb_pogody_indi = st.selectbox(
        "🌤️ Pogoda",
        LISTA_POGODY + ["🎲 Losowa pogoda"],
        key="indi_tryb_pogody"
    )

    if tryb_pogody_indi == "🎲 Losowa pogoda":

        if st.button(
            "🎲 Losuj pogodę",
            key="losuj_pogode_indi"
        ):

            st.session_state.indi_pogoda = losuj_pogode()

    else:

        st.session_state.indi_pogoda = tryb_pogody_indi

    st.info(
        f"Aktualna pogoda: **{st.session_state.indi_pogoda}**"
    )

    st.selectbox(
        "🛣️ Charakterystyka toru",
        [
            "⚖️ Tor Neutralny",
            "🧱 Tor Twardy",
            "🚜 Tor Przyczepny"
        ],
        key="indi_tor"
    )

    # --------------------------------------------------------
    # ZAWODNICY
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "👤 Zawodnicy"
    )

    st.caption(
        "Wpisz 16 zawodników. Dla Złotego Kasku pola 17 i 18 "
        "mogą służyć jako rezerwa."
    )

    for nr in range(1, 19):

        if nr <= 16:

            label = f"Zawodnik nr {nr}"

        elif nr == 17:

            label = "Rezerwa 1"

        else:

            label = "Rezerwa 2"

        st.markdown(
            f"**{label}**"
        )

        c1, c2, c3, c4 = st.columns(
            [3, 1, 1.5, 1.5]
        )

        with c1:

            st.session_state.indi_zawodnicy[nr]["name"] = st.text_input(
                "Imię i nazwisko",
                value=st.session_state.indi_zawodnicy[nr]["name"],
                key=f"indi_name_{nr}",
                placeholder="Imię i nazwisko"
            )

        with c2:

            st.session_state.indi_zawodnicy[nr]["ovr"] = st.number_input(
                "OVR",
                min_value=1,
                max_value=99,
                value=int(
                    st.session_state.indi_zawodnicy[nr]["ovr"]
                ),
                key=f"indi_ovr_{nr}"
            )

        with c3:

            st.session_state.indi_zawodnicy[nr]["narodowosc"] = st.selectbox(
                "Kraj",
                [
                    "Polska",
                    "Dania",
                    "Szwecja",
                    "Australia",
                    "Wielka Brytania",
                    "Czechy",
                    "Łotwa",
                    "Niemcy",
                    "Ukraina",
                    "Finlandia",
                    "Norwegia",
                    "Inny"
                ],
                index=0,
                key=f"indi_country_{nr}"
            )

        with c4:

            st.session_state.indi_zawodnicy[nr]["status"] = st.selectbox(
                "Status",
                [
                    "Senior",
                    "U24",
                    "Junior"
                ],
                key=f"indi_status_{nr}"
            )

    # --------------------------------------------------------
    # KONTROLA SKŁADU
    # --------------------------------------------------------

    st.divider()

    aktywni = aktywni_zawodnicy()

    st.write(
        f"**Wpisanych zawodników: {len(aktywni)} / 16**"
    )

    if len(aktywni) < 16:

        st.warning(
            "Aby rozpocząć zawody, wpisz 16 zawodników."
        )

    # --------------------------------------------------------
    # PRZYCISKI
    # --------------------------------------------------------

    c1, c2, c3 = st.columns(3)

    with c1:

        if st.button(
            "🔄 Nowe zawody",
            use_container_width=True
        ):

            reset_indywidualnych()

            st.rerun()

    with c2:

        if st.button(
            "🎲 Wylosuj pogodę",
            use_container_width=True
        ):

            st.session_state.indi_pogoda = losuj_pogode()

            st.rerun()

    with c3:

        if st.button(
            "📊 Wygeneruj statystyki",
            use_container_width=True
        ):

            if len(aktywni) >= 16:

                generuj_indi_baze()

                st.success(
                    "Statystyki zawodników wygenerowane."
                )

            else:

                st.warning(
                    "Najpierw wpisz 16 zawodników."
                )

    # --------------------------------------------------------
    # START ZAWODÓW
    # --------------------------------------------------------

    if (
        len(aktywni) >= 16
        and not st.session_state.indi_baza
    ):

        if st.button(
            "🏁 ROZPOCZNIJ ZAWODY",
            use_container_width=True
        ):

            generuj_indi_baze()

            st.session_state.indi_heat = 0
            st.session_state.indi_stage = "main"
            st.session_state.indi_finished = False

            st.rerun()

    # --------------------------------------------------------
    # SYMULACJA
    # --------------------------------------------------------

    if (
        len(aktywni) >= 16
        and st.session_state.indi_baza
    ):

        st.divider()

        if not st.session_state.indi_finished:

            if wybrany_format == "🌍 SGP — Grand Prix":

                uruchom_sgp()

            elif wybrany_format == "🇵🇱 IMP — Indywidualne Mistrzostwa Polski":

                uruchom_imp()

            elif wybrany_format == "🏆 Złoty Kask":

                uruchom_zloty_kask()

        else:

            st.success(
                "🏆 ZAWODY ZAKOŃCZONE"
            )

    # --------------------------------------------------------
    # KLASYFIKACJA
    # --------------------------------------------------------

    if st.session_state.indi_baza:

        st.divider()

        st.subheader(
            "📊 Aktualna klasyfikacja"
        )

        df_indi = klasyfikacja_indi()

        st.dataframe(
            df_indi,
            hide_index=True,
            use_container_width=True
        )

        # ----------------------------------------------------
        # RAPORT
        # ----------------------------------------------------

        st.divider()

        st.subheader(
            "📋 Raport zawodów"
        )

        if st.button(
            "📋 Pokaż cały raport",
            use_container_width=True
        ):

            st.code(
                raport_indi(),
                language="text"
            )

        st.caption(
            "Raport zawiera pogodę, wszystkie biegi, "
            "zdarzenia i klasyfikację."
        )

        # ----------------------------------------------------
        # HISTORIA
        # ----------------------------------------------------

        if st.session_state.indi_history:

            st.divider()

            st.subheader(
                "📜 Historia biegów"
            )

            for hist in reversed(
                st.session_state.indi_history
            ):

                with st.expander(
                    hist["bieg"]
                ):

                    for wynik in hist["wynik"]:

                        st.write(
                            wynik
                        )

                    if hist["zdarzenia"]:

                        for zdarzenie in hist["zdarzenia"]:

                            st.warning(
                                zdarzenie
                            )
