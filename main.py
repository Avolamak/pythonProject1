import requests
from tkinter import *

root = Tk()
root.title("Weather Forecsat")
root.geometry('200x500+500+100')
root.iconbitmap('weather.ico')
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)



api_key = '47b40e47a85f3b314fa9575f02fe7a55'
api_call = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key

running = True
i = 0
myList = Listbox(root, yscrollcommand = scrollbar.set, width = 500, height = 200)

while running:


    city = "Chelyabinsk"
    api_call += '&q=' + city



    json_data = requests.get(api_call).json()

    location_data = {
        'city': json_data['city']['name'],
        'country': json_data['city']['country']
    }

    w ='\n{city}, {country}'.format(**location_data)
    print(w)
    myList.insert(END, w, "\n")


    current_date = ''

    for item in json_data['list']:

        time = item['dt_txt']

        next_date, hour = time.split(' ')

        if current_date != next_date:
            current_date = next_date
            year, month, day = current_date.split('-')
            date = {'y': year, 'm': month, 'd': day}
            date2 = '\n{m}/{d}/{y}'.format(**date)
            print(date2)
            myList.insert(END, date2, "\n")



        hour = int(hour[:2])

        if hour < 12:
            if hour == 0:
                hour = 12
            meridiem = 'AM'
        else:
            if hour > 12:
                hour -= 12
            meridiem = 'PM'


        s ='\n%i:00 %s' % (hour, meridiem)
        print(s)
        myList.insert(END, s)

        temperature = item['main']['temp']

        description = item['weather'][0]['description'],

        cond ='Weather condition: %s' % description
        cel ='Celcius: {:.2f}'.format(temperature - 273.15)
        print(cond)
        print(cel)
        myList.insert(END, cond, cel, "\n")
    myList.pack(side = LEFT, fill = BOTH)
    scrollbar.config( command = myList.yview )


    break
root.mainloop()

