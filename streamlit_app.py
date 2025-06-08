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

    # ✅ Updated article structure
    articles = soup.find_all("li", class_="ListingListing__StyledListing-sc-1f1it3l-0")

    if not articles:
        st.warning("No rugby articles found — site layout may have changed.")

    for article in articles[:10]:
        title_tag = article.find("a")
        summary_tag = article.find("p")

        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag["href"]
            summary = summary_tag.get_text(strip=True) if summary_tag else "No summary available."

            st.subheader(title)
            st.write(summary)
            st.markdown(f"[Read More](https://www.rugbypass.com{link})")
            st.markdown("---")

except Exception as e:
    st.error("❌ Failed to fetch or parse rugby articles.")
    st.exception(e)
