import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
col1, col2 = st.columns([0.5, 0.5])

with col1:
    #st.image("images/photo.png")
    content2 = """
As I continue on my journey as a software developer, I'm constantly amazed by the new possibilities that emerge. Whether I'm automating tedious tasks, building data-driven web applications, or exploring the frontiers of artificial intelligence, Python is usually the first door I knock to help me bring my ideas to life. If you're also a Python and data science enthusiast, I'd love to connect and discuss our shared passion in this space. Who knows, maybe we can even collaborate on a project or two down the line! 
    
Below you can find some of the apps I have built in Python. Feel free to reach out anytime:
    
- Email: conveniencechibatamoto@gmail.com
- LinkedIn: https://www.linkedin.com/in/convenience-tinashe-chibatamoto
- Github: https://github.com/convenience-tinashe-chibatamoto
- Kaggle: https://www.kaggle.com/linedpenguin
"""
st.info(content2)

with col2:
    st.title("Convenience Tinashe Chibatamoto")
    content = """
Hello there! My name is Convenience, and I'm a software engineer, Python programmer and data science enthusiast. It's a pleasure to meet you.

I've been working with Python for the past 3 years, and I've grown to absolutely love this versatile and powerful programming language. What drew me to Python initially was its brevity and readability – the code just seems to flow naturally, which makes it a joy to work with. One of the things I enjoy most about being a Python programmer is the sense of community and collaboration. Python has a vibrant and supportive user base, and I've found that people are always willing to share their knowledge, contribute to open-source projects, and help each other grow. It's a truly rewarding experience to be a part of this dynamic ecosystem.

Over the years, I've had the opportunity to apply Python in a wide range of domains, from web development and data analysis to machine learning and automation. The rich ecosystem of libraries and frameworks, such as Django, NumPy, and TensorFlow, has been instrumental in helping me tackle complex problems and build robust, scalable applications. 
    """
    st.info(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("images/data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[View Source Code](https://github.com/convenience-tinashe-chibatamoto?tab=repositories)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[View Source Code](https://github.com/convenience-tinashe-chibatamoto?tab=repositories)")
