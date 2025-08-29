📝 Student Study Habits – Part-Time Job Prediction
📌 Project Overview

This project analyzes student study habits and predicts whether a student will take a part-time job based on their academic and personal attributes.

It applies machine learning classification techniques to discover patterns between study behavior and the decision to work part-time.

📊 Dataset

File: student_study_habits.csv

Each row: represents one student.

Features (examples):

📖 Study Hours per Week

🎓 GPA / Grades

😥 Stress Levels

🏀 Extracurricular Activities

💰 Financial Need

🛌 Sleep Hours

...

Target Variable:

Part_time_job → (Yes = 1, No = 0)

🎯 Problem Statement

Given student study habits and background factors, predict if the student will go for a part-time job or not.

This is a binary classification problem.

⚙️ Requirements

Before running the notebook, install dependencies:

pip install pandas numpy matplotlib seaborn scikit-learn jupyter

🚀 How to Run

Clone or download this repository.

Open the Jupyter Notebook:

jupyter notebook task.ipynb


Run all cells step by step.

The notebook will:

Load and clean the dataset

Perform Exploratory Data Analysis (EDA)

Train classification models (Logistic Regression, Decision Tree, Random Forest, Naïve Bayes, etc.)

Predict if a student will take a part-time job

📈 Results & Model Comparison
Model	                Accuracy	       Notes
Naïve Bayes	            ~0.31%	      Works well with small data, but less accurate here
🌟 Random Forest	   ~0.69%	     ✅ Best accuracy, robust and reliable

👉 Random Forest outperformed all other models in terms of accuracy and overall performance.

🎯 Expected Output

📊 Data insights (visualizations & statistics)

📌 Model performance metrics (accuracy, precision, recall, F1-score)

🤖 Final Prediction: Will a student take a part-time job (Yes/No)?

✨ Conclusion:
Random Forest proved to be the most effective model for predicting part-time job decisions based on student study habits.