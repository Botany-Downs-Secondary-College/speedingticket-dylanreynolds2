#SpeedingTicket.py
#he programme must ask for speed of vechicle, speed limit and calculate the outcome based on the following conditions
#Dylan Reynolds 10/06/2020

#variables
name = ' '
spd_vehicle = 0.00
speed_limit = 100.00
difference = 0.00
fine = 0.00

#works out the fine
def calculatefine(spd_vehicle, spd_limit):
    difference = spd_vehicle - spd_limit
    fine = difference * 10
    if difference > 0:
        if difference > 50:
            if difference < 80:
                print(name, 'you loose licence')
            else: 
                print(name, 'You are going to jail!')
        else:
            print(name, 'your fine is ${}'.format(fine))
    else:
        print('You are driving under the speed limit')

while name == '':
    name = input('What is your name?: ')

#sees if driver has an outstanding warrant
while True:
    try:
        spd_vehicle = float(input('What is your vehicle speed?: '))
        break
    except ValueError:
        print('Please enter a valid number?: ')

#asks the user to input
while True:
    try:
        name = input('What is the offenders name?: ')
        break
    except ValueError:
        print('Please enter a valid interger')

        spd_vehicle = float(input('Please enter your vehicle speed: '))
        break
    except ValueError:
        print('Please enter a valid interger')


#calling the function
calculatefine(spd_vehicle, speed_limit)
print('end')