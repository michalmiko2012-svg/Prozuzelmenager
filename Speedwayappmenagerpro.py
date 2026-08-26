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
# LISTA DRUŻYN
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
# KASKI
# ============================================================

KASKI = ["🔴", "⚪", "🔵", "🟡"]


# ============================================================
# POGODA
# ============================================================

POGODY = [
    "☀️ Słonecznie i ciepło",
    "⛅ Lekkie zachmurzenie",
    "🌬️ Wietrznie",
    "🌧️ Deszcz (Mżawka)",
    "🌩️ Burza / Ulewa"
]


def losuj_pogode():
    return random.choice(POGODY)


# ============================================================
# PROGRAM LIGOWY
# ============================================================

program_zawodow = [

    {
        "bieg": 1,
        "A": 1, "B": 9, "C": 3, "D": 11,
        "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}
    },
    {
        "bieg": 2,
        "A": 6, "B": 14, "C": 7, "D": 15,
        "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}
    },
    {
        "bieg": 3,
        "A": 10, "B": 2, "C": 12, "D": 4,
        "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}
    },
    {
        "bieg": 4,
        "A": 13, "B": 5, "C": 14, "D": 6,
        "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}
    },
    {
        "bieg": 5,
        "A": 3, "B": 9, "C": 4, "D": 10,
        "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}
    },
    {
        "bieg": 6,
        "A": 11, "B": 1, "C": 12, "D": 7,
        "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}
    },
    {
        "bieg": 7,
        "A": 2, "B": 13, "C": 5, "D": 15,
        "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}
    },
    {
        "bieg": 8,
        "A": 10, "B": 4, "C": 11, "D": 6,
        "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}
    },
    {
        "bieg": 9,
        "A": 1, "B": 9, "C": 2, "D": 12,
        "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}
    },
    {
        "bieg": 10,
        "A": 14, "B": 3, "C": 13, "D": 5,
        "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}
    },
    {
        "bieg": 11,
        "A": 4, "B": 13, "C": 1, "D": 9,
        "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}
    },
    {
        "bieg": 12,
        "A": 15, "B": 7, "C": 10, "D": 3,
        "kaski": {"A": "⚪", "B": "🔴", "C": "🟡", "D": "🔵"}
    },
    {
        "bieg": 13,
        "A": 5, "B": 11, "C": 2, "D": 12,
        "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}
    },
    {
        "bieg": 14,
        "A": 3, "B": 11, "C": 4, "D": 12,
        "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}
    },
    {
        "bieg": 15,
        "A": 1, "B": 9, "C": 2, "D": 10,
        "kaski": {"A": "🔴", "B": "⚪", "C": "🔵", "D": "🟡"}
    }
]


# ============================================================
# FUNKCJE WSPÓLNE
# ============================================================

def pobierz_zawodnika(nr, gospodarze=True):

    if gospodarze:
        return st.session_state.sklad_gospodarze.get(nr, "")

    return st.session_state.sklad_goscie.get(nr, "")


def pobierz_ovr(nr, gospodarze=True):

    if gospodarze:
        return st.session_state.sklad_gospodarze_ovr.get(nr, 60)

    return st.session_state.sklad_goscie_ovr.get(nr, 60)


def losuj_statystyki_ovr(ovr):

    odchylenie = random.randint(-2, 2)

    return {
        "ovr": ovr,
        "start": max(1, min(99, ovr + odchylenie)),
        "dystans": max(1, min(99, ovr - odchylenie)),
        "forma": random.randint(-3, 3)
    }


def sila_zawodnika(
    ovr,
    tryb_toru="neutralny",
    pogoda=""
):

    dane = losuj_statystyki_ovr(ovr)

    if tryb_toru == "twardy":
        waga_startu = 0.8
        waga_dystansu = 0.2

    elif tryb_toru == "przyczepny":
        waga_startu = 0.3
        waga_dystansu = 0.7

    else:
        waga_startu = 0.5
        waga_dystansu = 0.5

    if "Wietrznie" in pogoda:
        losowy = 6

    elif "Deszcz" in pogoda:
        losowy = 6

    elif "Burza" in pogoda:
        losowy = 7

    else:
        losowy = 5

    sila = (
        dane["start"] * waga_startu
        + dane["dystans"] * waga_dystansu
        + dane["forma"]
    )

    if "Wietrznie" in pogoda:
        sila -= 1

    if "Deszcz" in pogoda:
        sila -= 1

    if "Burza" in pogoda:
        sila -= 2

    sila += random.uniform(
        -losowy,
        losowy
    )

    return sila


def komentarz_biegu(
    uczestnicy,
    zdarzenia
):

    if zdarzenia:

        tekst = " ".join(
            zdarzenia
        )

        return random.choice([
            f"Niesamowite zamieszanie na torze. {tekst}",
            f"Sędzia przerywa bieg! {tekst}",
            f"Na torze dzieje się bardzo dużo! {tekst}",
            f"Co za dramatyczne wydarzenia! {tekst}"
        ])

    if not uczestnicy:

        return (
            "Bieg bez historii — nikt nie dojechał do mety."
        )

    zwyciezca = uczestnicy[0]["nazwisko"]

    drugi = (
        uczestnicy[1]["nazwisko"]
        if len(uczestnicy) > 1
        else None
    )

    trzeci = (
        uczestnicy[2]["nazwisko"]
        if len(uczestnicy) > 2
        else None
    )

    if drugi:

        roznica = (
            uczestnicy[0]["sila"]
            - uczestnicy[1]["sila"]
        )

    else:

        roznica = 100

    if (
        drugi
        and uczestnicy[0]["druzyna"]
        == uczestnicy[1]["druzyna"]
    ):

        return random.choice([
            f"🔥 Pojedynek parowy perfekcyjny! "
            f"{zwyciezca} i {drugi} wystrzelili spod taśmy i nie dali rywalom szans.",
            f"🚀 Para jak z żelaza! {zwyciezca} prowadził bieg, "
            f"a {drugi} skutecznie blokował rywali.",
            f"💥 Nokaut! Pokaz jazdy parą w wykonaniu duetu "
            f"{zwyciezca} - {drugi}."
        ])

    if (
        drugi
        and trzeci
        and uczestnicy[0]["druzyna"]
        != uczestnicy[1]["druzyna"]
        and uczestnicy[1]["druzyna"]
        == uczestnicy[2]["druzyna"]
    ):

        return random.choice([
            f"⚖️ Remis po twardej walce! {zwyciezca} wygrywa bieg, "
            f"ale {drugi} i {trzeci} dowożą punkty.",
            f"🎯 Samotny jastrząb! {zwyciezca} uciekł rywalom, "
            f"a para {drugi}, {trzeci} kontrolowała dalsze pozycje."
        ])

    if drugi and roznica < 1.5:

        return random.choice([
            f"😱 NIESAMOWITE! {zwyciezca} wyprzedza zawodnika "
            f"{drugi} dosłownie na kresce!",
            f"⚔️ Walka łokcie w łokcie! {zwyciezca} wyrywa zwycięstwo!",
            f"🔥 Co za mijanka! {zwyciezca} atakuje do samej mety!"
        ])

    if roznica > 6:

        return random.choice([
            f"⚡ Błyskawica od startu! {zwyciezca} zdemolował rywali.",
            f"🎯 Poza zasięgiem! {zwyciezca} założył całą stawkę.",
            f"👑 Profesor toru! {zwyciezca} dopasował przełożenia idealnie."
        ])

    return random.choice([
        f"🏍️ Zacięty bieg! {zwyciezca} utrzymał prowadzenie przed atakami {drugi}.",
        f"💨 Kąśliwe ataki na dystansie! {drugi} szukał prędkości.",
        f"🏁 Twarda walka o punkty! {zwyciezca} wygrywa start."
    ])


# ============================================================
# INICJALIZACJA LIGI
# ============================================================

def inicjalizuj_lige():

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

    if "gospodarz_biezacy" not in st.session_state:

        st.session_state.gospodarz_biezacy = (
            kluby_lista[0]
        )

    if "gosc_biezacy" not in st.session_state:

        st.session_state.gosc_biezacy = (
            kluby_lista[1]
        )

    if "pogoda_ligowa" not in st.session_state:

        st.session_state.pogoda_ligowa = POGODY[0]

    if "current_heat" not in st.session_state:

        reset_ligi()


def reset_ligi():

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

    st.session_state.baza_zawodnikow = {}


inicjalizuj_lige()


# ============================================================
# RESET TURNIEJU INDYWIDUALNEGO
# ============================================================

def reset_indywidualne():

    st.session_state.ind_current_heat = 0

    st.session_state.ind_history = []

    st.session_state.ind_points = {
        nr: 0 for nr in range(1, 21)
    }

    st.session_state.ind_bonuses = {
        nr: 0 for nr in range(1, 21)
    }

    st.session_state.ind_starts = {
        nr: 0 for nr in range(1, 21)
    }

    st.session_state.ind_heats = {
        nr: [] for nr in range(1, 21)
    }

    st.session_state.ind_finished = False
    st.session_state.ind_stage = "heats"


if "ind_current_heat" not in st.session_state:

    reset_indywidualne()


# ============================================================
# RESET REPREZENTACJI
# ============================================================

def reset_swc():

    st.session_state.swc_heat = 0

    st.session_state.swc_history = []

    st.session_state.swc_score = {
        1: 0,
        2: 0,
        3: 0,
        4: 0
    }

    st.session_state.swc_normal_starts = {
        f"{rep}_{nr}": 0
        for rep in range(1, 5)
        for nr in range(1, 6)
    }

    st.session_state.swc_rt = {
        f"{rep}_{nr}": 0
        for rep in range(1, 5)
        for nr in range(1, 6)
    }

    st.session_state.swc_heats = {
        f"{rep}_{nr}": []
        for rep in range(1, 5)
        for nr in range(1, 6)
    }

    st.session_state.swc_finished = False


if "swc_heat" not in st.session_state:

    reset_swc()


# ============================================================
# PROGRAM SWC
# ============================================================

# Każdy bieg ma po jednym zawodniku z każdej reprezentacji.
# W pierwszych 16 biegach program automatycznie rotuje
# zawodnikami 1-4.
# Nr 5 jest rezerwowym.
#
# Zasada w tym symulatorze:
# - 1-4 = podstawowi
# - 5 = rezerwowy
# - rezerwowy może wejść za zawodnika podstawowego
# - RT dostępne od biegu 3 do 16
# - biegi 17-20 bez RT
# - bez Z/Z

program_swc = []

for bieg in range(1, 21):

    obsada = {}

    for rep in range(1, 5):

        rider_nr = (
            ((bieg - 1 + rep - 1) % 4) + 1
        )

        obsada[rep] = rider_nr

    program_swc.append(obsada)


# ============================================================
# TRYB APLIKACJI
# ============================================================

tryb = st.sidebar.radio(
    "🏁 Tryb symulatora",
    [
        "🏟️ Mecz ligowy",
        "🏆 Zawody indywidualne",
        "🌍 Reprezentacje — SWC"
    ]
)


# ============================================================
# TRYB LIGOWY
# ============================================================

if tryb == "🏟️ Mecz ligowy":

    st.sidebar.header(
        "⚙️ Konfiguracja Meczu"
    )

    wybrany_gospodarz = st.sidebar.selectbox(
        "🏠 Gospodarz",
        kluby_lista,
        index=kluby_lista.index(
            st.session_state.gospodarz_biezacy
        ),
        key="gospodarz_biezacy"
    )

    wybrany_gosc = st.sidebar.selectbox(
        "✈️ Gość",
        kluby_lista,
        index=kluby_lista.index(
            st.session_state.gosc_biezacy
        ),
        key="gosc_biezacy"
    )

    pogoda_opcje = (
        POGODY
        + ["🎲 Losowa pogoda"]
    )

    wybrana_pogoda = st.sidebar.selectbox(
        "🌤️ Warunki atmosferyczne",
        pogoda_opcje
    )

    if wybrana_pogoda == "🎲 Losowa pogoda":

        if st.sidebar.button(
            "🎲 Wylosuj pogodę",
            use_container_width=True
        ):

            st.session_state.pogoda_ligowa = (
                losuj_pogode()
            )

            st.rerun()

        wybrana_pogoda = (
            st.session_state.pogoda_ligowa
        )

    else:

        st.session_state.pogoda_ligowa = (
            wybrana_pogoda
        )

    if (
        st.session_state.get("mecz_gospodarz")
        != wybrany_gospodarz
        or
        st.session_state.get("mecz_gosc")
        != wybrany_gosc
    ):

        st.session_state.mecz_gospodarz = (
            wybrany_gospodarz
        )

        st.session_state.mecz_gosc = (
            wybrany_gosc
        )

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

        reset_ligi()

        st.rerun()


    # ========================================================
    # TABY LIGOWE
    # ========================================================

    tab_kadry, tab_taktyka, tab_mecz = st.tabs([
        "👥 1. Wybór Drużyn i Kadry",
        "📣 2. Odprawa Taktyczna",
        "🏎️ 3. Centrum Meczowe"
    ])


    # ========================================================
    # KADRY
    # ========================================================

    with tab_kadry:

        st.header(
            f"Składy Meczowe: "
            f"{wybrany_gospodarz} vs "
            f"{wybrany_gosc}"
        )

        st.info(
            "✍️ Wpisz ręcznie imię i nazwisko oraz OVR. "
            "Nie ma gotowej bazy zawodników."
        )

        col_gosp, col_gosc = st.columns(2)


        with col_gosp:

            st.subheader(
                f"🏠 {wybrany_gospodarz}"
            )

            for nr in range(1, 9):

                if nr <= 5:
                    typ = "Senior / U24"

                elif nr <= 7:
                    typ = "Junior"

                else:
                    typ = "Rezerwa zwykła"

                st.markdown(
                    f"**Nr {nr} — {typ}**"
                )

                c1, c2 = st.columns([3, 1])

                with c1:

                    st.text_input(
                        f"Zawodnik nr {nr}",
                        key=f"manual_gosp_name_{nr}",
                        placeholder="Imię i nazwisko"
                    )

                    st.session_state.sklad_gospodarze[nr] = (
                        st.session_state[
                            f"manual_gosp_name_{nr}"
                        ]
                    )

                with c2:

                    st.number_input(
                        f"OVR {nr}",
                        min_value=1,
                        max_value=99,
                        value=60,
                        key=f"manual_gosp_ovr_{nr}"
                    )

                    st.session_state.sklad_gospodarze_ovr[nr] = (
                        st.session_state[
                            f"manual_gosp_ovr_{nr}"
                        ]
                    )


        with col_gosc:

            st.subheader(
                f"✈️ {wybrany_gosc}"
            )

            for nr in range(9, 17):

                if nr <= 13:
                    typ = "Senior / U24"

                elif nr <= 15:
                    typ = "Junior"

                else:
                    typ = "Rezerwa zwykła"

                st.markdown(
                    f"**Nr {nr} — {typ}**"
                )

                c1, c2 = st.columns([3, 1])

                with c1:

                    st.text_input(
                        f"Zawodnik nr {nr}",
                        key=f"manual_gosc_name_{nr}",
                        placeholder="Imię i nazwisko"
                    )

                    st.session_state.sklad_goscie[nr] = (
                        st.session_state[
                            f"manual_gosc_name_{nr}"
                        ]
                    )

                with c2:

                    st.number_input(
                        f"OVR {nr}",
                        min_value=1,
                        max_value=99,
                        value=60,
                        key=f"manual_gosc_ovr_{nr}"
                    )

                    st.session_state.sklad_goscie_ovr[nr] = (
                        st.session_state[
                            f"manual_gosc_ovr_{nr}"
                        ]
                    )


        st.divider()

        st.subheader(
            "🩹 Z/Z — Zastępstwo Zawodnika"
        )

        z1, z2 = st.columns(2)


        with z1:

            st.markdown(
                f"**🏠 {wybrany_gospodarz}**"
            )

            kand = [
                (
                    nr,
                    st.session_state.sklad_gospodarze.get(nr)
                )
                for nr in range(1, 6)
                if st.session_state.sklad_gospodarze.get(nr)
            ]

            if kand:

                wybor = st.selectbox(
                    "Zawodnik gospodarzy "
                    "zastępowany przez Z/Z",
                    ["Brak"]
                    + [
                        f"Nr {nr} - {nazwisko}"
                        for nr, nazwisko in kand
                    ],
                    key="zz_choice_gosp"
                )

                if wybor != "Brak":

                    nr = int(
                        wybor.split(" - ")[0]
                        .replace("Nr ", "")
                    )

                    st.session_state.zz_gosp = nr

                else:

                    st.session_state.zz_gosp = None

            else:

                st.info(
                    "Najpierw wpisz zawodników 1–5."
                )


        with z2:

            st.markdown(
                f"**✈️ {wybrany_gosc}**"
            )

            kand = [
                (
                    nr,
                    st.session_state.sklad_goscie.get(nr)
                )
                for nr in range(9, 14)
                if st.session_state.sklad_goscie.get(nr)
            ]

            if kand:

                wybor = st.selectbox(
                    "Zawodnik gości "
                    "zastępowany przez Z/Z",
                    ["Brak"]
                    + [
                        f"Nr {nr} - {nazwisko}"
                        for nr, nazwisko in kand
                    ],
                    key="zz_choice_gosc"
                )

                if wybor != "Brak":

                    nr = int(
                        wybor.split(" - ")[0]
                        .replace("Nr ", "")
                    )

                    st.session_state.zz_gosc = nr

                else:

                    st.session_state.zz_gosc = None

            else:

                st.info(
                    "Najpierw wpisz zawodników 9–13."
                )


    # ========================================================
    # TAKTYKA
    # ========================================================

    with tab_taktyka:

        st.title(
            "🛠️ Ustawienia Taktyczne Menedżerów"
        )

        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                f"🏠 {wybrany_gospodarz}"
            )

            st.selectbox(
                "📐 Przygotowanie Nawierzchni",
                [
                    "⚖️ Tor Neutralny",
                    "🧱 Tor Twardy",
                    "🚜 Tor Przyczepny"
                ],
                key="tor_gosp"
            )

            st.selectbox(
                "🔥 Styl Jazdy",
                [
                    "Standardowe nastawienie",
                    "Agresywne (większe ryzyko)",
                    "Defensywne (bezpieczne)"
                ],
                key="styl_gosp"
            )

            st.selectbox(
                "🔧 Sprzęt / Tuner",
                [
                    "🔧 Silnik Niezawodny (0% defektu)",
                    "🚀 Silnik Ekstra Mocny (+2 siły)"
                ],
                key="sprzet_gosp"
            )


        with col2:

            st.subheader(
                f"✈️ {wybrany_gosc}"
            )

            st.selectbox(
                "📐 Przygotowanie Nawierzchni",
                [
                    "⚖️ Tor Neutralny",
                    "🧱 Tor Twardy",
                    "🚜 Tor Przyczepny"
                ],
                key="tor_gosc"
            )

            st.selectbox(
                "🔥 Styl Jazdy",
                [
                    "Standardowe nastawienie",
                    "Agresywne (większe ryzyko)",
                    "Defensywne (bezpieczne)"
                ],
                key="styl_gosc"
            )

            st.selectbox(
                "🔧 Sprzęt / Tuner",
                [
                    "🔧 Silnik Niezawodny (0% defektu)",
                    "🚀 Silnik Ekstra Mocny (+2 siły)"
                ],
                key="sprzet_gosc"
            )


    # ========================================================
    # CENTRUM MECZOWE
    # ========================================================

    with tab_mecz:

        st.header(
            "🏎️ Panel Symulacji Meczowej"
        )

        if st.button(
            "🔄 Resetuj Mecz",
            use_container_width=True
        ):

            reset_ligi()

            st.rerun()


        st.markdown(
            f"### 📊 Aktualny Wynik: "
            f"{wybrany_gospodarz} **"
            f"{st.session_state.score_gosp} : "
            f"{st.session_state.score_gosc}"
            f"** {wybrany_gosc} | "
            f"Pogoda: {wybrana_pogoda}"
        )


        if (
            st.session_state.current_heat == 8
            and "Burza" in wybrana_pogoda
            and not st.session_state.decyzja_o_przerwaniu_podjeta
        ):

            st.warning(
                "⚠️ Burza! Sędzia wstrzymał zawody po 8. biegu."
            )

            a, b = st.columns(2)

            with a:

                if st.button(
                    "🔴 Przerwij mecz "
                    "i zalicz wynik"
                ):

                    st.session_state.mecz_przerwany = True

                    st.session_state.decyzja_o_przerwaniu_podjeta = True

                    st.rerun()

            with b:

                if st.button(
                    "🟢 Jedziemy dalej"
                ):

                    st.session_state.decyzja_o_przerwaniu_podjeta = True

                    st.rerun()


        if st.session_state.mecz_przerwany:

            st.error(
                f"🛑 MECZ PRZERWANY! "
                f"{wybrany_gospodarz} "
                f"{st.session_state.score_gosp}:"
                f"{st.session_state.score_gosc} "
                f"{wybrany_gosc}"
            )


        elif st.session_state.current_heat < 15:

            heat = program_zawodow[
                st.session_state.current_heat
            ]

            nr_b = heat["bieg"]

            st.divider()

            st.subheader(
                f"🚀 Bieg {nr_b} / 15"
            )


            roznica = (
                st.session_state.score_gosp
                - st.session_state.score_gosc
            )

            taktyczna_gosp = roznica <= -6
            taktyczna_gosc = roznica >= 6


            def get_pkt_sum(nr):

                suma = 0

                for wynik in st.session_state.rider_heats.get(
                    nr, []
                ):

                    if str(wynik).startswith("3"):
                        suma += 3

                    elif str(wynik).startswith("2"):
                        suma += 2

                    elif str(wynik).startswith("1"):
                        suma += 1

                return (
                    suma
                    + st.session_state.rider_bonuses.get(
                        nr,
                        0
                    )
                )


            def nr_jest_zz(nr):

                if nr <= 8:

                    return (
                        nr
                        == st.session_state.zz_gosp
                    )

                return (
                    nr
                    == st.session_state.zz_gosc
                )


            def moze_startowac(
                nr,
                bieg,
                jako_zz=False,
                jako_rt=False
            ):

                if nr in st.session_state.kontuzjowani:
                    return False

                normalne = (
                    st.session_state.normal_starts_count.get(
                        nr,
                        0
                    )
                )

                rt = (
                    st.session_state.rt_count.get(
                        nr,
                        0
                    )
                )

                zz = (
                    st.session_state.zz_count.get(
                        nr,
                        0
                    )
                )

                razem = (
                    normalne
                    + rt
                    + zz
                )

                if jako_zz:

                    return (
                        bieg != 2
                        and bieg <= 13
                        and zz < 1
                        and razem < 7
                    )

                if nr_jest_zz(nr):
                    return False

                if jako_rt:

                    return (
                        bieg >= 3
                        and bieg <= 13
                        and rt < 1
                        and razem < 7
                    )

                if bieg in [14, 15]:

                    return razem < 7

                return (
                    normalne < 5
                    and razem < 7
                )


            def opcje_gosp(
                prog_nr,
                wykluczone
            ):

                wynik = []

                if nr_jest_zz(prog_nr):

                    for nr in range(1, 9):

                        if (
                            nr != prog_nr
                            and nr not in wykluczone
                            and st.session_state.sklad_gospodarze.get(nr)
                            and moze_startowac(
                                nr,
                                nr_b,
                                jako_zz=True
                            )
                        ):

                            wynik.append(nr)

                    return wynik


                if nr_b in [14, 15]:

                    wynik = [
                        nr
                        for nr in range(1, 9)
                        if (
                            nr not in wykluczone
                            and st.session_state.sklad_gospodarze.get(nr)
                            and moze_startowac(
                                nr,
                                nr_b
                            )
                        )
                    ]

                    wynik.sort(
                        key=lambda x: (
                            x != prog_nr,
                            -get_pkt_sum(x)
                        )
                    )

                    return wynik


                if nr_b == 2:

                    for nr in [6, 7, 8]:

                        if (
                            nr not in wykluczone
                            and st.session_state.sklad_gospodarze.get(nr)
                            and moze_startowac(
                                nr,
                                nr_b
                            )
                        ):

                            wynik.append(nr)

                    return wynik


                if (
                    prog_nr not in wykluczone
                    and st.session_state.sklad_gospodarze.get(prog_nr)
                    and moze_startowac(
                        prog_nr,
                        nr_b
                    )
                ):

                    wynik.append(
                        prog_nr
                    )


                for nr in [8, 6, 7]:

                    if (
                        nr not in wynik
                        and nr not in wykluczone
                        and st.session_state.sklad_gospodarze.get(nr)
                        and moze_startowac(
                            nr,
                            nr_b
                        )
                    ):

                        wynik.append(
                            nr
                        )


                if taktyczna_gosp:

                    for nr in range(1, 6):

                        if (
                            nr not in wynik
                            and nr not in wykluczone
                            and st.session_state.sklad_gospodarze.get(nr)
                            and moze_startowac(
                                nr,
                                nr_b,
                                jako_rt=True
                            )
                        ):

                            wynik.append(
                                nr
                            )

                return wynik


            def opcje_gosc(
                prog_nr,
                wykluczone
            ):

                wynik = []

                if nr_jest_zz(prog_nr):

                    for nr in range(9, 17):

                        if (
                            nr != prog_nr
                            and nr not in wykluczone
                            and st.session_state.sklad_goscie.get(nr)
                            and moze_startowac(
                                nr,
                                nr_b,
                                jako_zz=True
                            )
                        ):

                            wynik.append(nr)

                    return wynik


                if nr_b in [14, 15]:

                    wynik = [
                        nr
                        for nr in range(9, 17)
                        if (
                            nr not in wykluczone
                            and st.session_state.sklad_goscie.get(nr)
                            and moze_startowac(
                                nr,
                                nr_b
                            )
                        )
                    ]

                    wynik.sort(
                        key=lambda x: (
                            x != prog_nr,
                            -get_pkt_sum(x)
                        )
                    )

                    return wynik


                if nr_b == 2:

                    for nr in [14, 15, 16]:

                        if (
                            nr not in wykluczone
                            and st.session_state.sklad_goscie.get(nr)
                            and moze_startowac(
                                nr,
                                nr_b
                            )
                        ):

                            wynik.append(
                                nr
                            )

                    return wynik


                if (
                    prog_nr not in wykluczone
                    and st.session_state.sklad_goscie.get(prog_nr)
                    and moze_startowac(
                        prog_nr,
                        nr_b
                    )
                ):

                    wynik.append(
                        prog_nr
                    )


                for nr in [16, 14, 15]:

                    if (
                        nr not in wynik
                        and nr not in wykluczone
                        and st.session_state.sklad_goscie.get(nr)
                        and moze_startowac(
                            nr,
                            nr_b
                        )
                    ):

                        wynik.append(
                            nr
                        )


                if taktyczna_gosc:

                    for nr in range(9, 14):

                        if (
                            nr not in wynik
                            and nr not in wykluczone
                            and st.session_state.sklad_goscie.get(nr)
                            and moze_startowac(
                                nr,
                                nr_b,
                                jako_rt=True
                            )
                        ):

                            wynik.append(
                                nr
                            )

                return wynik


            cols = st.columns(4)

            wybrane = []

            uczestnicy = {}


            for i, pole in enumerate(
                ["A", "B", "C", "D"]
            ):

                prog_nr = heat[pole]

                kask = heat["kaski"][pole]

                gospodarze = (
                    kask in ["🔴", "🔵"]
                )

                if gospodarze:

                    opcje = opcje_gosp(
                        prog_nr,
                        wybrane
                    )

                    sklad = (
                        st.session_state.sklad_gospodarze
                    )

                    ovr = (
                        st.session_state.sklad_gospodarze_ovr
                    )

                else:

                    opcje = opcje_gosc(
                        prog_nr,
                        wybrane
                    )

                    sklad = (
                        st.session_state.sklad_goscie
                    )

                    ovr = (
                        st.session_state.sklad_goscie_ovr
                    )


                with cols[i]:

                    if not opcje:

                        st.error(
                            f"Brak zawodnika dla pola {pole}."
                        )

                        st.stop()


                    def format_zawodnika(x):

                        return (
                            f"Nr {x} - "
                            f"{sklad[x]} "
                            f"(OVR: {ovr[x]})"
                        )


                    wybor = st.selectbox(
                        (
                            f"{kask} Pole {pole} "
                            f"(Program: Nr {prog_nr})"
                        ),
                        opcje,
                        format_func=format_zawodnika,
                        key=f"liga_heat_{nr_b}_{pole}"
                    )

                    wybrane.append(
                        wybor
                    )

                    czy_zz = nr_jest_zz(
                        prog_nr
                    )

                    czy_rt = (
                        not czy_zz
                        and wybor != prog_nr
                        and (
                            (
                                gospodarze
                                and wybor in range(1, 6)
                            )
                            or
                            (
                                not gospodarze
                                and wybor in range(9, 14)
                            )
                        )
                        and (
                            taktyczna_gosp
                            if gospodarze
                            else taktyczna_gosc
                        )
                        and nr_b not in [2, 14, 15]
                    )

                    uczestnicy[pole] = {
                        "nr": wybor,
                        "nazwisko": sklad[wybor],
                        "ovr": ovr[wybor],
                        "kask": kask,
                        "druzyna": (
                            "gosp"
                            if gospodarze
                            else "gosc"
                        ),
                        "czy_zz": czy_zz,
                        "czy_rt": czy_rt
                    }


            if st.button(
                "🏁 Jedź Bieg",
                use_container_width=True
            ):

                lista = list(
                    uczestnicy.values()
                )

                zdarzenia = []


                for u in lista:

                    nr = u["nr"]

                    if u["czy_zz"]:

                        st.session_state.zz_count[nr] += 1

                    elif u["czy_rt"]:

                        st.session_state.rt_count[nr] += 1

                    else:

                        st.session_state.normal_starts_count[nr] += 1

                    st.session_state.starts_count[nr] += 1


                for u in lista:

                    if u["druzyna"] == "gosp":

                        tor = st.session_state.get(
                            "tor_gosp",
                            "⚖️ Tor Neutralny"
                        )

                        styl = st.session_state.get(
                            "styl_gosp",
                            "Standardowe nastawienie"
                        )

                        sprzet = st.session_state.get(
                            "sprzet_gosp",
                            ""
                        )

                    else:

                        tor = st.session_state.get(
                            "tor_gosc",
                            "⚖️ Tor Neutralny"
                        )

                        styl = st.session_state.get(
                            "styl_gosc",
                            "Standardowe nastawienie"
                        )

                        sprzet = st.session_state.get(
                            "sprzet_gosc",
                            ""
                        )


                    if "Twardy" in tor:

                        typ_toru = "twardy"

                    elif "Przyczepny" in tor:

                        typ_toru = "przyczepny"

                    else:

                        typ_toru = "neutralny"


                    sila = sila_zawodnika(
                        u["ovr"],
                        typ_toru,
                        wybrana_pogoda
                    )


                    if "Agresywne" in styl:

                        sila += 1
                        szansa_defektu = 0.04

                    elif "Defensywne" in styl:

                        sila -= 0.5
                        szansa_defektu = 0.015

                    else:

                        szansa_defektu = 0.02


                    if "Ekstra Mocny" in sprzet:

                        sila += 2
                        szansa_defektu += 0.02


                    u["sila"] = sila

                    los = random.random()


                    if los < szansa_defektu:

                        u["wynik_litera"] = "D"

                        u["sila"] = -100

                        zdarzenia.append(
                            f"💨 Defekt sprzętu: "
                            f"{u['nazwisko']}!"
                        )


                    elif (
                        los
                        < szansa_defektu + 0.03
                    ):

                        u["wynik_litera"] = "U"

                        u["sila"] = -200

                        zdarzenia.append(
                            f"💥 Upadek: "
                            f"{u['nazwisko']}!"
                        )


                        if random.random() < 0.20:

                            st.session_state.kontuzjowani.add(
                                u["nr"]
                            )

                            zdarzenia.append(
                                f"🚑 {u['nazwisko']} "
                                f"niezdolny do dalszej jazdy!"
                            )


                    elif (
                        los
                        < szansa_defektu + 0.08
                    ):

                        u["wynik_litera"] = "W"

                        u["sila"] = -300

                        zdarzenia.append(
                            f"🚫 Wykluczenie: "
                            f"{u['nazwisko']}!"
                        )

                    else:

                        u["wynik_litera"] = None


                lista.sort(
                    key=lambda x: x["sila"],
                    reverse=True
                )


                sklasyfikowani = [
                    u for u in lista
                    if not u["wynik_litera"]
                ]

                niesklasyfikowani = [
                    u for u in lista
                    if u["wynik_litera"]
                ]


                punkty = [3, 2, 1, 0]

                wynik_g = 0
                wynik_go = 0


                for i, u in enumerate(
                    sklasyfikowani
                ):

                    pkt = (
                        punkty[i]
                        if i < len(punkty)
                        else 0
                    )

                    bonus = False


                    if pkt == 2:

                        if (
                            sklasyfikowani
                            and sklasyfikowani[0]["druzyna"]
                            == u["druzyna"]
                        ):

                            bonus = True


                    if pkt == 1:

                        if len(sklasyfikowani) >= 2:

                            if (
                                sklasyfikowani[0]["druzyna"]
                                == u["druzyna"]
                                or
                                sklasyfikowani[1]["druzyna"]
                                == u["druzyna"]
                            ):

                                bonus = True


                    zapis = (
                        f"{pkt}*"
                        if bonus
                        else str(pkt)
                    )


                    if bonus:

                        st.session_state.rider_bonuses[
                            u["nr"]
                        ] += 1


                    st.session_state.rider_heats[
                        u["nr"]
                    ].append(
                        zapis
                    )


                    if u["druzyna"] == "gosp":

                        wynik_g += pkt

                    else:

                        wynik_go += pkt


                for u in niesklasyfikowani:

                    st.session_state.rider_heats[
                        u["nr"]
                    ].append(
                        u["wynik_litera"]
                    )


                st.session_state.score_gosp += wynik_g
                st.session_state.score_gosc += wynik_go


                komentarz = komentarz_biegu(
                    sklasyfikowani,
                    zdarzenia
                )


                szczegoly = []


                for u in lista:

                    zapis = (
                        st.session_state.rider_heats[
                            u["nr"]
                        ][-1]
                    )

                    status = ""

                    if u["czy_zz"]:

                        status = " [Z/Z]"

                    elif u["czy_rt"]:

                        status = " [RT]"

                    szczegoly.append(
                        f"{u['nazwisko']} "
                        f"({u['kask']}) - "
                        f"{zapis}{status}"
                    )


                st.session_state.match_history.append({
                    "bieg": nr_b,
                    "wynik_biegu": (
                        f"{wynik_g}:{wynik_go}"
                    ),
                    "szczegoly": ", ".join(
                        szczegoly
                    ),
                    "komentarz": komentarz
                })


                st.session_state.current_heat += 1

                st.rerun()


        if st.session_state.current_heat >= 15:

            st.success(
                f"🏁 KONIEC MECZU! "
                f"{wybrany_gospodarz} "
                f"{st.session_state.score_gosp}:"
                f"{st.session_state.score_gosc} "
                f"{wybrany_gosc}"
            )


        if st.session_state.match_history:

            st.divider()

            st.subheader(
                "📜 Historia Biegów i Komentarz Live"
            )


            for hist in reversed(
                st.session_state.match_history
            ):

                with st.expander(
                    (
                        f"Bieg {hist['bieg']} | "
                        f"Wynik: {hist['wynik_biegu']}"
                    )
                ):

                    st.markdown(
                        f"**Kolejność na mecie:** "
                        f"{hist['szczegoly']}"
                    )

                    st.info(
                        f"🎙️ {hist['komentarz']}"
                    )


        st.divider()

        st.subheader(
            "📋 Tabela Punktowa Zawodników"
        )


        def tabela_ligi(
            sklad,
            gospodarze
        ):

            dane = []

            for nr, zawodnik in sklad.items():

                if not zawodnik:
                    continue

                biegi = (
                    st.session_state.rider_heats.get(
                        nr,
                        []
                    )
                )

                pkt = 0

                for x in biegi:

                    if str(x).startswith("3"):

                        pkt += 3

                    elif str(x).startswith("2"):

                        pkt += 2

                    elif str(x).startswith("1"):

                        pkt += 1

                bonus = (
                    st.session_state.rider_bonuses.get(
                        nr,
                        0
                    )
                )

                dane.append({

                    "Nr": nr,

                    "Zawodnik": zawodnik,

                    "OVR": pobierz_ovr(
                        nr,
                        gospodarze
                    ),

                    "Pkt": pkt,

                    "Bon": bonus,

                    "Razem":
                        f"{pkt}+{bonus}",

                    "Biegi":
                        ", ".join(
                            map(
                                str,
                                biegi
                            )
                        ),

                    "Starty":
                        len(biegi),

                    "Zwykłe":
                        st.session_state.normal_starts_count.get(
                            nr,
                            0
                        ),

                    "RT":
                        st.session_state.rt_count.get(
                            nr,
                            0
                        ),

                    "Z/Z":
                        st.session_state.zz_count.get(
                            nr,
                            0
                        )
                })

            return pd.DataFrame(dane)


        c1, c2 = st.columns(2)


        with c1:

            st.markdown(
                f"**🏠 {wybrany_gospodarz}**"
            )

            st.dataframe(
                tabela_ligi(
                    st.session_state.sklad_gospodarze,
                    True
                ),
                hide_index=True,
                use_container_width=True
            )


        with c2:

            st.markdown(
                f"**✈️ {wybrany_gosc}**"
            )

            st.dataframe(
                tabela_ligi(
                    st.session_state.sklad_goscie,
                    False
                ),
                hide_index=True,
                use_container_width=True
            )


        st.divider()

        st.subheader(
            "📄 Raport meczu"
        )


        raport = []

        raport.append(
            "========================================"
        )

        raport.append(
            "🏁 RAPORT MECZU ŻUŻLOWEGO"
        )

        raport.append(
            "========================================"
        )

        raport.append(
            f"Gospodarz: {wybrany_gospodarz}"
        )

        raport.append(
            f"Gość: {wybrany_gosc}"
        )

        raport.append(
            f"Pogoda: {wybrana_pogoda}"
        )

        raport.append("")

        raport.append(
            f"AKTUALNY WYNIK: "
            f"{st.session_state.score_gosp}:"
            f"{st.session_state.score_gosc}"
        )

        raport.append("")

        raport.append(
            "----------- BIEGI -----------"
        )


        for hist in st.session_state.match_history:

            raport.append(
                f"Bieg {hist['bieg']} | "
                f"Wynik: {hist['wynik_biegu']}"
            )

            raport.append(
                f"Kolejność na mecie: "
                f"{hist['szczegoly']}"
            )

            raport.append(
                f"Komentarz: "
                f"{hist['komentarz']}"
            )

            raport.append("")


        raport.append(
            "----------- PUNKTY -----------"
        )


        for sklad, gospodarze in [

            (
                st.session_state.sklad_gospodarze,
                True
            ),

            (
                st.session_state.sklad_goscie,
                False
            )
        ]:

            for nr, zawodnik in sklad.items():

                if not zawodnik:
                    continue

                biegi = (
                    st.session_state.rider_heats.get(
                        nr,
                        []
                    )
                )

                pkt = 0

                for x in biegi:

                    if str(x).startswith("3"):
                        pkt += 3

                    elif str(x).startswith("2"):
                        pkt += 2

                    elif str(x).startswith("1"):
                        pkt += 1

                bonus = (
                    st.session_state.rider_bonuses.get(
                        nr,
                        0
                    )
                )

                raport.append(
                    f"Nr {nr} | {zawodnik} | "
                    f"OVR {pobierz_ovr(nr, gospodarze)} | "
                    f"{pkt}+{bonus} | "
                    f"Biegi: "
                    f"{', '.join(map(str, biegi))}"
                )


        raport_text = "\n".join(
            raport
        )


        st.download_button(
            "📥 Pobierz raport meczu TXT",
            raport_text,
            file_name="raport_meczu.txt",
            mime="text/plain",
            use_container_width=True
        )


        st.text_area(
            "📋 Cały raport do skopiowania",
            raport_text,
            height=350
        )


# ============================================================
# TRYB ZAWODÓW INDYWIDUALNYCH
# ============================================================

elif tryb == "🏆 Zawody indywidualne":

    st.sidebar.header(
        "🏆 Zawody Indywidualne"
    )

    format_turnieju = st.sidebar.selectbox(
        "Format zawodów",
        [
            "🏆 SGP",
            "🇵🇱 IMP",
            "🥇 Złoty Kask"
        ]
    )


    if format_turnieju == "🏆 SGP":

        nazwa_turnieju = "SGP"

    elif format_turnieju == "🇵🇱 IMP":

        nazwa_turnieju = "IMP"

    else:

        nazwa_turnieju = "Złoty Kask"


    if (
        st.session_state.get("ostatni_format_ind")
        != format_turnieju
    ):

        st.session_state.ostatni_format_ind = (
            format_turnieju
        )

        reset_indywidualne()


    tab_ind_kadra, tab_ind_mecz, tab_ind_tabela = (
        st.tabs([
            "👥 Zawodnicy",
            "🏎️ Centrum Zawodów",
            "📊 Klasyfikacja"
        ])
    )


    with tab_ind_kadra:

        st.header(
            f"{nazwa_turnieju} — Lista zawodników"
        )

        st.info(
            "Wpisz 20 zawodników."
        )

        for nr in range(1, 21):

            st.markdown(
                f"### Nr {nr}"
            )

            c1, c2, c3, c4 = st.columns(
                [3, 1, 1, 1]
            )


            with c1:

                st.text_input(
                    "Imię i nazwisko",
                    key=f"ind_name_{nr}",
                    placeholder="np. Bartosz Zmarzlik"
                )


            with c2:

                st.number_input(
                    "OVR",
                    min_value=1,
                    max_value=99,
                    value=60,
                    key=f"ind_ovr_{nr}"
                )


            with c3:

                st.selectbox(
                    "Kraj",
                    [
                        "🇵🇱 Polska",
                        "🇩🇰 Dania",
                        "🇸🇪 Szwecja",
                        "🇬🇧 Wielka Brytania",
                        "🇦🇺 Australia",
                        "🇱🇻 Łotwa",
                        "🇫🇮 Finlandia",
                        "🇳🇴 Norwegia",
                        "🇨🇿 Czechy",
                        "🇩🇪 Niemcy",
                        "🇺🇦 Ukraina",
                        "Inny"
                    ],
                    key=f"ind_kraj_{nr}"
                )


            with c4:

                st.checkbox(
                    "U24",
                    key=f"ind_u24_{nr}"
                )


        st.divider()

        st.info(
            "Losowanie zawodników pozostawione wyłączone."
        )


    def zawodnicy_ind():

        wynik = []

        for nr in range(1, 21):

            nazwa = st.session_state.get(
                f"ind_name_{nr}",
                ""
            )

            if not nazwa:
                continue

            wynik.append({
                "nr": nr,
                "nazwisko": nazwa,
                "ovr": st.session_state.get(
                    f"ind_ovr_{nr}",
                    60
                ),
                "kraj": st.session_state.get(
                    f"ind_kraj_{nr}",
                    "🇵🇱 Polska"
                ),
                "u24": st.session_state.get(
                    f"ind_u24_{nr}",
                    False
                )
            })

        return wynik


    def program_indywidualny():

        program = []

        for bieg in range(1, 21):

            grupa = []

            start = (
                ((bieg - 1) % 5) + 1
            )

            for j in range(4):

                nr = (
                    (
                        start
                        - 1
                        + j * 5
                        + (bieg - 1) // 5
                    )
                    % 20
                ) + 1

                grupa.append(nr)

            grupa = list(
                dict.fromkeys(
                    grupa
                )
            )

            while len(grupa) < 4:

                kand = random.randint(
                    1,
                    20
                )

                if kand not in grupa:

                    grupa.append(
                        kand
                    )

            program.append(
                grupa[:4]
            )

        return program


    if "ind_program" not in st.session_state:

        st.session_state.ind_program = (
            program_indywidualny()
        )


    with tab_ind_mecz:

        zawodnicy = zawodnicy_ind()


        if len(zawodnicy) < 4:

            st.warning(
                "Wpisz co najmniej 4 zawodników."
            )

        else:

            st.header(
                f"🏁 {nazwa_turnieju}"
            )

            if st.button(
                "🔄 Resetuj zawody",
                use_container_width=True
            ):

                reset_indywidualne()

                st.session_state.ind_program = (
                    program_indywidualny()
                )

                st.rerun()


            if (
                st.session_state.ind_current_heat
                < 20
            ):

                nr_biegu = (
                    st.session_state.ind_current_heat
                    + 1
                )

                uczestnicy_programowi = (
                    st.session_state.ind_program[
                        st.session_state.ind_current_heat
                    ]
                )

                st.divider()

                st.subheader(
                    f"🚀 Bieg {nr_biegu} / 20"
                )

                opcje = []

                for nr in uczestnicy_programowi:

                    zawodnik = next(
                        (
                            x
                            for x in zawodnicy
                            if x["nr"] == nr
                        ),
                        None
                    )

                    if zawodnik:

                        opcje.append(
                            zawodnik
                        )


                cols = st.columns(4)

                wybrane_ind = []


                for i, zawodnik in enumerate(
                    opcje
                ):

                    with cols[i]:

                        st.markdown(
                            f"**{KASKI[i]} "
                            f"Nr {zawodnik['nr']}**"
                        )

                        st.markdown(
                            zawodnik["nazwisko"]
                        )

                        st.caption(
                            f"{zawodnik['kraj']} | "
                            f"OVR {zawodnik['ovr']}"
                        )

                        wybrane_ind.append(
                            zawodnik
                        )


                if len(wybrane_ind) == 4:

                    if st.button(
                        "🏁 Jedź Bieg",
                        use_container_width=True
                    ):

                        wyniki = []

                        zdarzenia = []


                        for u in wybrane_ind:

                            sila = sila_zawodnika(
                                u["ovr"],
                                "neutralny",
                                "☀️"
                            )

                            u2 = dict(u)

                            u2["sila"] = sila

                            u2["wynik_litera"] = None

                            los = random.random()


                            if los < 0.02:

                                u2["wynik_litera"] = "D"
                                u2["sila"] = -100

                            elif los < 0.05:

                                u2["wynik_litera"] = "U"
                                u2["sila"] = -200

                            elif los < 0.08:

                                u2["wynik_litera"] = "W"
                                u2["sila"] = -300

                            wyniki.append(
                                u2
                            )


                        wyniki.sort(
                            key=lambda x: x["sila"],
                            reverse=True
                        )


                        sklasyfikowani = [
                            x
                            for x in wyniki
                            if not x["wynik_litera"]
                        ]

                        niesklasyfikowani = [
                            x
                            for x in wyniki
                            if x["wynik_litera"]
                        ]

                        punkty = [
                            3,
                            2,
                            1,
                            0
                        ]


                        for i, u in enumerate(
                            sklasyfikowani
                        ):

                            pkt = (
                                punkty[i]
                                if i < 4
                                else 0
                            )

                            st.session_state.ind_points[
                                u["nr"]
                            ] += pkt

                            st.session_state.ind_heats[
                                u["nr"]
                            ].append(
                                str(pkt)
                            )


                        for u in niesklasyfikowani:

                            st.session_state.ind_heats[
                                u["nr"]
                            ].append(
                                u["wynik_litera"]
                            )

                            if (
                                u["wynik_litera"]
                                == "D"
                            ):

                                zdarzenia.append(
                                    f"💨 Defekt sprzętu: "
                                    f"{u['nazwisko']}!"
                                )

                            elif (
                                u["wynik_litera"]
                                == "U"
                            ):

                                zdarzenia.append(
                                    f"💥 Upadek: "
                                    f"{u['nazwisko']}!"
                                )

                            elif (
                                u["wynik_litera"]
                                == "W"
                            ):

                                zdarzenia.append(
                                    f"🚫 Wykluczenie: "
                                    f"{u['nazwisko']}!"
                                )


                        szczegoly = []

                        for i, u in enumerate(
                            wyniki
                        ):

                            if u["wynik_litera"]:

                                zapis = (
                                    u["wynik_litera"]
                                )

                            else:

                                index = (
                                    sklasyfikowani.index(
                                        u
                                    )
                                )

                                zapis = str(
                                    punkty[index]
                                )

                            szczegoly.append(
                                f"{u['nazwisko']} "
                                f"({KASKI[i]}) - "
                                f"{zapis}"
                            )


                        komentarz = (
                            komentarz_biegu(
                                [
                                    {
                                        "nazwisko":
                                            u["nazwisko"],
                                        "sila":
                                            u["sila"],
                                        "druzyna":
                                            "ind"
                                    }
                                    for u
                                    in sklasyfikowani
                                ],
                                zdarzenia
                            )
                        )


                        st.session_state.ind_history.append(
                            {
                                "bieg":
                                    nr_biegu,

                                "wynik_biegu":
                                    "IND",

                                "szczegoly":
                                    ", ".join(
                                        szczegoly
                                    ),

                                "komentarz":
                                    komentarz
                            }
                        )


                        st.session_state.ind_current_heat += 1

                        st.rerun()


            elif (
                st.session_state.ind_current_heat == 20
                and not st.session_state.ind_finished
            ):

                st.subheader(
                    "🏆 Półfinał / Finał"
                )

                ranking = sorted(
                    zawodnicy,
                    key=lambda x: (
                        st.session_state.ind_points.get(
                            x["nr"],
                            0
                        )
                    ),
                    reverse=True
                )


                if st.button(
                    "🏁 Rozegraj fazę finałową",
                    use_container_width=True
                ):

                    finalisci = ranking[:4]

                    final_wyniki = []

                    for x in finalisci:

                        sila = sila_zawodnika(
                            x["ovr"],
                            "neutralny",
                            ""
                        )

                        final_wyniki.append(
                            (
                                x,
                                sila
                            )
                        )

                    final_wyniki.sort(
                        key=lambda x: x[1],
                        reverse=True
                    )


                    for i, element in enumerate(
                        final_wyniki
                    ):

                        zawodnik = element[0]

                        punkty_finalu = [
                            6,
                            4,
                            2,
                            0
                        ][i]

                        st.session_state.ind_points[
                            zawodnik["nr"]
                        ] += punkty_finalu


                    st.session_state.ind_final_result = (
                        final_wyniki
                    )

                    st.session_state.ind_finished = True

                    st.rerun()


            if st.session_state.ind_finished:

                st.success(
                    f"🏆 KONIEC {nazwa_turnieju}!"
                )

                final = (
                    st.session_state.get(
                        "ind_final_result",
                        []
                    )
                )

                for i, element in enumerate(
                    final
                ):

                    zawodnik = element[0]

                    medal = [
                        "🥇",
                        "🥈",
                        "🥉",
                        "4️⃣"
                    ][i]

                    st.markdown(
                        f"### {medal} "
                        f"{zawodnik['nazwisko']}"
                    )

                    st.write(
                        f"{zawodnik['kraj']} | "
                        f"OVR {zawodnik['ovr']} | "
                        f"Łącznie: "
                        f"{st.session_state.ind_points[zawodnik['nr']]} pkt"
                    )


            if st.session_state.ind_history:

                st.divider()

                st.subheader(
                    "📜 Historia biegów"
                )

                for hist in reversed(
                    st.session_state.ind_history
                ):

                    with st.expander(
                        f"Bieg {hist['bieg']}"
                    ):

                        st.markdown(
                            f"**Kolejność na mecie:** "
                            f"{hist['szczegoly']}"
                        )

                        st.info(
                            f"🎙️ {hist['komentarz']}"
                        )


    with tab_ind_tabela:

        st.header
