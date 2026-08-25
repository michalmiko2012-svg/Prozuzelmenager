import streamlit as st
import random
import pandas as pd

st.set_page_config(
    page_title="Symulator Żużlowy PRO 2026",
    layout="wide"
)

st.title("🏁 Symulator Meczów Żużlowych - Sezon 2026")


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
# 2. FUNKCJE POMOCNICZE
# ============================================================

def pobierz_ovr(nr, gospodarze=True):
    if gospodarze:
        return st.session_state.sklad_gospodarze_ovr.get(nr, 60)
    else:
        return st.session_state.sklad_goscie_ovr.get(nr, 60)


def pobierz_zawodnika(nr, gospodarze=True):
    if gospodarze:
        return st.session_state.sklad_gospodarze.get(nr, "")
    else:
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
        zdarz_tekst = " ".join(zdarzenia)

        opisy_zdarzen = [
            f"Co za dramatyczne wydarzenia! {zdarz_tekst}",
            f"Sędzia przerywa bieg! {zdarz_tekst}",
            f"Niesamowite zamieszanie na torze. {zdarz_tekst}",
            f"Na torze dzieje się bardzo dużo! {zdarz_tekst}"
        ]

        return random.choice(opisy_zdarzen)

    if not uczestnicy:
        return "Bieg bez historii — nikt nie dojechał do mety."

    zwyciezca = uczestnicy[0]["nazwisko"]
    drugi = uczestnicy[1]["nazwisko"] if len(uczestnicy) > 1 else None
    trzeci = uczestnicy[2]["nazwisko"] if len(uczestnicy) > 2 else None
    czwarty = uczestnicy[3]["nazwisko"] if len(uczestnicy) > 3 else None

    roznica = (
        uczestnicy[0]["sila"] - uczestnicy[1]["sila"]
        if drugi
        else 100
    )

    if drugi and uczestnicy[0]["druzyna"] == uczestnicy[1]["druzyna"]:

        scenariusze_51 = [
            f"🔥 **Pojedynek parowy perfekcyjny!** {zwyciezca} i {drugi} wystrzelili spod taśmy i nie dali rywalom najmniejszych szans. Podwójna wygrana!",
            f"🚀 **Para jak z żelaza!** {zwyciezca} prowadził bieg, a {drugi} mądrze blokował ataki rywali. 5:1!",
            f"💥 **Nokaut!** Pokaz jazdy parą w wykonaniu duetu {zwyciezca} - {drugi}."
        ]

        return random.choice(scenariusze_51)

    if (
        drugi
        and trzeci
        and uczestnicy[0]["druzyna"] != uczestnicy[1]["druzyna"]
        and uczestnicy[1]["druzyna"] == uczestnicy[2]["druzyna"]
    ):

        scenariusze_remis = [
            f"⚖️ **Remis po twardej walce!** {zwyciezca} pewnie wygrywa bieg, ale {drugi} i {trzeci} dowożą cenne punkty.",
            f"🎯 **Samotny jastrząb!** {zwyciezca} uciekł reszcie stawki, lecz para rywali ({drugi}, {trzeci}) kontrolowała dalsze pozycje."
        ]

        return random.choice(scenariusze_remis)

    if drugi and roznica < 1.5:

        scenariusze_styk = [
            f"😱 **NIESAMOWITE!** {zwyciezca} wyprzedza zawodnika {drugi} dosłownie na kresce!",
            f"⚔️ **Walka łokcie w łokcie!** {zwyciezca} wyrywa zwycięstwo na ostatniej prostej!",
            f"🔥 **Co za mijanka!** {zwyciezca} atakuje do samej mety i wygrywa!"
        ]

        return random.choice(scenariusze_styk)

    if roznica > 6.0:

        scenariusze_dominacja = [
            f"⚡ **Błyskawica od startu!** {zwyciezca} zdemolował rywali na dojeździe do pierwszego łuku.",
            f"🎯 **Poza zasięgiem!** {zwyciezca} założył całą stawkę na pierwszym łuku.",
            f"👑 **Profesor toru!** {zwyciezca} dopasował przełożenia idealnie."
        ]

        return random.choice(scenariusze_dominacja)

    scenariusze_walka = [
        f"🏍️ **Zacięty bieg!** {zwyciezca} utrzymał prowadzenie przed atakami {drugi}.",
        f"💨 **Kąśliwe ataki na dystansie!** {drugi} szukał prędkości, ale {zwyciezca} dowiózł trójkę.",
        f"🏁 **Twarda walka o punkty!** {zwyciezca} wygrywa start, a z tyłu trwa walka."
    ]

    return random.choice(scenariusze_walka)


# ============================================================
# 3. PROGRAM BIEGÓW
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
# 4. INICJALIZACJA SKŁADÓW
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
# 5. WYBÓR DRUŻYN
# ============================================================

st.sidebar.header("⚙️ Konfiguracja Meczu")


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


wybrana_pogoda = st.sidebar.selectbox(
    "🌤️ Warunki atmosferyczne:",
    [
        "☀️ Słonecznie i ciepło",
        "⛅ Lekkie zachmurzenie",
        "🌬️ Wietrznie",
        "🌧️ Deszcz (Mżawka)",
        "🌩️ Burza / Ulewa"
    ]
)


# ============================================================
# 6. ZMIANA DRUŻYN = NOWY MECZ
# ============================================================

if (
    st.session_state.get("mecz_gospodarz") != wybrany_gospodarz
    or st.session_state.get("mecz_gosc") != wybrany_gosc
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

    # Nowe składy dla nowego meczu
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
# 7. TABS
# ============================================================

tab_kadry, tab_taktyka, tab_mecz = st.tabs(
    [
        "👥 1. Wybór Drużyn i Kadry",
        "📣 2. Odprawa Taktyczna",
        "🏎️ 3. Centrum Meczowe"
    ]
)


# ============================================================
# 8. KADRY — RĘCZNE WPISYWANIE
# ============================================================

with tab_kadry:

    st.header(
        f"Składy Meczowe: {wybrany_gospodarz} vs {wybrany_gosc}"
    )

    st.info(
        "✍️ Wpisz ręcznie imię i nazwisko oraz OVR każdego zawodnika. "
        "Możesz wpisać dowolnego zawodnika — nie ma już bazy składów."
    )

    col_gosp, col_gosc = st.columns(2)


    # --------------------------------------------------------
    # GOSPODARZ
    # --------------------------------------------------------

    with col_gosp:

        st.subheader(
            f"🏠 {wybrany_gospodarz}"
        )

        for nr in range(1, 9):

            typ = ""

            if nr in [1, 2, 3, 4, 5]:
                typ = "Senior / U24"

            elif nr in [6, 7]:
                typ = "Junior"

            elif nr == 8:
                typ = "Rezerwa zwykła"

            st.markdown(
                f"**Nr {nr} — {typ}**"
            )

            col_nazwa, col_ovr = st.columns([3, 1])

            with col_nazwa:

                st.session_state.sklad_gospodarze[nr] = st.text_input(
                    f"Zawodnik nr {nr}",
                    value=st.session_state.sklad_gospodarze.get(
                        nr,
                        ""
                    ),
                    key=f"manual_gosp_name_{nr}",
                    placeholder="Imię i nazwisko"
                )

            with col_ovr:

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
                    step=1,
                    key=f"manual_gosp_ovr_{nr}"
                )


    # --------------------------------------------------------
    # GOŚĆ
    # --------------------------------------------------------

    with col_gosc:

        st.subheader(
            f"✈️ {wybrany_gosc}"
        )

        for nr in range(9, 17):

            typ = ""

            if nr in [9, 10, 11, 12, 13]:
                typ = "Senior / U24"

            elif nr in [14, 15]:
                typ = "Junior"

            elif nr == 16:
                typ = "Rezerwa zwykła"

            st.markdown(
                f"**Nr {nr} — {typ}**"
            )

            col_nazwa, col_ovr = st.columns([3, 1])

            with col_nazwa:

                st.session_state.sklad_goscie[nr] = st.text_input(
                    f"Zawodnik nr {nr}",
                    value=st.session_state.sklad_goscie.get(
                        nr,
                        ""
                    ),
                    key=f"manual_gosc_name_{nr}",
                    placeholder="Imię i nazwisko"
                )

            with col_ovr:

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
                    step=1,
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
            "Statystyki start/dystans/forma zostały wygenerowane."
        )


    # ========================================================
    # Z/Z
    # ========================================================

    st.divider()

    st.subheader(
        "🩹 Z/Z — Zastępstwo Zawodnika"
    )

    st.caption(
        "Wybierz zawodnika podstawowego, którego numer będzie "
        "zastępowany przez Z/Z."
    )

    if "panel_zz_gosp" not in st.session_state:
        st.session_state.panel_zz_gosp = False

    if "panel_zz_gosc" not in st.session_state:
        st.session_state.panel_zz_gosc = False


    zz_col_g, zz_col_go = st.columns(2)


    # --------------------------------------------------------
    # Z/Z GOSPODARZA
    # --------------------------------------------------------

    with zz_col_g:

        st.markdown(
            f"**🏠 {wybrany_gospodarz}**"
        )

        if st.button(
            "🩹 Ustaw Z/Z gospodarza",
            key="otworz_zz_gosp",
            use_container_width=True
        ):

            st.session_state.panel_zz_gosp = (
                not st.session_state.panel_zz_gosp
            )

        if st.session_state.get("zz_gosp") is not None:

            nr_zz = st.session_state.zz_gosp

            st.success(
                f"Z/Z aktywne: Nr {nr_zz} — "
                f"{pobierz_zawodnika(nr_zz, True)}"
            )

            if st.button(
                "❌ Usuń Z/Z gospodarza",
                key="usun_zz_gosp",
                use_container_width=True
            ):

                st.session_state.zz_gosp = None
                st.session_state.panel_zz_gosp = False

                st.rerun()


        if st.session_state.panel_zz_gosp:

            kand = [
                st.session_state.sklad_gospodarze[nr]
                for nr in range(1, 6)
                if st.session_state.sklad_gospodarze.get(nr)
            ]

            if kand:

                wybor = st.selectbox(
                    "Zawodnik, którego numer będzie zastępowany",
                    kand,
                    key="zz_select_gosp"
                )

                if st.button(
                    "✅ Potwierdź Z/Z gospodarza",
                    key="potwierdz_zz_gosp",
                    use_container_width=True
                ):

                    nr = next(
                        (
                            n for n in range(1, 6)
                            if st.session_state.sklad_gospodarze.get(n)
                            == wybor
                        ),
                        None
                    )

                    st.session_state.zz_gosp = nr
                    st.session_state.panel_zz_gosp = False

                    st.rerun()

            else:

                st.warning(
                    "Najpierw wpisz zawodników 1–5."
                )


    # --------------------------------------------------------
    # Z/Z GOŚCIA
    # --------------------------------------------------------

    with zz_col_go:

        st.markdown(
            f"**✈️ {wybrany_gosc}**"
        )

        if st.button(
            "🩹 Ustaw Z/Z gościa",
            key="otworz_zz_gosc",
            use_container_width=True
        ):

            st.session_state.panel_zz_gosc = (
                not st.session_state.panel_zz_gosc
            )

        if st.session_state.get("zz_gosc") is not None:

            nr_zz = st.session_state.zz_gosc

            st.success(
                f"Z/Z aktywne: Nr {nr_zz} — "
                f"{pobierz_zawodnika(nr_zz, False)}"
            )

            if st.button(
                "❌ Usuń Z/Z gościa",
                key="usun_zz_gosc",
                use_container_width=True
            ):

                st.session_state.zz_gosc = None
                st.session_state.panel_zz_gosc = False

                st.rerun()


        if st.session_state.panel_zz_gosc:

            kand = [
                st.session_state.sklad_goscie[nr]
                for nr in range(9, 14)
                if st.session_state.sklad_goscie.get(nr)
            ]

            if kand:

                wybor = st.selectbox(
                    "Zawodnik, którego numer będzie zastępowany",
                    kand,
                    key="zz_select_gosc"
                )

                if st.button(
                    "✅ Potwierdź Z/Z gościa",
                    key="potwierdz_zz_gosc",
                    use_container_width=True
                ):

                    nr = next(
                        (
                            n for n in range(9, 14)
                            if st.session_state.sklad_goscie.get(n)
                            == wybor
                        ),
                        None
                    )

                    st.session_state.zz_gosc = nr
                    st.session_state.panel_zz_gosc = False

                    st.rerun()

            else:

                st.warning(
                    "Najpierw wpisz zawodników 9–13."
                )


# ============================================================
# 9. TAKTYKA
# ============================================================

with tab_taktyka:

    st.title(
        "🛠️ Ustawienia Taktyczne Menedżerów"
    )

    st.info(
        "📣 **PRZERWA / ODPRAWA TAKTYCZNA:** Odprawa przedmeczowa"
    )

    col_tak_gosp, col_tak_gosc = st.columns(2)


    with col_tak_gosp:

        st.subheader(
            f"🏠 Gospodarz ({wybrany_gospodarz})"
        )

        st.selectbox(
            "📐 Przygotowanie Nawierzchni:",
            [
                "⚖️ Tor Neutralny",
                "🧱 Tor Twardy",
                "🚜 Tor Przyczepny"
            ],
            key="przygotowanie_toru_gosp"
        )

        st.selectbox(
            "🔥 Styl Jazdy Drużyny:",
            [
                "Standardowe nastawienie",
                "Agresywne (większe ryzyko)",
                "Defensywne (bezpieczne)"
            ],
            key="styl_jazdy_gosp"
        )

        st.selectbox(
            "🔧 Sprzęt / Tuner:",
            [
                "🔧 Silnik Niezawodny (0% defektu)",
                "🚀 Silnik Ekstra Mocny (+2 siły, wyższy defekt)"
            ],
            key="sprzet_gosp"
        )


    with col_tak_gosc:

        st.subheader(
            f"✈️ Gość ({wybrany_gosc})"
        )

        st.selectbox(
            "🔥 Styl Jazdy Drużyny:",
            [
                "Standardowe nastawienie",
                "Agresywne (większe ryzyko)",
                "Defensywne (bezpieczne)"
            ],
            key="styl_jazdy_gosc"
        )

        st.selectbox(
            "🔧 Sprzęt / Tuner:",
            [
                "🔧 Silnik Niezawodny (0% defektu)",
                "🚀 Silnik Ekstra Mocny (+2 siły, wyższy defekt)"
            ],
            key="sprzet_gosc"
        )


# ============================================================
# 10. CENTRUM MECZOWE
# ============================================================

with tab_mecz:

    st.header(
        "Panel Symulacji Meczowej"
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


    col_top1, col_top2 = st.columns([4, 1])


    with col_top2:

        if st.button(
            "🔄 Resetuj Mecz",
            use_container_width=True
        ):

            reset_stats()
            st.rerun()


    # ========================================================
    # STATYSTYKI
    # ========================================================

    if not st.session_state.get("baza_zawodnikow"):

        st.session_state.baza_zawodnikow = (
            generuj_statystyki_zawodnikow()
        )


    typ_toru = st.session_state.get(
        "przygotowanie_toru_gosp",
        "⚖️ Tor Neutralny"
    )


    if "Twardy" in typ_toru:

        waga_startu = 0.8
        waga_dystansu = 0.2

    elif "Neutralny" in typ_toru:

        waga_startu = 0.5
        waga_dystansu = 0.5

    else:

        waga_startu = 0.3
        waga_dystansu = 0.7


    roznica = (
        st.session_state.score_gosp
        - st.session_state.score_gosc
    )


    st.markdown(
        f"### 📊 Aktualny Wynik: "
        f"{wybrany_gospodarz} **"
        f"{st.session_state.score_gosp} : "
        f"{st.session_state.score_gosc}"
        f"** {wybrany_gosc} | Pogoda: {wybrana_pogoda}"
    )


    # ========================================================
    # KONTUZJE
    # ========================================================

    if st.session_state.kontuzjowani:

        kontuzje = []

        for nr in sorted(
            st.session_state.kontuzjowani
        ):

            if nr <= 8:
                nazwa = pobierz_zawodnika(nr, True)
            else:
                nazwa = pobierz_zawodnika(nr, False)

            if nazwa:
                kontuzje.append(
                    f"Nr {nr}: {nazwa}"
                )

        if kontuzje:

            st.warning(
                "⚠️ **Zawodnicy niezdolni do jazdy:** "
                + ", ".join(kontuzje)
            )


    # ========================================================
    # Z/Z INFO
    # ========================================================

    if (
        st.session_state.get("zz_gosp") is not None
        or st.session_state.get("zz_gosc") is not None
    ):

        zz_info = []

        if st.session_state.get("zz_gosp") is not None:

            nr = st.session_state.zz_gosp

            zz_info.append(
                f"🏠 Z/Z: Nr {nr} "
                f"{pobierz_zawodnika(nr, True)}"
            )

        if st.session_state.get("zz_gosc") is not None:

            nr = st.session_state.zz_gosc

            zz_info.append(
                f"✈️ Z/Z: Nr {nr} "
                f"{pobierz_zawodnika(nr, False)}"
            )

        st.info(
            " | ".join(zz_info)
        )


    # ========================================================
    # BURZA PO 8 BIEGU
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
            "⚠️ Nad stadionem przeszła gwałtowna burza! "
            "Sędzia wstrzymał zawody po 8. biegu."
        )

        col_przerw1, col_przerw2 = st.columns(2)


        with col_przerw1:

            if st.button(
                "🔴 Przerwij mecz i zalicz wynik"
            ):

                st.session_state.mecz_przerwany = True
                st.session_state.decyzja_o_przerwaniu_podjeta = True

                st.rerun()


        with col_przerw2:

            if st.button(
                "🟢 Czekamy na poprawę pogody – jedziemy dalej"
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
            f"🛑 **MECZ PRZERWANY!** "
            f"Wynik: {wybrany_gospodarz} "
            f"{st.session_state.score_gosp}:"
            f"{st.session_state.score_gosc} "
            f"{wybrany_gosc}"
        )


    # ========================================================
    # BIEGI
    # ========================================================

    elif st.session_state.current_heat < 15:

        heat_data = program_zawodow[
            st.session_state.current_heat
        ]

        nr_b = heat_data["bieg"]
        kaski_map = heat_data["kaski"]

        st.divider()

        st.subheader(
            f"🚀 Bieg {nr_b} / 15"
        )


        taktyczna_gosp = roznica <= -6
        taktyczna_gosc = roznica >= 6


        # ====================================================
        # SUMA PUNKTÓW
        # ====================================================

        def get_pkt_sum(nr):

            starty = st.session_state.rider_heats.get(
                nr,
                []
            )

            s_pkt = 0

            for s in starty:

                s_str = str(s)

                if s_str.startswith("3"):
                    s_pkt += 3

                elif s_str.startswith("2"):
                    s_pkt += 2

                elif s_str.startswith("1"):
                    s_pkt += 1

            return (
                s_pkt
                + st.session_state.rider_bonuses.get(
                    nr,
                    0
                )
            )


        # ====================================================
        # Z/Z
        # ====================================================

        def nr_jest_zz(nr):

            if 1 <= nr <= 8:

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


        # ====================================================
        # CZY MOŻE STARTOWAĆ
        # ====================================================

        def zawodnik_moze_startowac(
            nr,
            nr_biegu,
            jako_zz=False,
            jako_rt=False
        ):

            if nr in st.session_state.kontuzjowani:
                return False

            normalne = st.session_state.get(
                "normal_starts_count",
                {}
            ).get(nr, 0)

            rt = st.session_state.get(
                "rt_count",
                {}
            ).get(nr, 0)

            zz = st.session_state.get(
                "zz_count",
                {}
            ).get(nr, 0)

            lacznie = (
                normalne
                + rt
                + zz
            )


            # Z/Z

            if jako_zz:

                return (
                    nr_biegu in [1]
                    + list(range(3, 14))
                    and zz < 1
                    and lacznie < 7
                )


            # Zawodnik oznaczony jako Z/Z
            # nie jedzie normalnie.

            if nr_jest_zz(nr):
                return False


            # RT

            if jako_rt:

                return (
                    nr_biegu in list(range(3, 16))
                    and rt < 1
                    and lacznie < 7
                )


            # Biegi nominowane

            if nr_biegu in [14, 15] and (
                rt > 0
                or zz > 0
            ):

                return lacznie < 7


            # Zwykły limit

            return (
                normalne < 5
                and lacznie < 7
            )


        # ====================================================
        # OPCJE GOSPODARZA
        # ====================================================

        def buduj_opcje_gosp(
            prog_nr,
            wykluczone_numery=None
        ):

            if wykluczone_numery is None:
                wykluczone_numery = []

            opcje = []


            # Z/Z

            if nr_jest_zz(prog_nr):

                if nr_b in [1] + list(range(3, 14)):

                    for nr in range(1, 9):

                        if (
                            nr != prog_nr
                            and nr not in wykluczone_numery
                            and st.session_state.sklad_gospodarze.get(nr)
                            and zawodnik_moze_startowac(
                                nr,
                                nr_b,
                                jako_zz=True
                            )
                        ):

                            opcje.append(nr)

                return opcje


            # Biegi 14-15

            if nr_b in [14, 15]:

                dostepni = [
                    nr
                    for nr in range(1, 9)
                    if (
                        nr not in wykluczone_numery
                        and st.session_state.sklad_gospodarze.get(nr)
                        and zawodnik_moze_startowac(
                            nr,
                            nr_b
                        )
                    )
                ]

                dostepni.sort(
                    key=lambda nr: (
                        nr != prog_nr,
                        -get_pkt_sum(nr)
                    )
                )

                return dostepni


            # Bieg 2 — juniorzy

            if nr_b == 2:

                for r_nr in [6, 7, 8]:

                    if (
                        r_nr not in wykluczone_numery
                        and st.session_state.sklad_gospodarze.get(r_nr)
                        and zawodnik_moze_startowac(
                            r_nr,
                            nr_b
                        )
                    ):

                        opcje.append(r_nr)

                return opcje


            # Zawodnik programowy

            if (
                prog_nr not in wykluczone_numery
                and st.session_state.sklad_gospodarze.get(prog_nr)
                and zawodnik_moze_startowac(
                    prog_nr,
                    nr_b
                )
            ):

                opcje.append(prog_nr)


            # Rezerwa zwykła

            for r_nr in [8, 6, 7]:

                if (
                    r_nr not in opcje
                    and r_nr not in wykluczone_numery
                    and st.session_state.sklad_gospodarze.get(r_nr)
                    and zawodnik_moze_startowac(
                        r_nr,
                        nr_b
                    )
                ):

                    opcje.append(r_nr)


            # RT

            if taktyczna_gosp:

                for nr in range(1, 6):

                    if (
                        nr not in opcje
                        and nr not in wykluczone_numery
                        and st.session_state.sklad_gospodarze.get(nr)
                        and zawodnik_moze_startowac(
                            nr,
                            nr_b,
                            jako_rt=True
                        )
                    ):

                        opcje.append(nr)


            return opcje


        # ====================================================
        # OPCJE GOŚCIA
        # ====================================================

        def buduj_opcje_gosc(
            prog_nr,
            wykluczone_numery=None
        ):

            if wykluczone_numery is None:
                wykluczone_numery = []

            opcje = []


            # Z/Z

            if nr_jest_zz(prog_nr):

                if nr_b in [1] + list(range(3, 14)):

                    for nr in range(9, 17):

                        if (
                            nr != prog_nr
                            and nr not in wykluczone_numery
                            and st.session_state.sklad_goscie.get(nr)
                            and zawodnik_moze_startowac(
                                nr,
                                nr_b,
                                jako_zz=True
                            )
                        ):

                            opcje.append(nr)

                return opcje


            # Biegi 14-15

            if nr_b in [14, 15]:

                dostepni = [
                    nr
                    for nr in range(9, 17)
                    if (
                        nr not in wykluczone_numery
                        and st.session_state.sklad_goscie.get(nr)
                        and zawodnik_moze_startowac(
                            nr,
                            nr_b
                        )
                    )
                ]

                dostepni.sort(
                    key=lambda nr: (
                        nr != prog_nr,
                        -get_pkt_sum(nr)
                    )
                )

                return dostepni


            # Bieg 2 — juniorzy

            if nr_b == 2:

                for r_nr in [14, 15, 16]:

                    if (
                        r_nr not in wykluczone_numery
                        and st.session_state.sklad_goscie.get(r_nr)
                        and zawodnik_moze_startowac(
                            r_nr,
                            nr_b
                        )
                    ):

                        opcje.append(r_nr)

                return opcje


            # Zawodnik programowy

            if (
                prog_nr not in wykluczone_numery
                and st.session_state.sklad_goscie.get(prog_nr)
                and zawodnik_moze_startowac(
                    prog_nr,
                    nr_b
                )
            ):

                opcje.append(prog_nr)


            # Rezerwa zwykła

            for r_nr in [16, 14, 15]:

                if (
                    r_nr not in opcje
                    and r_nr not in wykluczone_numery
                    and st.session_state.sklad_goscie.get(r_nr)
                    and zawodnik_moze_startowac(
                        r_nr,
                        nr_b
                    )
                ):

                    opcje.append(r_nr)


            # RT

            if taktyczna_gosc:

                for nr in range(9, 14):

                    if (
                        nr not in opcje
                        and nr not in wykluczone_numery
                        and st.session_state.sklad_goscie.get(nr)
                        and zawodnik_moze_startowac(
                            nr,
                            nr_b,
                            jako_rt=True
                        )
                    ):

                        opcje.append(nr)


            return opcje


        # ====================================================
        # WYBÓR 4 ZAWODNIKÓW
        # ====================================================

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

                if czy_gospodarz:

                    opcje = buduj_opcje_gosp(
                        prog_nr,
                        wybrane_numery
                    )

                    sklad = (
                        st.session_state.sklad_gospodarze
                    )

                    sklad_ovr = (
                        st.session_state.sklad_gospodarze_ovr
                    )

                else:

                    opcje = buduj_opcje_gosc(
                        prog_nr,
                        wybrane_numery
                    )

                    sklad = (
                        st.session_state.sklad_goscie
                    )

                    sklad_ovr = (
                        st.session_state.sklad_goscie_ovr
                    )


                if not opcje:

                    st.error(
                        "Brak uprawnionego zawodnika "
                        f"dla pola {pole}, "
                        f"program Nr {prog_nr}."
                    )

                    st.stop()


                label_extra = ""

                if nr_jest_zz(prog_nr):
                    label_extra = " 🩹 Z/Z"


                def format_zawodnika(x):
                    return (
                        f"Nr {x} - "
                        f"{sklad[x]} "
                        f"(OVR: {sklad_ovr[x]})"
                    )


                wybrany_nr = st.selectbox(
                    (
                        f"{kask} Pole {pole} "
                        f"(Program: Nr {prog_nr})"
                        f"{label_extra}"
                    ),
                    opcje,
                    format_func=format_zawodnika,
                    key=f"h_{nr_b}_{pole}"
                )


                wybrane_numery.append(
                    wybrany_nr
                )


                czy_zz = nr_jest_zz(
                    prog_nr
                )


                czy_rt = (
                    not czy_zz
                    and wybrany_nr != prog_nr
                    and (
                        (
                            czy_gospodarz
                            and wybrany_nr in range(1, 6)
                        )
                        or (
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
                    "nazwisko": sklad[wybrany_nr],
                    "ovr": sklad_ovr[wybrany_nr],
                    "druzyna": (
                        "gosp"
                        if czy_gospodarz
                        else "gosc"
                    ),
                    "czy_zz": czy_zz,
                    "czy_rt": czy_rt
                }


        # ====================================================
        # PRZYCISK JEDŹ BIEG
        # ====================================================

        col_btn1, col_btn2 = st.columns(
            [1, 4]
        )


        with col_btn1:

            if st.button(
                "🏁 Jedź Bieg",
                use_container_width=True
            ):

                uczestnicy = list(
                    wybrani_zawodnicy.values()
                )

                zdarzenia = []


                # ------------------------------------------------
                # ZAPIS RODZAJU STARTU
                # ------------------------------------------------

                for u in uczestnicy:

                    nr = u["nr"]

                    if u.get("czy_zz"):

                        st.session_state.zz_count[nr] += 1

                    elif u.get("czy_rt"):

                        st.session_state.rt_count[nr] += 1

                    else:

                        st.session_state.normal_starts_count[nr] += 1


                # ------------------------------------------------
                # SIŁA
                # ------------------------------------------------

                for u in uczestnicy:

                    if u["druzyna"] == "gosp":
                        klucz = f"g_{u['nr']}"
                    else:
                        klucz = f"gosc_{u['nr']}"


                    zaw = st.session_state.baza_zawodnikow.get(
                        klucz
                    )


                    if not zaw:

                        ovr = u["ovr"]

                        zaw = {
                            "ovr": ovr,
                            "start": ovr,
                            "dystans": ovr,
                            "forma": 0
                        }


                    sila = (
                        zaw["start"] * waga_startu
                        + zaw["dystans"] * waga_dystansu
                        + zaw["forma"]
                    )


                    losowy_wplyw = 5.0


                    styl = st.session_state.get(
                        f"styl_jazdy_{u['druzyna']}",
                        "Standardowe nastawienie"
                    )


                    if "Agresywne" in styl:

                        sila += 1.0
                        losowy_wplyw = 6.0


                    elif "Defensywne" in styl:

                        sila -= 0.5
                        losowy_wplyw = 3.5


                    # --------------------------------------------
                    # POGODA
                    # --------------------------------------------

                    waga_startu_biezaca = waga_startu
                    waga_dystansu_biezaca = waga_dystansu
                    kara_pogodowa = 0.0


                    if "Wietrznie" in wybrana_pogoda:

                        kara_pogodowa = 1.0
                        losowy_wplyw += 1.0


                    elif "Deszcz" in wybrana_pogoda:

                        waga_startu_biezaca *= 0.9
                        waga_dystansu_biezaca *= 1.1
                        kara_pogodowa = 1.0


                    elif "Burza" in wybrana_pogoda:

                        waga_startu_biezaca *= 0.85
                        waga_dystansu_biezaca *= 1.05
                        kara_pogodowa = 2.0


                    sila = (
                        zaw["start"]
                        * waga_startu_biezaca
                        + zaw["dystans"]
                        * waga_dystansu_biezaca
                        + zaw["forma"]
                        - kara_pogodowa
                    )


                    sila += random.uniform(
                        -losowy_wplyw,
                        losowy_wplyw
                    )


                    # --------------------------------------------
                    # SPRZĘT
                    # --------------------------------------------

                    takt_sprzet = st.session_state.get(
                        f"sprzet_{u['druzyna']}",
                        ""
                    )


                    szansa_defekt = 0.02


                    if "Ekstra Mocny" in takt_sprzet:

                        sila += 2.0
                        szansa_defekt = 0.04


                    u["sila"] = sila


                    # --------------------------------------------
                    # ZDARZENIA
                    # --------------------------------------------

                    los_zdarzenie = random.random()


                    if los_zdarzenie < szansa_defekt:

                        zdarzenia.append(
                            f"💨 Defekt sprzętu: "
                            f"{u['nazwisko']}!"
                        )

                        u["wynik_litera"] = "D"
                        u["sila"] = -100


                    elif (
                        los_zdarzenie
                        < szansa_defekt + 0.03
                    ):

                        zdarzenia.append(
                            f"💥 Upadek: "
                            f"{u['nazwisko']}!"
                        )

                        u["wynik_litera"] = "U"
                        u["sila"] = -200


                        if random.random() < 0.2:

                            st.session_state.kontuzjowani.add(
                                u["nr"]
                            )

                            zdarzenia.append(
                                f"🚑 {u['nazwisko']} "
                                "niezdolny do dalszej jazdy!"
                            )


                    elif (
                        los_zdarzenie
                        < szansa_defekt + 0.05
                    ):

                        zdarzenia.append(
                            f"🚫 Wykluczenie: "
                            f"{u['nazwisko']}!"
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
                    u for u in uczestnicy
                    if not u["wynik_litera"]
                ]


                niesklasyfikowani = [
                    u for u in uczestnicy
                    if u["wynik_litera"]
                ]


                punkty = [3, 2, 1, 0]


                wyniki_biegu_gosp = 0
                wyniki_biegu_gosc = 0


                # ------------------------------------------------
                # STARTY
                # ------------------------------------------------

                for u in uczestnicy:

                    st.session_state.starts_count[
                        u["nr"]
                    ] += 1


                # ------------------------------------------------
                # PUNKTY
                # ------------------------------------------------

                for i, u in enumerate(
                    sklasyfikowani
                ):

                    pkt = (
                        punkty[i]
                        if i < len(punkty)
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

                        wyniki_biegu_gosp += pkt

                    else:

                        wyniki_biegu_gosc += pkt


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
                    wyniki_biegu_gosp
                )

                st.session_state.score_gosc += (
                    wyniki_biegu_gosc
                )


                # ------------------------------------------------
                # KOMENTARZ
                # ------------------------------------------------

                komentarz = generuj_komentarz_sf(
                    sklasyfikowani,
                    zdarzenia
                )


                # ------------------------------------------------
                # HISTORIA
                # ------------------------------------------------

                szczegoly = []


                for u in uczestnicy:

                    ostatni_zapis = (
                        st.session_state.rider_heats[
                            u["nr"]
                        ][-1]
                    )


                    status = ""


                    if u.get("czy_zz"):

                        status = " [Z/Z]"


                    elif u.get("czy_rt"):

                        status = " [RT]"


                    szczegoly.append(
                        f"{u['nazwisko']} "
                        f"({u['kask']}) - "
                        f"{ostatni_zapis}"
                        f"{status}"
                    )


                st.session_state.match_history.append(
                    {
                        "bieg": nr_b,
                        "wynik_biegu": (
                            f"{wyniki_biegu_gosp}:"
                            f"{wyniki_biegu_gosc}"
                        ),
                        "szczegoly": ", ".join(
                            szczegoly
                        ),
                        "komentarz": komentarz
                    }
                )


                st.session_state.current_heat += 1

                st.rerun()


    # ========================================================
    # KONIEC MECZU
    # ========================================================

    if st.session_state.current_heat >= 15:

        st.success(
            f"🏁 **KONIEC MECZU!** "
            f"{wybrany_gospodarz} "
            f"{st.session_state.score_gosp}:"
            f"{st.session_state.score_gosc} "
            f"{wybrany_gosc}"
        )


    # ========================================================
    # HISTORIA
    # ========================================================

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
                ),
                expanded=(
                    hist["bieg"]
                    == st.session_state.current_heat
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
    # TABELA PUNKTOWA
    # ========================================================

    st.divider()

    st.subheader(
        "📋 Tabela Punktowa Zawodników"
    )


    def generuj_tabele_wynikow(
        sklad_dict
    ):

        dane = []


        for nr, zawodnik in sklad_dict.items():

            if not zawodnik:
                continue


            starty = (
                st.session_state.rider_heats.get(
                    nr,
                    []
                )
            )


            suma_pkt = 0


            bonusy = (
                st.session_state.rider_bonuses.get(
                    nr,
                    0
                )
            )


            biegi_str = []


            for s in starty:

                s_str = str(s)

                biegi_str.append(
                    s_str
                )


                if s_str.startswith("3"):
                    suma_pkt += 3

                elif s_str.startswith("2"):
                    suma_pkt += 2

                elif s_str.startswith("1"):
                    suma_pkt += 1


            dane.append(
                {
                    "Nr": nr,
                    "Zawodnik": zawodnik,
                    "OVR": (
                        st.session_state.sklad_gospodarze_ovr.get(nr, 60)
                        if nr <= 8
                        else
                        st.session_state.sklad_goscie_ovr.get(nr, 60)
                    ),
                    "Pkt": suma_pkt,
                    "Bon": bonusy,
                    "Razem": f"{suma_pkt}+{bonusy}",
                    "Biegi": (
                        ", ".join(biegi_str)
                        if biegi_str
                        else "-"
                    ),
                    "Starty": len(starty),
                    "Zwykłe": (
                        st.session_state.get(
                            "normal_starts_count",
                            {}
                        ).get(nr, 0)
                    ),
                    "RT": (
                        st.session_state.get(
                            "rt_count",
                            {}
                        ).get(nr, 0)
                    ),
                    "Z/Z": (
                        st.session_state.get(
                            "zz_count",
                            {}
                        ).get(nr, 0)
                    )
                }
            )


        return pd.DataFrame(dane)


    col_tab_gosp, col_tab_gosc = st.columns(2)


    with col_tab_gosp:

        st.markdown(
            f"**🏠 {wybrany_gospodarz}**"
        )

        df_gosp = generuj_tabele_wynikow(
            st.session_state.sklad_gospodarze
        )

        st.dataframe(
            df_gosp,
            hide_index=True,
            use_container_width=True
        )


    with col_tab_gosc:

        st.markdown(
            f"**✈️ {wybrany_gosc}**"
        )

        df_gosc = generuj_tabele_wynikow(
            st.session_state.sklad_goscie
        )

        st.dataframe(
            df_gosc,
            hide_index=True,
            use_container_width=True
        )
