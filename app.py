#!/usr/bin/env python3

from aws_cdk import App, Environment
from mnsys_isucon.mnsys_isucon_stack import PrivateIsuStack
from context import context

app = App(context=context)

PrivateIsuStack(
    app,
    "PrivateIsuStack",
    env=Environment(region="ap-northeast-1"),
)

app.synth()
