
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class PHQFeatureEngineer(BaseEstimator, TransformerMixin):

    phq_cols = [
        "1. In a semester, how often have you had little interest or pleasure in doing things?",
        "2. In a semester, how often have you been feeling down, depressed or hopeless?",
        "3. In a semester, how often have you had trouble falling or staying asleep, or sleeping too much? ",
        "4. In a semester, how often have you been feeling tired or having little energy? ",
        "5. In a semester, how often have you had poor appetite or overeating? ",
        "6. In a semester, how often have you been feeling bad about yourself - or that you are a failure or have let yourself or your family down? ",
        "7. In a semester, how often have you been having trouble concentrating on things, such as reading the books or watching television? ",
        "8. In a semester, how often have you moved or spoke too slowly for other people to notice? Or you've been moving a lot more than usual because you've been restless? ",
        "9. In a semester, how often have you had thoughts that you would be better off dead, or of hurting yourself? ",
    ]

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        present_cols = [c for c in self.phq_cols if c in X.columns]
        for col in present_cols:
            X[col] = pd.to_numeric(X[col], errors="coerce").fillna(0).astype(int)

        # ── Derived features 
        if present_cols:
            X["phq_total"]           = X[present_cols].sum(axis=1)
            X["severe_symptom_count"] = (X[present_cols] >= 2).sum(axis=1)
        else:
            X["phq_total"]            = 0
            X["severe_symptom_count"] = 0

        return X