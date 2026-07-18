# ❤️ Heart Disease Predictor

A machine learning web application built with Streamlit that predicts the likelihood of heart disease using multiple classification models. The application provides an interactive interface where users can enter medical information and receive predictions from different machine learning algorithms.

---

## 🚀 Features

* Interactive and user-friendly Streamlit interface.
* Predict heart disease risk instantly.
* Supports predictions from multiple machine learning models:

  * Logistic Regression
  * Decision Tree
  * Random Forest
  * K-Nearest Neighbors (KNN)
  * Support Vector Machine (SVM)
* Bulk prediction using CSV files.
* Displays model information and performance.
* Fast and lightweight deployment.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Scikit-learn**
* **Pandas**
* **NumPy**
* **Pickle**

---

## 📂 Project Structure

```text
HeartDiseasePrediction/
│
├── app.py                  # Main Streamlit application
├── models/
│   ├── logistic.pkl
│   ├── decision_tree.pkl
│   ├── random_forest.pkl
│   ├── knn.pkl
│   └── svm.pkl
│
├── dataset/
│   └── heart.csv
│
├── requirements.txt
├── README.md
└── assets/
```

---

## 📊 Dataset Features

The application uses the following medical attributes:

| Feature                 | Description                       |
| ----------------------- | --------------------------------- |
| Age                     | Age of the patient                |
| Sex                     | Male/Female                       |
| Chest Pain Type         | Type of chest pain                |
| Resting Blood Pressure  | Blood pressure in mm Hg           |
| Cholesterol             | Serum cholesterol level           |
| Fasting Blood Sugar     | Blood sugar > 120 mg/dl           |
| Resting ECG             | Electrocardiographic results      |
| Maximum Heart Rate      | Maximum heart rate achieved       |
| Exercise-Induced Angina | Chest pain during exercise        |
| Oldpeak                 | ST depression induced by exercise |
| ST Slope                | Slope of the ST segment           |

---

## 🧠 Machine Learning Models

The following algorithms are used:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* K-Nearest Neighbors
* Support Vector Machine

The models are trained on heart disease data and serialized using Pickle.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/HeartDiseasePrediction.git
```

Move into the project directory:

```bash
cd HeartDiseasePrediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 📷 Application Screens

* Single patient prediction.
* Bulk prediction using CSV upload.
* Model comparison page.
* Prediction results dashboard.

---

## 📈 Future Improvements

* Add prediction confidence scores.
* Deploy using Streamlit Cloud.
* Improve model accuracy with hyperparameter tuning.
* Add visual analytics and charts.
* Integrate patient history tracking.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push to GitHub.

```bash
git push origin feature-name
```

5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Sourav**

B.Tech (AIML) Student at BIT Mesra

Passionate about Artificial Intelligence, Machine Learning, and Software Development.

⭐ If you found this project useful, consider giving it a star on GitHub!
