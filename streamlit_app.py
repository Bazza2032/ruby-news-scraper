import streamlit as st
import feedparser

st.set_page_config(page_title="Rugby News Headlines", layout="wide")
st.title("🏉 Rugby Headlines Around the World")

FEED_URL = "https://news.google.com/rss/search?q=rugby+union&hl=en-GB&gl=GB&ceid=GB:en"

try:
    feed = feedparser.parse(FEED_URL)
    if not feed.entries:
        st.warning("No rugby articles found — Google feed may be empty.")

    for entry in feed.entries[:10]:
        title = entry.title
        raw_summary = entry.summary if "summary" in entry else "No summary available."
        clean_summary = BeautifulSoup(raw_summary, "html.parser").get_text()
        link = entry.link

        st.subheader(title)
        st.write(clean_summary)
        st.markdown(f"[Read More]({link})")
        st.markdown("---")

except Exception as e:
    st.error("❌ Failed to fetch or parse rugby headlines.")
    st.exception(e)
