import streamlit as st

st.header("Cau 2")  # C
options = st.multiselect("Your favorite colors:",
                         options=["Green", "Yellow", "Red", "Blue"],
                         default=["Yellow", "Red"])
st.write("You selected:", options)

st.header("Cau 4")
image_path = "Module_1\\Week_4\\Homework\\data\\dog.jpeg"
# argument "width" only takes int or None -> C
st.image(image_path, caption="A dog", width=None, channels="BGR")

st.header("Cau 7")  # D
with st.form("My form"):
    col1, col2 = st.columns(2)
    first_name = col1.text_input("First Name")
    last_name = col2.text_input("Last Name")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"First Name: {first_name} - Last Name: {last_name}")


st.header("Cau 8")  # A
uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

st.header("Cau 9")  # st.slider() cannot write code -> D
st.code("write code with 'st.code()'")
with st.echo():
    st.write("write code with 'st.echo()")
st.markdown("`write code with 'st.markdown()`")
