from redata.commons import issue_request

HEADERS = {'Content-Type': 'application/json'}


def test_issue_request():

    # Testing with Figshare API
    baseurl = "https://api.figshare.com/v2/"

    for article in [12966581, 97662]:
        url = baseurl + f'articles/{article}'
        response_data = issue_request.redata_request('GET', url,
                                                     headers=HEADERS)
        assert isinstance(response_data, dict)
