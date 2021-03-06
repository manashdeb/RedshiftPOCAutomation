import json
import pytest

from aws_cdk import core
from redshift_poc_automation.redshift_poc_automation_stack import RedshiftPocAutomationStack


def get_template():
    app = core.App()
    RedshiftPocAutomationStack(app, "redshift-poc-automation")
    return json.dumps(app.synth().get_stack("redshift-poc-automation").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
