# API to PetClinic

### Installation Guide
* Clone this repository [here](https://github.com/Vitaly182/flask_sqlalchemy_marshmallow_postgres_docker.git).
* Run "docker-compose up" to start the application.
* Connect to the API using Postman on port 5000.
### API Endpoints

| HTTP    | Endpoints                                  | Action                                                       | Body Required |
|---------|--------------------------------------------|--------------------------------------------------------------|---------------|
| CLIENTS |
| POST    | 127.0.0.1:5000/clients                     | To create a new client                                       | Yes           |
| PUT     | 127.0.0.1:5000/client/clientId             | To update a single client                                    | Yes           |
| PATCH   | 127.0.0.1:5000/client/clientId             | To edit the details of a single client                       | Yes           |
| GET     | 127.0.0.1:5000/clients                     | To retrieve all clients                                      | ---           |
| GET     | 127.0.0.1:5000/client/clientId             | To retrieve a single client                                  | ---           |
| GET     | 127.0.0.1:5000/clients/search/search_signs | To retrieve all clients that first_name fit the search_signs | ---           |
| DELETE  | 127.0.0.1:5000/client/clientId             | To delete a client                                           | ---           |
| PETS    | 
| POST    | 127.0.0.1:5000/pets                        | To create a new pet                                          | Yes           |
| PUT     | 127.0.0.1:5000/pet/petId                   | To update a single pet                                       | Yes           |
| PATCH   | 127.0.0.1:5000/pet/petId                   | To edit the details of a single pet                          | Yes           |
| GET     | 127.0.0.1:5000/pets                        | To retrieve all pets                                         | ---           |
| GET     | 127.0.0.1:5000/pet/petId                   | To retrieve a single pet                                     | ---           |
| GET     | 127.0.0.1:5000/pets/search/search_signs    | To retrieve all pets that pet_name fit the search_signs      | ---           |
| DELETE  | 127.0.0.1:5000/pet/petId                   | To delete a pet                                              | ---           |


### Body Examples

#### Clients - POST / PUT (all fields required)

{
    "first_name":"name_1",
    "last_name":"name_2",
    "phone":"89266765656515",
    "city":"M_2"
}

#### Clients - PATCH

{
    "phone": "892667656565415"
}

#### Pets - POST (only field "petname" required)

{
    "petname":"Pet_1",
    "birth_date":"2021-01-01",
    "description":"des_1",
    "owner_id":"1"
}

#### Pets - PUT / PATCH

{
    "birth_date":"2021-01-01",
    "description":"des_1",
    "owner_id":"1"
}


