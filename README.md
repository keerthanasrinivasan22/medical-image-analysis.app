# medical-image-analysis.app
This repository features a Streamlit application designed for analyzing medical images. The application leverages a generative AI model to provide visual descriptions, potential conditions, and advice based on the uploaded images.

## Features
- **Upload and Analyze**: Submit medical images for analysis.
- **Detailed Visual Descriptions**: Get a comprehensive description of the image features.
- **Potential Conditions Identification**: Insights into possible conditions such as aphthous ulcers, herpes simplex infections, or allergic reactions.
- **Critical Advice**: Important reminders to consult a medical professional.
- **Generative AI Integration**: Utilizes Google’s Gemini 1.5 Flash model for insightful analysis.

## How to Use
1. **Upload a Medical Image**: Use the file uploader to submit your image.
2. **Generate Analysis**: Click "Generate the Analysis" to receive results.
3. **Review the Results**: Read the analysis, potential conditions, and critical advice.

## Sample Output
1. **Visual Description**: The image shows a close-up of a person's lower lip with a red patch and white halo.
2. **Potential Conditions**:
   - **Aphthous Ulcers**
   - **Herpes Simplex Virus (HSV) Infection**
   - **Allergic Reaction**
3. **Specific Observations**: The red patch with a white halo is characteristic of aphthous ulcers.
4. **Critical Advice**: Consult a medical professional for accurate diagnosis and treatment.

## Deployment
- [Streamlit App Link](https://medical-image-analysis.streamlit.app)

## Dependencies
- `streamlit`
- `google-generativeai`
- Other libraries listed in `requirements.txt`


