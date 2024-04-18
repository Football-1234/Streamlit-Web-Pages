import streamlit as st

st.write("## <center>Let's make something awesome together</center>", unsafe_allow_html=True)
st.write("<center>Drop us a line, or give us a heads up if you're interested in visiting us.</center>", unsafe_allow_html=True)

st.write("---")
st.markdown("<div style='color: #3366ff;font-size: 30px;font-weight: bold;text-align: center;'> Get in touch, Let's walk about your project!</div>",unsafe_allow_html=True)
contact_form="""
<form action="https://formsubmit.co/zahranzahid886@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
<input type="text" name="name" placeholder="Your name" required>
<input type="email" name="email" placeholder="Your email" required>
<textarea name="message" placeholder="Your message here" required></textarea>
<button type="submit">Send</button>
</form>
"""

# use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")

left_column, right_column=st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()

# for remove Hamburger Menu and Streamlit Header
hide_st_style="""
<style>
#Main Menu {visibility: hidden;}
footer {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)