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
# PROGRAM MECZU LIGOWEGO
# ============================================================

program_zawodow = [
    {
        "bieg": 1,
        "A": 1, "B": 9, "C": 3, "D": 11,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },
    {
        "bieg": 2,
        "A": 6, "B": 14, "C": 7, "D": 15,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },
    {
        "bieg": 3,
        "A": 10, "B": 2, "C": 12, "D": 4,
        "kaski": {
            "A": "⚪",
            "B": "🔴",
            "C": "🟡",
            "D": "🔵"
        }
    },
    {
        "bieg": 4,
        "A": 13, "B": 5, "C": 14, "D": 6,
        "kaski": {
            "A": "⚪",
            "B": "🔴",
            "C": "🟡",
            "D": "🔵"
        }
    },
    {
        "bieg": 5,
        "A": 3, "B": 9, "C": 4, "D": 10,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },
    {
        "bieg": 6,
        "A": 11, "B": 1, "C": 12, "D": 7,
        "kaski": {
            "A": "⚪",
            "B": "🔴",
            "C": "🟡",
            "D": "🔵"
        }
    },
    {
        "bieg": 7,
        "A": 2, "B": 13, "C": 5, "D": 15,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },
    {
        "bieg": 8,
        "A": 10, "B": 4, "C": 11, "D": 6,
        "kaski": {
            "A": "⚪",
            "B": "🔴",
            "C": "🟡",
            "D": "🔵"
        }
    },
    {
        "bieg": 9,
        "A": 1, "B": 9, "C": 2, "D": 12,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },
    {
        "bieg": 10,
        "A": 14, "B": 3, "C": 13, "D": 5,
        "kaski": {
            "A": "⚪",
            "B": "🔴",
            "C": "🟡",
            "D": "🔵"
        }
    },
    {
        "bieg": 11,
        "A": 4, "B": 13, "C": 1, "D": 9,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },
    {
        "bieg": 12,
        "A": 15, "B": 7, "C": 10, "D": 3,
        "kaski": {
            "A": "⚪",
            "B": "🔴",
            "C": "🟡",
            "D": "🔵"
        }
    },
    {
        "bieg": 13,
        "A": 5, "B": 11, "C": 2, "D": 12,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },
    {
        "bieg": 14,
        "A": 3, "B": 11, "C": 4, "D": 12,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },
    {
        "bieg": 15,
        "A": 1, "B": 9, "C": 2, "D": 10,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
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
    elif "Deszcz" in pogoda:
        sila -= 1
    elif "Burza" in pogoda:
        sila -= 2

    sila += random.uniform(-losowy, losowy)

    return sila


def komentarz_biegu(uczestnicy, zdarzenia):

    if zdarzenia:
        tekst = " ".join(zdarzenia)

        return random.choice([
            f"Niesamowite zamieszanie na torze. {tekst}",
            f"Sędzia przerywa bieg! {tekst}",
            f"Na torze dzieje się bardzo dużo! {tekst}",
            f"Co za dramatyczne wydarzenia! {tekst}"
        ])

    if not uczestnicy:
        return "Bieg bez historii — nikt nie dojechał do mety."

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
            f"🔥 Pojedynek parowy perfekcyjny! {zwyciezca} i {drugi} wystrzelili spod taśmy i nie dali rywalom szans.",
            f"🚀 Para jak z żelaza! {zwyciezca} prowadził bieg, a {drugi} skutecznie blokował rywali.",
            f"💥 Nokaut! Pokaz jazdy parą w wykonaniu duetu {zwyciezca} - {drugi}."
        ])

    if (
        drugi
        and trzeci
        and uczestnicy[0]["druzyna"] != uczestnicy[1]["druzyna"]
        and uczestnicy[1]["druzyna"] == uczestnicy[2]["druzyna"]
    ):
        return random.choice([
            f"⚖️ Remis po twardej walce! {zwyciezca} wygrywa bieg, ale {drugi} i {trzeci} dowożą punkty.",
            f"🎯 Samotny jastrząb! {zwyciezca} uciekł rywalom, a para {drugi}, {trzeci} kontrolowała dalsze pozycje."
        ])

    if drugi and roznica < 1.5:
        return random.choice([
            f"😱 NIESAMOWITE! {zwyciezca} wyprzedza zawodnika {drugi} dosłownie na kresce!",
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
# RESET MECZU LIGOWEGO
# ============================================================

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
        st.session_state.gospodarz_biezacy = kluby_lista[0]

    if "gosc_biezacy" not in st.session_state:
        st.session_state.gosc_biezacy = kluby_lista[1]

    if "pogoda_ligowa" not in st.session_state:
        st.session_state.pogoda_ligowa = POGODY[0]

    if "current_heat" not in st.session_state:
        reset_ligi()


inicjalizuj_lige()


# ============================================================
# RESET ZAWODÓW INDYWIDUALNYCH
# ============================================================

def reset_indywidualne():

    st.session_state.ind_current_heat = 0

    st.session_state.ind_history = []

    st.session_state.ind_points = {
        nr: 0 for nr in range(1, 21)
    }

    st.session_state.ind_heats = {
        nr: [] for nr in range(1, 21)
    }

    st.session_state.ind_finished = False

    st.session_state.ind_final_result = []


if "ind_current_heat" not in st.session_state:
    reset_indywidualne()


# ============================================================
# RESET SWC
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

    st.session_state.swc_winner = None


if "swc_heat" not in st.session_state:
    reset_swc()


# ============================================================
# PROGRAM SWC
# ============================================================

program_swc = []

for bieg in range(1, 21):

    obsada = {}

    for rep in range(1, 5):

        obsada[rep] = (
            ((bieg - 1 + rep - 1) % 4) + 1
        )

    program_swc.append(obsada)


# ============================================================
# TRYB SYMULATORA
# ============================================================

tryb = st.sidebar.radio(
    "🏁 Tryb symulatora",
    [
        "🏟️ Mecz ligowy",
        "🏆 Zawody indywidualne",
        "🌍 Reprezentacje — SWC"
    ],
    key="glowny_tryb"
)


# ============================================================
# TRYB MECZU LIGOWEGO
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

    wybrana_pogoda = st.sidebar.selectbox(
        "🌤️ Warunki atmosferyczne",
        POGODY + ["🎲 Losowa pogoda"],
        key="liga_pogoda"
    )

    if wybrana_pogoda == "🎲 Losowa pogoda":

        if st.sidebar.button(
            "🎲 Wylosuj pogodę",
            use_container_width=True,
            key="liga_losuj_pogode"
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


    # --------------------------------------------------------
    # ZMIANA DRUŻYN = NOWY MECZ
    # --------------------------------------------------------

    if (
        st.session_state.get(
            "mecz_gospodarz"
        ) != wybrany_gospodarz
        or
        st.session_state.get(
            "mecz_gosc"
        ) != wybrany_gosc
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

        # usuwamy stare widgety składów
        for nr in range(1, 9):
            st.session_state.pop(
                f"manual_gosp_name_{nr}",
                None
            )
            st.session_state.pop(
                f"manual_gosp_ovr_{nr}",
                None
            )

        for nr in range(9, 17):
            st.session_state.pop(
                f"manual_gosc_name_{nr}",
                None
            )
            st.session_state.pop(
                f"manual_gosc_ovr_{nr}",
                None
            )

        reset_ligi()

        st.rerun()


    # --------------------------------------------------------
    # TABY LIGOWE
    # --------------------------------------------------------

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
            f"{wybrany_gospodarz} vs {wybrany_gosc}"
        )

        st.info(
            "✍️ Wpisz ręcznie imię i nazwisko oraz OVR."
        )

        col_gosp, col_gosc = st.columns(2)


        # ----------------------------------------------------
        # GOSPODARZ
        # ----------------------------------------------------

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

                    name_key = (
                        f"manual_gosp_name_{nr}"
                    )

                    if name_key not in st.session_state:

                        st.session_state[name_key] = (
                            st.session_state.sklad_gospodarze.get(
                                nr,
                                ""
                            )
                        )

                    st.text_input(
                        f"Zawodnik nr {nr}",
                        key=name_key,
                        placeholder="Imię i nazwisko"
                    )

                    st.session_state.sklad_gospodarze[
                        nr
                    ] = st.session_state[name_key]


                with c2:

                    ovr_key = (
                        f"manual_gosp_ovr_{nr}"
                    )

                    if ovr_key not in st.session_state:

                        st.session_state[ovr_key] = 60

                    st.number_input(
                        f"OVR {nr}",
                        min_value=1,
                        max_value=99,
                        step=1,
                        key=ovr_key
                    )

                    st.session_state.sklad_gospodarze_ovr[
                        nr
                    ] = st.session_state[ovr_key]


        # ----------------------------------------------------
        # GOŚĆ
        # ----------------------------------------------------

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

                    name_key = (
                        f"manual_gosc_name_{nr}"
                    )

                    if name_key not in st.session_state:

                        st.session_state[name_key] = (
                            st.session_state.sklad_goscie.get(
                                nr,
                                ""
                            )
                        )

                    st.text_input(
                        f"Zawodnik nr {nr}",
                        key=name_key,
                        placeholder="Imię i nazwisko"
                    )

                    st.session_state.sklad_goscie[
                        nr
                    ] = st.session_state[name_key]


                with c2:

                    ovr_key = (
                        f"manual_gosc_ovr_{nr}"
                    )

                    if ovr_key not in st.session_state:

                        st.session_state[ovr_key] = 60

                    st.number_input(
                        f"OVR {nr}",
                        min_value=1,
                        max_value=99,
                        step=1,
                        key=ovr_key
                    )

                    st.session_state.sklad_goscie_ovr[
                        nr
                    ] = st.session_state[ovr_key]


        # ----------------------------------------------------
        # Z/Z
        # ----------------------------------------------------

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
                    st.session_state.sklad_gospodarze.get(
                        nr
                    )
                )
                for nr in range(1, 6)
                if st.session_state.sklad_gospodarze.get(
                    nr
                )
            ]

            if kand:

                wybor = st.selectbox(
                    "Zawodnik gospodarzy zastępowany przez Z/Z",
                    ["Brak"] + [
                        f"Nr {nr} - {nazwisko}"
                        for nr, nazwisko in kand
                    ],
                    key="zz_choice_gosp"
                )

                if wybor == "Brak":

                    st.session_state.zz_gosp = (
                        None
                    )

                else:

                    st.session_state.zz_gosp = int(
                        wybor
                        .split(" - ")[0]
                        .replace("Nr ", "")
                    )

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
                    st.session_state.sklad_goscie.get(
                        nr
                    )
                )
                for nr in range(9, 14)
                if st.session_state.sklad_goscie.get(
                    nr
                )
            ]

            if kand:

                wybor = st.selectbox(
                    "Zawodnik gości zastępowany przez Z/Z",
                    ["Brak"] + [
                        f"Nr {nr} - {nazwisko}"
                        for nr, nazwisko in kand
                    ],
                    key="zz_choice_gosc"
                )

                if wybor == "Brak":

                    st.session_state.zz_gosc = (
                        None
                    )

                else:

                    st.session_state.zz_gosc = int(
                        wybor
                        .split(" - ")[0]
                        .replace("Nr ", "")
                    )

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
            use_container_width=True,
            key="reset_mecz_liga"
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


        # ----------------------------------------------------
        # BURZA
        # ----------------------------------------------------

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
                    "🔴 Przerwij mecz i zalicz wynik",
                    key="liga_przerwij"
                ):

                    st.session_state.mecz_przerwany = (
                        True
                    )

                    st.session_state.decyzja_o_przerwaniu_podjeta = (
                        True
                    )

                    st.rerun()


            with b:

                if st.button(
                    "🟢 Jedziemy dalej",
                    key="liga_jedziemy"
                ):

                    st.session_state.decyzja_o_przerwaniu_podjeta = (
                        True
                    )

                    st.rerun()


        # ----------------------------------------------------
        # MECZ PRZERWANY
        # ----------------------------------------------------

        if st.session_state.mecz_przerwany:

            st.error(
                f"🛑 MECZ PRZERWANY! "
                f"{wybrany_gospodarz} "
                f"{st.session_state.score_gosp}:"
                f"{st.session_state.score_gosc} "
                f"{wybrany_gosc}"
            )


        # ----------------------------------------------------
        # BIEGI
        # ----------------------------------------------------

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

            taktyczna_gosp = (
                roznica <= -6
            )

            taktyczna_gosc = (
                roznica >= 6
            )


            # ------------------------------------------------
            # SUMA PUNKTÓW
            # ------------------------------------------------

            def get_pkt_sum(nr):

                suma = 0

                for wynik in (
                    st.session_state.rider_heats.get(
                        nr,
                        []
                    )
                ):

                    tekst = str(wynik)

                    if tekst.startswith("3"):
                        suma += 3

                    elif tekst.startswith("2"):
                        suma += 2

                    elif tekst.startswith("1"):
                        suma += 1

                return (
                    suma
                    + st.session_state.rider_bonuses.get(
                        nr,
                        0
                    )
                )


            # ------------------------------------------------
            # Z/Z
            # ------------------------------------------------

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


            # ------------------------------------------------
            # LIMIT STARTÓW
            # ------------------------------------------------

            def moze_startowac(
                nr,
                bieg,
                jako_zz=False,
                jako_rt=False
            ):

                if (
                    nr
                    in st.session_state.kontuzjowani
                ):
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

                    return (
                        razem < 7
                    )


                return (
                    normalne < 5
                    and razem < 7
                )


            # ------------------------------------------------
            # OPCJE GOSPODARZA
            # ------------------------------------------------

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
                            and st.session_state.sklad_gospodarze.get(
                                nr
                            )
                            and moze_startowac(
                                nr,
                                nr_b,
                                jako_zz=True
                            )
                        ):

                            wynik.append(
                                nr
                            )

                    return wynik


                if nr_b in [14, 15]:

                    wynik = [
                        nr
                        for nr in range(1, 9)
                        if (
                            nr not in wykluczone
                            and st.session_state.sklad_gospodarze.get(
                                nr
                            )
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
                            and st.session_state.sklad_gospodarze.get(
                                nr
                            )
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
                    and st.session_state.sklad_gospodarze.get(
                        prog_nr
                    )
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
                        and st.session_state.sklad_gospodarze.get(
                            nr
                        )
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
                            and st.session_state.sklad_gospodarze.get(
                                nr
                            )
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


            # ------------------------------------------------
            # OPCJE GOŚCIA
            # ------------------------------------------------

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
                            and st.session_state.sklad_goscie.get(
                                nr
                            )
                            and moze_startowac(
                                nr,
                                nr_b,
                                jako_zz=True
                            )
                        ):

                            wynik.append(
                                nr
                            )

                    return wynik


                if nr_b in [14, 15]:

                    wynik = [
                        nr
                        for nr in range(9, 17)
                        if (
                            nr not in wykluczone
                            and st.session_state.sklad_goscie.get(
                                nr
                            )
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
                            and st.session_state.sklad_goscie.get(
                                nr
                            )
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
                    and st.session_state.sklad_goscie.get(
                        prog_nr
                    )
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
                        and st.session_state.sklad_goscie.get(
                            nr
                        )
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
                            and st.session_state.sklad_goscie.get(
                                nr
                            )
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


            # ------------------------------------------------
            # WYBÓR 4 ZAWODNIKÓW
            # ------------------------------------------------

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


                    def format_zawodnika(
                        x,
                        sklad=sklad,
                        ovr=ovr
                    ):

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
                        key=(
                            f"liga_heat_{nr_b}_{pole}"
                        )
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
                            or (
                                not gospodarze
                                and wybor in range(9, 14)
                            )
                        )
                        and (
                            taktyczna_gosp
                            if gospodarze
                            else taktyczna_gosc
                        )
                        and nr_b not in [
                            2,
                            14,
                            15
                        ]
                    )


                    uczestnicy[pole] = {

                        "nr":
                            wybor,

                        "nazwisko":
                            sklad[wybor],

                        "ovr":
                            ovr[wybor],

                        "kask":
                            kask,

                        "druzyna":
                            (
                                "gosp"
                                if gospodarze
                                else "gosc"
                            ),

                        "czy_zz":
                            czy_zz,

                        "czy_rt":
                            czy_rt
                    }


            # ------------------------------------------------
            # JEDŹ BIEG
            # ------------------------------------------------

            if st.button(
                "🏁 Jedź Bieg",
                use_container_width=True,
                key=f"liga_jedz_{nr_b}"
            ):

                lista = list(
                    uczestnicy.values()
                )

                zdarzenia = []


                # --------------------------------------------
                # RODZAJ STARTU
                # --------------------------------------------

                for u in lista:

                    nr = u["nr"]

                    if u["czy_zz"]:

                        st.session_state.zz_count[
                            nr
                        ] += 1

                    elif u["czy_rt"]:

                        st.session_state.rt_count[
                            nr
                        ] += 1

                    else:

                        st.session_state.normal_starts_count[
                            nr
                        ] += 1


                    st.session_state.starts_count[
                        nr
                    ] += 1


                # --------------------------------------------
                # SIŁA
                # --------------------------------------------

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


                    elif los < (
                        szansa_defektu + 0.03
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


                    elif los < (
                        szansa_defektu + 0.08
                    ):

                        u["wynik_litera"] = "W"

                        u["sila"] = -300

                        zdarzenia.append(
                            f"🚫 Wykluczenie: "
                            f"{u['nazwisko']}!"
                        )


                    else:

                        u["wynik_litera"] = None


                # --------------------------------------------
                # KLASYFIKACJA
                # --------------------------------------------

                lista.sort(
                    key=lambda x: x["sila"],
                    reverse=True
                )


                sklasyfikowani = [
                    u
                    for u in lista
                    if not u["wynik_litera"]
                ]


                niesklasyfikowani = [
                    u
                    for u in lista
                    if u["wynik_litera"]
                ]


                punkty = [
                    3,
                    2,
                    1,
                    0
                ]


                wynik_g = 0

                wynik_go = 0


                # --------------------------------------------
                # PUNKTY
                # --------------------------------------------

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
                            and
                            sklasyfikowani[0][
                                "druzyna"
                            ]
                            == u["druzyna"]
                        ):

                            bonus = True


                    if pkt == 1:

                        if len(sklasyfikowani) >= 2:

                            if (
                                sklasyfikowani[0][
                                    "druzyna"
                                ]
                                == u["druzyna"]
                                or
                                sklasyfikowani[1][
                                    "druzyna"
                                ]
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


                # --------------------------------------------
                # D/U/W
                # --------------------------------------------

                for u in niesklasyfikowani:

                    st.session_state.rider_heats[
                        u["nr"]
                    ].append(
                        u["wynik_litera"]
                    )


                st.session_state.score_gosp += (
                    wynik_g
                )

                st.session_state.score_gosc += (
                    wynik_go
                )


                komentarz = komentarz_biegu(
                    sklasyfikowani,
                    zdarzenia
                )


                # --------------------------------------------
                # HISTORIA
                # --------------------------------------------

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

                    "bieg":
                        nr_b,

                    "wynik_biegu":
                        f"{wynik_g}:{wynik_go}",

                    "szczegoly":
                        ", ".join(
                            szczegoly
                        ),

                    "komentarz":
                        komentarz
                })


                st.session_state.current_heat += 1

                st.rerun()


        # ----------------------------------------------------
        # KONIEC
        # ----------------------------------------------------

        if st.session_state.current_heat >= 15:

            st.success(
                f"🏁 KONIEC MECZU! "
                f"{wybrany_gospodarz} "
                f"{st.session_state.score_gosp}:"
                f"{st.session_state.score_gosc} "
                f"{wybrany_gosc}"
            )


        # ----------------------------------------------------
        # HISTORIA
        # ----------------------------------------------------

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


        # ----------------------------------------------------
        # TABELA
        # ----------------------------------------------------

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

                    tekst = str(x)

                    if tekst.startswith("3"):
                        pkt += 3

                    elif tekst.startswith("2"):
                        pkt += 2

                    elif tekst.startswith("1"):
                        pkt += 1


                bonus = (
                    st.session_state.rider_bonuses.get(
                        nr,
                        0
                    )
                )


                dane.append({

                    "Nr":
                        nr,

                    "Zawodnik":
                        zawodnik,

                    "OVR":
                        pobierz_ovr(
                            nr,
                            gospodarze
                        ),

                    "Pkt":
                        pkt,

                    "Bon":
                        bonus,

                    "Razem":
                        f"{pkt}+{bonus}",

                    "Biegi":
                        (
                            ", ".join(
                                map(
                                    str,
                                    biegi
                                )
                            )
                            if biegi
                            else "-"
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


            return pd.DataFrame(
                dane
            )


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


        # ----------------------------------------------------
        # RAPORT MECZU
        # ----------------------------------------------------

        st.divider()

        st.subheader(
            "📄 Raport meczu"
        )


        raport = []

        raport.append(
            "=========================================="
        )

        raport.append(
            "🏁 RAPORT MECZU ŻUŻLOWEGO"
        )

        raport.append(
            "=========================================="
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
            f"Aktualny wynik: "
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

                    tekst = str(x)

                    if tekst.startswith("3"):
                        pkt += 3

                    elif tekst.startswith("2"):
                        pkt += 2

                    elif tekst.startswith("1"):
                        pkt += 1


                bonus = (
                    st.session_state.rider_bonuses.get(
                        nr,
                        0
                    )
                )


                raport.append(
                    f"Nr {nr} | "
                    f"{zawodnik} | "
                    f"OVR {pobierz_ovr(nr, gospodarze)} | "
                    f"{pkt}+{bonus} | "
                    f"Biegi: "
                    f"{', '.join(map(str, biegi)) if biegi else '-'}"
                )


        raport_text = "\n".join(
            raport
        )


        st.download_button(
            "📥 Pobierz raport meczu TXT",
            raport_text,
            file_name="raport_meczu.txt",
            mime="text/plain",
            use_container_width=True,
            key="download_raport_liga"
        )


        st.text_area(
            "📋 Cały raport do skopiowania",
            raport_text,
            height=350,
            key="raport_liga_text"
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
        ],
        key="format_indywidualny"
    )


    if format_turnieju == "🏆 SGP":
        nazwa_turnieju = "SGP"

    elif format_turnieju == "🇵🇱 IMP":
        nazwa_turnieju = "IMP"

    else:
        nazwa_turnieju = "Złoty Kask"


    if (
        st.session_state.get(
            "ostatni_format_ind"
        )
        != format_turnieju
    ):

        st.session_state.ostatni_format_ind = (
            format_turnieju
        )

        reset_indywidualne()


    # --------------------------------------------------------
    # TABY
    # --------------------------------------------------------

    tab_ind_kadra, tab_ind_mecz, tab_ind_tabela = st.tabs([
        "👥 Zawodnicy",
        "🏎️ Centrum Zawodów",
        "📊 Klasyfikacja"
    ])


    # ========================================================
    # KADRA INDYWIDUALNA
    # ========================================================

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


    # ========================================================
    # FUNKCJE INDYWIDUALNE
    # ========================================================

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
                "nr":
                    nr,

                "nazwisko":
                    nazwa,

                "ovr":
                    st.session_state.get(
                        f"ind_ovr_{nr}",
                        60
                    ),

                "kraj":
                    st.session_state.get(
                        f"ind_kraj_{nr}",
                        "🇵🇱 Polska"
                    ),

                "u24":
                    st.session_state.get(
                        f"ind_u24_{nr}",
                        False
                    )
            })


        return wynik


    def generuj_program_indywidualny():

        program = []


        for bieg in range(20):

            grupa = [
                ((bieg + 0) % 20) + 1,
                ((bieg + 5) % 20) + 1,
                ((bieg + 10) % 20) + 1,
                ((bieg + 15) % 20) + 1
            ]

            program.append(
                grupa
            )


        return program


    if "ind_program" not in st.session_state:

        st.session_state.ind_program = (
            generuj_program_indywidualny()
        )


    # ========================================================
    # CENTRUM INDYWIDUALNE
    # ========================================================

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
                use_container_width=True,
                key="reset_indywidualne"
            ):

                reset_indywidualne()

                st.session_state.ind_program = (
                    generuj_program_indywidualny()
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


                program = (
                    st.session_state.ind_program[
                        st.session_state.ind_current_heat
                    ]
                )


                st.divider()

                st.subheader(
                    f"🚀 Bieg {nr_biegu} / 20"
                )


                cols = st.columns(4)

                wybrane_ind = []


                for i, nr in enumerate(
                    program
                ):

                    zawodnik = next(
                        (
                            x
                            for x in zawodnicy
                            if x["nr"] == nr
                        ),
                        None
                    )


                    with cols[i]:

                        if zawodnik:

                            st.markdown(
                                f"**{KASKI[i]} "
                                f"Nr {zawodnik['nr']}**"
                            )

                            st.write(
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
                        use_container_width=True,
                        key=f"ind_jedz_{nr_biegu}"
                    ):

                        wyniki = []

                        zdarzenia = []


                        for u in wybrane_ind:

                            sila = sila_zawodnika(
                                u["ovr"],
                                "neutralny",
                                "☀️"
                            )


                            zawodnik = dict(u)

                            zawodnik["sila"] = (
                                sila
                            )

                            zawodnik["wynik_litera"] = (
                                None
                            )


                            los = random.random()


                            if los < 0.02:

                                zawodnik[
                                    "wynik_litera"
                                ] = "D"

                                zawodnik[
                                    "sila"
                                ] = -100


                                zdarzenia.append(
                                    f"💨 Defekt sprzętu: "
                                    f"{u['nazwisko']}!"
                                )


                            elif los < 0.05:

                                zawodnik[
                                    "wynik_litera"
                                ] = "U"

                                zawodnik[
                                    "sila"
                                ] = -200


                                zdarzenia.append(
                                    f"💥 Upadek: "
                                    f"{u['nazwisko']}!"
                                )


                            elif los < 0.08:

                                zawodnik[
                                    "wynik_litera"
                                ] = "W"

                                zawodnik[
                                    "sila"
                                ] = -300


                                zdarzenia.append(
                                    f"🚫 Wykluczenie: "
                                    f"{u['nazwisko']}!"
                                )


                            wyniki.append(
                                zawodnik
                            )


                        wyniki.sort(
                            key=lambda x: x["sila"],
                            reverse=True
                        )


                        sklasyfikowani = [
                            x
                            for x in wyniki
                            if not x[
                                "wynik_litera"
                            ]
                        ]


                        niesklasyfikowani = [
                            x
                            for x in wyniki
                            if x[
                                "wynik_litera"
                            ]
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

                            pkt = punkty[i]


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


                        szczegoly = []


                        for i, u in enumerate(
                            wyniki
                        ):

                            if u["wynik_litera"]:

                                zapis = (
                                    u["wynik_litera"]
                                )

                            else:

                                poz = (
                                    sklasyfikowani.index(
                                        u
                                    )
                                )

                                zapis = str(
                                    punkty[poz]
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


                        st.session_state.ind_history.append({

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
                        })


                        st.session_state.ind_current_heat += 1

                        st.rerun()


            # ------------------------------------------------
            # FINAŁ
            # ------------------------------------------------

            elif (
                st.session_state.ind_current_heat >= 20
                and not st.session_state.ind_finished
            ):

                st.subheader(
                    "🏆 Finał"
                )


                ranking = sorted(
                    zawodnicy,
                    key=lambda x:
                        st.session_state.ind_points.get(
                            x["nr"],
                            0
                        ),
                    reverse=True
                )


                finalisci = ranking[:4]


                for i, zawodnik in enumerate(
                    finalisci
                ):

                    st.write(
                        f"{i + 1}. "
                        f"{zawodnik['nazwisko']} — "
                        f"{st.session_state.ind_points[zawodnik['nr']]} pkt"
                    )


                if st.button(
                    "🏁 Jedź Finał",
                    use_container_width=True,
                    key="ind_jedz_final"
                ):

                    final_wyniki = []


                    for zawodnik in finalisci:

                        sila = sila_zawodnika(
                            zawodnik["ovr"],
                            "neutralny",
                            ""
                        )


                        final_wyniki.append(
                            (
                                zawodnik,
                                sila
                            )
                        )


                    final_wyniki.sort(
                        key=lambda x: x[1],
                        reverse=True
                    )


                    bonus_final = [
                        6,
                        4,
                        2,
                        0
                    ]


                    for i, (
                        zawodnik,
                        _
                    ) in enumerate(
                        final_wyniki
                    ):

                        st.session_state.ind_points[
                            zawodnik["nr"]
                        ] += bonus_final[i]


                    st.session_state.ind_final_result = (
                        final_wyniki
                    )

                    st.session_state.ind_finished = (
                        True
                    )

                    st.rerun()


            # ------------------------------------------------
            # KONIEC
            # ------------------------------------------------

            if st.session_state.ind_finished:

                st.success(
                    f"🏆 KONIEC {nazwa_turnieju}!"
                )


                for i, (
                    zawodnik,
                    _
                ) in enumerate(
                    st.session_state.ind_final_result
                ):

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
                        f"{st.session_state.ind_points[zawodnik['nr']]} pkt"
                    )


            # ------------------------------------------------
            # HISTORIA
            # ------------------------------------------------

            if st.session_state.ind_history:

                st.divider()

                st.subheader(
                    "📜 Historia biegów"
                )


                for hist in reversed(
                    st.session_state.ind_history
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


    # ========================================================
    # TABELA INDYWIDUALNA
    # ========================================================

    with tab_ind_tabela:

        st.header(
            f"📊 Klasyfikacja — {nazwa_turnieju}"
        )


        zawodnicy = zawodnicy_ind()

        dane = []


        for zawodnik in zawodnicy:

            nr = zawodnik["nr"]


            dane.append({

                "Miejsce":
                    0,

                "Nr":
                    nr,

                "Zawodnik":
                    zawodnik["nazwisko"],

                "Kraj":
                    zawodnik["kraj"],

                "U24":
                    (
                        "TAK"
                        if zawodnik["u24"]
                        else "NIE"
                    ),

                "OVR":
                    zawodnik["ovr"],

                "Pkt":
                    st.session_state.ind_points.get(
                        nr,
                        0
                    ),

                "Biegi":
                    ", ".join(
                        st.session_state.ind_heats.get(
                            nr,
                            []
                        )
                    )
            })


        df = pd.DataFrame(
            dane
        )


        if not df.empty:

            df = df.sort_values(
                by=[
                    "Pkt",
                    "OVR"
                ],
                ascending=[
                    False,
                    False
                ]
            ).reset_index(
                drop=True
            )


            df["Miejsce"] = range(
                1,
                len(df) + 1
            )


            st.dataframe(
                df,
                hide_index=True,
                use_container_width=True
            )


        # ----------------------------------------------------
        # RAPORT INDYWIDUALNY
        # ----------------------------------------------------

        st.divider()

        st.subheader(
            "📄 Raport zawodów indywidualnych"
        )


        raport_ind = []


        raport_ind.append(
            "=========================================="
        )

        raport_ind.append(
            f"🏆 {nazwa_turnieju}"
        )

        raport_ind.append(
            "=========================================="
        )

        raport_ind.append("")


        raport_ind.append(
            "----------- BIEGI -----------"
        )


        for hist in st.session_state.ind_history:

            raport_ind.append(
                f"Bieg {hist['bieg']} | "
                f"Wynik: {hist['wynik_biegu']}"
            )

            raport_ind.append(
                f"Kolejność na mecie: "
                f"{hist['szczegoly']}"
            )

            raport_ind.append(
                f"Komentarz: "
                f"{hist['komentarz']}"
            )

            raport_ind.append("")


        raport_ind.append(
            "----------- KLASYFIKACJA -----------"
        )


        ranking_ind = sorted(
            zawodnicy,
            key=lambda x:
                st.session_state.ind_points.get(
                    x["nr"],
                    0
                ),
            reverse=True
        )


        for miejsce, zawodnik in enumerate(
            ranking_ind,
            start=1
        ):

            raport_ind.append(
                f"{miejsce}. "
                f"{zawodnik['nazwisko']} | "
                f"{zawodnik['kraj']} | "
                f"OVR {zawodnik['ovr']} | "
                f"{st.session_state.ind_points.get(zawodnik['nr'], 0)} pkt | "
                f"Biegi: "
                f"{', '.join(map(str, st.session_state.ind_heats.get(zawodnik['nr'], [])))}"
            )


        raport_ind_text = "\n".join(
            raport_ind
        )


        st.download_button(
            "📥 Pobierz raport zawodów TXT",
            raport_ind_text,
            file_name=f"raport_{nazwa_turnieju}.txt",
            mime="text/plain",
            use_container_width=True,
            key="download_raport_ind"
        )


        st.text_area(
            "📋 Cały raport do skopiowania",
            raport_ind_text,
            height=400,
            key="raport_ind_text"
        )


# ============================================================
# TRYB REPREZENTACJI — SWC
# ============================================================

else:

    st.sidebar.header(
        "🌍 Speedway World Cup"
    )


    # --------------------------------------------------------
    # POGODA SWC
    # --------------------------------------------------------

    swc_pogoda = st.sidebar.selectbox(
        "🌤️ Pogoda reprezentacji",
        POGODY + ["🎲 Losowa pogoda"],
        key="swc_pogoda_select"
    )


    if swc_pogoda == "🎲 Losowa pogoda":

        if st.sidebar.button(
            "🎲 Wylosuj pogodę",
            key="swc_random_weather",
            use_container_width=True
        ):

            st.session_state.swc_pogoda = (
                losuj_pogode()
            )

            st.rerun()


        swc_pogoda = st.session_state.get(
            "swc_pogoda",
            POGODY[0]
        )


    else:

        st.session_state.swc_pogoda = (
            swc_pogoda
        )


    # ========================================================
    # NAZWY REPREZENTACJI
    # ========================================================

    if (
        "swc_reprezentacje"
        not in st.session_state
    ):

        st.session_state.swc_reprezentacje = {
            1: "",
            2: "",
            3: "",
            4: ""
        }


    st.subheader(
        "🌍 Reprezentacje"
    )


    rep_cols = st.columns(4)


    for rep in range(1, 5):

        with rep_cols[rep - 1]:

            nazwa = st.text_input(
                f"Reprezentacja {rep}",
                key=f"swc_panstwo_{rep}",
                placeholder="Wpisz dowolne państwo"
            )


            st.session_state.swc_reprezentacje[
                rep
            ] = nazwa.strip()


    # ========================================================
    # TABY SWC
    # ========================================================

    swc_kadra, swc_mecz, swc_tabela = st.tabs([
        "👥 1. Składy reprezentacji",
        "🏎️ 2. Centrum SWC",
        "📊 3. Klasyfikacja"
    ])


    # ========================================================
    # SKŁADY SWC
    # ========================================================

    with swc_kadra:

        st.header(
            "👥 Składy reprezentacji"
        )

        st.warning(
            "⚠️ W tym trybie nie ma Z/Z."
        )


        for rep in range(1, 5):

            nazwa_rep = (
                st.session_state.swc_reprezentacje[
                    rep
                ]
                or
                f"Reprezentacja {rep}"
            )


            with st.expander(
                nazwa_rep,
                expanded=True
            ):

                for nr in range(1, 6):

                    rodzaj = (
                        "Podstawowy"
                        if nr <= 4
                        else
                        "Rezerwowy"
                    )


                    st.markdown(
                        f"**Nr {nr} — {rodzaj}**"
                    )


                    c1, c2 = st.columns(
                        [3, 1]
                    )


                    with c1:

                        st.text_input(
                            "Imię i nazwisko",
                            key=f"swc_name_{rep}_{nr}",
                            placeholder="np. Bartosz Zmarzlik"
                        )


                    with c2:

                        st.number_input(
                            "OVR",
                            min_value=1,
                            max_value=99,
                            value=60,
                            key=f"swc_ovr_{rep}_{nr}"
                        )


    # ========================================================
    # CENTRUM SWC
    # ========================================================

    with swc_mecz:

        st.header(
            "🏎️ Centrum SWC"
        )


        st.markdown(
            f"### 🌤️ Pogoda: {swc_pogoda}"
        )


        st.divider()

        st.subheader(
            "📊 Aktualny wynik"
        )


        wynik_cols = st.columns(4)


        for rep in range(1, 5):

            nazwa_rep = (
                st.session_state.swc_reprezentacje[
                    rep
                ]
                or
                f"Reprezentacja {rep}"
            )


            with wynik_cols[rep - 1]:

                st.metric(
                    nazwa_rep,
                    st.session_state.swc_score[
                        rep
                    ]
                )


        st.divider()


        # ----------------------------------------------------
        # RESET SWC
        # ----------------------------------------------------

        if st.button(
            "🔄 Resetuj zawody SWC",
            use_container_width=True,
            key="swc_reset_zawodow"
        ):

            reset_swc()

            st.rerun()


        # ----------------------------------------------------
        # WALIDACJA SKŁADÓW
        # ----------------------------------------------------

        brak = []


        for rep in range(1, 5):

            for nr in range(1, 6):

                nazwa = st.session_state.get(
                    f"swc_name_{rep}_{nr}",
                    ""
                )


                if not nazwa.strip():

                    brak.append(
                        (
                            rep,
                            nr
                        )
                    )


        if brak:

            st.warning(
                "Najpierw wpisz wszystkich 5 zawodników "
                "w każdej reprezentacji."
            )


        # ----------------------------------------------------
        # AKTUALNY BIEG
        # ----------------------------------------------------

        if (
            not brak
            and not st.session_state.swc_finished
            and st.session_state.swc_heat < 20
        ):

            nr_biegu = (
                st.session_state.swc_heat
                + 1
            )


            program = (
                program_swc[
                    st.session_state.swc_heat
                ]
            )


            st.subheader(
                f"🚀 Bieg {nr_biegu} / 20"
            )


            cols = st.columns(4)

            wybrani = []


            # ------------------------------------------------
            # WYBÓR ZAWODNIKÓW
            # ------------------------------------------------

            for rep in range(1, 5):

                prog_nr = program[rep]


                klucz_prog = (
                    f"{rep}_{prog_nr}"
                )


                prog_starty = (
                    st.session_state.swc_normal_starts.get(
                        klucz_prog,
                        0
                    )
                    +
                    st.session_state.swc_rt.get(
                        klucz_prog,
                        0
                    )
                )


                opcje = []

                opis_opcji = {}


                # --------------------------------------------
                # PROGRAMOWY
                # --------------------------------------------

                if prog_starty < 6:

                    opcje.append(
                        prog_nr
                    )

                    opis_opcji[
                        prog_nr
                    ] = "PROGRAM"


                # --------------------------------------------
                # INNI PODSTAWOWI
                # --------------------------------------------

                for nr in range(1, 5):

                    if nr == prog_nr:
                        continue


                    klucz = (
                        f"{rep}_{nr}"
                    )


                    starty = (
                        st.session_state.swc_normal_starts.get(
                            klucz,
                            0
                        )
                        +
                        st.session_state.swc_rt.get(
                            klucz,
                            0
                        )
                    )


                    if starty < 6:

                        if nr not in opcje:

                            opcje.append(
                                nr
                            )

                            opis_opcji[
                                nr
                            ] = (
                                "REZERWA PODSTAWOWA"
                            )


                # --------------------------------------------
                # REZERWOWY NR 5
                # --------------------------------------------

                klucz_rez = (
                    f"{rep}_5"
                )


                starty_rez = (
                    st.session_state.swc_normal_starts.get(
                        klucz_rez,
                        0
                    )
                    +
                    st.session_state.swc_rt.get(
                        klucz_rez,
                        0
                    )
                )


                if starty_rez < 6:

                    opcje.append(
                        5
                    )

                    opis_opcji[
                        5
                    ] = "REZERWOWY"


                # --------------------------------------------
                # RT
                # --------------------------------------------

                pozostale_repy = [
                    r
                    for r in range(1, 5)
                    if r != rep
                ]


                najblizszy_wynik = min(
                    st.session_state.swc_score[r]
                    for r in pozostale_repy
                )


                roznica = (
                    st.session_state.swc_score[rep]
                    - najblizszy_wynik
                )


                if (
                    nr_biegu >= 3
                    and nr_biegu <= 16
                    and roznica <= -6
                ):

                    for nr in range(1, 5):

                        klucz = (
                            f"{rep}_{nr}"
                        )


                        rt_count = (
                            st.session_state.swc_rt.get(
                                klucz,
                                0
                            )
                        )


                        total = (
                            st.session_state.swc_normal_starts.get(
                                klucz,
                                0
                            )
                            + rt_count
                        )


                        if (
                            rt_count < 1
                            and total < 6
                        ):

                            if nr not in opcje:

                                opcje.append(
                                    nr
                                )

                                opis_opcji[
                                    nr
                                ] = "RT"


                opcje = list(
                    dict.fromkeys(
                        opcje
                    )
                )


                with cols[rep - 1]:

                    nazwa_rep = (
                        st.session_state.swc_reprezentacje[
                            rep
                        ]
                        or
                        f"Reprezentacja {rep}"
                    )


                    st.markdown(
                        f"**{KASKI[rep - 1]} "
                        f"{nazwa_rep}**"
                    )


                    def format_swc(
                        x,
                        rep=rep
                    ):

                        nazwa = st.session_state.get(
                            f"swc_name_{rep}_{x}",
                            ""
                        )


                        ovr = st.session_state.get(
                            f"swc_ovr_{rep}_{x}",
                            60
                        )


                        rodzaj = (
                            "REZERWA"
                            if x == 5
                            else
                            "PODSTAWOWY"
                        )


                        return (
                            f"Nr {x} - "
                            f"{nazwa} "
                            f"(OVR: {ovr}) "
                            f"[{rodzaj}]"
                        )


                    if not opcje:

                        st.error(
                            "Brak dostępnego zawodnika."
                        )

                        st.stop()


                    wybor = st.selectbox(
                        (
                            f"Pole {KASKI[rep - 1]} "
                            f"(Program: Nr {prog_nr})"
                        ),
                        opcje,
                        format_func=format_swc,
                        key=(
                            f"swc_heat_"
                            f"{nr_biegu}_"
                            f"{rep}"
                        )
                    )


                    czy_rezerwa = (
                        wybor == 5
                    )


                    czy_rt = (
                        wybor != prog_nr
                        and not czy_rezerwa
                        and wybor <= 4
                        and nr_biegu >= 3
                        and nr_biegu <= 16
                        and opis_opcji.get(
                            wybor,
                            ""
                        ) == "RT"
                    )


                    wybrani.append({

                        "rep":
                            rep,

                        "nr":
                            wybor,

                        "program_nr":
                            prog_nr,

                        "nazwisko":
                            st.session_state.get(
                                f"swc_name_{rep}_{wybor}",
                                ""
                            ),

                        "ovr":
                            st.session_state.get(
                                f"swc_ovr_{rep}_{wybor}",
                                60
                            ),

                        "kask":
                            KASKI[rep - 1],

                        "czy_rt":
                            czy_rt,

                        "czy_rezerwa":
                            czy_rezerwa
                    })


            # ------------------------------------------------
            # START BIEGU
            # ------------------------------------------------

            if st.button(
                "🏁 Jedź Bieg",
                use_container_width=True,
                key=f"swc_jedz_{nr_biegu}"
            ):

                uczestnicy = []

                zdarzenia = []


                # --------------------------------------------
                # LIMIT
                # --------------------------------------------

                for u in wybrani:

                    klucz = (
                        f"{u['rep']}_{u['nr']}"
                    )


                    normalne = (
                        st.session_state.swc_normal_starts.get(
                            klucz,
                            0
                        )
                    )


                    rt = (
                        st.session_state.swc_rt.get(
                            klucz,
                            0
                        )
                    )


                    razem = (
                        normalne
                        + rt
                    )


                    if razem >= 6:

                        st.error(
                            f"{u['nazwisko']} "
                            f"nie może już wystartować."
                        )

                        st.stop()


                # --------------------------------------------
                # RODZAJ STARTU
                # --------------------------------------------

                for u in wybrani:

                    klucz = (
                        f"{u['rep']}_{u['nr']}"
                    )


                    if u["czy_rt"]:

                        st.session_state.swc_rt[
                            klucz
                        ] += 1

                    else:

                        st.session_state.swc_normal_starts[
                            klucz
                        ] += 1


                # --------------------------------------------
                # SYMULACJA
                # --------------------------------------------

                for u in wybrani:

                    sila = sila_zawodnika(
                        u["ovr"],
                        "neutralny",
                        swc_pogoda
                    )


                    if u["czy_rt"]:
                        sila += 1.0


                    if u["czy_rezerwa"]:
                        sila += 0.2


                    u["sila"] = sila


                    los = random.random()


                    if los < 0.02:

                        u["wynik_litera"] = "D"

                        u["sila"] = -100

                        zdarzenia.append(
                            f"💨 Defekt sprzętu: "
                            f"{u['nazwisko']}!"
                        )


                    elif los < 0.05:

                        u["wynik_litera"] = "U"

                        u["sila"] = -200

                        zdarzenia.append(
                            f"💥 Upadek: "
                            f"{u['nazwisko']}!"
                        )


                    elif los < 0.08:

                        u["wynik_litera"] = "W"

                        u["sila"] = -300

                        zdarzenia.append(
                            f"🚫 Wykluczenie: "
                            f"{u['nazwisko']}!"
                        )


                    else:

                        u["wynik_litera"] = None


                    uczestnicy.append(
                        u
                    )


                # --------------------------------------------
                # KLASYFIKACJA
                # --------------------------------------------

                uczestnicy.sort(
                    key=lambda x: x["sila"],
                    reverse=True
                )


                sklasyfikowani = [
                    u
                    for u in uczestnicy
                    if not u["wynik_litera"]
                ]


                niesklasyfikowani = [
                    u
                    for u in uczestnicy
                    if u["wynik_litera"]
                ]


                punkty = [
                    3,
                    2,
                    1,
                    0
                ]


                wynik_reprezentacji = {
                    1: 0,
                    2: 0,
                    3: 0,
                    4: 0
                }


                # --------------------------------------------
                # PUNKTY
                # --------------------------------------------

                for i, u in enumerate(
                    sklasyfikowani
                ):

                    pkt = (
                        punkty[i]
                        if i < 4
                        else 0
                    )


                    wynik_reprezentacji[
                        u["rep"]
                    ] += pkt


                    klucz = (
                        f"{u['rep']}_{u['nr']}"
                    )


                    st.session_state.swc_heats[
                        klucz
                    ].append(
                        str(pkt)
                    )


                # --------------------------------------------
                # D/U/W
                # --------------------------------------------

                for u in niesklasyfikowani:

                    klucz = (
                        f"{u['rep']}_{u['nr']}"
                    )


                    st.session_state.swc_heats[
                        klucz
                    ].append(
                        u["wynik_litera"]
                    )


                # --------------------------------------------
                # PUNKTY REPREZENTACJI
                # --------------------------------------------

                for rep in range(1, 5):

                    st.session_state.swc_score[
                        rep
                    ] += (
                        wynik_reprezentacji[
                            rep
                        ]
                    )


                # --------------------------------------------
                # KOMENTARZ
                # --------------------------------------------

                uczestnicy_komentarz = []


                for u in sklasyfikowani:

                    uczestnicy_komentarz.append({

                        "nazwisko":
                            u["nazwisko"],

                        "sila":
                            u["sila"],

                        "druzyna":
                            u["rep"]
                    })


                komentarz = komentarz_biegu(
                    uczestnicy_komentarz,
                    zdarzenia
                )


                # --------------------------------------------
                # HISTORIA
                # --------------------------------------------

                szczegoly = []


                for u in uczestnicy:

                    klucz = (
                        f"{u['rep']}_{u['nr']}"
                    )


                    zapis = (
                        st.session_state.swc_heats[
                            klucz
                        ][-1]
                    )


                    status = ""


                    if u["czy_rt"]:

                        status = " [RT]"

                    elif u["czy_rezerwa"]:

                        status = " [REZERWA]"


                    szczegoly.append(
                        f"{u['nazwisko']} "
                        f"({u['kask']}) - "
                        f"{zapis}{status}"
                    )


                st.session_state.swc_history.append({

                    "bieg":
                        nr_biegu,

                    "wynik_biegu":
                        (
                            f"{wynik_reprezentacji[1]}:"
                            f"{wynik_reprezentacji[2]}:"
                            f"{wynik_reprezentacji[3]}:"
                            f"{wynik_reprezentacji[4]}"
                        ),

                    "szczegoly":
                        ", ".join(
                            szczegoly
                        ),

                    "komentarz":
                        komentarz
                })


                st.session_state.swc_heat += 1

                st.rerun()


        # ----------------------------------------------------
        # KONIEC SWC
        # ----------------------------------------------------

        if (
            st.session_state.swc_heat >= 20
            and not st.session_state.swc_finished
        ):

            ranking = sorted(
                range(1, 5),
                key=lambda rep:
                    st.session_state.swc_score[
                        rep
                    ],
                reverse=True
            )


            # -----------------------------------------------
            # REMIS
            # -----------------------------------------------

            if (
                len(ranking) >= 2
                and
                st.session_state.swc_score[
                    ranking[0]
                ]
                ==
                st.session_state.swc_score[
                    ranking[1]
                ]
            ):

                st.warning(
                    "⚠️ Remis na pierwszym miejscu."
                )


                if st.button(
                    "🏁 Rozstrzygnij remis",
                    key="swc_dogrywka"
                ):

                    rep_a = ranking[0]

                    rep_b = ranking[1]

                    kand_a = []

                    kand_b = []


                    for nr in range(1, 6):

                        nazwa_a = st.session_state.get(
                            f"swc_name_{rep_a}_{nr}",
                            ""
                        )


                        if nazwa_a:

                            kand_a.append({

                                "rep":
                                    rep_a,

                                "nr":
                                    nr,

                                "nazwisko":
                                    nazwa_a,

                                "ovr":
                                    st.session_state.get(
                                        f"swc_ovr_{rep_a}_{nr}",
                                        60
                                    )
                            })


                        nazwa_b = st.session_state.get(
                            f"swc_name_{rep_b}_{nr}",
                            ""
                        )


                        if nazwa_b:

                            kand_b.append({

                                "rep":
                                    rep_b,

                                "nr":
                                    nr,

                                "nazwisko":
                                    nazwa_b,

                                "ovr":
                                    st.session_state.get(
                                        f"swc_ovr_{rep_b}_{nr}",
                                        60
                                    )
                            })


                    if kand_a and kand_b:

                        zawodnik_a = max(
                            kand_a,
                            key=lambda x:
                                sila_zawodnika(
                                    x["ovr"],
                                    "neutralny",
                                    swc_pogoda
                                )
                        )


                        zawodnik_b = max(
                            kand_b,
                            key=lambda x:
                                sila_zawodnika(
                                    x["ovr"],
                                    "neutralny",
                                    swc_pogoda
                                )
                        )


                        sila_a = sila_zawodnika(
                            zawodnik_a["ovr"],
                            "neutralny",
                            swc_pogoda
                        )


                        sila_b = sila_zawodnika(
                            zawodnik_b["ovr"],
                            "neutralny",
                            swc_pogoda
                        )


                        if sila_a >= sila_b:

                            winner = rep_a

                        else:

                            winner = rep_b


                        st.session_state.swc_winner = (
                            winner
                        )

                        st.session_state.swc_finished = (
                            True
                        )

                        st.rerun()


                    else:

                        st.error(
                            "Brak zawodników do dogrywki."
                        )


            else:

                st.session_state.swc_winner = (
                    ranking[0]
                )

                st.session_state.swc_finished = (
                    True
                )


        # ----------------------------------------------------
        # ZWYCIĘZCA
        # ----------------------------------------------------

        if st.session_state.swc_finished:

            winner = st.session_state.get(
                "swc_winner"
            )


            if winner:

                winner_name = (
                    st.session_state.swc_reprezentacje[
                        winner
                    ]
                    or
                    f"Reprezentacja {winner}"
                )


                st.success(
                    f"🏆 ZWYCIĘZCA SWC: "
                    f"{winner_name}"
                )


        # ----------------------------------------------------
        # HISTORIA
        # ----------------------------------------------------

        if st.session_state.swc_history:

            st.divider()

            st.subheader(
                "📜 Historia Biegów i Komentarz Live"
            )


            for hist in reversed(
                st.session_state.swc_history
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


    # ========================================================
    # TABELA SWC
    # ========================================================

    with swc_tabela:

        st.header(
            "📊 Klasyfikacja SWC"
        )


        tabela_rep = []


        for rep in range(1, 5):

            nazwa_rep = (
                st.session_state.swc_reprezentacje[
                    rep
                ]
                or
                f"Reprezentacja {rep}"
            )


            tabela_rep.append({

                "Miejsce":
                    0,

                "Reprezentacja":
                    nazwa_rep,

                "Pkt":
                    st.session_state.swc_score[
                        rep
                    ]
            })


        df_rep = pd.DataFrame(
            tabela_rep
        )


        if not df_rep.empty:

            df_rep = df_rep.sort_values(
                by="Pkt",
                ascending=False
            ).reset_index(
                drop=True
            )


            df_rep["Miejsce"] = range(
                1,
                len(df_rep) + 1
            )


            st.dataframe(
                df_rep,
                hide_index=True,
                use_container_width=True
            )


        # ----------------------------------------------------
        # PUNKTY ZAWODNIKÓW
        # ----------------------------------------------------

        st.divider()

        st.subheader(
            "👤 Punkty zawodników"
        )


        tabela_zawodnikow = []


        for rep in range(1, 5):

            nazwa_rep = (
                st.session_state.swc_reprezentacje[
                    rep
                ]
                or
                f"Reprezentacja {rep}"
            )


            for nr in range(1, 6):

                nazwa = st.session_state.get(
                    f"swc_name_{rep}_{nr}",
                    ""
                )


                if not nazwa:
                    continue


                klucz = (
                    f"{rep}_{nr}"
                )


                biegi = (
                    st.session_state.swc_heats.get(
                        klucz,
                        []
                    )
                )


                pkt = 0


                for x in biegi:

                    tekst = str(x)

                    if tekst.startswith("3"):
                        pkt += 3

                    elif tekst.startswith("2"):
                        pkt += 2

                    elif tekst.startswith("1"):
                        pkt += 1


                tabela_zawodnikow.append({

                    "Reprezentacja":
                        nazwa_rep,

                    "Nr":
                        nr,

                    "Zawodnik":
                        nazwa,

                    "OVR":
                        st.session_state.get(
                            f"swc_ovr_{rep}_{nr}",
                            60
                        ),

                    "Pkt":
                        pkt,

                    "Biegi":
                        (
                            ", ".join(
                                map(
                                    str,
                                    biegi
                                )
                            )
                            if biegi
                            else "-"
                        ),

                    "Starty":
                        len(biegi),

                    "Normalne":
                        st.session_state.swc_normal_starts.get(
                            klucz,
                            0
                        ),

                    "RT":
                        st.session_state.swc_rt.get(
                            klucz,
                            0
                        ),

                    "Z/Z":
                        "NIE"
                })


        df_zaw = pd.DataFrame(
            tabela_zawodnikow
        )


        if not df_zaw.empty:

            df_zaw = df_zaw.sort_values(
                by="Pkt",
                ascending=False
            ).reset_index(
                drop=True
            )


            st.dataframe(
                df_zaw,
                hide_index=True,
                use_container_width=True
            )


        # ====================================================
        # RAPORT SWC
        # ====================================================

        st.divider()

        st.subheader(
            "📄 Raport Speedway World Cup"
        )


        raport_swc = []


        raport_swc.append(
            "=========================================="
        )


        raport_swc.append(
            "🌍 SPEEDWAY WORLD CUP"
        )


        raport_swc.append(
            "=========================================="
        )


        raport_swc.append(
            f"Pogoda: "
            f"{st.session_state.get(
                'swc_pogoda',
                swc_pogoda
            )}"
        )


        raport_swc.append("")


        raport_swc.append(
            "----------- KLASYFIKACJA -----------"
        )


        ranking_raport = sorted(
            range(1, 5),
            key=lambda rep:
                st.session_state.swc_score[
                    rep
                ],
            reverse=True
        )


        for miejsce, rep in enumerate(
            ranking_raport,
            start=1
        ):

            nazwa_rep = (
                st.session_state.swc_reprezentacje[
                    rep
                ]
                or
                f"Reprezentacja {rep}"
            )


            raport_swc.append(
                f"{miejsce}. "
                f"{nazwa_rep} — "
                f"{st.session_state.swc_score[rep]} pkt"
            )


        raport_swc.append("")


        raport_swc.append(
            "----------- BIEG PO BIEGU -----------"
        )


        for hist in st.session_state.swc_history:

            raport_swc.append(
                f"Bieg {hist['bieg']} | "
                f"Wynik: {hist['wynik_biegu']}"
            )

            raport_swc.append(
                f"Kolejność na mecie: "
                f"{hist['szczegoly']}"
            )

            raport_swc.append(
                f"Komentarz: "
                f"{hist['komentarz']}"
            )

            raport_swc.append("")


        raport_swc.append(
            "----------- PUNKTY ZAWODNIKÓW -----------"
        )


        for rep in range(1, 5):

            nazwa_rep = (
                st.session_state.swc_reprezentacje[
                    rep
                ]
                or
                f"Reprezentacja {rep}"
            )


            raport_swc.append("")


            raport_swc.append(
                nazwa_rep
            )


            for nr in range(1, 6):

                nazwa = st.session_state.get(
                    f"swc_name_{rep}_{nr}",
                    ""
                )


                if not nazwa:
                    continue


                klucz = (
                    f"{rep}_{nr}"
                )


                biegi = (
                    st.session_state.swc_heats.get(
                        klucz,
                        []
                    )
                )


                pkt = 0


                for x in biegi:

                    tekst = str(x)

                    if tekst.startswith("3"):
                        pkt += 3

                    elif tekst.startswith("2"):
                        pkt += 2

                    elif tekst.startswith("1"):
                        pkt += 1


                raport_swc.append(
                    f"Nr {nr} | "
                    f"{nazwa} | "
                    f"OVR "
                    f"{st.session_state.get(
                        f'swc_ovr_{rep}_{nr}',
                        60
                    )} | "
                    f"{pkt} pkt | "
                    f"Biegi: "
                    f"{', '.join(
                        map(str, biegi)
                    ) if biegi else '-'} | "
                    f"Normalne: "
                    f"{st.session_state.swc_normal_starts.get(
                        klucz,
                        0
                    )} | "
                    f"RT: "
                    f"{st.session_state.swc_rt.get(
                        klucz,
                        0
                    )} | "
                    f"Z/Z: NIE"
                )


        raport_swc_text = "\n".join(
            raport_swc
        )


        st.download_button(
            "📥 Pobierz raport SWC TXT",
            raport_swc_text,
            file_name="raport_swc.txt",
            mime="text/plain",
            use_container_width=True,
            key="download_raport_swc"
        )


        st.text_area(
            "📋 Cały raport SWC do skopiowania",
            raport_swc_text,
            height=450,
            key="raport_swc_text"
        )
