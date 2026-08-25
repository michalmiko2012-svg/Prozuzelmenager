# ============================================================
# RAPORT MECZU
# ============================================================

def generuj_raport_meczu():

    raport = []

    raport.append("=" * 70)
    raport.append("🏁 RAPORT MECZU ŻUŻLOWEGO")
    raport.append("=" * 70)

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
        f"AKTUALNY WYNIK: "
        f"{st.session_state.score_gosp}:"
        f"{st.session_state.score_gosc}"
    )

    raport.append("")
    raport.append("=" * 70)
    raport.append("BIEGI")
    raport.append("=" * 70)

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
                f"Zawodnicy: {hist['szczegoly']}"
            )

            raport.append(
                f"Komentarz: {hist['komentarz']}"
            )

            raport.append("-" * 70)


    raport.append("")
    raport.append("=" * 70)
    raport.append("TABELA PUNKTOWA")
    raport.append("=" * 70)


    def dodaj_tabele_do_raportu(
        sklad,
        nazwa_druzyny
    ):

        raport.append("")
        raport.append(
            f"--- {nazwa_druzyny} ---"
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

            suma_pkt = 0

            for wynik in starty:

                wynik_str = str(wynik)

                if wynik_str.startswith("3"):
                    suma_pkt += 3

                elif wynik_str.startswith("2"):
                    suma_pkt += 2

                elif wynik_str.startswith("1"):
                    suma_pkt += 1


            bonusy = (
                st.session_state.rider_bonuses.get(
                    nr,
                    0
                )
            )

            ovr = (
                st.session_state.sklad_gospodarze_ovr.get(
                    nr,
                    60
                )
                if nr <= 8
                else
                st.session_state.sklad_goscie_ovr.get(
                    nr,
                    60
                )
            )

            zwykle = (
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

            biegi = (
                ", ".join(
                    str(x)
                    for x in starty
                )
                if starty
                else "-"
            )

            raport.append(
                f"Nr {nr} | "
                f"{zawodnik} | "
                f"OVR {ovr} | "
                f"Pkt {suma_pkt}+{bonusy} | "
                f"Biegi: {biegi} | "
                f"Starty: {len(starty)} | "
                f"Zwykłe: {zwykle} | "
                f"RT: {rt} | "
                f"Z/Z: {zz}"
            )


    dodaj_tabele_do_raportu(
        st.session_state.sklad_gospodarze,
        wybrany_gospodarz
    )

    dodaj_tabele_do_raportu(
        st.session_state.sklad_goscie,
        wybrany_gosc
    )


    raport.append("")
    raport.append("=" * 70)
    raport.append("KONIEC RAPORTU")
    raport.append("=" * 70)

    return "\n".join(raport)
