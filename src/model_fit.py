# %%
import pandas as pd
from sklearn import tree
from sklearn import ensemble
from sklearn import pipeline
from sklearn import metrics

import matplotlib.pyplot as plt

from feature_engine.encoding import OneHotEncoder
from feature_engine.imputation import ArbitraryNumberImputer
from feature_engine.imputation import CategoricalImputer


# %%

df = pd.read_excel("data/data.xlsx")
df.head()

# %%

old_columns = df.columns.tolist()
txt_remove = "Com qual frequência esses eventos acontecem com você? ["
rename_columns = {i:i.replace(txt_remove,"").strip("]") for i in old_columns}
df = df.rename( columns=rename_columns )
df.head()

# %%

target = "Qual a sua altura em centímetros? Por favor use apenas números"
features = df.columns.tolist()[1:-1]

# %%
# Identificando os tipos de variáveis

cat_features = df[features].dtypes[ df[features].dtypes == 'object' ].index.tolist()
num_features = list(set( features ) - set( cat_features ))

def fix_altura(c):
    if c < 3:
        return c * 100
    else:
        return c

# Tirando valores que não conhecemos a target
df_train = df.dropna( subset=[target], how="all" )
df_train[target] = df_train[target].apply(fix_altura)

print(df_train[target].describe())

df_train[target].hist(bins=25)

# %%

# Definição do pipeline de Machine Learning
cat_imput = CategoricalImputer( variables=cat_features,
                                fill_value="Missing" )

num_imput = ArbitraryNumberImputer( variables=num_features,
                                    arbitrary_number=-999 )

onehot_task = OneHotEncoder(variables=cat_features)

rg_task = ensemble.GradientBoostingRegressor(random_state=42,
                                            n_estimators=300,
                                            learning_rate=0.85,
                                            subsample=0.7,
                                            max_depth=2,
                                            
                                        )

model_pipeline = pipeline.Pipeline(steps=[ ("cat_imputer", cat_imput),
                                           ("num_imputer", num_imput),
                                           ("onehot", onehot_task),
                                           ("model_tree", rg_task)  ]
)

model_pipeline.fit(df_train[features], df_train[target])

pred = model_pipeline.predict(df_train[features])
avg_abs_erro = metrics.mean_absolute_error(df_train[target], pred)
r2 = metrics.r2_score( df_train[target], pred )
print("Performance Árvore")
print("Médio do erro absoluto:", avg_abs_erro)
print("R2:", r2)
print(f"Foram usadas {df_train.shape[0]} respostas.")

# %%

df_model = pd.Series(
    {"model": model_pipeline,
    "features": features,
    "r2": r2,
    "mean_abs_err": avg_abs_erro}
)

df_model.to_pickle("models/model_tree.pkl")

# %%
