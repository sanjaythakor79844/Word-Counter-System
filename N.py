import streamlit as st
st.set_page_config(page_title="Word Counter System", page_icon="🖋️")

# App Title
st.title("Word Counter System")
st.markdown("""
    This Program counts the number of words in the text you provide.
    - Enter your sentence or paragraph in the text box .
    - Click the **Count Words** button to view the result.
""")

# Text Area for Input
U_input = st.text_area(
    "Enter Text or Paragraph:",
    placeholder="Type or paste your paragraph here...",
    height=100
)

# Button to trigger word count
if st.button("Count Words"):
    if not U_input.strip():
        st.warning("Input cannot be empty. Please enter a paragraph or Text.")
    else:
        # Count words
        words = U_input.split()
        word_count = len(words)

        # Display the word count
        st.success(f"**Total Number of Words:** {word_count}")

# Footer
st.markdown("---")
st.markdown("Crafted with passion and powered by [Streamlit]")
