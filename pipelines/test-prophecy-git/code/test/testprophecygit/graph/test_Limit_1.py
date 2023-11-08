from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from testprophecygit.graph.Limit_1 import *
from testprophecygit.config.ConfigStore import *


class Limit_1Test(BaseTestCase):

    def test_unit_test_(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/testprophecygit/graph/Limit_1/in0/schema.json',
            'test/resources/data/testprophecygit/graph/Limit_1/in0/data/test_unit_test_.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/testprophecygit/graph/Limit_1/out/schema.json',
            'test/resources/data/testprophecygit/graph/Limit_1/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = Limit_1(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select("Churn", "ContractRenewal", "DataPlan", "DayMins", "DayCalls", "OverageFee", "RoamMins"),
            dfOutComputed.select(
              "Churn",
              "ContractRenewal",
              "DataPlan",
              "DayMins",
              "DayCalls",
              "OverageFee",
              "RoamMins"
            ),
            self.maxUnequalRowsToShow
        )

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        Utils.initializeFromArgs(
            self.spark,
            Namespace(
              file = f"configs/resources/config/{fabricName}.json",
              config = None,
              overrideJson = None,
              defaultConfFile = None
            )
        )
