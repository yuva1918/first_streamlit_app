import streamlit
import pandas
import requests
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
try:
  fruit_choice=streamlit.text_input('What fruit would you like information about')
  if not fruit_choice:
    streamlit.error("Please select the fruit to get information")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e
  streamlit.error()

streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows=my_cur.fetchall()
streamlit.header("Fruit load list contains")
streamlit.dataframe (my_data_rows)

add_my_fruit=streamlit.text_input ("What Fruit would you like to add ")
streamlit.write ("Thanks for adding " ,add_my_fruit)

my_cur.execute ("insert into FRUIT_LOAD_LIST values ('from streamlit')")


