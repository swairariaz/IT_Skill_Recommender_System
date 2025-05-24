<div align="center">
  <h1>🚀 SkillSwapGPT</h1>
  <h3>AI-Powered IT Skill Recommender System</h3>

  ## 📺 Demo

<div align="center" style="margin: 2rem 0;">
  <a href="https://www.youtube.com/watch?v=Ap_Q9KL5HEo" target="_blank">
    <img 
      src="https://img.youtube.com/vi/Ap_Q9KL5HEo/maxresdefault.jpg" 
      alt="SkillSwapGPT Demo" 
      style="width:100%; max-width:800px; border-radius:8px; cursor:pointer; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"
    >
    <br>
  </a>
</div>
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
