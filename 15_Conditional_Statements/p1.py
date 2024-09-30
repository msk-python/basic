print("use 1, 0 for Yes or No:")

seat_belt_on = int( input("seat belt on: ") )
road_clear   = int( input("road clear: ") )

def start_car():
    if not seat_belt_on:
        print('Please wear your Seat-Belt! 🧑‍🦼‍➡️')
        return
    if not road_clear:
        print('Road is not clear please wait 🔴')
        return
    print('Car has been started! 🚗💨')

start_car()