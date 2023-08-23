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
def get_fruit_vice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice=streamlit.text_input('What fruit would you like information about')
  if not fruit_choice:
    streamlit.error("Please select the fruit to get information")
  else:
    back_from_function=get_fruit_vice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()



def get_fruit_load_list ():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
if streamlit.button("View Our Fruit List- Add Your Favourites"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe (my_data_rows)

def insert_row_into_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into FRUIT_LOAD_LIST values ('"+ new_fruit + "')")
    return "Thanks for adding new fruit " + new_fruit

add_my_fruit=streamlit.text_input ('What Fruit would you like to add ')
if streamlit.button ("Add Fruit to list"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function=insert_row_into_snowflake(add_my_fruit)
  my_cnx.close()
  streamlit.text(back_from_function)



