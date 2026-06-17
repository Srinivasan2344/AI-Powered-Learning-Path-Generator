import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df=pd.read_csv("data/student_engagement.csv")

X=df[["login_frequency","assignment_completion_rate","quiz_attempts","study_hours_per_week"]]

y=df["risk_level"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = RandomForestClassifier(random_state=42)
model.fit(X_train,y_train)

joblib.dump(model,"data/engagement_model,pkl")

print("accuracy:",model.score(X_test,y_test))