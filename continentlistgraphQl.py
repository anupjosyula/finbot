

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


def FetchContinentslist():
    # Executing a GraphQL API in RASA using python

    print("Hello from FetchContinentslist")

    _transport = RequestsHTTPTransport(
        url='https://countries.trevorblades.com/',
        use_json=True,
    )
    client = Client(
        transport=_transport,
        fetch_schema_from_transport=True,
    )

    query = gql('''
        query getContinents {
          continents {
            code
            name
          }
        }
    ''')
    result = client.execute(query)
    print(result)
   # modified_data = result['continents'][2]
   # print("modified_data is {}".format(modified_data))
    return result
