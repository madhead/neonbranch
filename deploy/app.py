#!/usr/bin/env python3
import aws_cdk as cdk

from neonbranch.neonbranch_stack import NeonbranchStack

app = cdk.App()

NeonbranchStack(app, "NeonbranchStack")

app.synth()
