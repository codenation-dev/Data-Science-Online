import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Visualization:
    def __init__(self):
        pass
    def regression_viz(self, y_true, y_pred, nome):
        '''
        Visualize the quality of regression model
        :param y_true: pd.Series with true label values
        :param y_pred: pd.Series with predicted label values
        :param nome: Name of the file wich will be saved
        :return: Save files in specified path
        '''
        residual = y_pred - y_true
        data = pd.DataFrame({'pred' : y_pred, 'true' : y_true, 'residual': residual})
        plot1 = sns.distplot(data['residual'], bins = 50)
        plot2 = sns.scatterplot(x= 'true', y = 'residual', data = data)
        plt.savefig(plot1, '../data/'+nome+'_distplot.csv')
        plt.savefig(plot1, '../data/' + nome + 'scatterplot.csv')
        plt.show()