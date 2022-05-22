# coding: utf-8

from random import random
import pandas as pd
EFFICACY = .9
N = 30000
INCIDENCE = .15


def got_covid(group):
    if group == "control":
        return random() < INCIDENCE
    else:
        if random() < INCIDENCE:
            return random() > EFFICACY
        else:
            return False


out = []
for i in range(N):
    if random() < .5:
        group = "control"
    else:
        group = "treatment"

    out.append({"group": group, "covid": got_covid(group)})

df = pd.DataFrame(out)
df.to_csv("clinical_trial.csv", index=False)
