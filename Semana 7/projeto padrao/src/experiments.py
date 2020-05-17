import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from catboost import CatBoostRegressor

from preprocessing import Preprocessing
from data_source import DataSource 
from metrics import Metrics

class Experiments:
    def __init__(self):
        self.tested_algorithms = {'linear' : LinearRegression(),
                                  'ridge' : Ridge(), 
                                  'decision_tree' : DecisionTreeRegressor(), 
                                  'random_forest': RandomForestRegressor(), 
                                  'svm': SVR(),
                                  'catboost': CatBoostRegressor()}
        self.dict_of_models = None
        
        
    def train_model(self, X_train, y_train):
        '''
        Train the model with especified experiments
        :param X_train: pd.DataFrame with train data
        :param y_train: pd.Series with train labels
        :return: Dict with trained model
        '''
        for alg in self.tested_algorithms.keys():   
            print('Treinando o modelo ', alg)
            test = self.tested_algorithms[alg]
            print(test)
            test.fit(X_train, y_train)
            if self.dict_of_models is None:
                self.dict_of_models = {alg : test}
            else: 
                self.dict_of_models.update({alg:test})
        return self.dict_of_models

    def run_experiment(self):
        '''
        Run especified experiments
        :return: Dict with metrics
        '''
        pre = Preprocessing()
        print('Reading Data')
        train_df = DataSource().read_data(etapa_treino = True)
        test_df, y_test = DataSource().read_data(etapa_treino = False)
        y_test = y_test['SalePrice']
        print('Preprocessing Data')
        X_train, y_train = pre.process(train_df, etapa_treino = True)
        print('Processing Test Data')
        X_test = pre.process(test_df[pre.train_features], etapa_treino=False)
        print('Training Model')
        models = Experiments().train_model(X_train, y_train)
        print('Running Metrics')
        for model in models.keys():
            print(model)
            y_pred = models[model].predict(X_test)
            print(Metrics().calculate_regression(y_test, pd.Series(y_pred)))
            metrics = Metrics().calculate_regression(y_test, pd.Series(y_pred))
            pd.DataFrame.from_dict(metrics, orient= 'index').to_csv('../output/'+model+'.csv')
        return metrics
                    