import pulumi
from shared_vpc import SharedVPC, SharedVPCArgs

config = pulumi.Config()
vpc_name = config.require('vpc_name')
cidr_block = config.require('vpc_cidr_block')

vpc_args = SharedVPCArgs(
    name=vpc_name,
    cidr_block=cidr_block
)

created_vpc = SharedVPC('shared-vpc', vpc_args)

pulumi.export('vpc_id', created_vpc.vpc.id)
