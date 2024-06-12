import requests as rq
import json
import streamlit as st
f=open ('default.txt', 'r')
city=f.read()
if (city=='Default'):
    city_name=st.text_input('I want to know the weather at the next default city...')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=80dfc5415edfd995583e08d0977bf427"
    r = rq.get(url)
    results = json.loads(r.text)
    if city_name:
        while results['cod']=='404':
            city_name = st.text_input('Try again')
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=80dfc5415edfd995583e08d0977bf427"
            r = rq.get(url)
            results = json.loads(r.text)
    city_name_1=st.text_input(f'In addition to {city_name}, I might want to know the weather at...')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name_1}&appid=80dfc5415edfd995583e08d0977bf427"
    r = rq.get(url)
    results = json.loads(r.text)
    if city_name_1:
        while results['cod'] == '404':
            city_name_1 = st.text_input('Try again')
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name_1}&appid=80dfc5415edfd995583e08d0977bf427"
            r = rq.get(url)
            results = json.loads(r.text)
    city_name_2 =st.text_input('Type another city name:')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name_2}&appid=80dfc5415edfd995583e08d0977bf427"
    r = rq.get(url)
    results = json.loads(r.text)
    if city_name_2:
        while results['cod'] == '404':
            city_name_2 = st.text_input('Try again')
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name_2}&appid=80dfc5415edfd995583e08d0977bf427"
            r = rq.get(url)
            results = json.loads(r.text)
    type=st.text_input('I want the temperature to be presented in (type f or c)')
    if type:
        while type != 'c' and 'f':
            type = st.text_input('Try again')
    if st.button("Send"):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=80dfc5415edfd995583e08d0977bf427"
        r = rq.get(url)
        results = json.loads(r.text)
        st.write(f'The weather at {city_name} is', results['weather'][0]['main'])
        if (type == 'c'):
            st.write(f'The temperature at {city_name} is', int((results['main']['temp']) - 273), "Celsius Degrees")
        else:
            st.write(f'The temperature at {city_name} is', 1.8 * int((results['main']['temp']) - 273) + 32, "Fahrenheit Degrees")
        st.write(f'The humidity percent at {city_name} is', results['main']['humidity'], "%")
        f = open('default.txt', 'w'):
        print(city_name, file=f)
        print(city_name_1, file=f)
        print(city_name_2, file=f)
        f.close()
        ff = open('defaulttemp.txt', 'w')
        print(type, file=ff)
        ff.close()
else:
    cities=[]
    with open('default.txt', 'r') as f:
        for line in f:
            city_from_list_striped=line.strip()
            cities.append(city_from_list_striped)
    results_button=[]
    results_button.append(f'default city: {cities[0]}')
    for i in range (1,int(len(cities))):
        results_button.append(cities[i])
    results_button.append('Another city')
    choises = st.radio('Pick Up a city', results_button)
    if choises == f'default city: {cities[0]}':
        new_city_name = cities[0]
        ff = open('defaulttemp.txt', 'r')
        f_or_c = ff.read()
        ff.close()
    elif choises!='Another City':
        new_city_name = choises
        ff = open('defaulttemp.txt', 'r')
        f_or_c = ff.read().strip()
        ff.close()
    if choises=='Another city':
        ncn=st.text_input('Please type the city name:')
        url3 = f"https://api.openweathermap.org/data/2.5/weather?q={ncn}&appid=80dfc5415edfd995583e08d0977bf427"
        r = rq.get(url3)
        results = json.loads(r.text)
        while results['cod'] == '404':
            ncn = st.text_input('Try again')
            url = f"https://api.openweathermap.org/data/2.5/weather?q={ncn}&appid=80dfc5415edfd995583e08d0977bf427"
            r = rq.get(url)
            results = json.loads(r.text)
        Yes_or_No1 = st.text_input(f'Do you want to define the new city as your default city? Type Yes or No')
        if Yes_or_No1=='Yes':
            with open('default.txt', 'w') as f:
                print (ncn, file=f)
                for word in cities:
                    print (word, file=f)
        else:
            Yes_or_No2 = st.text_input(f'Do you want to append the new city to my favorite list? Type Yes or No')
            if Yes_or_No2=='Yes':
                f = open('default.txt', 'a')
                print(ncn, file=f)
                f.close()
        ff = open('defaulttemp.txt', 'r')
        f_or_c = ff.read().strip()
        ff.close()
    if choises=='Another city':
        new_type1 = st.text_input(
            f'Type change if you want to change the temperature unit from {f_or_c}, else press enter')
        if (new_type1 == ''):
            pass
        else:
            ff = open('defaulttemp.txt', 'r')
            if (ff.read().strip() == 'f'):
                ff.close()
                ff = open('defaulttemp.txt', 'w')
                print('c', file=ff)
                ff.close()
            else:
                ff.close()
                ff = open('defaulttemp.txt', 'w')
                print('f', file=ff)
                ff.close()
                ff = open('defaulttemp.txt', 'r')
                f_or_c = ff.read().strip()
                ff.close()
        if ncn:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={ncn}&appid=80dfc5415edfd995583e08d0977bf427"
            r = rq.get(url)
            results = json.loads(r.text)
            st.write(f'The weather at {ncn} is', results['weather'][0]['main'])
            if (f_or_c == 'c'):
                st.write(f'The temperature at {ncn} is', int((results['main']['temp']) - 273),
                        "Celsius Degrees")
            else:
                st.write(f'The temperature at {ncn} is', 1.8 * int((results['main']['temp']) - 273) + 32,
                        "Fahrenheit Degrees")
            st.write(f'The humidity percent at {ncn} is', results['main']['humidity'], "%")
    elif choises!='Another city':
        new_type = st.text_input(
            f'Type change if you want to change the temperature unit from {f_or_c}, else press enter')
        if (new_type == ''):
            pass
        else:
            ff = open('defaulttemp.txt', 'r')
            if (ff.read().strip() == 'f'):
                ff.close()
                ff = open('defaulttemp.txt', 'w')
                print('c', file=ff)
                ff.close()
            else:
                ff.close()
                ff = open('defaulttemp.txt', 'w')
                print('f', file=ff)
                ff.close()
                ff = open('defaulttemp.txt', 'r')
                f_or_c = ff.read().strip()
                ff.close()
        ff = open('defaulttemp.txt', 'r')
        f_or_c = ff.read().strip()
        ff.close()
        if new_city_name:
            url1 = f"https://api.openweathermap.org/data/2.5/weather?q={new_city_name}&appid=80dfc5415edfd995583e08d0977bf427"
            r = rq.get(url1)
            results = json.loads(r.text)
            st.write(f'The weather at {new_city_name} is', results['weather'][0]['main'])
            if (f_or_c == 'c'):
                st.write(f'The temperature at {new_city_name} is', int((results['main']['temp']) - 273),
                        "Celsius Degrees")
            else:
                st.write(f'The temperature at {new_city_name} is', 1.8 * int((results['main']['temp']) - 273) + 32,
                        "Fahrenheit Degrees")
            st.write(f'The humidity percent at {new_city_name} is', results['main']['humidity'], "%")
