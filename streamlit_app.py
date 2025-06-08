import streamlit as st
import feedparser

st.set_page_config(page_title="Global Rugby News", layout="wide")
st.title("🏉 Rugby Headlines Around the World")

# Planet Rugby RSS feed
FEED_URL = "https://www.planetrugby.com/feed"

try:
    feed = feedparser.parse(FEED_URL)
    if not feed.entries:
        st.warning("No rugby articles found — RSS feed may be empty.")

    for entry in feed.entries[:10]:
        title = entry.title
        summary = entry.summary
        link = entry.link

        st.subheader(title)
        st.write(summary)
        st.markdown(f"[Read More]({link})")
        st.markdown("---")

except Exception as e:
    st.error("❌ Failed to fetch or parse the rugby feed.")
    st.exception(e)
