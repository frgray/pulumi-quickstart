import pulumi
import pulumi_aws as aws

from network.vpc import SharedVPC


config = pulumi.Config()
vpc_name = config.require('vpc_name')
cidr_block = config.require('vpc_cidr_block')

azs = aws.get_availability_zones(state="available")

created_vpc = SharedVPC(name=vpc_name,
                        availability_zones=azs.names[0:3],
                        cidr_block=cidr_block
                        )

pulumi.export('vpc_id', created_vpc.vpc.id)
# pulumi.export('route_tables', created_vpc.route_tables["private"])
# pulumi.export('private_subnet_ids', created_vpc.subnets["private"])
