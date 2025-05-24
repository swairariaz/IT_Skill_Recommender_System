<div align="center">
  <h1>🚀 SkillSwapGPT</h1>
  <h3>AI-Powered IT Skill Recommender System</h3>

  <!-- YouTube Video Embed -->
  <div style="width: 100%; max-width: 700px; margin: 20px auto;">
    <iframe 
      width="100%" 
      height="394" 
      src="https://youtu.be/Ap_Q9KL5HEo" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen
      style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
    </iframe>
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
