import pulumi
import pulumi_aws as aws

# Create an AWS resource (S3 Bucket)
bucket = aws.s3.Bucket('my-bucket',
                   website=aws.s3.BucketWebsiteArgs(
                   index_document='index.html')
                   )

ownership_controls = aws.s3.BucketOwnershipControls(
    'ownership-controls',
    bucket=bucket.id,
    rule=aws.s3.BucketOwnershipControlsRuleArgs(
        object_ownership='ObjectWriter'
    )
)

public_access_block = aws.s3.BucketPublicAccessBlock(
    'public-access-block',
    bucket=bucket.id,
    block_public_acls=False
)

bucketObject = aws.s3.BucketObject(
    'index.html',
    bucket=bucket.id,
    source=pulumi.FileAsset('./index.html'),
    content_type='text/html',
    acl='public-read',
    opts=pulumi.ResourceOptions(depends_on=[public_access_block])
)

azs = aws.get_availability_zones(state="available")

pulumi.export('bucket_name', bucket.id)
pulumi.export('bucket_endpoint', pulumi.Output.concat('http://', bucket.website_endpoint))
pulumi.export('azs', azs.names)
