import streamlit as st
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
from PIL import Image
import io
import requests
import json
import pandas as pd
import httpx
# fastapi endpoint
url = 'http://ml_layer:8000'
endpoint = '/segmentation'
APPLICATION_SERVICE_URL=url+endpoint

application_form = st.form(key='application-layer')
application_email = application_form.text_input('Enter your email')
application_password = application_form.text_input('Enter your password')
application_submit = application_form.form_submit_button('Submit')

st.title('DeepLabV3 image segmentation')


if application_submit:
    login_data = {"email": application_email,"password":application_password}
    r = requests.post(APPLICATION_SERVICE_URL + "login", data=json.dumps(login_data))
    st.write(f'hello {r.text}')
    if r.status_code == 200:
        st.write('''Obtain semantic segmentation maps of the image in input via DeepLabV3 implemented in PyTorch.
                This streamlit example uses a FastAPI service as backend.
                Visit this URL at `:8000/docs` for FastAPI documentation.''') # description and instructions

        image = st.file_uploader('insert image')  # image upload widget


        def process(image, server_url: str):

            m = MultipartEncoder(
                fields={'file': ('filename', image, 'image/jpeg')}
                )

            r = requests.post(server_url,
                            data=m,
                            headers={'Content-Type': m.content_type},
                            timeout=8000)

            return r


        if st.button('Get segmentation map'):

            if image == None:
                st.write("Insert an image!")  # handle case with no image
            else:
                segments = process(image, url+endpoint)
                segmented_image = Image.open(io.BytesIO(segments.content)).convert('RGB')
                st.image([image, segmented_image], width=300)  # output dyptich
