import json
import pathlib
import airflow.utils.dates
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# Generate DAG instance
dag = DAG(
    dag_id = "Apache_Airflow_Assignment",
    description = "Make Airflow DAG and Workflow",
    start_date = airflow.utils.dates.days_ago(1),
    schedule_interval = "@hourly",
    )

# Weather Forecast
def _weather_forecast():
    pass
# Operator
weather_forecast = PythonOperator(
    task_id = "weather_forecast",
    python_callable = _weather_forecast,
    dag = dag,
    )

# Seoul Public Bike
def _public_bike():
    pass
# Operator
public_bike = PythonOperator(
    task_id = "public_bike",
    python_callable = _public_bike,
    dag = dag,
    )

# Weather Extract
def _weather_extract():
    pass
# Operator
weather_extract = PythonOperator(
    task_id = "weather_extract",
    python_callable = _weather_extract,
    dag = dag,
    )

# Bike Extract
def _bike_extract():
    pass
# Operator
bike_extract = PythonOperator(
    task_id = "bike_extract",
    python_callable = _bike_extract,
    dag = dag,
    )

# Concat Dataset
# Operator
concat_dataset = BashOperator(
    task_id = "concat_dataset",
    bash_command = "date",
    dag = dag,
    )

# Model Training
def _model_training():
    pass
# Operator
model_training = PythonOperator(
    task_id = "model_training",
    python_callable = _model_training,
    dag = dag,
    )

# Predict
# Operator
predict = BashOperator(
    task_id = "predict",
    bash_command = "date",
    dag = dag,
    )


# Dependency
weather_forecast >> weather_extract
public_bike >> bike_extract
[weather_extract, bike_extract] >> concat_dataset >> model_training >> predict