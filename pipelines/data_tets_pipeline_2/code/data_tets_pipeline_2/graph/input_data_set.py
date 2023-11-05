from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from data_tets_pipeline_2.config.ConfigStore import *
from data_tets_pipeline_2.udfs.UDFs import *

def input_data_set(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("Churn", StringType(), True), StructField("AccountWeeks", StringType(), True), StructField("ContractRenewal", StringType(), True), StructField("DataPlan", StringType(), True), StructField("DataUsage", StringType(), True), StructField("CustServCalls", StringType(), True), StructField("DayMins", StringType(), True), StructField("DayCalls", StringType(), True), StructField("MonthlyCharge", StringType(), True), StructField("OverageFee", StringType(), True), StructField("RoamMins", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/mnt/data/case4/telecom_churn.csv")
