

def tribonacci(n):
    if n < 4:
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


def tallest_player(nba_player_data):
    list = []
    max_pies, max_pulgadas = [0,0]
    for key, value in nba_player_data.items():
        pies, pulgadas = value[3].split('-')
        if(int(pies) > max_pies):
            max_pies, max_pulgadas = [int(pies), int(pulgadas)]
            list.clear()      #Se olvidan los jugadores mas bajos
            list.append(key)  #Se guarda el nombre del jugador mas alto
        elif(int(pies) == max_pies and int(pulgadas) > max_pulgadas):
            max_pies, max_pulgadas = [int(pies), int(pulgadas)]
            list.clear()      #Se olvidan los jugadores mas bajos
            list.append(key)  #Se guarda el nombre del jugador mas alto
        elif (int(pies) == max_pies and int(pulgadas) == max_pulgadas):
            list.append(key) #se gudarda el jugador mas (o igual) alto
    return list

def more_time_position_player(nba_player_data, position):
    list = []
    max_time = 0;
    for key, value in nba_player_data.items():
        if(position == value[2]):
            time = int(value[1]) - int(value[0])
            if time > max_time:
                max_time = time
                list.clear()
                list.append(key)
            elif time == max_time:
                list.append(key)
    return list