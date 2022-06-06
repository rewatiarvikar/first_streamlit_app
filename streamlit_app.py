import streamlit
import pandas

streamlit.title("My parents New Healthy diner")
streamlit.header("Breakfast menu")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, spinach & Rocket Smoothie")
streamlit.text("🥑🍞 Avocado Toast")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruiy_list = my_fruit_list.set_index('Fruit')

streamlit.mutiselect("Pick some fruits:" ,list(my_fruit_list.index))
