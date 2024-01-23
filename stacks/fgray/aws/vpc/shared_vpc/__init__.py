import pulumi_aws as aws

from pulumi import ComponentResource, ResourceOptions, export


class SharedVPCArgs(object):
    def __init__(self,
                 name: str,
                 cidr_block: str,
                 dns_hostnames: bool = True,
                 dns_support: bool = True) -> None:
        self.name = name
        self.cidr_block = cidr_block
        self.dns_hostnames = dns_hostnames
        self.dns_support = dns_support


class SharedVPC(ComponentResource):
    def __init__(self,
                 name: str,
                 args: SharedVPCArgs,
                 opts: ResourceOptions = None) -> None:
        super().__init__('instructure:net:SharedVPC', name, {}, opts)
        self.vpc = aws.ec2.Vpc(
            args.name,
            cidr_block=args.cidr_block,
            enable_dns_hostnames=args.dns_hostnames,
            enable_dns_support=args.dns_support,
            tags={
                'Name': args.name
            },
            opts=ResourceOptions(parent=self)
        )


export('SharedVPC', SharedVPC)