from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

DATA_FILE = "dataset/telecom_data.csv"

df = pd.read_csv(DATA_FILE)


@app.route("/")
def home():

    total_records = len(df)
    total_columns = len(df.columns)
    missing_values = int(df.isnull().sum().sum())
    duplicate_records = int(df.duplicated().sum())

    return render_template(
        "index.html",
        total_records=total_records,
        total_columns=total_columns,
        missing_values=missing_values,
        duplicate_records=duplicate_records
    )


@app.route("/governance")
def governance():

    return render_template("governance.html")


@app.route("/data-quality")
def data_quality():

    total_records = len(df)
    total_columns = len(df.columns)
    missing_values = int(df.isnull().sum().sum())
    duplicate_records = int(df.duplicated().sum())

    if missing_values == 0 and duplicate_records == 0:
        quality_status = "Good"
    else:
        quality_status = "Needs Improvement"

    return render_template(
        "data_quality.html",
        total_records=total_records,
        total_columns=total_columns,
        missing_values=missing_values,
        duplicate_records=duplicate_records,
        quality_status=quality_status
    )


@app.route("/security")
def security():

    return render_template("security.html")
@app.route("/lifecycle")
def lifecycle():

    return render_template("lifecycle.html")


if __name__ == "__main__":
    app.run(debug=False)