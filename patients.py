from tokenize import String
import pandas as pd
from datetime import datetime
from ._base import DataFrameFromJSONMixin


class Patients(DataFrameFromJSONMixin):
    def __init__(self, path):
        super().__init__(path)

    def get_age(self, dob, input_date):
        '''
        Question 1-1
        Calculate the age of the patient.

        Create a function that calculates the age based on the birthday and a given date. This will be used to apply to each row of the
        patient dataframe. 

        For example if the dob is 2000-01-01 and the input_date is 2024-01-03 then the age is 24

        inputs: 
        dob: string birthdate of patient
        input_date: string date used to calculate the age. yyyy-mm-dd

        Output:
        age_years: integer the age of the patient in years 
        '''
        dob = datetime.strptime(dob, "%Y-%m-%d")
        input_date = datetime.strptime(input_date, "%Y-%m-%d")

        age = input_date.year - dob.year - ((input_date.month, input_date.day) < (dob.month, dob.day))
        return age

        # raise NotImplementedError

    def get_marital_status(self, df: pd.DataFrame):

    
        df['maritalStatus'] = df['maritalStatus'].apply(lambda x: x.get('text', 'Unknown') if isinstance(x, dict) else 'Unknown')
        
        # Define expected categories
        categories = ["Divorced", "Married", "Widowed", "Never Married"]
        
        # Perform one-hot encoding
        for category in categories:
            df[f'married_{category}'] = (df['maritalStatus'] == category).astype(int)
        
        # Drop original maritalStatus column
        df.drop(columns=['maritalStatus'], inplace=True)
        
        return df

    def pipeline(self):
        """
        Pipeline function to process patient data.
        """
        patient_df = self.data

        # Apply age calculation
        patient_df["age"] = patient_df['birthDate'].apply(lambda x: self.get_age(x, '2023-11-05'))

        # Apply marital status encoding
        patient_df = self.get_marital_status(patient_df)

        # Return only the required columns
        return patient_df[['id', 'age', 'married_Divorced', 'married_Married', 'married_Widowed', 'married_Never Married']]