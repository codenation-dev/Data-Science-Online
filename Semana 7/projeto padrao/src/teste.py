import pandas as pd
from model_training import ModelTraining
from preprocessing import Preprocessing
from metrics import Metrics
from data_source import DataSource
from experiments import Experiments
from model_inference import ModelInference

model = Experiments().run_experiment()

ModelTraining().model_training()

ModelInference().predict()
