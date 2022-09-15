def test_page_not_found(client, image_path):
    """
    GIVEN a Flask application
    WHEN an invalid URL / Endpoint is requested (POST)
    THEN check that a '404 Not Found' status code is returned 
    """
    response = client.post('/invalid-path',
                           data={'imageFile': open(image_path, 'rb')})

    assert response.status_code == 404
    assert b'message' in response.data