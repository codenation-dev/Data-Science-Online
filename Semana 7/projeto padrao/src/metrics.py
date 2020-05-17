import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error


class Metrics:
    def __init__(self):
        pass

    def calculate_regression(self, y_true, y_pred):
        '''
        Calculate the metrics from a regression problem
        :param y_true: Numpy.ndarray or Pandas.Series
        :param y_pred: Numpy.ndarray or Pandas.Series
        :return: Dict with metrics
        '''
        mean_abs_err = mean_absolute_error(y_true, y_pred)
        mean_sqr_err = mean_squared_error(y_true, y_pred)
        return {'mean_abs_err' : mean_abs_err, 'mean_sqr_err' : mean_sqr_err}
    