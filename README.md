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
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "user": "test 5",
            "description": "test album 5",
            "image": "https://simpleisbetterthancomplex.com",
            "created_at": "2020-07-01T09:09:38.323023Z",
            "updated_at": "2020-07-01T09:11:13.603775Z",
            "albums": [
                1
            ]
        },
        {
            "id": 2,
            "user": "test 6",
            "description": "test album 6",
            "image": "https://simpleisbetterthancomplex.com",
            "created_at": "2020-07-01T09:09:51.006959Z",
            "updated_at": "2020-07-01T09:09:51.007015Z",
            "albums": []
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
            "name": "Birthday bash 1",
            "description": "Birthday photos 1",
            "created_at": "2020-07-01T09:10:10.069375Z",
            "updated_at": "2020-07-01T09:11:19.612676Z",
            "photos": [
                {
                    "id": 1,
                    "user": "test 5",
                    "description": "test album 5",
                    "image": "https://simpleisbetterthancomplex.com",
                    "created_at": "2020-07-01T09:09:38.323023Z",
                    "updated_at": "2020-07-01T09:11:13.603775Z",
                    "albums": [
                        1
                    ]
                }
            ]
        }
    ]
}
```
