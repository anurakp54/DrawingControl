import qrcode
import streamlit as st

header = st.container()

with header:
    st.title("Automatic QR Code Generator")
    st.markdown("*Type Drawing number to generate QR Code*")

    with st.form(key='Drawing_input_form', clear_on_submit=True):
        Drawing_Number = st.text_input("Drawing Number XX-XX-XXXX")
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            # Data to be encoded
            data = Drawing_Number

            # Encoding data using make() function
            img = qrcode.make( 'http://127.0.0.1:5000/'+data)
            # Saving as an image file
            img.save('/Users/mbpro/PycharmProjects/flask/data/temp_qr.png')

    st.image('/Users/mbpro/PycharmProjects/flask/data/temp_qr.png')