<div align="center">
  <h1>🚀 SkillSwapGPT</h1>
  <h3>AI-Powered IT Skill Recommender System</h3>

  ## 📺 Demo

<p align="center">
  <a href="https://youtu.be/Ap_Q9KL5HEo">
    <img src="https://www.youtube.com/watch?v=Ap_Q9KL5HEo" alt="Watch on YouTube" width="700"/>
  </a>
</p>
> Click the image to watch the full demo on YouTube.
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
