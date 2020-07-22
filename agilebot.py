

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


def FetchResourceslist():
    # Executing a GraphQL API in RASA using python

    print("Hello from agile bot function")

    _transport = RequestsHTTPTransport(
        url='https://wlivfllgizadjcmus3gp35izou.appsync-api.us-east-1.amazonaws.com/graphql',
        headers={
            "Content-type": "application/json",
            "x-api-key":"da2-v7a3ylacdvg4vn37ta4fik4ypu",
        },
        use_json=True,
    )
    client = Client(
        transport=_transport,
        fetch_schema_from_transport=True,
    )

    query = gql('''
        query{
            listResources{
            items{
            resourceName,
            resource_id,
            created_at
            }
           }
         }
    ''')

    resp = client.execute(query)
    print(resp)
   # modified_data = result['continents'][2]
   # print("modified_data is {}".format(modified_data))
    return resp
