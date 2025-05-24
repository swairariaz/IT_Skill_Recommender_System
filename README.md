<div align="center">
  <h1>🚀 SkillSwapGPT</h1>
  <h3>IT Skill Recommendation Engine</h3>
  
  <!-- Demo Video -->
  <iframe width="700" height="394" src="[https://www.youtube.com/embed/YOUR_ID](https://youtu.be/Ap_Q9KL5HEo?si=S_C-ISur9L2XIZVr)" frameborder="0" allowfullscreen></iframe>
</div>

## 🔍 Introduction
**SkillSwapGPT** is a machine learning-based recommendation system that suggests relevant IT skills to learn next based on your current skillset. Built with:

- **Python** for core functionality
- **Scikit-learn's Nearest Neighbors** for skill recommendations
- **Pandas** for data processing
- **Streamlit** for the web interface

The system analyzes skill relationships from the `it_skills.csv` dataset, where each skill is mapped to related technologies and categories. When users input their current skills, the algorithm calculates the closest matching skills using cosine similarity and returns the top recommendations with confidence scores.

Key features implemented:
- Case-insensitive skill matching (handles variations like "DeepLearning" or "deep learning")
- Dynamic skill relationship matrix generation
- Confidence percentage scoring
- Clean, interactive Streamlit UI
</div>
