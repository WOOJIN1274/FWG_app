import streamlit as st

def app():
    st.title("RAG")
    
    # 보기 옵션 선택
    option = st.radio("보기 옵션을 선택하세요:", ["RAG Documentation", "GPT Model"])

    if option == "RAG Documentation":
        st.write("RAG 관련 문서를 아래에서 확인하세요:")
        st.markdown(
            """
            <iframe src="https://chow-unbiased-wallaby.ngrok-free.app/" 
                    width="100%" height="800px" style="border:none;"></iframe>
            """,
            unsafe_allow_html=True
        )

    elif option == "GPT Model":
        st.write("GPT 모델 관련 내용을 아래에서 확인하세요:")
        st.write("현재 GPT 모델 관련 페이지는 iframe으로 표시할 수 없습니다. 아래 버튼을 클릭하면 새 탭에서 열립니다:")
        if st.button("Visit GPT Model"):
            st.write("GPT 모델 관련 링크로 이동 중입니다...")
            st.markdown("[Visit GPT Model](https://chatgpt.com/)", unsafe_allow_html=True)

# 메인 실행
if __name__ == "__main__":
    app()
