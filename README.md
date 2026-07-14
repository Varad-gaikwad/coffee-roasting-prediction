# ☕ Coffee Roast Quality Predictor

A neural network built using **TensorFlow/Keras** to predict whether a coffee roast is **Good** or **Bad** based on roasting temperature and roasting time.

The project also includes a **Streamlit web application**, allowing users to interact with the trained model through a clean browser interface.

---

## 🚀 Live Features

-Link: https://coffee-roasting-prediction.streamlit.app/

- Predicts coffee roast quality in real time
- Interactive Streamlit web interface
- Neural Network built using TensorFlow/Keras
- Automatic feature normalization
- Binary classification using Sigmoid activation
- Training and evaluation pipeline included

---

## 🧠 Problem Statement

Coffee roasting quality depends heavily on two factors:

- 🌡️ Roasting Temperature
- ⏱️ Roasting Time

This project trains a neural network to learn the relationship between these variables and determine whether a roast is likely to be **Good** or **Bad**.

---

# 📊 Dataset

The dataset contains the following features:

| Feature | Description |
|----------|-------------|
| Temperature | Roasting temperature (°C) |
| Time | Roasting time (minutes) |

**Target**

| Label | Meaning |
|--------|---------|
| 0 | Bad Roast |
| 1 | Good Roast |

---

# 🏗️ Model Architecture

The model is built using TensorFlow's Sequential API.

```text
Input Layer
      ↓
Normalization Layer
      ↓
Dense (16) → ReLU
      ↓
Dense (8) → ReLU
      ↓
Dense (4) → ReLU
      ↓
Dense (1) → Sigmoid
```

The output neuron uses the **Sigmoid activation function**, producing a probability between **0 and 1**.

---

# ⚙️ Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Pandas
- Scikit-Learn
- Streamlit

---

# 📈 Training Pipeline

### 1. Data Loading

The coffee roasting dataset is loaded using **Pandas**.

---

### 2. Train/Test Split

The dataset is split into:

- 80% Training
- 20% Testing

using Scikit-Learn's `train_test_split()`.

---

### 3. Feature Normalization

A TensorFlow **Normalization Layer** computes the mean and standard deviation from the training data and automatically scales all inputs before they enter the neural network.

---

### 4. Model Training

The network is trained using:

- **Adam Optimizer**
- **Binary Cross Entropy Loss**
- **Sigmoid Output Layer**

---

### 5. Evaluation

After training, the model is evaluated on unseen test data to measure its performance and generalization capability.

---

# 🌐 Streamlit Web Application

The trained model is deployed as a simple interactive web application.

Users can:

- Select roasting temperature
- Select roasting time
- Predict roast quality instantly

Example:

```
Temperature: 220°C
Time: 15 minutes

Prediction:
✅ Good Roast
Confidence: 99.35%
```
<img width="903" height="505" alt="image" src="https://github.com/user-attachments/assets/fc02649a-acab-41a8-9bbf-28a0986b03c9" />

---

# 📁 Project Structure

```text
coffee-roast-quality-predictor/
│
├── app.py                  # Streamlit web application
├── coffee_prediction.py    # Model training & prediction
├── coffee_model.keras      # Saved trained model
├── coffee_roasting_dataset.csv
├── requirements.txt
└── README.md
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/coffee-roast-quality-predictor.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📚 What I Learned

Through this project I gained practical experience with:

- Building Neural Networks using TensorFlow/Keras
- Binary Classification
- Feature Normalization
- Train/Test Splitting
- Model Evaluation
- Model Serialization (`.keras`)
- Deploying Machine Learning models using Streamlit
- Creating interactive ML applications


---

# 👨‍💻 Author

**Varad**

Computer Science Student • Machine Learning Enthusiast • Python Developer

This project was built as part of my machine learning learning journey while studying neural networks and TensorFlow.
