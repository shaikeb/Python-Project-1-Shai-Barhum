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
    while results['cod']=='404':
        city_name = st.text_input('Try again')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=80dfc5415edfd995583e08d0977bf427"
        r = rq.get(url)
        results = json.loads(r.text)
    city_name_1=st.text_input(f'In addition to {city_name}, I might want to know the weather at...')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name_1}&appid=80dfc5415edfd995583e08d0977bf427"
    r = rq.get(url)
    results = json.loads(r.text)
    while results['cod'] == '404':
        city_name_1 = st.text_input('Try again')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name_1}&appid=80dfc5415edfd995583e08d0977bf427"
        r = rq.get(url)
        results = json.loads(r.text)
    city_name_2 =st.text_input('In case there is another city, type it now, else click enter')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name_2}&appid=80dfc5415edfd995583e08d0977bf427"
    r = rq.get(url)
    results = json.loads(r.text)
    while results['cod'] == '404':
        city_name_2 = st.text_input('Try again')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name_2}&appid=80dfc5415edfd995583e08d0977bf427"
        r = rq.get(url)
        results = json.loads(r.text)
    type=st.text_input('I want the temperature to be presented in (type f or c)')
    while type != 'c' and 'f':
        type = st.text_input('Try again')
    f=open('default.txt', 'w')
    print (city_name, file=f)
    print(city_name_1, file=f)
    print(city_name_2, file=f)
    f.close()
    ff = open('defaulttemp.txt', 'w')
    print(type, file=ff)
    ff.close()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=80dfc5415edfd995583e08d0977bf427"
    r = rq.get(url)
    results = json.loads(r.text)
    st.write(f'The weather at {city_name} is', results['weather'][0]['main'])
    if (type == 'c'):
        st.write(f'The temperature at {city_name} is', int((results['main']['temp']) - 273), "Celsius Degrees")
    else:
        st.write(f'The temperature at {city_name} is', 1.8 * int((results['main']['temp']) - 273) + 32, "Fahrenheit Degrees")
    st.write(f'The humidity percent at {city_name} is', results['main']['humidity'], "%")
else:
    ff = open('defaulttemp.txt', 'r')
    f_or_cc = ff.read()
    ff.close()
    cities=[]
    with open('default.txt', 'r') as f:
        for line in f:
            city_from_list_striped=line.strip()
            cities.append(city_from_list_striped)
    f.close()
    st.write(f'I want to know the weather at...., press enter for the default city: {cities[0]}')
    st.write(f'You can also pick up one of your favorite cities:')
    for i in range (1,int(len(cities))):
        st.write (cities[i])
    new_city_name=st.text_input('Please type the city name:')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={new_city_name}&appid=80dfc5415edfd995583e08d0977bf427"
    r = rq.get(url)
    results = json.loads(r.text)
    while results['cod'] == '404':
        new_city_name = st.text_input('Try again')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={new_city_name}&appid=80dfc5415edfd995583e08d0977bf427"
        r = rq.get(url)
        results = json.loads(r.text)
    if new_city_name not in cities and new_city_name!='':
        Yes_or_No1 = st.text_input(f'Do you want to define the new city as your default city? Type Yes or No')
        if Yes_or_No1=='Yes':
            with open('default.txt', 'w') as f:
                print (new_city_name, file=f)
                for word in cities:
                    print (word, file=f)
        else:
            Yes_or_No2 = st.text_input(f'Do you want to append the new city to my favorite list? Type Yes or No')
            if Yes_or_No2=='Yes':
                f = open('default.txt', 'a')
                print(new_city_name, file=f)
                f.close()
    new_type=st.text_input(f'Type change if you want to change the temperature unit from {f_or_cc}, else press enter')
    if  (new_type==''):
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
    f_or_c=ff.read().strip()
    ff.close()
    if new_city_name=='':
        f = open('default.txt', 'r')
        new_city_name=f.readline()
        ff.close()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={new_city_name}&appid=80dfc5415edfd995583e08d0977bf427"
    r=rq.get(url)
    results=json.loads(r.text)
    st.write (f'The weather at {new_city_name} is',results['weather'][0]['main'])
    if (f_or_c=='c'):
        st.write (f'The temperature at {new_city_name} is', int((results['main']['temp'])-273), "Celsius Degrees")
    else:
        st.write(f'The temperature at {new_city_name} is', 1.8*int((results['main']['temp']) - 273)+32, "Fahrenheit Degrees")
    st.write (f'The humidity percent at {new_city_name} is', results['main']['humidity'], "%")