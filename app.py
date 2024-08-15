import streamlit as st
from pathlib import Path
import google.generativeai as genai
from api_key import api_key

# Configure genai with the correct API key
genai.configure(api_key=api_key)

# Define generation configuration with slightly increased temperature
generation_config = {
    "temperature": 0.2,  # Slight increase for more varied responses
    "top_p": 0.9,
    "top_k": 10,
    "max_output_tokens": 4096,
}

# Apply safety settings
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Define system prompt with emphasis on detailed analysis
system_prompt = """
You are analyzing a medical image with the goal of identifying any abnormalities, potential conditions, or specific issues. Your analysis should be detailed, including:

1. **Visual Description**: Describe the visible features in the image.
2. **Potential Conditions**: Identify possible conditions such as skin allergies, rashes, or other visible anomalies.
3. **Specific Observations**: Mention any specific observations if the image shows signs of common conditions.
4. **Critical Advice**: Remind the user to seek a professional medical opinion.

Important Notes:
- Focus on detailed and specific analysis.
- Ensure only a single disclaimer at the end.
- If the image quality is unclear, mention that it cannot be analyzed.
- Include the phrase: "Consult with a Doctor before making any decision."
"""

# Set up the model with the updated version
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Set the page configuration
st.set_page_config(page_title="Medical Image Analysis", page_icon=":robot:")

# Set the logo
st.image("Screenshot (926).png", width=150)

# Set the title
st.title("Medical Image Analysis 👩‍⚕")

# Set the subtitle
st.subheader("An application that helps users diagnose issues by uploading medical images.")

# File uploader for image
uploaded_file = st.file_uploader("Submit your medical image for analysis.", type=["png", "jpg", "jpeg"])

# Button to trigger analysis
submit_button = st.button("Generate the Analysis")

# Add disclaimer to the response
disclaimer = "\n\n**Disclaimer:** I am an AI and cannot provide medical advice. Please consult a qualified medical professional for accurate diagnosis and treatment."

if submit_button:
    if uploaded_file is not None:
        try:
            # Read and process the image data
            image_data = uploaded_file.read()
            image_parts = [{"mime_type": "image/jpeg", "data": image_data}]
            prompt_parts = [image_parts[0], system_prompt]

            # Generate content using the model
            response = model.generate_content(prompt_parts)
            output_text = response.text.strip()

            # Format the output to ensure clarity
            if not output_text:
                output_text = "No analysis available. Please check the image quality or try a different image."

            # Ensure only one disclaimer is included
            output_text = output_text.replace(disclaimer, "")
            output_text += disclaimer

            st.write(output_text)
        except Exception as e:
            st.error(f"An error occurred while processing the image: {str(e)}")
    else:
        st.warning("Please upload an image file.")
