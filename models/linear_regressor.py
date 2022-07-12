
from models.utils import save_experiment, timer, build_dataframe

from models.raw_data import loan_payments_dataset, loan_payments_dataset_scoring
from sklearn.linear_model import LinearRegression


from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.pipeline import Pipeline # !!!

from models.utils import Feature

def start_experiment():
	
    features = [
        Feature("PaymentPrincipal", loan_payments_dataset['PaymentPrincipal'], 1)
	]

    y = loan_payments_dataset["Target"].copy()
    x = build_dataframe(features)

    columns = [f.name for f in features]
    
    x = loan_payments_dataset[columns]
    y = loan_payments_dataset.Target

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=2022)
    model = LinearRegression().fit(X_train, y_train)

    y_predicted = model.predict(X_test)
    
    save_experiment(
		'linear_regression', model, features,
		y_predicted, y_test,
		metrics = [
			(mean_absolute_error, "mean_absolute_error"), 
		]
	)

start_experiment()