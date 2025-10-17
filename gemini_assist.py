import google.generativeai as genai
import streamlit as st

API_KEY = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=API_KEY)

contents_tuning = genai.GenerationConfig(temperature=0.2,
                                         top_p=0.9)
model = genai.GenerativeModel('gemini-2.5-pro', generation_config=contents_tuning)

def generate_analysis(features, percentile, installs):
    prompt = f"""
        Analyze the following app idea based on its features and my model's prediction.

          App Features:
          Category: {features['Category']}, Size: {features['Size']} KB
          Price: ${features['Price']}, Content Rating: {features['Content Rating']}
          Year of Release: {features['year']}

          My Model's Prediction
          Predicted Installs: {installs} 
          Success Percentile: {percentile} % (the percentage of apps with fewer installs than this one)

          Your Task:
            Provide a brief, professional analysis for the app developer. 
            Based on the features and the prediction, list 2 potential strengths and 2 potential risks for this app idea in bullet points. 
            Keep the tone encouraging but realistic. Keep in mind that my model only predicts based on the category, 
            size, price, content rating, and year of release. It does not account for other factors like the app design, 
            user experience, marketing strategy, or competition in the app store.
            
            Your response will be shown directly to the user of the "App Success Predictor" app. Act as the analysis 
            engine of the app. Do not include any conversational introductions, greetings, or acknowledgements.
            Avoid phrases like "Of course, here is the analysis..." or "Thank you for sharing...". 
            Begin your response immediately with the "App Idea Analysis" heading.
        """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception:
        return "Error generating analysis."



