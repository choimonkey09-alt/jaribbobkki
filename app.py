import streamlit as st
import os
import streamlit.components.v1 as components

st.set_page_config(
    page_title="✨ 원희와 함께하는 갸루 뱀사다리 자리배치파티 🐍💖",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_html_app():
    html_file_path = os.path.join("htmls", "index.html")
    
    if os.path.exists(html_file_path):
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        return html_content
    else:
        return f"""
        <div style="font-family: sans-serif; color: #ff69b4; text-align: center; padding: 50px; background: #1a001a; min-height: 100vh;">
            <h1 style="color: #ffd700;">⚠️ 오류 발생!</h1>
            <p><code>{html_file_path}</code> 경로를 찾을 수 없습니다.</p>
            <p>GitHub 저장소의 <code>htmls/index.html</code> 위치에 파일이 정확히 업로드되었는지 확인해주세요!</p>
        </div>
        """

def main():
    html_code = load_html_app()
    # Render the full interactive web application via Streamlit components
    components.html(html_code, height=950, scrolling=True)

if __name__ == "__main__":
    main()
