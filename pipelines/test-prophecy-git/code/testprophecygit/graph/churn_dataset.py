from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testprophecygit.config.ConfigStore import *
from testprophecygit.udfs.UDFs import *

def churn_dataset(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("Churn", StringType(), True), StructField("AccountWeeks", StringType(), True), StructField("ContractRenewal", StringType(), True), StructField("DataPlan", StringType(), True), StructField("DataUsage", StringType(), True), StructField("CustServCalls", StringType(), True), StructField("DayMins", StringType(), True), StructField("DayCalls", StringType(), True), StructField("MonthlyCharge", StringType(), True), StructField("OverageFee", StringType(), True), StructField("RoamMins", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/mnt/data/Prophecy_H/telecom_churn.csv")
