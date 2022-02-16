# Healthcare (Stroke-prediction)

According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths.

So in an attempt to reduce the death from stroke, I tried to build a dummy model to predict whether a patient is likely to get stroke. This can help a patient in early detection and diagnosis of stroke.

To build this model I have leveraged a publicly available **[kaggle dataset](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset)**. Which consists following attributes

<details>
<summary><b>Column's Name and their definition</b></summary>

1. id: unique identifier
2. gender: "Male", "Female" or "Other"
3. age: age of the patient
4. hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
5. heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
6. ever_married: "No" or "Yes"
7. work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
8. Residence_type: "Rural" or "Urban"
9. avg_glucose_level: average glucose level in blood
10. bmi: body mass index
11. smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"\*
12. stroke: 1 if the patient had a stroke or 0 if not

</details>
<br>

## Model training (quick walkthrough)

- **[Distribution]:** The dataset was highly unbalanced so `SMOTE` is utilized for balancing it out
- **[Evaluation Metric]:** The recall value of stroke class was highly prioritized for model evaluation and hence was the metric for model performance evaluation.
- **[Feature Selection]:** According to Information gain's score with theshold 0.005 following features were good for stroke prediction `['age', 'hypertension', 'bmi', 'work_type_Self-employed', 'work_type_children']`
- **[Best Model]:** Out of following models `[LogisticRegression, DecisionTreeClassifier, XGBClassifier, SVC, RandomForestClassifier`, `SVM` was the best performer with recall value of 0.85 for the stroke class.

## Installation and user guide

The script for testing the model is made interactive which allows you to test it both on single input or a csv file containing multiple input and accept continuous query.

Also the script is dockerized and can be pulled directly from docker hub using the following command.

> `docker pull aman4004/predict_stroke`

After downloading the container in your system you can run it. As I said above the model has two mode of input, single input, and file input.

1. **[Single Input Mode]:** If you just want to test the model on single input you can run the container in this way. This will allow you enter your input manually but keep in mind that with this command you want be able to test the model with file.

   > `docker run -it aman4004/predict_stroke`

2. **[Both Input Mode|Recommended]:** If you want to try both mode of input you need to bind your local directory (where your input file is) with the container directory so that it can read your file. The syntax looks like this

   > `docker run -it -v <your local directory where your input file is>:/usr/app/ aman4004/predict_stroke`

   Example: If your input file is in desktop folder you can run it like this

   > `docker run -it -v C:/Users/myname/Desktop/:/usr/app/ aman4004/predict_stroke`

Now after running these command you can follow the instruction and you are ready to rock.
