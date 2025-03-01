import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a bar chart for average scores by gender
def average_scores_by_gender(df):
    # Gets the average math, reading and writing score for each gender
    avg_scores = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
    # Plots the data
    avg_scores.plot(kind='bar', figsize=(8, 6))
    plt.title('Average Scores by Gender')
    plt.ylabel('Average Score')
    plt.xticks(rotation=0) # Makes the text go horoizontally
    plt.savefig('Assignment1/Q2/results/average_scores_by_gender.png')
    plt.show()

# Create a stacked bar chart for test preparation completion by gender
def test_prep_by_race(df):
    # Group by race/ethnicity and test preparation course completion
    prep_by_race = df.groupby(['race/ethnicity', 'test preparation course']).size().unstack()

    # Getting the percentage for each group
    prep_percentage = prep_by_race.div(prep_by_race.sum(axis=1), axis=0) * 100

    # Plotting the data
    prep_percentage.completed.plot(kind='bar', figsize=(8, 6))
    plt.title('Percentage of Students Who Completed the Test Preparation Course by Race/Ethnicity\n') # Newline for formatting
    plt.xlabel('Race/Ethnicity')
    plt.ylabel('Percentage of Students')
    plt.xticks(rotation=0) # Makes the text go horoizontally
    plt.savefig('Assignment1/Q2/results/test_prep_by_race.png')
    plt.show()

# Create a box plot for math scores by parental level of education
def math_score_by_parental_education(df):
    # This orders the data more cleanly
    education_order = [
        "some high school", 
        "high school", 
        "some college", 
        "associate's degree", 
        "bachelor's degree", 
        "master's degree"
    ]

    # Plot box plot for math scores by parental level of education
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='parental level of education', y='math score', data=df, order=education_order)
    plt.title('Math Score Distribution by Parental Level of Education')
    plt.xticks(rotation=10) # Makes text fit while looking kind of nice
    plt.savefig('Assignment1/Q2/results/math_score_by_parental_education.png')
    plt.show()

# Create a bar chart for average scores by free/reduced lunch or standard lunch
def avg_scores_by_lunch_type(df):
    avg_scores = df.groupby('lunch')[['math score', 'reading score', 'writing score']].mean()
    avg_scores.plot(kind='bar', figsize=(8, 6))
    plt.title('Average Scores by Lunch Type')
    plt.ylabel('Average Score')
    plt.xticks(rotation=0)
    plt.savefig('Assignment1/Q2/results/avg_scores_by_lunch_type.png')
    plt.show()

# Create a box plot for math, reading, and writing scores by test preparation course
def test_prep_impact(df):
    plt.figure(figsize=(12, 8)) # More graphs need more space
    subjects = ['math score', 'reading score', 'writing score']
    # Making the boxplots for each subject
    for i, subject in enumerate(subjects, 1):
        plt.subplot(1, 3, i)
        sns.boxplot(x='test preparation course', y=subject, data=df)
        plt.title(f'{subject.capitalize()} by Test Prep Course')

    plt.tight_layout() # Makes everything fit a little better together
    plt.savefig('Assignment1/Q2/results/test_prep_impact.png')
    plt.show()

df = pd.read_csv('Assignment1/Q2/data_clean/clean_students_performance.csv')
average_scores_by_gender(df)
test_prep_by_race(df)
math_score_by_parental_education(df)
avg_scores_by_lunch_type(df)
test_prep_impact(df)