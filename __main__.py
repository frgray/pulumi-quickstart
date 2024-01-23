"""An AWS Python Pulumi program"""

from pulumi import StackReference
import pulumi_aws as aws

pul
s3 = StackReference('stacks/instructure/aws/s3')
vpc = StackReference('stacks/instructure/aws/vpc')