# 👥❌ Customer Churn Prediction Web Application

### 🚀 **Live Demo**

🔗 [Try the Application Here](https://your-streamlit-app-link-here) — **Instantly predict customer churn with an intuitive web interface!**

---

## 📌 Project Overview

Understanding why customers leave is critical for business success. This project offers a **data-driven solution** to predict churn using **machine learning**. Built with **Logistic Regression**, and deployed using **Streamlit**, it helps businesses identify at-risk customers and take timely action to retain them.

From **exploratory data analysis** to **model training, serialization (with Pickle & Joblib)**, and deployment — this project demonstrates a complete **ML lifecycle** with an emphasis on usability.

---

## 🛠️ Tech Stack & Tools

| Technology           | Purpose                                         |
|----------------------|-------------------------------------------------|
| 🐍 Python 3.8+       | Core language for analysis & modeling           |
| 🧪 Scikit-learn       | Model building, evaluation, preprocessing       |
| 🧠 Joblib & Pickle    | Model serialization & loading                   |
| 📊 Pandas & NumPy     | Data manipulation & numerical analysis          |
| 📈 Seaborn & Matplotlib | Visualization & EDA                            |
| ⚡ Streamlit           | Rapid development of interactive web UI        |

---

## ✨ Key Features

- 🔍 **Exploratory Data Analysis (EDA)** to uncover trends and patterns
- ⚙️ **Logistic Regression model** trained and serialized for deployment
- 💾 **Model storage using both `joblib` and `pickle`**
- 🧪 **Model evaluation** using real test sets (`x_test`, `y_test`)
- 🖥️ **Interactive Streamlit App** to make live churn predictions
- 📂 **Modular folder structure** for ease of understanding and scalability

---

## ⚙️ Setup & Run Locally

Get started in just a few steps:

### 1. Clone the Repository
```bash
git clone https://github.com/YourUsername/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```
### 2. Create & Activate a Virtual Environment
``` bash
python -m venv venv
```
### 3. Install Dependencies
``` bash
pip install -r requirements.txt
```
### 4. Run the Streamlit Application
``` bash
streamlit run app.py
```
#### Once the server starts, your browser will automatically open with the app interface.
---
## 📂 Project Structure
``` plaintext
Customer-Churn-Prediction/
│
├── Dataset/
│   └── Customer_Churn.csv              # Original dataset
│
├── Models/
│   ├── Logistic_Pipeline.pkl           # Pickled model pipeline
│   ├── model.joblib                    # Joblib serialized model
│   ├── x_test.pkl                      # Test features
│   └── y_test.pkl                      # Test labels
│
├── Notebooks/
│   ├── EDA.ipynb                       # Exploratory data analysis
│   ├── Training Model.ipynb            # Training and validation
│   ├── Testing Model.ipynb             # Model testing and evaluation
│   └── Rough Test.ipynb                # Miscellaneous experimentation
│
├── app.py                              # Streamlit app for UI
├── requirements.txt                    # Project dependencies
├── LICENSE                             # Open-source license
├── .gitignore                          # Ignored files/folders
└── README.md                           # Project documentation
```
---
## 🧰 Tools & Software Needed
| Tool                 | Link                                                    |
| -------------------- | ------------------------------------------------------- |
| 🐍 Python            | [python.org](https://www.python.org/downloads/)         |
| 🐙 GitHub            | [github.com](https://github.com/)                       |
| 📝 VS Code           | [code.visualstudio.com](https://code.visualstudio.com/) |
| 🖥️ Git CLI          | [git-scm.com](https://git-scm.com/downloads)            |
| ⚡ Streamlit          | [streamlit.io](https://streamlit.io/)                   |
| 🐳 Docker (optional) | [docker.com](https://www.docker.com/)                   |

---

## 👩‍💻 Contribution Guidelines
Contributions are **highly welcome!** Feel free to make this project better by following these steps:

1. Fork the repository
2. Create your feature branch:

   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add feature or fix description"
   ```
4. Push your branch:

   ```bash
   git push origin feature-name
   ```
5. Open a pull request and let’s discuss! 🚀

---

## 📜 License
This project is licensed under the **[MIT License](./LICENSE)** — feel free to use, modify, and distribute!
---
## 👤 Author

**Samarth Kumar Samal**
🔗 [GitHub Profile](https://github.com/Samarth-Kumar-Samal-Sam)

---

## 🙏 Acknowledgements

A big thanks to the open-source libraries and community:

- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [Streamlit](https://streamlit.io/)
- [Joblib](https://joblib.readthedocs.io/)
- [Pickle](https://docs.python.org/3/library/pickle.html)

---