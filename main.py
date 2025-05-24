import pandas as pd
from sklearn.neighbors import NearestNeighbors
import streamlit as st
import numpy as np
import re

# MUST be first Streamlit command
st.set_page_config(layout="wide", page_title="SkillSwapGPT", page_icon="🚀")


# Load and clean data
@st.cache_data
def load_data():
    df = pd.read_csv('it_skills.csv')
    df = df.drop_duplicates(subset=['skill_name'])
    df['related_skills'] = df['related_skills'].fillna('')
    return df


skills_df = load_data()


# Normalize skill names for matching
def normalize_skill_name(skill):
    # Remove special characters and make lowercase
    skill = re.sub(r'[^a-zA-Z0-9\s]', '', skill.lower())
    # Replace common variations
    skill = skill.replace(" ", "").replace("-", "").replace("_", "")
    return skill


# Get all unique skills and create normalized versions
all_skills = set(skills_df['skill_name'])
skill_normalization_map = {}
for skill in all_skills:
    skill_normalization_map[normalize_skill_name(skill)] = skill

# Add related skills to our map
for skills in skills_df['related_skills']:
    related = [s.strip() for s in skills.split(',') if s.strip()]
    for skill in related:
        normalized = normalize_skill_name(skill)
        if normalized not in skill_normalization_map:
            skill_normalization_map[normalized] = skill
            all_skills.add(skill)

all_skills = sorted(all_skills)

# Create skill matrix
skill_matrix = pd.DataFrame(0, index=skills_df.index, columns=all_skills)

for idx, row in skills_df.iterrows():
    main_skill = row['skill_name']
    related = [s.strip() for s in row['related_skills'].split(',') if s.strip()]

    skill_matrix.loc[idx, main_skill] = 1
    for skill in related:
        if skill in all_skills:
            skill_matrix.loc[idx, skill] = 1

# Train model
model = NearestNeighbors(n_neighbors=10, metric='cosine')
model.fit(skill_matrix)


# Recommendation function
def recommend_skills(user_skills):
    user_skills = [s.strip() for s in user_skills.split(',')]
    valid_skills = []

    for skill in user_skills:
        normalized = normalize_skill_name(skill)
        if normalized in skill_normalization_map:
            valid_skills.append(skill_normalization_map[normalized])

    if not valid_skills:
        return []

    # Create user vector
    user_vector = pd.Series(0, index=all_skills)
    for skill in valid_skills:
        user_vector[skill] = 1

    # Get recommendations
    distances, indices = model.kneighbors([user_vector])

    recommendations = []
    seen = set(s.lower() for s in valid_skills)

    for idx in indices[0]:
        skill = skills_df.iloc[idx]['skill_name']
        if skill.lower() not in seen:
            recommendations.append({
                'skill': skill,
                'category': skills_df.iloc[idx]['category'],
                'confidence': (1 - distances[0][indices[0].tolist().index(idx)]) * 100,
                'related': skills_df.iloc[idx]['related_skills']
            })
            seen.add(skill.lower())

    return sorted(recommendations, key=lambda x: -x['confidence'])[:3]  # Top 3 recommendations


# Enhanced UI
st.title("🚀 SkillSwapGPT - IT Skill Recommender")
st.markdown("""
Enter your current skills below (comma separated) to get personalized recommendations for what to learn next!
""")

user_input = st.text_input(
    "Enter your skills (comma separated):",
    "Python, JavaScript",
    help="Try variations like 'DeepLearning' or 'c++' - we'll understand it!"
)

if st.button("Get Recommendations", help="Click to get your personalized skill recommendations"):
    recommendations = recommend_skills(user_input)

    if recommendations:
        st.subheader("Top 3 Recommended Skills:")
        for i, rec in enumerate(recommendations, 1):
            with st.expander(f"🌟 {i}. {rec['skill']} ({rec['category']}) - {rec['confidence']:.0f}% match"):
                st.markdown(f"""
                **Category:** {rec['category']}  
                **Confidence Score:** {rec['confidence']:.0f}%  
                **Related Skills:** {rec['related'] or 'None'}
                """)
                st.progress(int(rec['confidence']))
    else:
        st.warning("""
        No valid skills recognized. Try some of these examples:
        - Python, JavaScript, SQL
        - AWS, Docker, Kubernetes
        - MachineLearning, DeepLearning
        - C++, Csharp
        """)
