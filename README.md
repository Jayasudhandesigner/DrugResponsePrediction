# Drug Response Prediction using Machine Learning

## 📌 Project Overview
This project develops a **machine learning model** to predict **patient responses to drugs** based on **biomarkers** (e.g., age, genetic markers, blood levels).  
The model, inspired by Pfizer’s **precision medicine** initiatives, uses the **Gradient Boosting Classifier** to classify drug response as **positive (1) or negative (0)**.

## 🚀 Features
- **Synthetic dataset generation** for biomarker-based drug response analysis.
- **Data preprocessing**, including scaling, missing value handling, and encoding.
- **Machine learning model (Gradient Boosting)** for classification.
- **Performance evaluation** with accuracy score and classification report.
- **Feature importance visualization** to understand biomarker impact.

## 🐂 Project Structure
```
├── generate_dataset.py         # Generates synthetic biomarker dataset
├── train_model.py              # Trains model and makes predictions
├── biomarker_response_data.csv # Synthetic dataset (Generated)
├── README.md                   # Project documentation
```

## 🛠️ Installation & Setup

### 1️⃣ Install Dependencies
Ensure you have **Python 3.7+** installed. Then, install required libraries:

```sh
pip install pandas numpy scikit-learn matplotlib
```

### 2️⃣ Generate the Dataset
Run the script to create a **synthetic dataset**:

```sh
python generate_dataset.py
```

This will generate `biomarker_response_data.csv`.

### 3️⃣ Train the Model & Predict
Run the model training and prediction script:

```sh
python train_model.py
```

This will:
- Train the model
- Print accuracy and classification report
- Show feature importance plot
- Predict drug response for a sample patient

## 🧑‍💻 Usage
To make a new prediction, modify `train_model.py` by changing the sample **age, genetic marker, and blood level**:

```python
new_patient = pd.DataFrame([[50, 0.6, 45]], columns=['age', 'genetic_marker', 'blood_level'])
```

Then, re-run:

```sh
python train_model.py
```

## 💊 Expected Output
- **Accuracy Score** (target: >85%)
- **Feature Importance Graph**
- **Example Prediction:**
  ```
  Predicted Response (1 = Positive, 0 = Negative): 1
  ```

## 🏥 Application in Precision Medicine
- **Pharmaceutical Use Case:** Predicts patient response, helping companies like **Pfizer** optimize drug trials.
- **AI in Healthcare:** Reduces clinical trial failures, aiding personalized treatment plans.

## 📚 References
1. Pfizer. (2023). "ATTR-CM Study with AI." [pfizer.com](https://www.pfizer.com)
2. Scikit-learn Documentation. ["GradientBoostingClassifier."](https://scikit-learn.org)

---

🚀 **Contribute & Improve:** Feel free to modify the model or improve dataset accuracy!  
#DrugResponsePrediction

