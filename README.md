# ☕ Coffee Roasting Quality Predictor using TensorFlow

A beginner-friendly Machine Learning project that predicts whether a coffee roast is **Good** or **Bad** based on roasting **Temperature** and **Time** using a Neural Network built with TensorFlow and Keras.

---

## 📌 Project Overview

This project demonstrates the complete machine learning workflow:

- Loading a dataset
- Data preprocessing
- Splitting data into training and testing sets
- Feature normalization
- Building a Neural Network
- Training the model
- Evaluating model performance
- Making predictions from user input

This project was created for learning the fundamentals of **Artificial Neural Networks (ANNs)** using TensorFlow.

---

## 📂 Project Structure

```
Coffee-Roasting-Predictor/
│
├── coffee_prediction.py          # Main Python script
├── Coffee_predictor.ipynb        # Jupyter Notebook version
├── coffee_roasting_dataset.csv   # Dataset
├── README.md
```

---

## 🧠 Technologies Used

- Python 3.12
- TensorFlow / Keras
- Pandas
- NumPy
- Scikit-learn

---

## 📊 Dataset

The dataset contains **105 coffee roasting samples**.

### Features

| Feature | Description |
|---------|-------------|
| Temperature | Roasting temperature (°C) |
| Time | Roasting time (minutes) |

### Target

| Target | Meaning |
|---------|---------|
| GoodRoast | 1 = Good Roast, 0 = Bad Roast |

---

## 🏗 Neural Network Architecture

```
Input Layer
      │
Normalization Layer
      │
Dense Layer (8 neurons, ReLU)
      │
Dense Layer (4 neurons, ReLU)
      │
Output Layer (1 neuron, Sigmoid)
```

---

## ⚙ Model Configuration

| Parameter | Value |
|-----------|-------|
| Optimizer | Adam |
| Loss Function | Binary Crossentropy |
| Metric | Accuracy |
| Epochs | 1000 |

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Varad-gaikwad/coffee-roasting-prediction.git
```

### 2. Install dependencies

```bash
pip install tensorflow pandas numpy scikit-learn
```

### 3. Run the program

```bash
python coffee_prediction.py
```

---

## 💻 Example

```
Enter roasting temperature (°C): 205
Enter roasting time (minutes): 13

GOOD ROAST

```

---

## 📈 Results

The trained model achieved approximately **95% test accuracy** on the provided dataset.

*(Accuracy may vary slightly due to random train-test splitting.)*
<img width="299" height="132" alt="image" src="https://github.com/user-attachments/assets/e5379736-093f-4167-a86f-db198ff6dff3" />


---

## 📚 Concepts Covered

This project covers:

- Artificial Neural Networks (ANN)
- Data preprocessing
- Train/Test split
- Feature normalization
- Activation functions (ReLU & Sigmoid)
- Forward propagation
- Binary classification
- Model evaluation
- Prediction using trained models

---

## 🎯 Future Improvements

- Larger real-world coffee roasting dataset
- More roasting parameters (humidity, bean type, airflow)
- Hyperparameter tuning
- Save and load trained model
- Web interface using Flask or Streamlit
- Interactive visualization of training metrics

---

## 👨‍💻 Author

**Varad**

Built as a learning project to understand TensorFlow, Neural Networks, and Machine Learning fundamentals.

---

## ⭐ If you found this project helpful, consider giving it a star!
