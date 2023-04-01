import streamlit as st
import pandas as pd
import numpy as np
import cv2 as cv


input = st.file_uploader(
    "Upload an Image to find bounds:",
    type=[".png", "jpg", "jpeg"],
    key="input_image"
)

image = []
if input is not None:
    image = cv.imdecode(np.frombuffer(input.getvalue(), dtype=np.uint8), cv.IMREAD_COLOR) # type: ignore
else:
    st.stop()


gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# remove noise
img = cv.GaussianBlur(gray,(3,3),0)

# convolute with proper kernels
laplacian = cv.Laplacian(img,cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)  # x
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)  # y

output = np.asarray(image)
laplacian = np.asarray(laplacian)
sobelx = np.asarray(sobelx)
sobely = np.asarray(sobely)

def image_convert_from_single_channel(px_by_px):
    red_channel = px_by_px
    green_channel = px_by_px
    blue_channel = px_by_px # np.zeros_like(red_channel)

    # Stack the three channels along a new axis to create a 3D array
    image = np.stack([red_channel, green_channel, blue_channel], axis=2)

    return image


# print(output)
"# Original"
st.image(output, clamp=True, channels='BGR')
"# Laplacian"
st.image(image_convert_from_single_channel(laplacian), clamp=True, channels='BGR')
"# Sobel X"
st.image(image_convert_from_single_channel(sobelx), clamp=True, channels='BGR')
"# Sobel Y"
st.image(image_convert_from_single_channel(sobely), clamp=True, channels='BGR')