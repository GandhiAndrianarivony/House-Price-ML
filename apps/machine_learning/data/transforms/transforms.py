from typing import Dict, Callable

import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin


class CategoricalMapper(BaseEstimator, TransformerMixin):
    def __init__(self, columns: Dict = None, cols_order=None):
        self.columns = columns
        self.cols_order = cols_order

    def fit(self, X, y=None):
        return self

    def transform(self, X: pd.DataFrame):
        X_copy = X.copy()

        # Encode categorical feature
        if self.columns is not None:
            for col_name in self.columns.keys():
                try:
                    X_copy[col_name] = getattr(X_copy, col_name).map(
                        self.columns[col_name]
                    )
                except:
                    continue

        return X_copy[self.cols_order]


class LogTransformer(BaseEstimator, TransformerMixin):
    """Class being used to log_transform feature data"""

    def __init__(self, columns=None):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X: pd.DataFrame):
        X_copy = X.copy()
        X_copy[self.columns] = X_copy[self.columns].apply(np.log1p, axis=1)
        return X_copy


class Imputer(BaseEstimator, TransformerMixin):
    def __init__(self, columns: Dict[str, list], statistics: Dict[str, Callable]):
        self.columns = columns
        self.statistics = statistics

    def fit(self, X, y=None):
        self.strategy_result = dict()

        if self.columns is not None:
            for strategy, cols in self.columns.items():
                self.strategy_result[strategy] = self.statistics[strategy](
                    X[cols], axis=0
                )

        return self

    def transform(self, X: pd.DataFrame):
        X_copy = X.copy()

        if self.columns is not None:
            for strategy, cols in self.columns.items():
                X_copy[cols] = np.where(
                    np.isnan(X[cols]), self.strategy_result[strategy], X[cols]
                )

        return X_copy
