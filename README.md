# APP SUCCESS PREDICTOR

## Description / Purpose
The APP SUCCESS PREDICTOR is a machine learning-based tool designed to help app developers estimate the potential success of their mobile applications before launch. By analyzing historical app data, the tool predicts the number of installs an app might achieve and provides a success percentile score, indicating how the app might perform relative to other apps in the market.

The tool uses an XGBoost regression model trained on preprocessed app data, considering features such as app category, size, price, content rating, and release year. Additionally, it leverages Google's Gemini AI to provide qualitative analysis of the app's potential strengths and risks.

## Installation Instructions

1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up your Google API key for Gemini AI:
   - Create a `.streamlit/secrets.toml` file
   - Add your Google API key: `GOOGLE_API_KEY = "your-api-key-here"`

## Usage Instructions / Examples

1. Train the model (optional, as a pre-trained model is included):
   ```
   python train_xgboost.py
   ```

2. Run the Streamlit web application:
   ```
   streamlit run streamlit_ui.py
   ```

3. In the web interface:
   - Select the app category from the dropdown menu
   - Choose the expected content rating
   - Enter the app size in kilobytes
   - Specify the price in dollars
   - Set the expected release year
   - Click "PREDICT" to get the success metrics
   - Click "GET GEMINI ANALYSIS" for AI-powered insights about your app idea

Example: For a productivity app of size 19,000 KB, priced at $0.00, with "Everyone" content rating, and a 2025 release year, the model will provide predicted installs and a success percentile.

## Dependencies
The project relies on the following Python packages:
- pandas (~=2.3.2): For data manipulation and analysis
- numpy (~=2.3.3): For numerical operations
- scikit-learn (~=1.7.2): For machine learning preprocessing and pipelines
- xgboost (~=3.0.5): For the gradient boosting model
- joblib (~=1.5.2): For model serialization
- streamlit (~=1.50.0): For the web interface
- google-generativeai (~=0.8.5): For AI-powered analysis using Google's Gemini

## Citation
Dataset used in this project: [Harshvir Singh – Cleaned Google Play Store Dataset](https://www.kaggle.com/datasets/harshvir04/cleaned-google-play-store-dataset)


## Notes and Tips

- **Model Limitations**: The predictions are based solely on the specified features (category, size, price, content rating, and release year) and do not account for other important factors like app design, user experience, marketing strategy, or market competition.

- **Data Directory**: The project uses data from the `data/` directory and saves models to the `models/` directory. 

- **Gemini AI Integration**: The AI analysis feature requires a valid Google API key with access to the Gemini API. Store this key securely in the Streamlit secrets file.

- **Log Transformation**: The model uses log transformation on the install numbers to handle the wide range of values, which is a common practice for this type of prediction task.

- **Percentile Calculation**: The success percentile indicates the percentage of apps that have fewer installs than the predicted value, providing context for the raw install numbers.
