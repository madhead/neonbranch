from aws_cdk import (
    Stack,
    aws_lambda as lmbda
)
from constructs import Construct


class NeonbranchStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        functionNeonbranch = lmbda.Function(
            scope=self,
            id="neonbranch",
            function_name="neonbranch",
            architecture=lmbda.Architecture.ARM_64,
            runtime=lmbda.Runtime.PYTHON_3_9,
            code=lmbda.Code.from_asset(
                path="../lambda/neonbranch.zip"
            ),
            handler="lambda.neonbranch.handle",
        )
