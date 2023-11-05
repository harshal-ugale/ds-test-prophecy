from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from data_tets_pipeline_2.config.ConfigStore import *
from data_tets_pipeline_2.udfs.UDFs import *
from prophecy.utils import *
from data_tets_pipeline_2.graph import *

def pipeline(spark: SparkSession) -> None:
    df_input_data_set = input_data_set(spark)
    df_OrderBy_1 = OrderBy_1(spark, df_input_data_set)
    output_data_set(spark, df_OrderBy_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/data_tets_pipeline_2")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/data_tets_pipeline_2", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/data_tets_pipeline_2")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
