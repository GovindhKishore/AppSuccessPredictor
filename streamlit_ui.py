import streamlit as st
from predict import predict
from gemini_assist import generate_analysis

st.title("APP SUCCESS PREDICTOR")
st.write("")
_, middle_space, _ = st.columns([1, 3, 1])

with middle_space:
    category = st.selectbox("Select App Category",
                ['BOOKS_AND_REFERENCE', 'FAMILY', 'VIDEO_PLAYERS', 'BUSINESS',
       'HOUSE_AND_HOME', 'DATING', 'GAME', 'LIBRARIES_AND_DEMO',
       'FINANCE', 'HEALTH_AND_FITNESS', 'MEDICAL', 'ENTERTAINMENT',
       'TRAVEL_AND_LOCAL', 'GAME_ACTION', 'LIFESTYLE',
       'GAME_ROLE_PLAYING', 'EVENTS', 'PRODUCTIVITY', 'FOOD_AND_DRINK',
       'NEWS_AND_MAGAZINES', 'SPORTS', 'TOOLS', 'GAME_SIMULATION',
       'SOCIAL', 'PHOTOGRAPHY', 'AUTO_AND_VEHICLES', 'SHOPPING',
       'EDUCATION', 'COMMUNICATION', 'PERSONALIZATION', 'GAME_CARD',
       'ART_AND_DESIGN', 'PARENTING', 'MUSIC_AND_AUDIO', 'COMICS',
       'MAPS_AND_NAVIGATION', 'WEATHER', 'GAME_BOARD', 'GAME_STRATEGY',
       'GAME_SPORTS', 'BEAUTY', 'GAME_ADVENTURE', 'GAME_MUSIC',
       'GAME_RACING', 'GAME_PUZZLE', 'GAME_WORD'])
    st.success(f"CATEGORY: {category}")
    st.write("")

col1, col2 = st.columns(2)

with col1:
    content_rating = st.selectbox("Expected Content Rating",
                                  ['Everyone', 'Teen', 'Mature 17+', 'Everyone 10+',
                                   'Adults only 18+'])
    st.success(f"Expected rating: {content_rating}")
    st.write("")

    size = st.number_input("Size of the App(in kB)", min_value=0.0,
                           value=187000.0, step=100.0)
    st.success(f"Size: {size:.3f}")
    st.write("")

with col2:
    price = st.number_input("Enter price in Dollars",
                            min_value=0.0, value=0.0,
                            step=1.0)
    st.success(f"Price: {price:.2f}")
    st.write("")

    year = st.number_input("Enter expected realese year",
                           step=1, value=2025, min_value=2015, max_value=2026)
    st.success(f"Year: {year}")
    st.write("")

feature_map = {"Category": category, "Size": size, "Price": price,
               "Content Rating": content_rating, "year": year}

st.info("""
The success percentage and installs predictions provided by this app are solely based on historical app data, including factors like category, size, ratings, reviews, price, and release year. 
These predictions do not take into account other important aspects such as app design and user experience (UX), marketing efforts, competition in the market, external trends, or seasonal effects. 
As a result, the outputs should be considered as **data-driven estimates**, not guaranteed outcomes.
""")
st.write("")

if "predict_pressed" not in st.session_state:
    st.session_state["predict_pressed"] = False

left, middle_space, right  = st.columns([1.5, 1, 1])

with middle_space:
    if st.button("PREDICT"):
        st.session_state["predict_pressed"] = True
        percentile, installs = predict(category, size, price, content_rating, year)
        st.session_state["percentile"] = percentile
        st.session_state["installs"] = installs
        with left:
            st.metric(label="Success Percentile", value=f"{percentile:.2f} %",
                      help="This indicates the percentage of apps that have fewer installs "
                           "than your app based on historical data.")
        with right:
            st.metric(label="Predicted Installs", value=f"{int(installs)}",
                      help="This is the estimated number of installs your app might achieve "
                           "based on historical data.")
st.write("")
_, col2, _ = st.columns([1.2, 1, 1])

if "analysis_ready" not in st.session_state:
    st.session_state["analysis_ready"] = False

with col2:
    if st.button("GET GEMINI ANALYSIS"):
        if not st.session_state["predict_pressed"]:
            st.session_state["analysis_ready"] = False
            st.error("Please click the PREDICT button first.")
        else:
            st.session_state["analysis_ready"] = True
            st.session_state["analysis"] = generate_analysis(feature_map,
                                         f"{st.session_state['percentile']:.2f}",
                                         f"{int(st.session_state['installs'])}")
            st.session_state["predict_pressed"] = False

if st.session_state["analysis_ready"]:
    _, middle, _ = st.columns([1, 5, 1])
    with middle:
        st.info(st.session_state["analysis"])



