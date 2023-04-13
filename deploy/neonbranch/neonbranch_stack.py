from aws_cdk import (
    CfnOutput,
    Stack,
    aws_lambda as lmbda,
)
from constructs import Construct


class NeonbranchStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        function_neonbranch = lmbda.Function(
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

        function_neonbranch_url = function_neonbranch.add_function_url(
            auth_type=lmbda.FunctionUrlAuthType.NONE,
        )

        CfnOutput(
            scope=self,
            id="url",
            value=function_neonbranch_url.url,
        )
