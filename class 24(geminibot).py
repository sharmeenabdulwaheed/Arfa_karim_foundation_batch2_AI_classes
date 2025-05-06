import streamlit as st
from google import genai
from google.genai import types

api_key = "your_api"
st.title("Python Course Admission Assistant")
st.write("Ask any questions about enrolling in our Python course.")

# User input box
user_input = st.text_input("Your question:", "")

# Submit button
if st.button("Submit") and user_input:
    client = genai.Client(api_key=api_key)

    model = "gemini-1.5-flash"

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_input),
            ],
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=0.1,
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="BLOCK_ONLY_HIGH",
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="BLOCK_MEDIUM_AND_ABOVE",
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                threshold="BLOCK_LOW_AND_ABOVE",
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="BLOCK_LOW_AND_ABOVE",
            ),
        ],
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are an assistant for a website that offers a Python course.
            Keep long and detailed responses. Focus on resolving student admission queries."""),
        ],
    )

    print("\nAssistant:", end=" ")
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        st.write(chunk.text, end="")
