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

st.title("🏁 Symulator Meczów Żużlowych PRO 2026")


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
    "Trans MF Landshut Devils",
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

pogody = [
    "☀️ Słonecznie i ciepło",
    "⛅ Lekkie zachmurzenie",
    "🌬️ Wietrznie",
    "🌧️ Deszcz (Mżawka)",
    "🌩️ Burza / Ulewa"
]


# ============================================================
# 3. INICJALIZACJA
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

    if "sklad_gospodarze_kraj" not in st.session_state:
        st.session_state.sklad_gospodarze_kraj = {
            nr: "Polak" for nr in range(1, 9)
        }

    if "sklad_goscie_kraj" not in st.session_state:
        st.session_state.sklad_goscie_kraj = {
            nr: "Polak" for nr in range(9, 17)
        }

    if "sklad_gospodarze_wiek" not in st.session_state:
        st.session_state.sklad_gospodarze_wiek = {
            nr: "Senior" for nr in range(1, 9)
        }

    if "sklad_goscie_wiek" not in st.session_state:
        st.session_state.sklad_goscie_wiek = {
            nr: "Senior" for nr in range(9, 17)
        }


inicjalizuj_sklad()


# ============================================================
# 4. FUNKCJE POMOCNICZE
# ============================================================

def pobierz_zawodnika(nr, gospodarze=True):

    if gospodarze:
        return st.session_state.sklad_gospodarze.get(nr, "")

    return st.session_state.sklad_goscie.get(nr, "")


def pobierz_ovr(nr, gospodarze=True):

    if gospodarze:
        return st.session_state.sklad_gospodarze_ovr.get(nr, 60)

    return st.session_state.sklad_goscie_ovr.get(nr, 60)


def pobierz_kraj(nr, gospodarze=True):

    if gospodarze:
        return st.session_state.sklad_gospodarze_kraj.get(
            nr,
            "Polak"
        )

    return st.session_state.sklad_goscie_kraj.get(
        nr,
        "Polak"
    )


def pobierz_wiek(nr, gospodarze=True):

    if gospodarze:
        return st.session_state.sklad_gospodarze_wiek.get(
            nr,
            "Senior"
        )

    return st.session_state.sklad_goscie_wiek.get(
        nr,
        "Senior"
    )


def czy_u24(nr, gospodarze=True):

    return pobierz_wiek(nr, gospodarze) == "U24"


def czy_junior(nr, gospodarze=True):

    return pobierz_wiek(nr, gospodarze) == "Junior"


def czy_polak(nr, gospodarze=True):

    return pobierz_kraj(nr, gospodarze) == "Polak"


def get_ovr_info(nr, gospodarze=True):

    zawodnik = pobierz_zawodnika(
        nr,
        gospodarze
    )

    ovr = pobierz_ovr(
        nr,
        gospodarze
    )

    if not zawodnik:
        return "-"

    return f"{zawodnik} (OVR: {ovr})"


# ============================================================
# 5. REGULAMIN SKŁADU
# ============================================================

def sprawdz_regulamin_skladu(
    gospodarze=True
):

    if gospodarze:

        sklad = st.session_state.sklad_gospodarze
        kraj = st.session_state.sklad_gospodarze_kraj
        wiek = st.session_state.sklad_gospodarze_wiek

    else:

        sklad = st.session_state.sklad_goscie
        kraj = st.session_state.sklad_goscie_kraj
        wiek = st.session_state.sklad_goscie_wiek


    bledy = []
    ostrzezenia = []


    # --------------------------------------------------------
    # ZAWODNICY
    # --------------------------------------------------------

    wypelnieni = [
        nr for nr in sklad
        if sklad.get(nr, "").strip()
    ]

    liczba = len(wypelnieni)


    if liczba < 6:

        bledy.append(
            f"Skład zawiera tylko {liczba} zawodników. "
            "Wymagane jest minimum 6."
        )


    if liczba > 8:

        bledy.append(
            "Skład zawiera więcej niż 8 zawodników."
        )


    # --------------------------------------------------------
    # JUNIORZY 6/7
    # --------------------------------------------------------

    juniorzy = []

    for nr in [6, 7]:

        if sklad.get(nr, "").strip():

            if wiek.get(nr) != "Junior":

                bledy.append(
                    f"Nr {nr}: zawodnik musi być juniorem."
                )

            else:

                juniorzy.append(nr)


    if len(juniorzy) < 2:

        bledy.append(
            "Na numerach 6 i 7 muszą znajdować się "
            "dwaj zawodnicy młodzieżowi."
        )


    # --------------------------------------------------------
    # MINIMUM JEDEN POLAK WŚRÓD JUNIORÓW
    # --------------------------------------------------------

    polski_junior = any(
        kraj.get(nr) == "Polak"
        for nr in [6, 7]
        if sklad.get(nr, "").strip()
    )

    if len(juniorzy) == 2 and not polski_junior:

        bledy.append(
            "Przynajmniej jeden z zawodników na pozycji "
            "6 lub 7 musi być Polakiem."
        )


    # --------------------------------------------------------
    # U24 WŚRÓD NUMERÓW 1-5
    # --------------------------------------------------------

    u24_w_podstawowym = any(
        wiek.get(nr) == "U24"
        for nr in range(1, 6)
        if sklad.get(nr, "").strip()
    )

    if not u24_w_podstawowym:

        bledy.append(
            "Wśród zawodników z numerami 1-5 musi "
            "znajdować się zawodnik U24."
        )


    # --------------------------------------------------------
    # REZERWOWY NR 8
    # --------------------------------------------------------

    if sklad.get(8, "").strip():

        if wiek.get(8) != "U24":

            bledy.append(
                "Zawodnik z numerem 8 musi być zawodnikiem U24."
            )


    # --------------------------------------------------------
    # MINIMUM 4 POLAKÓW
    # --------------------------------------------------------

    polacy = sum(
        1
        for nr in range(1, 8)
        if (
            sklad.get(nr, "").strip()
            and kraj.get(nr) == "Polak"
        )
    )


    if polacy < 4:

        bledy.append(
            f"W podstawowej części składu jest tylko "
            f"{polacy} Polaków. Wymagane minimum: 4."
        )


    # --------------------------------------------------------
    # OSTRZEŻENIA
    # --------------------------------------------------------

    if liczba < 8:

        ostrzezenia.append(
            f"Skład ma {liczba} zawodników. "
            "Możesz zgłosić maksymalnie 8."
        )


    if sklad.get(8, "").strip() == "":

        ostrzezenia.append(
            "Nie wpisano zawodnika rezerwowego z numerem 8."
        )


    return bledy, ostrzezenia


# ============================================================
# 6. STATYSTYKI ZAWODNIKÓW
# ============================================================

def generuj_statystyki_zawodnikow():

    baza = {}


    for nr in range(1, 9):

        nazwisko = (
            st.session_state.sklad_gospodarze.get(
                nr,
                ""
            )
        )

        if not nazwisko:
            continue

        ovr = (
            st.session_state.sklad_gospodarze_ovr.get(
                nr,
                60
            )
        )

        odchylenie = random.randint(-2, 2)

        baza[f"g_{nr}"] = {

            "nazwisko": nazwisko,

            "ovr": ovr,

            "start": max(
                50,
                min(
                    99,
                    ovr + odchylenie
                )
            ),

            "dystans": max(
                50,
                min(
                    99,
                    ovr - odchylenie
                )
            ),

            "forma": random.randint(
                -3,
                3
            ),

            "rola": (
                "junior"
                if nr in [6, 7]
                else "senior"
            )
        }


    for nr in range(9, 17):

        nazwisko = (
            st.session_state.sklad_goscie.get(
                nr,
                ""
            )
        )

        if not nazwisko:
            continue

        ovr = (
            st.session_state.sklad_goscie_ovr.get(
                nr,
                60
            )
        )

        odchylenie = random.randint(-2, 2)

        baza[f"gosc_{nr}"] = {

            "nazwisko": nazwisko,

            "ovr": ovr,

            "start": max(
                50,
                min(
                    99,
                    ovr + odchylenie
                )
            ),

            "dystans": max(
                50,
                min(
                    99,
                    ovr - odchylenie
                )
            ),

            "forma": random.randint(
                -3,
                3
            ),

            "rola": (
                "junior"
                if nr in [14, 15]
                else "senior"
            )
        }


    return baza


# ============================================================
# 7. KOMENTARZE
# ============================================================

def generuj_komentarz_sf(
    uczestnicy,
    zdarzenia
):

    if zdarzenia:

        tekst = " ".join(
            zdarzenia
        )

        return random.choice([
            f"Co za dramatyczne wydarzenia! {tekst}",
            f"Sędzia ma pełne ręce roboty! {tekst}",
            f"Na torze dzieje się bardzo dużo! {tekst}",
            f"To był niezwykle emocjonujący bieg! {tekst}"
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

    roznica = (

        uczestnicy[0]["sila"]
        - uczestnicy[1]["sila"]

        if drugi
        else 100
    )


    if (
        drugi
        and uczestnicy[0]["druzyna"]
        == uczestnicy[1]["druzyna"]
    ):

        return random.choice([
            f"🔥 Pojedynek parowy perfekcyjny! "
            f"{zwyciezca} i {drugi} wygrywają 5:1!",
            
            f"🚀 Para jak z żelaza! "
            f"{zwyciezca} prowadził, a {drugi} "
            f"pilnował drugiej pozycji.",

            f"💥 Nokaut! "
            f"{zwyciezca} i {drugi} pokazali świetną jazdę."
        ])


    if drugi and roznica < 1.5:

        return random.choice([
            f"😱 NIESAMOWITE! "
            f"{zwyciezca} wygrywa dosłownie na kresce!",

            f"⚔️ Walka łokieć w łokieć! "
            f"{zwyciezca} wyrywa zwycięstwo!",

            f"🔥 Co za mijanka! "
            f"{zwyciezca} atakuje do samej mety!"
        ])


    if roznica > 6:

        return random.choice([
            f"⚡ Błyskawica od startu! "
            f"{zwyciezca} odjechał rywalom.",

            f"🎯 Poza zasięgiem! "
            f"{zwyciezca} kontrolował cały bieg.",

            f"👑 Profesor toru! "
            f"{zwyciezca} idealnie dobrał ustawienia."
        ])


    return random.choice([
        f"🏍️ Zacięty bieg! "
        f"{zwyciezca} utrzymał prowadzenie przed {drugi}.",

        f"💨 Twarda walka na dystansie! "
        f"{zwyciezca} dowozi zwycięstwo.",

        f"🏁 Walka o punkty do samej mety! "
        f"{zwyciezca} wygrywa."
    ])


# ============================================================
# 8. PROGRAM BIEGÓW
# ============================================================

program_zawodow = [

    {
        "bieg": 1,
        "A": 1,
        "B": 9,
        "C": 3,
        "D": 11,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },

    {
        "bieg": 2,
        "A": 6,
        "B": 14,
        "C": 7,
        "D": 15,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },

    {
        "bieg": 3,
        "A": 10,
        "B": 2,
        "C": 12,
        "D": 4,
        "kaski": {
            "A": "⚪",
            "B": "🔴",
            "C": "🟡",
            "D": "🔵"
        }
    },

    {
        "bieg": 4,
        "A": 13,
        "B": 5,
        "C": 14,
        "D": 6,
        "kaski": {
            "A": "⚪",
            "B": "🔴",
            "C": "🟡",
            "D": "🔵"
        }
    },

    {
        "bieg": 5,
        "A": 3,
        "B": 9,
        "C": 4,
        "D": 10,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },

    {
        "bieg": 6,
        "A": 11,
        "B": 1,
        "C": 12,
        "D": 7,
        "kaski": {
            "A": "⚪",
            "B": "🔴",
            "C": "🟡",
            "D": "🔵"
        }
    },

    {
        "bieg": 7,
        "A": 2,
        "B": 13,
        "C": 5,
        "D": 15,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },

    {
        "bieg": 8,
        "A": 10,
        "B": 4,
        "C": 11,
        "D": 6,
        "kaski": {
            "A": "⚪",
            "B": "🔴",
            "C": "🟡",
            "D": "🔵"
        }
    },

    {
        "bieg": 9,
        "A": 1,
        "B": 9,
        "C": 2,
        "D": 12,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },

    {
        "bieg": 10,
        "A": 14,
        "B": 3,
        "C": 13,
        "D": 5,
        "kaski": {
            "A": "⚪",
            "B": "🔴",
            "C": "🟡",
            "D": "🔵"
        }
    },

    {
        "bieg": 11,
        "A": 4,
        "B": 13,
        "C": 1,
        "D": 9,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },

    {
        "bieg": 12,
        "A": 15,
        "B": 7,
        "C": 10,
        "D": 3,
        "kaski": {
            "A": "⚪",
            "B": "🔴",
            "C": "🟡",
            "D": "🔵"
        }
    },

    {
        "bieg": 13,
        "A": 5,
        "B": 11,
        "C": 2,
        "D": 12,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },

    {
        "bieg": 14,
        "A": 3,
        "B": 11,
        "C": 4,
        "D": 12,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    },

    {
        "bieg": 15,
        "A": 1,
        "B": 9,
        "C": 2,
        "D": 10,
        "kaski": {
            "A": "🔴",
            "B": "⚪",
            "C": "🔵",
            "D": "🟡"
        }
    }
]


# ============================================================
# 9. WYBÓR DRUŻYN
# ============================================================

st.sidebar.header("⚙️ Konfiguracja Meczu")


if (
    "gospodarz_biezacy" not in st.session_state
    or st.session_state.gospodarz_biezacy
    not in kluby_lista
):

    st.session_state.gospodarz_biezacy = kluby_lista[0]


if (
    "gosc_biezacy" not in st.session_state
    or st.session_state.gosc_biezacy
    not in kluby_lista
):

    st.session_state.gosc_biezacy = kluby_lista[1]


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


# ============================================================
# 10. POGODA
# ============================================================

st.sidebar.subheader("🌤️ Pogoda")


losowa_pogoda = st.sidebar.checkbox(
    "🎲 Losowa pogoda"
)


if losowa_pogoda:

    if (
        "wylosowana_pogoda_mecz"
        not in st.session_state
    ):

        st.session_state.wylosowana_pogoda_mecz = (
            random.choice(pogody)
        )


    if st.sidebar.button(
        "🎲 Losuj pogodę ponownie",
        use_container_width=True
    ):

        st.session_state.wylosowana_pogoda_mecz = (
            random.choice(pogody)
        )

        st.rerun()


    wybrana_pogoda = (
        st.session_state.wylosowana_pogoda_mecz
    )

    st.sidebar.success(
        f"🎲 Wylosowano: {wybrana_pogoda}"
    )

else:

    wybrana_pogoda = st.sidebar.selectbox(
        "Warunki atmosferyczne:",
        pogody,
        key="pogoda_reczna"
    )


# ============================================================
# 11. ZMIANA DRUŻYN = NOWY MECZ
# ============================================================

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

    st.session_state.current_heat = 0
    st.session_state.score_gosp = 0
    st.session_state.score_gosc = 0

    st.session_state.match_history = []

    st.session_state.starts_count = {
        nr: 0
        for nr in range(1, 17)
    }

    st.session_state.rider_heats = {
        nr: []
        for nr in range(1, 17)
    }

    st.session_state.normal_starts_count = {
        nr: 0
        for nr in range(1, 17)
    }

    st.session_state.rt_count = {
        nr: 0
        for nr in range(1, 17)
    }

    st.session_state.zz_count = {
        nr: 0
        for nr in range(1, 17)
    }

    st.session_state.rider_bonuses = {
        nr: 0
        for nr in range(1, 17)
    }

    st.session_state.kontuzjowani = set()

    st.session_state.zz_gosp = None
    st.session_state.zz_gosc = None

    st.session_state.mecz_przerwany = False

    st.session_state.decyzja_o_przerwaniu_podjeta = False

    st.session_state.baza_zawodnikow = {}

    st.rerun()


# ============================================================
# 12. TABS
# ============================================================

tab_kadry, tab_taktyka, tab_mecz = st.tabs([
    "👥 1. Kadry",
    "📣 2. Taktyka",
    "🏎️ 3. Centrum Meczowe"
])


# ============================================================
# 13. KADRY
# ============================================================

with tab_kadry:

    st.header(
        f"{wybrany_gospodarz} vs {wybrany_gosc}"
    )

    st.info(
        "Wpisz dowolnego zawodnika. "
        "Nie ma tutaj gotowej bazy zawodników."
    )


    col_gosp, col_gosc = st.columns(2)


    # ========================================================
    # GOSPODARZ
    # ========================================================

    with col_gosp:

        st.subheader(
            f"🏠 {wybrany_gospodarz}"
        )

        for nr in range(1, 9):

            st.markdown(
                f"### Nr {nr}"
            )

            c1, c2 = st.columns([3, 1])

            name_key = (
                f"manual_gosp_name_{nr}"
            )

            ovr_key = (
                f"manual_gosp_ovr_{nr}"
            )

            kraj_key = (
                f"manual_gosp_kraj_{nr}"
            )

            wiek_key = (
                f"manual_gosp_wiek_{nr}"
            )


            if name_key not in st.session_state:

                st.session_state[name_key] = (
                    st.session_state.sklad_gospodarze.get(
                        nr,
                        ""
                    )
                )


            if ovr_key not in st.session_state:

                st.session_state[ovr_key] = int(
                    st.session_state.sklad_gospodarze_ovr.get(
                        nr,
                        60
                    )
                )


            if kraj_key not in st.session_state:

                st.session_state[kraj_key] = (
                    st.session_state.sklad_gospodarze_kraj.get(
                        nr,
                        "Polak"
                    )
                )


            if wiek_key not in st.session_state:

                st.session_state[wiek_key] = (
                    st.session_state.sklad_gospodarze_wiek.get(
                        nr,
                        "Senior"
                    )
                )


            with c1:

                st.text_input(
                    "Imię i nazwisko",
                    key=name_key,
                    placeholder="np. Jan Kowalski"
                )


            with c2:

                st.number_input(
                    "OVR",
                    min_value=1,
                    max_value=99,
                    step=1,
                    key=ovr_key
                )


            c3, c4 = st.columns(2)


            with c3:

                st.selectbox(
                    "Narodowość",
                    [
                        "Polak",
                        "Obcokrajowiec"
                    ],
                    key=kraj_key
                )


            with c4:

                if nr in [6, 7]:

                    opcje_wiek = [
                        "Junior"
                    ]

                elif nr == 8:

                    opcje_wiek = [
                        "U24"
                    ]

                else:

                    opcje_wiek = [
                        "Senior",
                        "U24"
                    ]


                st.selectbox(
                    "Kategoria",
                    opcje_wiek,
                    key=wiek_key
                )


            st.session_state.sklad_gospodarze[nr] = (
                st.session_state[name_key]
            )

            st.session_state.sklad_gospodarze_ovr[nr] = (
                st.session_state[ovr_key]
            )

            st.session_state.sklad_gospodarze_kraj[nr] = (
                st.session_state[kraj_key]
            )

            st.session_state.sklad_gospodarze_wiek[nr] = (
                st.session_state[wiek_key]
            )


    # ========================================================
    # GOŚĆ
    # ========================================================

    with col_gosc:

        st.subheader(
            f"✈️ {wybrany_gosc}"
        )

        for nr in range(9, 17):

            st.markdown(
                f"### Nr {nr}"
            )

            c1, c2 = st.columns([3, 1])

            name_key = (
                f"manual_gosc_name_{nr}"
            )

            ovr_key = (
                f"manual_gosc_ovr_{nr}"
            )

            kraj_key = (
                f"manual_gosc_kraj_{nr}"
            )

            wiek_key = (
                f"manual_gosc_wiek_{nr}"
            )


            if name_key not in st.session_state:

                st.session_state[name_key] = (
                    st.session_state.sklad_goscie.get(
                        nr,
                        ""
                    )
                )


            if ovr_key not in st.session_state:

                st.session_state[ovr_key] = int(
                    st.session_state.sklad_goscie_ovr.get(
                        nr,
                        60
                    )
                )


            if kraj_key not in st.session_state:

                st.session_state[kraj_key] = (
                    st.session_state.sklad_goscie_kraj.get(
                        nr,
                        "Polak"
                    )
                )


            if wiek_key not in st.session_state:

                st.session_state[wiek_key] = (
                    st.session_state.sklad_goscie_wiek.get(
                        nr,
                        "Senior"
                    )
                )


            with c1:

                st.text_input(
                    "Imię i nazwisko",
                    key=name_key,
                    placeholder="np. Jan Kowalski"
                )


            with c2:

                st.number_input(
                    "OVR",
                    min_value=1,
                    max_value=99,
                    step=1,
                    key=ovr_key
                )


            c3, c4 = st.columns(2)


            with c3:

                st.selectbox(
                    "Narodowość",
                    [
                        "Polak",
                        "Obcokrajowiec"
                    ],
                    key=kraj_key
                )


            with c4:

                if nr in [14, 15]:

                    opcje_wiek = [
                        "Junior"
                    ]

                elif nr == 16:

                    opcje_wiek = [
                        "U24"
                    ]

                else:

                    opcje_wiek = [
                        "Senior",
                        "U24"
                    ]


                st.selectbox(
                    "Kategoria",
                    opcje_wiek,
                    key=wiek_key
                )


            st.session_state.sklad_goscie[nr] = (
                st.session_state[name_key]
            )

            st.session_state.sklad_goscie_ovr[nr] = (
                st.session_state[ovr_key]
            )

            st.session_state.sklad_goscie_kraj[nr] = (
                st.session_state[kraj_key]
            )

            st.session_state.sklad_goscie_wiek[nr] = (
                st.session_state[wiek_key]
            )


    # ========================================================
    # KONTROLA REGULAMINU
    # ========================================================

    st.divider()

    st.header(
        "📋 Kontrola regulaminowa składów"
    )

    st.caption(
        "Kontrola jest przygotowana pod zasady PGE Ekstraligi 2026."
    )


    reg_gosp, reg_gosc = st.columns(2)


    with reg_gosp:

        st.subheader(
            f"🏠 {wybrany_gospodarz}"
        )

        bledy, ostrzezenia = (
            sprawdz_regulamin_skladu(True)
        )

        if not bledy:

            st.success(
                "✅ Skład spełnia sprawdzane wymagania."
            )

        else:

            st.error(
                "❌ Skład NIE jest regulaminowy."
            )

            for blad in bledy:

                st.markdown(
                    f"- ❌ {blad}"
                )


        for ostrz in ostrzezenia:

            st.warning(
                f"⚠️ {ostrz}"
            )


    with reg_gosc:

        st.subheader(
            f"✈️ {wybrany_gosc}"
        )

        bledy, ostrzezenia = (
            sprawdz_regulamin_skladu(False)
        )

        if not bledy:

            st.success(
                "✅ Skład spełnia sprawdzane wymagania."
            )

        else:

            st.error(
                "❌ Skład NIE jest regulaminowy."
            )

            for blad in bledy:

                st.markdown(
                    f"- ❌ {blad}"
                )


        for ostrz in ostrzezenia:

            st.warning(
                f"⚠️ {ostrz}"
            )


    # ========================================================
    # STATYSTYKI
    # ========================================================

    st.divider()

    if st.button(
        "🎲 Wylosuj statystyki zawodników",
        use_container_width=True
    ):

        st.session_state.baza_zawodnikow = (
            generuj_statystyki_zawodnikow()
        )

        st.success(
            "Statystyki zostały wygenerowane."
        )


    # ========================================================
    # Z/Z
    # ========================================================

    st.divider()

    st.subheader(
        "🩹 Z/Z — Zastępstwo Zawodnika"
    )


    if "panel_zz_gosp" not in st.session_state:
        st.session_state.panel_zz_gosp = False


    if "panel_zz_gosc" not in st.session_state:
        st.session_state.panel_zz_gosc = False


    zz_g, zz_go = st.columns(2)


    with zz_g:

        st.markdown(
            f"**🏠 {wybrany_gospodarz}**"
        )

        if st.button(
            "🩹 Ustaw Z/Z",
            key="otworz_zz_gosp",
            use_container_width=True
        ):

            st.session_state.panel_zz_gosp = (
                not st.session_state.panel_zz_gosp
            )


        if st.session_state.get(
            "zz_gosp"
        ) is not None:

            nr = st.session_state.zz_gosp

            st.success(
                f"Z/Z aktywne: Nr {nr} — "
                f"{pobierz_zawodnika(nr, True)}"
            )

            if st.button(
                "❌ Usuń Z/Z",
                key="usun_zz_gosp"
            ):

                st.session_state.zz_gosp = None

                st.rerun()


        if st.session_state.panel_zz_gosp:

            kandydaci = [
                nr
                for nr in range(1, 6)
                if st.session_state.sklad_gospodarze.get(nr)
            ]

            if kandydaci:

                wybor = st.selectbox(
                    "Zawodnik",
                    kandydaci,
                    format_func=lambda x:
                        f"Nr {x} - "
                        f"{pobierz_zawodnika(x, True)}",
                    key="zz_select_gosp"
                )

                if st.button(
                    "✅ Potwierdź Z/Z",
                    key="potwierdz_zz_gosp"
                ):

                    st.session_state.zz_gosp = wybor

                    st.session_state.panel_zz_gosp = False

                    st.rerun()

            else:

                st.warning(
                    "Najpierw wpisz zawodników 1-5."
                )


    with zz_go:

        st.markdown(
            f"**✈️ {wybrany_gosc}**"
        )

        if st.button(
            "🩹 Ustaw Z/Z",
            key="otworz_zz_gosc",
            use_container_width=True
        ):

            st.session_state.panel_zz_gosc = (
                not st.session_state.panel_zz_gosc
            )


        if st.session_state.get(
            "zz_gosc"
        ) is not None:

            nr = st.session_state.zz_gosc

            st.success(
                f"Z/Z aktywne: Nr {nr} — "
                f"{pobierz_zawodnika(nr, False)}"
            )

            if st.button(
                "❌ Usuń Z/Z",
                key="usun_zz_gosc"
            ):

                st.session_state.zz_gosc = None

                st.rerun()


        if st.session_state.panel_zz_gosc:

            kandydaci = [
                nr
                for nr in range(9, 14)
                if st.session_state.sklad_goscie.get(nr)
            ]

            if kandydaci:

                wybor = st.selectbox(
                    "Zawodnik",
                    kandydaci,
                    format_func=lambda x:
                        f"Nr {x} - "
                        f"{pobierz_zawodnika(x, False)}",
                    key="zz_select_gosc"
                )

                if st.button(
                    "✅ Potwierdź Z/Z",
                    key="potwierdz_zz_gosc"
                ):

                    st.session_state.zz_gosc = wybor

                    st.session_state.panel_zz_gosc = False

                    st.rerun()

            else:

                st.warning(
                    "Najpierw wpisz zawodników 9-13."
                )


# ============================================================
# 14. TAKTYKA
# ============================================================

with tab_taktyka:

    st.header(
        "📣 Odprawa Taktyczna"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.subheader(
            f"🏠 {wybrany_gospodarz}"
        )

        st.selectbox(
            "📐 Przygotowanie toru",
            [
                "⚖️ Tor Neutralny",
                "🧱 Tor Twardy",
                "🚜 Tor Przyczepny"
            ],
            key="przygotowanie_toru_gosp"
        )

        st.selectbox(
            "🔥 Styl jazdy",
            [
                "Standardowe nastawienie",
                "Agresywne (większe ryzyko)",
                "Defensywne (bezpieczne)"
            ],
            key="styl_jazdy_gosp"
        )

        st.selectbox(
            "🔧 Sprzęt",
            [
                "🔧 Silnik Niezawodny",
                "🚀 Silnik Ekstra Mocny"
            ],
            key="sprzet_gosp"
        )


    with col2:

        st.subheader(
            f"✈️ {wybrany_gosc}"
        )

        st.selectbox(
            "🔥 Styl jazdy",
            [
                "Standardowe nastawienie",
                "Agresywne (większe ryzyko)",
                "Defensywne (bezpieczne)"
            ],
            key="styl_jazdy_gosc"
        )

        st.selectbox(
            "🔧 Sprzęt",
            [
                "🔧 Silnik Niezawodny",
                "🚀 Silnik Ekstra Mocny"
            ],
            key="sprzet_gosc"
        )


# ============================================================
# 15. CENTRUM MECZOWE
# ============================================================

with tab_mecz:

    st.header(
        "🏎️ Centrum Meczowe"
    )


    # ========================================================
    # RESET
    # ========================================================

    def reset_stats():

        st.session_state.current_heat = 0

        st.session_state.score_gosp = 0
        st.session_state.score_gosc = 0

        st.session_state.match_history = []

        st.session_state.starts_count = {
            nr: 0
            for nr in range(1, 17)
        }

        st.session_state.rider_heats = {
            nr: []
            for nr in range(1, 17)
        }

        st.session_state.normal_starts_count = {
            nr: 0
            for nr in range(1, 17)
        }

        st.session_state.rt_count = {
            nr: 0
            for nr in range(1, 17)
        }

        st.session_state.zz_count = {
            nr: 0
            for nr in range(1, 17)
        }

        st.session_state.rider_bonuses = {
            nr: 0
            for nr in range(1, 17)
        }

        st.session_state.kontuzjowani = set()

        st.session_state.mecz_przerwany = False

        st.session_state.decyzja_o_przerwaniu_podjeta = False

        st.session_state.zz_gosp = None
        st.session_state.zz_gosc = None

        st.session_state.baza_zawodnikow = (
            generuj_statystyki_zawodnikow()
        )


    if (
        "current_heat" not in st.session_state
        or "rider_heats" not in st.session_state
        or "kontuzjowani" not in st.session_state
    ):

        reset_stats()


    if st.button(
        "🔄 Resetuj Mecz",
        use_container_width=True
    ):

        reset_stats()

        st.rerun()


    # ========================================================
    # RAPORT
    # ========================================================

    def generuj_raport_meczu():

        raport = []

        raport.append("=" * 75)
        raport.append(
            "🏁 RAPORT MECZU ŻUŻLOWEGO PRO 2026"
        )
        raport.append("=" * 75)

        raport.append("")

        raport.append(
            f"GOSPODARZ: {wybrany_gospodarz}"
        )

        raport.append(
            f"GOŚĆ:      {wybrany_gosc}"
        )

        raport.append(
            f"POGODA:    {wybrana_pogoda}"
        )

        raport.append("")

        raport.append(
            f"WYNIK: "
            f"{st.session_state.score_gosp}:"
            f"{st.session_state.score_gosc}"
        )

        raport.append("")

        raport.append("=" * 75)
        raport.append("BIEGI")
        raport.append("=" * 75)


        if not st.session_state.match_history:

            raport.append(
                "Nie rozegrano jeszcze żadnego biegu."
            )

        else:

            for hist in st.session_state.match_history:

                raport.append("")

                raport.append(
                    f"BIEG {hist['bieg']} | "
                    f"WYNIK {hist['wynik_biegu']}"
                )

                raport.append(
                    f"KOLEJNOŚĆ: {hist['szczegoly']}"
                )

                raport.append(
                    f"KOMENTARZ: {hist['komentarz']}"
                )

                raport.append(
                    "-" * 75
                )


        raport.append("")
        raport.append("=" * 75)
        raport.append("PUNKTY ZAWODNIKÓW")
        raport.append("=" * 75)


        def dodaj_druzyna_do_raportu(
            sklad,
            ovr_dict,
            nazwa
        ):

            raport.append("")
            raport.append(
                f"--- {nazwa} ---"
            )


            for nr, zawodnik in sklad.items():

                if not zawodnik:
                    continue


                starty = (
                    st.session_state.rider_heats.get(
                        nr,
                        []
                    )
                )


                pkt = 0

                for wynik in starty:

                    wynik = str(wynik)

                    if wynik.startswith("3"):
                        pkt += 3

                    elif wynik.startswith("2"):
                        pkt += 2

                    elif wynik.startswith("1"):
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
                    f"OVR {ovr_dict.get(nr, 60)} | "
                    f"{pobierz_kraj(nr, nr <= 8)} | "
                    f"{pobierz_wiek(nr, nr <= 8)} | "
                    f"Pkt: {pkt}+{bonus} | "
                    f"Biegi: "
                    f"{', '.join(map(str, starty)) if starty else '-'} | "
                    f"Starty: {len(starty)}"
                )


        dodaj_druzyna_do_raportu(
            st.session_state.sklad_gospodarze,
            st.session_state.sklad_gospodarze_ovr,
            wybrany_gospodarz
        )


        dodaj_druzyna_do_raportu(
            st.session_state.sklad_goscie,
            st.session_state.sklad_goscie_ovr,
            wybrany_gosc
        )


        raport.append("")
        raport.append("=" * 75)
        raport.append("KONIEC RAPORTU")
        raport.append("=" * 75)

        return "\n".join(raport)


    with st.expander(
        "📋 Pełny raport meczu — KOPIUJ",
        expanded=False
    ):

        raport_meczu = generuj_raport_meczu()

        st.code(
            raport_meczu,
            language="text"
        )

        st.caption(
            "Kliknij ikonę kopiowania w prawym górnym rogu pola tekstowego."
        )


    # ========================================================
    # BAZA STATYSTYK
    # ========================================================

    if not st.session_state.get(
        "baza_zawodnikow"
    ):

        st.session_state.baza_zawodnikow = (
            generuj_statystyki_zawodnikow()
        )


    # ========================================================
    # TOR
    # ========================================================

    typ_toru = st.session_state.get(
        "przygotowanie_toru_gosp",
        "⚖️ Tor Neutralny"
    )


    if "Twardy" in typ_toru:

        waga_startu = 0.8
        waga_dystansu = 0.2

    elif "Przyczepny" in typ_toru:

        waga_startu = 0.3
        waga_dystansu = 0.7

    else:

        waga_startu = 0.5
        waga_dystansu = 0.5


    roznica = (
        st.session_state.score_gosp
        - st.session_state.score_gosc
    )


    st.markdown(
        f"### 📊 "
        f"{wybrany_gospodarz} "
        f"**{st.session_state.score_gosp}:"
        f"{st.session_state.score_gosc}** "
        f"{wybrany_gosc}"
    )

    st.info(
        f"🌤️ Pogoda: **{wybrana_pogoda}**"
    )


    # ========================================================
    # KONTUZJE
    # ========================================================

    if st.session_state.kontuzjowani:

        lista = []

        for nr in sorted(
            st.session_state.kontuzjowani
        ):

            if nr <= 8:

                nazwa = pobierz_zawodnika(
                    nr,
                    True
                )

            else:

                nazwa = pobierz_zawodnika(
                    nr,
                    False
                )

            if nazwa:

                lista.append(
                    f"Nr {nr}: {nazwa}"
                )


        if lista:

            st.warning(
                "⚠️ Zawodnicy niezdolni do dalszej jazdy: "
                + ", ".join(lista)
            )


    # ========================================================
    # BURZA
    # ========================================================

    if (
        st.session_state.current_heat == 8
        and wybrana_pogoda == "🌩️ Burza / Ulewa"
        and not st.session_state.get(
            "decyzja_o_przerwaniu_podjeta",
            False
        )
    ):

        st.warning(
            "⚠️ Burza! Sędzia zatrzymał zawody po 8. biegu."
        )

        c1, c2 = st.columns(2)


        with c1:

            if st.button(
                "🔴 Przerwij mecz"
            ):

                st.session_state.mecz_przerwany = True

                st.session_state.decyzja_o_przerwaniu_podjeta = True

                st.rerun()


        with c2:

            if st.button(
                "🟢 Jedziemy dalej"
            ):

                st.session_state.decyzja_o_przerwaniu_podjeta = True

                st.rerun()


    # ========================================================
    # MECZ PRZERWANY
    # ========================================================

    if st.session_state.get(
        "mecz_przerwany",
        False
    ):

        st.error(
            f"🛑 MECZ PRZERWANY — "
            f"{wybrany_gospodarz} "
            f"{st.session_state.score_gosp}:"
            f"{st.session_state.score_gosc} "
            f"{wybrany_gosc}"
        )


    # ========================================================
    # FUNKCJE BIEGU
    # ========================================================

    if (
        not st.session_state.get(
            "mecz_przerwany",
            False
        )
        and st.session_state.current_heat < 15
    ):

        heat_data = program_zawodow[
            st.session_state.current_heat
        ]

        nr_b = heat_data["bieg"]

        kaski_map = heat_data["kaski"]


        def get_pkt_sum(nr):

            starty = (
                st.session_state.rider_heats.get(
                    nr,
                    []
                )
            )

            suma = 0

            for s in starty:

                s = str(s)

                if s.startswith("3"):
                    suma += 3

                elif s.startswith("2"):
                    suma += 2

                elif s.startswith("1"):
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
                    == st.session_state.get(
                        "zz_gosp"
                    )
                )

            return (
                nr
                == st.session_state.get(
                    "zz_gosc"
                )
            )


        def zawodnik_moze_startowac(
            nr,
            nr_biegu,
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

            lacznie = (
                normalne
                + rt
                + zz
            )


            if jako_zz:

                return (
                    nr_biegu in [1]
                    + list(range(3, 14))
                    and zz < 1
                    and lacznie < 7
                )


            if nr_jest_zz(nr):

                return False


            if jako_rt:

                return (
                    nr_biegu in list(range(3, 14))
                    and rt < 1
                    and lacznie < 7
                )


            if nr_biegu in [14, 15]:

                return (
                    normalne < 5
                    and lacznie < 7
                )


            return (
                normalne < 5
                and lacznie < 7
            )


        def buduj_opcje(
            prog_nr,
            gospodarze,
            wykluczone
        ):

            opcje = []


            if gospodarze:

                zakres = range(1, 9)

            else:

                zakres = range(9, 17)


            # Z/Z

            if nr_jest_zz(prog_nr):

                for nr in zakres:

                    if (
                        nr != prog_nr
                        and nr not in wykluczone
                        and pobierz_zawodnika(
                            nr,
                            gospodarze
                        )
                        and zawodnik_moze_startowac(
                            nr,
                            nr_b,
                            jako_zz=True
                        )
                    ):

                        opcje.append(nr)

                return opcje


            # Biegi 14/15
            # tutaj można swobodnie wybrać
            # zawodnika spełniającego limit startów

            if nr_b in [14, 15]:

                for nr in zakres:

                    if (
                        nr not in wykluczone
                        and pobierz_zawodnika(
                            nr,
                            gospodarze
                        )
                        and zawodnik_moze_startowac(
                            nr,
                            nr_b
                        )
                    ):

                        opcje.append(nr)


                opcje.sort(
                    key=lambda x: (
                        x != prog_nr,
                        -get_pkt_sum(x)
                    )
                )

                return opcje


            # Bieg juniorów

            if nr_b == 2:

                if gospodarze:

                    zakres_junior = [6, 7, 8]

                else:

                    zakres_junior = [14, 15, 16]


                for nr in zakres_junior:

                    if (
                        nr not in wykluczone
                        and pobierz_zawodnika(
                            nr,
                            gospodarze
                        )
                        and (
                            pobierz_wiek(
                                nr,
                                gospodarze
                            )
                            == "Junior"
                        )
                        and zawodnik_moze_startowac(
                            nr,
                            nr_b
                        )
                    ):

                        opcje.append(nr)


                return opcje


            # Nominalny

            if (
                prog_nr not in wykluczone
                and pobierz_zawodnika(
                    prog_nr,
                    gospodarze
                )
                and zawodnik_moze_startowac(
                    prog_nr,
                    nr_b
                )
            ):

                opcje.append(prog_nr)


            # Rezerwa

            if gospodarze:

                rezerwy = [8, 6, 7]

            else:

                rezerwy = [16, 14, 15]


            for nr in rezerwy:

                if (
                    nr not in opcje
                    and nr not in wykluczone
                    and pobierz_zawodnika(
                        nr,
                        gospodarze
                    )
                    and zawodnik_moze_startowac(
                        nr,
                        nr_b
                    )
                ):

                    opcje.append(nr)


            # Rezerwa taktyczna

            przegrywa_gosp = (
                roznica <= -6
            )

            przegrywa_gosc = (
                roznica >= 6
            )


            if (
                gospodarze
                and przegrywa_gosp
            ):

                zakres_rt = range(1, 6)

            elif (
                not gospodarze
                and przegrywa_gosc
            ):

                zakres_rt = range(9, 14)

            else:

                zakres_rt = []


            for nr in zakres_rt:

                if (
                    nr not in opcje
                    and nr not in wykluczone
                    and pobierz_zawodnika(
                        nr,
                        gospodarze
                    )
                    and zawodnik_moze_startowac(
                        nr,
                        nr_b,
                        jako_rt=True
                    )
                ):

                    opcje.append(nr)


            return opcje


        # ====================================================
        # WYBÓR ZAWODNIKÓW
        # ====================================================

        st.divider()

        st.subheader(
            f"🚀 Bieg {nr_b} / 15"
        )


        taktyczna_gosp = (
            roznica <= -6
        )

        taktyczna_gosc = (
            roznica >= 6
        )


        cols = st.columns(4)

        wybrane_numery = []

        wybrani_zawodnicy = {}


        for i, pole in enumerate(
            ["A", "B", "C", "D"]
        ):

            prog_nr = heat_data[pole]

            kask = kaski_map[pole]

            czy_gospodarz = (
                kask in ["🔴", "🔵"]
            )


            with cols[i]:

                opcje = buduj_opcje(
                    prog_nr,
                    czy_gospodarz,
                    wybrane_numery
                )


                if not opcje:

                    st.error(
                        f"Brak zawodnika dla pola {pole}."
                    )

                    st.stop()


                if czy_gospodarz:

                    sklad = (
                        st.session_state.sklad_gospodarze
                    )

                    ovr = (
                        st.session_state.sklad_gospodarze_ovr
                    )

                else:

                    sklad = (
                        st.session_state.sklad_goscie
                    )

                    ovr = (
                        st.session_state.sklad_goscie_ovr
                    )


                def format_zawodnika(x):

                    return (
                        f"Nr {x} — "
                        f"{sklad[x]} "
                        f"(OVR {ovr[x]})"
                    )


                wybrany_nr = st.selectbox(
                    (
                        f"{kask} Pole {pole} "
                        f"(program: {prog_nr})"
                    ),
                    opcje,
                    format_func=format_zawodnika,
                    key=f"heat_{nr_b}_{pole}"
                )


                wybrane_numery.append(
                    wybrany_nr
                )


                czy_zz = (
                    nr_jest_zz(
                        prog_nr
                    )
                )


                czy_rt = (
                    not czy_zz
                    and wybrany_nr != prog_nr
                    and (
                        (
                            czy_gospodarz
                            and wybrany_nr in range(1, 6)
                        )
                        or
                        (
                            not czy_gospodarz
                            and wybrany_nr in range(9, 14)
                        )
                    )
                    and (
                        taktyczna_gosp
                        if czy_gospodarz
                        else taktyczna_gosc
                    )
                    and nr_b not in [2, 14, 15]
                )


                wybrani_zawodnicy[pole] = {

                    "kask": kask,

                    "pole": pole,

                    "nr": wybrany_nr,

                    "program_nr": prog_nr,

                    "nazwisko": sklad[
                        wybrany_nr
                    ],

                    "ovr": ovr[
                        wybrany_nr
                    ],

                    "druzyna": (
                        "gosp"
                        if czy_gospodarz
                        else "gosc"
                    ),

                    "czy_zz": czy_zz,

                    "czy_rt": czy_rt
                }


        # ====================================================
        # JEDŹ
        # ====================================================

        if st.button(
            "🏁 JEDŹ BIEG",
            use_container_width=True,
            type="primary"
        ):

            uczestnicy = list(
                wybrani_zawodnicy.values()
            )

            zdarzenia = []


            # ------------------------------------------------
            # STARTY
            # ------------------------------------------------

            for u in uczestnicy:

                nr = u["nr"]

                if u["czy_zz"]:

                    st.session_state.zz_count[nr] += 1

                elif u["czy_rt"]:

                    st.session_state.rt_count[nr] += 1

                else:

                    st.session_state.normal_starts_count[nr] += 1


                st.session_state.starts_count[nr] += 1


            # ------------------------------------------------
            # SIŁA
            # ------------------------------------------------

            for u in uczestnicy:

                if u["druzyna"] == "gosp":

                    klucz = (
                        f"g_{u['nr']}"
                    )

                else:

                    klucz = (
                        f"gosc_{u['nr']}"
                    )


                zaw = (
                    st.session_state.baza_zawodnikow.get(
                        klucz
                    )
                )


                if not zaw:

                    zaw = {

                        "ovr": u["ovr"],

                        "start": u["ovr"],

                        "dystans": u["ovr"],

                        "forma": 0
                    }


                start = zaw["start"]

                dystans = zaw["dystans"]

                forma = zaw["forma"]


                # ------------------------------------------------
                # POGODA
                # ------------------------------------------------

                w_start = waga_startu

                w_dystans = waga_dystansu

                kara = 0

                losowy = 5.0


                if "Wietrznie" in wybrana_pogoda:

                    kara = 1

                    losowy = 6


                elif "Deszcz" in wybrana_pogoda:

                    w_start *= 0.9

                    w_dystans *= 1.1

                    kara = 1


                elif "Burza" in wybrana_pogoda:

                    w_start *= 0.85

                    w_dystans *= 1.05

                    kara = 2

                    losowy = 7


                sila = (
                    start * w_start
                    + dystans * w_dystans
                    + forma
                    - kara
                )


                # ------------------------------------------------
                # STYL
                # ------------------------------------------------

                styl = st.session_state.get(
                    f"styl_jazdy_{u['druzyna']}",
                    "Standardowe nastawienie"
                )


                if "Agresywne" in styl:

                    sila += 1

                    losowy = 6


                elif "Defensywne" in styl:

                    sila -= 0.5

                    losowy = 3.5


                sila += random.uniform(
                    -losowy,
                    losowy
                )


                # ------------------------------------------------
                # SPRZĘT
                # ------------------------------------------------

                sprzet = st.session_state.get(
                    f"sprzet_{u['druzyna']}",
                    ""
                )


                szansa_defekt = 0.02


                if "Ekstra Mocny" in sprzet:

                    sila += 2

                    szansa_defekt = 0.04


                u["sila"] = sila


                # ------------------------------------------------
                # ZDARZENIA
                # ------------------------------------------------

                los = random.random()


                if los < szansa_defekt:

                    zdarzenia.append(
                        f"💨 Defekt: "
                        f"{u['nazwisko']}"
                    )

                    u["wynik_litera"] = "D"

                    u["sila"] = -100


                elif los < szansa_defekt + 0.03:

                    zdarzenia.append(
                        f"💥 Upadek: "
                        f"{u['nazwisko']}"
                    )

                    u["wynik_litera"] = "U"

                    u["sila"] = -200


                    if random.random() < 0.20:

                        st.session_state.kontuzjowani.add(
                            u["nr"]
                        )

                        zdarzenia.append(
                            f"🚑 {u['nazwisko']} "
                            "niezdolny do dalszej jazdy."
                        )


                elif los < szansa_defekt + 0.05:

                    zdarzenia.append(
                        f"🚫 Wykluczenie: "
                        f"{u['nazwisko']}"
                    )

                    u["wynik_litera"] = "W"

                    u["sila"] = -300


                else:

                    u["wynik_litera"] = None


            # ------------------------------------------------
            # KLASYFIKACJA
            # ------------------------------------------------

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


            wynik_gosp = 0
            wynik_gosc = 0


            # ------------------------------------------------
            # PUNKTY
            # ------------------------------------------------

            for i, u in enumerate(
                sklasyfikowani
            ):

                pkt = (
                    punkty[i]
                    if i < 4
                    else 0
                )


                bonus = False


                if (
                    pkt == 2
                    and sklasyfikowani
                    and sklasyfikowani[0]["druzyna"]
                    == u["druzyna"]
                ):

                    bonus = True


                elif (
                    pkt == 1
                    and len(sklasyfikowani) >= 2
                    and (
                        sklasyfikowani[0]["druzyna"]
                        == u["druzyna"]

                        or

                        sklasyfikowani[1]["druzyna"]
                        == u["druzyna"]
                    )
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

                    wynik_gosp += pkt

                else:

                    wynik_gosc += pkt


            # ------------------------------------------------
            # D/U/W
            # ------------------------------------------------

            for u in niesklasyfikowani:

                st.session_state.rider_heats[
                    u["nr"]
                ].append(
                    u["wynik_litera"]
                )


            # ------------------------------------------------
            # WYNIK MECZU
            # ------------------------------------------------

            st.session_state.score_gosp += (
                wynik_gosp
            )

            st.session_state.score_gosc += (
                wynik_gosc
            )


            # ------------------------------------------------
            # KOMENTARZ
            # ------------------------------------------------

            komentarz = (
                generuj_komentarz_sf(
                    sklasyfikowani,
                    zdarzenia
                )
            )


            # ------------------------------------------------
            # HISTORIA
            # ------------------------------------------------

            szczegoly = []


            for u in uczestnicy:

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
                    f"{zapis}"
                    f"{status}"
                )


            st.session_state.match_history.append({

                "bieg": nr_b,

                "wynik_biegu":
                    f"{wynik_gosp}:{wynik_gosc}",

                "szczegoly":
                    ", ".join(szczegoly),

                "komentarz":
                    komentarz
            })


            st.session_state.current_heat += 1

            st.rerun()


    # ========================================================
    # KONIEC MECZU
    # ========================================================

    if st.session_state.current_heat >= 15:

        st.success(
            f"🏁 KONIEC MECZU! "
            f"{wybrany_gospodarz} "
            f"{st.session_state.score_gosp}:"
            f"{st.session_state.score_gosc} "
            f"{wybrany_gosc}"
        )


    # ========================================================
    # HISTORIA BIEGÓW
    # ========================================================

    if st.session_state.match_history:

        st.divider()

        st.subheader(
            "📜 Historia biegów"
        )


        for hist in reversed(
            st.session_state.match_history
        ):

            with st.expander(
                f"Bieg {hist['bieg']} | "
                f"Wynik {hist['wynik_biegu']}",
                expanded=False
            ):

                st.markdown(
                    f"**Kolejność:** "
                    f"{hist['szczegoly']}"
                )

                st.info(
                    f"🎙️ {hist['komentarz']}"
                )


    # ========================================================
    # TABELA PUNKTOWA
    # ========================================================

    st.divider()

    st.subheader(
        "📋 Tabela Punktowa Zawodników"
    )


    def generuj_tabele_wynikow(
        sklad,
        ovr_dict,
        gospodarze
    ):

        dane = []


        for nr, zawodnik in sklad.items():

            if not zawodnik:
                continue


            starty = (
                st.session_state.rider_heats.get(
                    nr,
                    []
                )
            )


            pkt = 0


            for s in starty:

                s = str(s)

                if s.startswith("3"):
                    pkt += 3

                elif s.startswith("2"):
                    pkt += 2

                elif s.startswith("1"):
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
                    ovr_dict.get(
                        nr,
                        60
                    ),

                "Kraj":
                    pobierz_kraj(
                        nr,
                        gospodarze
                    ),

                "Kategoria":
                    pobierz_wiek(
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
                    ", ".join(
                        map(
                            str,
                            starty
                        )
                    )
                    if starty
                    else "-",

                "Starty":
                    len(starty),

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


    tab1, tab2 = st.columns(2)


    with tab1:

        st.markdown(
            f"### 🏠 {wybrany_gospodarz}"
        )

        df = generuj_tabele_wynikow(
            st.session_state.sklad_gospodarze,
            st.session_state.sklad_gospodarze_ovr,
            True
        )

        st.dataframe(
            df,
            hide_index=True,
            use_container_width=True
        )


    with tab2:

        st.markdown(
            f"### ✈️ {wybrany_gosc}"
        )

        df = generuj_tabele_wynikow(
            st.session_state.sklad_goscie,
            st.session_state.sklad_goscie_ovr,
            False
        )

        st.dataframe(
            df,
            hide_index=True,
            use_container_width=True
        )
