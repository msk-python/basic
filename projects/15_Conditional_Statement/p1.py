is_seat_belt_on = True
is_road_clear = False

def start_car():
    if not is_seat_belt_on:
        print('Please wear your Seat-Belt! 🧑‍🦼‍➡️')
        return
    if not is_road_clear:
        print('Road is not clear 🔴')
        return
    print('Car has been started! 🚗💨')

start_car()