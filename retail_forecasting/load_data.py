# #1. Import necessary libraries
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama

# #2. Create the database connection engine
# WARNING: Ensure the connection string is correctly configured before execution!
engine = create_engine('postgresql+psycopg2://retail_manager:secureRetail2024@localhost:5433/retail_db')

# #2. Instantiate the LLM model (Llama3.2 via Ollama)
llm = Ollama(model="llama3.2")

# #3. Create the output parser for processing LLM responses
output_parser = StrOutputParser()

# #3. Function to load data from CSV files into PostgreSQL tables
def load_data_to_db(csv_file, table_name, schema):
    """
    Reads data from a CSV file and inserts it into the specified PostgreSQL table.
    Handles errors and ensures data integrity.
    """
	try:
			# #4. Reads the CSV file into a Pandas DataFrame
			df = pd.read_csv(csv_file)

			# #5. Inserts the data into the specified PostgreSQL table
			df.to_sql(table_name, engine, schema=schema, if_exists='append', index=False)
			print(f"✅ Data from {csv_file} successfully inserted into {schema}.{table_name}.")
		
	except Exception as error:
			print(f"❌ Error inserting data from {csv_file} into {schema}.{table_name}: {error}")


# #6. Load data into the 'retail_project' schema
load_data_to_db('retail_suppliers.csv', 'suppliers', 'retail_project')
load_data_to_db('retail_categories.csv', 'categories', 'retail_project')
load_data_to_db('retail_products.csv', 'products', 'retail_project')
load_data_to_db('retail_customers.csv', 'customers', 'retail_project')
load_data_to_db('retail_sales.csv', 'sales', 'retail_project')
load_data_to_db('retail_inventory.csv', 'inventory', 'retail_project')
load_data_to_db('retail_seasonality.csv', 'seasonality', 'retail_project')
load_data_to_db('retail_forecast.csv', 'demand_forecast', 'retail_project')
load_data_to_db('retail_restocking.csv', 'restocking', 'retail_project')
load_data_to_db('retail_orders.csv', 'orders', 'retail_project')

print("\\n🎯 Data Load Completed Successfully! You can verify using pgAdmin if needed.\\n")
print("\\n🔍 Initiating AI-Driven Data Analysis. Please be patient while the system processes the insights!\\n")