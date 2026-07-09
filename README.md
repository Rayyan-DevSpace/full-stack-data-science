<div align="center">

# 📚 Data Science & ML Learning Journey

*Learning by doing — one library at a time, one project at a time.*

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Progress](https://img.shields.io/badge/Progress-5%2F7%20topics-yellow?style=flat-square)
![Last Updated](https://img.shields.io/badge/Updated-July%202026-blue?style=flat-square)

</div>

---

### 👋 About

I'm learning data analysis, visualization, statistics, and machine learning from the ground up. This repo is my public log: every topic gets its own folder with a **course notebook** (concepts + practice) and a **project notebook** (something real built with it).

No tutorials copy-pasted blindly — every notebook here is something I've actually typed out and understood.

---

### 🧭 Roadmap

<table>
<tr><th>Stage</th><th>Topic</th><th>Status</th><th>Notebooks</th></tr>

<tr><td rowspan="5">📊 Data Handling & Viz</td>
<td>NumPy</td><td>✅ Done</td><td><a href="./01-numpy/numpy_course.ipynb">Course</a> · <a href="./01-numpy/numpy_project.ipynb">Project</a></td></tr>

<tr><td>Pandas</td><td>✅ Done</td><td><a href="./02-pandas/pandas_course.ipynb">Course</a> · <a href="./02-pandas/pandas_project.ipynb">Project</a></td></tr>

<tr><td>Matplotlib</td><td>✅ Done</td><td><a href="./03-matplotlib/matplotlib_course.ipynb">Course</a> · <a href="./03-matplotlib/matplotlib_project.ipynb">Project</a></td></tr>

<tr><td>Seaborn</td><td>✅ Done</td><td><a href="./04-seaborn/seaborn_course.ipynb">Course</a> · <a href="./04-seaborn/seaborn_project.ipynb">Project</a></td></tr>

<tr><td>Plotly</td><td>🔶 In Progress</td><td><a href="./05-plotly/plotly_course.ipynb">Course</a> · <a href="./05-plotly/plotly_project.ipynb">Project</a></td></tr>

<tr><td rowspan="2">📈 Foundations & ML</td>
<td>Statistics</td><td>🔜 Up Next</td><td>—</td></tr>

<tr><td>Machine Learning</td><td>🔜 Up Next</td><td>—</td></tr>

</table>

`✅ Done` &nbsp;·&nbsp; `🔶 In Progress` &nbsp;·&nbsp; `🔜 Up Next`

---

### 🗂️ Structure

Every topic follows the same two-file convention:

```text
0X-topic-name/
├── topic_course.ipynb    → notes, concepts, hands-on practice
└── topic_project.ipynb   → a small project applying the topic
```

<details>
<summary><b>Click to see the full folder tree</b></summary>

```text
learning-journey/
├── 01-numpy/
│   ├── numpy_course.ipynb
│   └── numpy_project.ipynb
├── 02-pandas/
│   ├── pandas_course.ipynb
│   └── pandas_project.ipynb
├── 03-matplotlib/
│   ├── matplotlib_course.ipynb
│   └── matplotlib_project.ipynb
├── 04-seaborn/
│   ├── seaborn_course.ipynb
│   └── seaborn_project.ipynb
├── 05-plotly/
│   ├── plotly_course.ipynb
│   └── plotly_project.ipynb
├── 06-statistics/
│   ├── statistics_course.ipynb
│   └── statistics_project.ipynb
├── 07-machine-learning/
│   ├── ml_course.ipynb
│   └── ml_project.ipynb
├── requirements.txt
└── README.md
```

</details>

New topics get added as `08-...`, `09-...` in the same pattern — no restructuring needed as the repo grows.

---

### ⚙️ Run It Locally

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
jupyter notebook
```

---

### 🎯 Why This Repo Exists

Most "learning in public" repos are a pile of disconnected notebooks. This one isn't:

- **Consistent structure** → every topic is easy to find and compare
- **Course + Project pairing** → I don't move on until I've built something with it
- **Visible progress** → the roadmap table above is the single source of truth

---

### 🔮 Coming Up

- [ ] Wrap up Plotly (interactive dashboards)
- [ ] Statistics — probability, distributions, hypothesis testing
- [ ] Machine Learning — scikit-learn, regression, classification, model evaluation
- [ ] Deep Learning — TensorFlow / PyTorch *(stretch goal)*

---

<div align="center">

If this helped you structure your own learning repo, a ⭐ would mean a lot.

</div>
