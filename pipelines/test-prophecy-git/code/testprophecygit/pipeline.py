from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from testprophecygit.config.ConfigStore import *
from testprophecygit.udfs.UDFs import *
from prophecy.utils import *
from testprophecygit.graph import *

def pipeline(spark: SparkSession) -> None:
    df_churn_dataset = churn_dataset(spark)
    df_Limit_1 = Limit_1(spark, df_churn_dataset)
    churn_limited_data(spark, df_Limit_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/test-prophecy-git")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/test-prophecy-git", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/test-prophecy-git")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
