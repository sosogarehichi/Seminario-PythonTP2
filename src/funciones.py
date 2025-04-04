# imprimir ronda
def print_round(r, i):
    space = " " * 6
    round_title = (
        "Jugador" + space + "Kills" + space + " Asistencias" + space +
        "Muertes" + space + "MVPs" + space + "Puntaje"
        )
    return f"Ranking {r}: {i} \n" + f"{round_title} \n" + "─" * 72


# imprimir stats de los players
def print_player(player, stats):
    space = "  " * 4
    separador = "╰" + "─" * 71
    # .ljust(n) ajusta la longitud de una salida a n caracteres
    players_info = (
                f"{str(player).ljust(7)}{space}{str(stats['kills']).ljust(6)}"
                f"{space}{str(stats['assists']).ljust(7)}{space}"
                f"{str(stats['deaths']).ljust(4)}{space}"
                f"{str(stats['MVPs']).ljust(3)}{space}"
                f"{str(stats['points']).ljust(2)}\n{separador}"
              )
    return players_info


# calcular los puntos
def calculate_points(kills, assists, deaths):
    points = kills * 3 + assists - deaths
    return points


# cargar nuevo jugador
def load_player(players_data, round, player, death, kda):
    players_data[player] = {
        'kills': round[player]['kills'],
        'assists': round[player]['assists'],
        'deaths': death,
        'MVPs': 0,
        'points': kda,
    }


# actualizar stats del jugador
def update_player(player, players_data, round, death, kda):
    players_data[player]['kills'] += round[player]['kills']
    players_data[player]['assists'] += round[player]['assists']
    players_data[player]['deaths'] += death
    players_data[player]['points'] += kda


# definir quien es el mvp
def who_is_mvp(best_kda, kda, mvp_player, player):
    if kda > best_kda:
        best_kda = kda
        mvp_player = player
    return best_kda, mvp_player
