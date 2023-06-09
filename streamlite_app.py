import streamlit

import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


# import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
#streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_selected = streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruit_to_show = my_fruit_list.loc[fruits_selected]
  
#display the table on the page
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruit_to_show)


#New Section to display fruitvice api response
# streamlit.header('Fruityvice Fruit Advice')
# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)

# import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())


#New Section to display fruitvice api response - file formats 
# streamlit.header('Fruityvice Fruit Advice')
# try: 
#   fruit_choice = streamlit.text_input('What fruit would you like information about?')
#   if not fruit_choice:
#     streamlit.error("Please select a fruit to get information.")
#   else:
#     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#     fruityvice_normalized =  pandas.json_normalize(fruityvice_response.json())
#     streamlit.dataframe(fruityvice_normalized)

#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
	fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
	fruityvice_normalized =  pandas.json_normalize(fruityvice_response.json())
	return fruityvice_normalized

#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = streamlit.text_input('What fruit would you like infomration about?')
if not fruit_choice:
	streamlit.error("Please select a fruit to get information.")
else:
	back_from_function = get_fruityvice_data(fruit_choice)
	streamlit.dataframe(back_from_function)

    
except URLError as e:
streamlit.error()


  
# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)

# import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())





# new line with table format
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Table with details
# streamlit.dataframe(fruityvice_normalized)


#don't run anything past here while we troubleshoot 
streamlit.stop()

#file_import
# import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)


my_cur = my_cnx.cursor()
my_cur.execute("Select * from fruit_load_list")
my_data_row = my_cur.fetchone()
# streamlit.text("The fruit load list contains:")
# streamlit.text(my_data_row)
# streamlit.Header("The fruit load list contains:")
# streamlit.dataframe(my_data_row)
my_data_rows = my_cur.fetchall()
streamlit.Header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)










