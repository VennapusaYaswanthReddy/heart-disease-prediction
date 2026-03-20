# ❤️ Heart Disease Prediction System

## 📌 Project Overview

The **Heart Disease Prediction System** is a Machine Learning-based web application that predicts whether a patient is at risk of heart disease using medical attributes.
The system is built with **Python, Scikit-learn, and Streamlit**, and provides a simple interface for uploading datasets and viewing predictions.

---

## 🎯 Objectives

* Predict heart disease risk using patient data
* Provide an easy-to-use web interface
* Help in early detection and analysis
* Demonstrate ML model deployment using Streamlit

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Pickle
* **Frontend/UI:** Streamlit
* **Model:** Logistic Regression (or your model)

---

## 📂 Project Structure

```
heart-disease-project/
│── app.py               # Main Streamlit application
│── model.pkl            # Trained ML model
│── scaler.pkl           # Data scaler
│── train_model.py       # Model training script
│── heart.csv            # Dataset
│── README.md            # Project documentation
```

---

## 📊 Dataset Information

The dataset contains medical attributes such as:

* `age` – Age of the patient
* `sex` – Gender (1 = male, 0 = female)
* `cp` – Chest pain type
* `trestbps` – Resting blood pressure
* `chol` – Cholesterol level
* `fbs` – Fasting blood sugar
* `restecg` – Resting ECG results
* `thalach` – Maximum heart rate achieved
* `exang` – Exercise-induced angina
* `oldpeak` – ST depression
* `slope` – Slope of peak exercise
* `ca` – Number of major vessels
* `thal` – Thalassemia
* `target` – 1 (Disease), 0 (No Disease)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/heart-disease-project.git
cd heart-disease-project
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have requirements.txt, install manually:

```bash
pip install streamlit pandas scikit-learn
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🔐 Login Credentials

```
Username: admin
Password: 1234
```

---

## 🚀 Features

* 🔐 Login system using Streamlit session state
* 📁 Upload CSV dataset
* 📊 Dataset preview
* 🤖 Machine learning prediction
* 📈 Prediction results display
* 📊 Summary (High risk vs Low risk patients)

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Scaling
4. Model Training (Logistic Regression)
5. Model Saving using Pickle
6. Deployment using Streamlit

---

## 📸 Output Screens

* Login Page
* Dataset Upload
* Dataset Preview
* Prediction Results

---

## ⚠️ Limitations

* Model accuracy depends on dataset quality
* Not a replacement for medical diagnosis
* Requires proper feature format

---

## 🔮 Future Enhancements

* Add visualization (charts/graphs)
* Deploy on Streamlit Cloud / AWS
* Add user input form (manual prediction)
* Improve model accuracy with advanced algorithms

---

## 📌 Conclusion

This project demonstrates how Machine Learning can be integrated into a web application to provide real-time predictions. It is useful for learning end-to-end ML deployment.

---

## 👨‍💻 Author

**Yaswanth Reddy**
CSE (Machine Learning)

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub
