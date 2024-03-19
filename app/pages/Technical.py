import streamlit as st
import os

# Get a list of all post files in the 'posts' directory
post_files = os.listdir('app/pages/tech_posts')

for post_file in post_files[::-1]:
    with open(os.path.join('app/pages/tech_posts/', post_file), 'r', encoding='utf-8') as f:
        post_content = f.read().split('\n')
    with st.container():
        st.markdown(f"### {post_content[0]}", unsafe_allow_html=True)  # Make the title bigger
        st.markdown(f"{post_content[2]}...", unsafe_allow_html=True)  # Display the first few sentences in italic
        
        with st.expander("Read more"):
            for line in post_content[3:]:
                st.write(line)
