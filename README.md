## URL patterns

```
URL pattern: ^api/v1/albums/$ 
URL pattern: ^api/albums/{pk}/$ 
URL pattern: ^api/v1/photos/$ 
URL pattern: ^api/photos/{pk}/$ 
```


## Sample Response:

Method: GET

Api Endpoint: api/v1/photos/

Response:

```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "user": "test 2",
            "description": "test album 2",
            "image": "https://simpleis.com",
            "created_at": "2020-07-01T04:58:18.463360Z",
            "updated_at": "2020-07-01T04:58:18.463418Z",
            "albums": [
                {
                    "id": 1,
                    "name": "Birthday bash",
                    "description": "Birthday photos",
                    "created_at": "2020-07-01T04:58:32.667685Z",
                    "updated_at": "2020-07-01T04:59:36.381241Z",
                    "photos": [
                        1
                    ]
                }
            ]
        }
    ]
}
```
=============

Method: GET

Api Endpoint: api/v1/albums/

Response:

```

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Birthday bash",
            "description": "Birthday photos",
            "created_at": "2020-07-01T04:58:32.667685Z",
            "updated_at": "2020-07-01T04:59:36.381241Z",
            "photos": [
                1
            ]
        }
    ]
}
```
