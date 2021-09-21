import numpy as np

from sklearn.ensemble import IsolationForest
from sklearn.covariance import EllipticEnvelope
from sklearn.neighbors import LocalOutlierFactor


class OutlierDetection:
    def __init__(self, data, features, target=None, method='isolation_forest'):
        self.data = data
        self.x = np.array(data[features].values).reshape(-1, 1)

        self.y = None
        if target:
            self.y = np.array(data[target].values)

        if method == 'iForest':
            self.method = IsolationForest()
        elif method == 'MCD':
            self.method = EllipticEnvelope()
        elif method == 'LOF':
            self.method = LocalOutlierFactor()
        else:
            raise ValueError(f"Method: '{method}' is not supported.")

    def detect_outliers(self):
        if self.x.shape[0] > 1:
            y_hat = self.method.fit_predict(X=self.x)
            outliers_idx = [i for i, y in enumerate(y_hat) if y == -1]
        else:
            outliers_idx = list()

        return outliers_idx

    def remove_outliers(self):
        outliers_idx = self.detect_outliers()
        new_data = self.data.drop(outliers_idx)

        return new_data
