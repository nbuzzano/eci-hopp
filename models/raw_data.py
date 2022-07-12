# import numpy as np
import pandas as pd
import os

LOCAL_PATH = 'data'
ROOT_PATH = LOCAL_PATH

loan_agency_product_name = pd.read_csv(f"{ROOT_PATH}/loan_agency_product_name.csv")
loan_dindexdto_dataset = pd.read_csv(f"{ROOT_PATH}/loan_dindexedto_dataset.csv")
loan_funding_origination_info = pd.read_csv(f"{ROOT_PATH}/loan_funding_origination_info.csv")

loan_payments_dataset = pd.read_csv(f"{ROOT_PATH}/loan_payments_dataset.csv")
loan_payments_dataset['Target'] = loan_payments_dataset['PaymentPrincipal']

loan_payments_dataset_scoring = pd.read_csv(
    f"{ROOT_PATH}/loan_payments_dataset_scoring.csv", 
    names=['PaymentCode', 'PaymentPrincipal'], 
    header=None, 
    dtype={'PaymentCode': str}
)
