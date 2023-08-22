import streamlit
import pandas
import requests
import snowflake 
import snowflake.connector
from urllib.error import URLError



streamlit.title('My Parents New Healthy Diner')

streamlit.header ('Breakfast Favourites')

streamlit.text ('🥣 Omega 3 & Blueberry Oat meal')

streamlit.text ('🥗 Kale , Spinach & Rocket Smoothie')

streamlit.text ('🐔 Hard-Boiled Free Range Eggs')

streamlit.text ('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index ('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include
Fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
Fruit_to_show=my_fruit_list.loc[Fruits_selected]

streamlit.dataframe (Fruit_to_show)


streamlit.header("Fruityvice Fruit Advice!")

fruit_choice=streamlit.text_input('What fruit would you like information about','Kiwi')
streamlit.write ('The user entered ' ,fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
   
