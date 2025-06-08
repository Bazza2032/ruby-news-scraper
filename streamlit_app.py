import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Global Rugby News", layout="wide")
st.title("🏉 Rugby Headlines Around the World")

URL = "https://www.rugbypass.com/news/"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    articles = soup.find_all("div", class_="article-block")

    if not articles:
        st.warning("No rugby articles found — the site structure may have changed.")

    for article in articles[:10]:
        title_tag = article.find("h4", class_="article-title")
        summary_tag = article.find("p", class_="excerpt")
        link_tag = article.find("a", href=True)

        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            summary = summary_tag.get_text(strip=True) if summary_tag else "No summary available."
            link = link_tag["href"]

            st.subheader(title)
            st.write(summary)
            st.markdown(f"[Read More]({link})")
            st.markdown("---")

except Exception as e:
    st.error("❌ Failed to fetch or parse rugby articles.")
    st.exception(e)
