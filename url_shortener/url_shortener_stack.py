from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda,
    aws_apigateway,
    aws_certificatemanager as acm,
    aws_route53,
    aws_route53_targets
)
from constructs import Construct


class UrlShortenerStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        table = dynamodb.Table(self, "mapping-table", partition_key=dynamodb.Attribute(
            name="id", type=dynamodb.AttributeType.STRING))
        function = aws_lambda.Function(self, "backend",
                                       runtime=aws_lambda.Runtime.PYTHON_3_7,
                                       handler="handler.main",
                                       code=aws_lambda.Code.from_asset("./lambda"))
        table.grant_read_write_data(function)
        function.add_environment("TABLE_NAME", table.table_name)
        api = aws_apigateway.LambdaRestApi(self, 'api',
                                           handler=function,
                                           domain_name=aws_apigateway.DomainNameOptions(
                                               domain_name="go.crazymagic.studio",
                                               certificate=acm.Certificate.from_certificate_arn(self, 'cert', "arn:aws:acm:us-east-1:478062622781:certificate/3f63a892-ae7b-41f7-aba4-f32c64a42f6e")
                                           ))
        hosted_zone = aws_route53.HostedZone.from_hosted_zone_attributes(self, 'imported-hosted-zone',
                                                                         hosted_zone_id="Z03983981EGB0ECNSGVGV",
                                                                         zone_name="go.crazymagic.studio")
        route = aws_route53.ARecord(self, 'go-alias-record', zone=hosted_zone, target=aws_route53.RecordTarget.from_alias(aws_route53_targets.ApiGateway(api)))
