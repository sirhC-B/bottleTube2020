import boto3

session = boto3.session.Session()

sqs = session.client('sqs', region_name='us-east-1')

r = sqs.send_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/790933937313/xmas2020',
    MessageAttributes={
    'MatNr':{ 'DataType': 'Number',
            'StringValue': '***',
            },
    'StudentName':{ 'DataType': 'String',
                    'StringValue': 'Chris Boesener',
            },
    'Email-Adresse':{ 'DataType': 'String',
                      'StringValue': 'boesener@th-brandenburg.de',
            },
    'ReplyUrl':{ 'DataType': 'String',
                 'StringValue': 'https://sqs.us-east-1.amazonaws.com/272763356340/testQueue',
            },},
    MessageBody=('ESA3 - SQS \n\n MatNr: *** \n StudentName: Chris Boesener \n Email-Adresse: boesener@th-brandenburg.de \n ReplyUrl: https://sqs.us-east-1.amazonaws.com/272763356340/testQueue \n\n Gesundes neues Jahr! ')
    )

print (r)
