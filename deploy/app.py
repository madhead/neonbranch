#!/usr/bin/env python3
import aws_cdk as cdk

from neonbranch.neonbranch_stack import NeonbranchStack

app = cdk.App()
environment = app.node.try_get_context("environment")

if environment:
    stack_name = f"NeonbranchStack-{environment}"
else:
    stack_name = "NeonbranchStack"

NeonbranchStack(app, stack_name)

app.synth()
