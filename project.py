import pandas as pd
import numpy as np
from xgboost import XGBClassifier

modelclf = XGBClassifier()
modelclf.load_model("./model/model.bin")


def cal_pro(test_data):

    ldata = list(test_data.values())
    ldata = ldata[1:]
    ndata = np.array(ldata).reshape((1, -1))
    dfdata = pd.DataFrame(ndata, columns=["Age", "Baseline heart rate", "Uric acid", "D-dimer", "Chlorine", "GCS", "GFR"])
    result = round(modelclf.predict_proba(dfdata)[0][1], 4)
    return result

