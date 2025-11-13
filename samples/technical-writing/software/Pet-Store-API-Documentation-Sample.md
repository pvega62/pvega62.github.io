---
title: Pet Store API Documentation Sample
slug: pet-store-api
sidebar_position: 3
id: pet-store-api
---
## Introduction
 
 This document provides an API reference for a sample Petstore server. The requests found here can help developers make calls to the Petstore server to send or request data about any pets and orders entered into the system.

With the Petstore API, a developer can: 
 
 **Pets**
 - Create, read, update, and delete pets in the database.
 - Upload an image for a pet.
 - Find pets by their status (available, pending, sold), tags, or unique identifiers.

**Store**
 - Get inventory of pets, categorized by status.
 - Place an order for a pet.
 - Find purchase orders by their ID.
 - Cancel an order.

**User**
 - Create a new user account (individually or from a list).
 - Log users in and out of the system.
 - Find a user by their ID.
 - Retrieve, update, and delete a user's information by their username. 

This example uses a dog (Krypto) and the ID number 210.
## Connection prerequisites

 The base URL of all API requests is `https://petstore3.swagger.io/api/v3`.
## Authentication
 To authenticate your connection to the Petstore's API, use OAuth 2.0 or an assigned API key. To request a key, email budbaker@bhavenpets.com.

  > For security purposes, don't share API keys with other users. If you suspect a breach in your API key's security, please contact your administrator immediately to revoke the old key and issue a new one.

# Functions
## Pets
With these API functions, you can manage the pets in your store's database.

### Adding a new pet
Adds a new pet to the store's database.

Endpoint: https://petstore3.swagger.io/api/v3/pet

Operation: `POST`

#### Examples
**API Key cURL Example**
```bash
POST "https://petstore3.swagger.io/api/v3/pet" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "api_key: <YOUR_API_KEY>" \
-d '{
  "id": 0,
  "name": "string",
  "category": {
    "id": 0,
    "name": "string"
  },
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}'
```

**OAuth 2.0 cURL Example**
```bash
POST "https://petstore3.swagger.io/api/v3/pet" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>" \
-d '{
  "id": 0,
  "name": "string",
  "category": {
    "id": 0,
    "name": "string"
  },
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}'
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | Successful operation|
| 400  | Invalid input |
| 404  | Pet not found |
| 422 | Validation exception |
| default | Unexpected error |

##### Response example

`200: Successful operation`
```json
{
  "id": 210,
  "name": "Krypto",
  "category": {
    "id": 1,
    "name": "Dogs"
  },
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
```

#### Parameters
##### Request body
| Name | Type | Description |
|------|------|-------------|
| body | Pet object | **(Required)** The `Pet` object to add to the store. |

### Updating an existing pet
Updates an existing pet by its ID.

Endpoint: https://petstore3.swagger.io/api/v3/pet

Operation: `PUT`
#### Examples
**API Key cURL Example**
```bash
PUT "https://petstore3.swagger.io/api/v3/pet" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "api_key: <YOUR_API_KEY>" \
-d '{
    "id": 210,
    "name": "Krypto",
    "status": "available"
  }'
```

**OAuth 2.0 cURL Example**
```bash
PUT "https://petstore3.swagger.io/api/v3/pet" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>" \
-d '{
    "id": 210,
    "name": "Krypto",
    "status": "available"
  }'
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | Successful operation |
| 400  | Invalid input |
| 404  | Pet not found |
| 422 | Validation exception |
| default | Unexpected error |

##### Response example
`200: Successful operation`
```json
{
  "id": 210,
  "name": "Krypto",
  "category": {
    "id": 1,
    "name": "Dogs"
  },
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
```
#### Parameters
##### Request body
| Name | Type | Description |
|------|------|-------------|
| body | Pet object | **(Required)** Pet object to update. |

### Finding a pet by status
Finds pets by their status.

Endpoint: https://petstore3.swagger.io/api/v3/pet/findByStatus

Operation: `GET`

#### Examples
**API Key cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/pet/findByStatus?status=available" \
-H "accept: application/json" \
-H "api_key: <YOUR_API_KEY>"
```

**OAuth 2.0 cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/pet/findByStatus?status=available" \
-H "accept: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>"
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | Successful operation |
| 400  | Invalid input |
| default | Unexpected error |
#### Response example
`200: Successful operation`
```json
[
  {
    "id": 210,
    "name": "Krypto",
    "category": {
      "id": 1,
      "name": "Dogs"
    },
    "photoUrls": [
      "string"
    ],
    "tags": [
      {
        "id": 0,
        "name": "string"
      }
    ],
    "status": "available"
  }
]
```
#### Parameters
##### Query parameters
| Name   | Type   | Description                                                                                             |
|--------|--------|---------------------------------------------------------------------------------------------------------|
| status | string | Status of the pet to find. <br /> **Default:** `available`. <br /> **Allowed values:** `available`, `pending`, `sold`. |
### Finding pets by tags

Finds pets by their tags.

Endpoint: https://petstore3.swagger.io/api/v3/pet/findByTags

Operation: `GET`

#### Examples
**API Key cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/pet/findByTags?tags=string" \
-H "accept: application/json" \
-H "api_key: <YOUR_API_KEY>"
```

**OAuth 2.0 cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/pet/findByTags?tags=string" \
-H "accept: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>"
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | Successful operation |
| 400  | Invalid input |
| default | Unexpected error |

##### Response example
`200: Successful operation`
```json
[
  {
    "id": 210,
    "name": "Krypto",
    "category": {
      "id": 1,
      "name": "Dogs"
    },
    "photoUrls": [
      "string"
    ],
    "tags": [
      {
        "id": 0,
        "name": "string"
      }
    ],
    "status": "available"
  }
]
```
#### Parameters
##### Query parameters
| Name   | Type   | Description                                                                                             |
|--------|--------|---------------------------------------------------------------------------------------------------------|
| tags | array | Tags to filter by. <br /> **Default:** `[]`. <br /> **Allowed values:** Any valid tag names. |

### Finding a pet by Id
Finds a pet by its unique ID.

Endpoint: https://petstore3.swagger.io/api/v3/pet/{petId}

Operation: `GET`

#### Examples
**API Key cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/pet/210" \
-H "accept: application/json" \
-H "api_key: <YOUR_API_KEY>"
```
**OAuth 2.0 cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/pet/210" \
-H "accept: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>"
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | Successful operation |
| 400  | Invalid ID supplied |
| 404  | Pet not found |
| default | Unexpected error |
#### Response example
`200: Successful operation`
```json
{
  "id": 210,
  "name": "Krypto",
  "category": {
    "id": 1,
    "name": "Dogs"
  },
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
```
#### Parameters
##### Path p1arameters
| Name   | Type   | Description                                                                                             |
|--------|--------|---------------------------------------------------------------------------------------------------------|
| petId   | integer  | ID of pet to return |

### Updating a pet with form data
Updates a pet in the store with form data.

Endpoint: https://petstore3.swagger.io/api/v3/pet/{petId}

Operation: `POST`

#### Examples
**API Key cURL Example**
```bash
POST "https://petstore3.swagger.io/api/v3/pet/210" \
-H "api_key: <YOUR_API_KEY>" \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode "name=Krypto" \
--data-urlencode "status=available"
```
**OAuth 2.0 cURL Example**
```bash
POST "https://petstore3.swagger.io/api/v3/pet/210" \
-H "accept: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>" \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode "name=Krypto" \
--data-urlencode "status=available"
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | Successful operation |
| 405  | Invalid input |
| default | Unexpected error |

##### Response example
`200: Successful operation`
```json
{
  "id": 210,
  "name": "Krypto",
  "category": {
    "id": 1,
    "name": "Dogs"
  },
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
```

#### Parameters
##### Path parameters
| Name   | Type   | Description                               | 
|--------|--------|-------------------------------------------|
| petId  | integer  | ID of pet to update        |

##### Query parameters
| Name   | Type   | Description                 |
|--------|--------|-----------------------------|
| name   | string | Name of pet to update |
| status | string | Status of pet to update |

### Deleting a pet
Deletes a pet from the database.

Endpoint: https://petstore3.swagger.io/api/v3/pet/{petId}

Operation: `DELETE`

#### Examples
**API Key cURL Example**
```bash
DELETE "https://petstore3.swagger.io/api/v3/pet/210" \
-H "api_key: <YOUR_API_KEY>"
```
**OAuth 2.0 cURL Example**
```bash
DELETE "https://petstore3.swagger.io/api/v3/pet/210" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>"
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | Pet deleted |
| 400  | Invalid ID supplied |
| 404  | Pet not found |

(A successful deletion returns a `200` code with no response body.)

#### Parameters
##### Path parameters
| Name   | Type   | Description                                                                                             |
|--------|--------|---------------------------------------------------------------------------------------------------------|
| petId   | integer  | ID of pet to delete |

### Uploading an image
Uploads an image for a pet.

Endpoint: https://petstore3.swagger.io/api/v3/pet/{petId}/uploadImage

Operation: `POST`

#### Examples
**API Key cURL Example**
```bash
POST "https://petstore3.swagger.io/api/v3/pet/210/uploadImage" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-H "api_key: <YOUR_API_KEY>" \
--form "file=@/path/to/your/file"
```
**OAuth 2.0 cURL Example**
```bash
POST "https://petstore3.swagger.io/api/v3/pet/210/uploadImage" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>" \
--form "file=@/path/to/your/file"
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | Successful operation |
| default | Unexpected error |
##### Response examples
`200: Successful operation`
```json
{
  "code": 200,
  "type": "unknown",
  "message": "additional data"
}
```
#### Parameters
##### Path parameters
| Name   | Type   | Description                                                                                             |
|--------|--------|---------------------------------------------------------------------------------------------------------|
| petId   | integer  | ID of pet to update |
##### Form data parameters
| Name   | Type   | Description|
|--------|--------|------------|
| additionalMetadata | string | Extra data to pass to server. |
| file | file | File to upload. |

## Store
With these API functions, you can manage your pet store's inventory and orders.

### Getting pet inventories
Returns pet inventories by status.

Endpoint: https://petstore3.swagger.io/api/v3/store/inventory

Operation: `GET`

#### Examples
**API Key cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/store/inventory" \
-H "accept: application/json" \
-H "api_key: <YOUR_API_KEY>"
```
**OAuth 2.0 cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/store/inventory" \
-H "accept: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>"
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | Successful operation |
| default | Unexpected error |
##### Response example
`200: Successful operation`
```json
{
  "sold": 0,
  "available": 0,
  "pending": 0
}
```
#### Parameters
None

### Placing an order
Places an order for a pet.

Endpoint: https://petstore3.swagger.io/api/v3/store/order

Operation: `POST`

#### Examples
**API Key cURL Example**
```bash
POST "https://petstore3.swagger.io/api/v3/store/order" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "api_key: <YOUR_API_KEY>" \
-d '{
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2025-08-11T15:13:06.939Z",
  "status": "placed",
  "complete": false
}'
```
**OAuth 2.0 cURL Example**
```bash
POST "https://petstore3.swagger.io/api/v3/store/order" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>" \
-d '{
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2025-08-11T15:13:06.939Z",
  "status": "placed",
  "complete": false
}'
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | Successful operation |
| 400  | Invalid Order |
| default | Unexpected error |
##### Response example

`200: Successful operation`
```json
{
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2025-08-11T15:13:06.939Z",
  "status": "placed",
  "complete": false
}
```
#### Parameters
##### Request body
| Name | Type | Description |
|------|------|-------------|
| body | Order object | **(Required)** The `Order` object for the pet. |

### Finding an order
Finds an order by its ID.

Endpoint: https://petstore3.swagger.io/api/v3/store/order/{orderId}

Operation: `GET`

#### Examples
**API Key cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/store/order/1" \
-H "accept: application/json" \
-H "api_key: <YOUR_API_KEY>"
```
**OAuth 2.0 cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/store/order/1" \
-H "accept: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>"
```

#### Responses
| Code | Description |
|------|-------------|
| 200  | Successful operation |
| 400  | Invalid ID supplied |
| 404  | Order not found |
| default | Unexpected error |
##### Response example

`200: Successful operation`
```json
{
  "id": 1,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2025-08-11T15:13:06.939Z",
  "status": "placed",
  "complete": false
}
```
#### Parameters
##### Path parameters
| Name   | Type   | Description                                                                                             |
|--------|--------|---------------------------------------------------------------------------------------------------------|
| orderId   | integer  | ID of the purchase order to fetch |


### Deleting an order
Deletes an order by its ID.

Endpoint: https://petstore3.swagger.io/api/v3/store/order/{orderId}

Operation: `DELETE`

#### Examples

**API Key cURL Example**
```bash
DELETE "https://petstore3.swagger.io/api/v3/store/order/1" \
-H "accept: application/json" \
-H "api_key: <YOUR_API_KEY>"
```
**OAuth 2.0 cURL Example**
```bash
DELETE "https://petstore3.swagger.io/api/v3/store/order/1" \
-H "accept: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>"
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | order deleted |
| 400  | Invalid ID supplied |
| 404  | Order not found |
| default | Unexpected error |

(A successful deletion returns a `200` code with no response body.)

#### Parameters
##### Path parameters
| Name   | Type   | Description                                                                                             |
|--------|--------|---------------------------------------------------------------------------------------------------------|
| orderId   | integer  | ID of the order to delete |

## User
This section describes operations related to users.

### Creating a user
Creates a new user account.

Endpoint: https://petstore3.swagger.io/api/v3/user

Operation: `POST`

#### Examples
**API Key cURL Example**
```bash
POST "https://petstore3.swagger.io/api/v3/user" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "api_key: <YOUR_API_KEY>" \
-d '{
  "id": 0,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}'
```
**OAuth 2.0 cURL Example**
```bash
POST "https://petstore3.swagger.io/api/v3/user" \
-H "accept: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
  "id": 0,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}'
```
#### Responses
| Code | Description |
| default | successful operation |
##### Response example
`200: successful operation`
```json
{
  "id": 10,
  "username": "theUser",
  "firstName": "John",
  "lastName": "James",
  "email": "john@email.com",
  "password": "12345",
  "phone": "12345",
  "userStatus": 1
}
```

#### Parameters
##### Request body
| Name | Type | Description |
|------|------|-------------|
| body | User object | **(Required)** The `User` object to create. |

### Creating a list of users with list
Creates list of users with given input list.

Endpoint: https://petstore3.swagger.io/api/v3/user/createWithList

Operation: `POST`

#### Examples
**API Key cURL Example**
```bash
POST "https://petstore3.swagger.io/api/v3/user/createWithList" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "api_key: <YOUR_API_KEY>" \
-d \
  [
    {
      "id": 0,
      "username": "string",
      "firstName": "string",
      "lastName": "string",
      "email": "string",
      "password": "string",
      "phone": "string",
      "userStatus": 0
    }
  ]
```
**OAuth 2.0 cURL Example**
```bash
POST "https://petstore3.swagger.io/api/v3/user/createWithList" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>" \
-d \
  [
    {
      "id": 0,
      "username": "string",
      "firstName": "string",
      "lastName": "string",
      "email": "string",
      "password": "string",
      "phone": "string",
      "userStatus": 0
    }
  ]
```
#### Responses
| Code | Description |
|------|-------------|
| default | successful operation |
##### Response example
`200: Successful operation`
```json
{
  "id": 0,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}
```

#### Parameters
##### Request body
| Name | Type | Description |
|------|------|-------------|
| body | Array of User objects | **(Required)** The list of `User` objects to create. |

### Logging in
Logs user into the system.

Endpoint: https://petstore3.swagger.io/api/v3/user/login

Operation: `GET`

#### Examples
**API Key cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/user/login?username=string&password=string" \
-H "accept: application/json" \
-H "api_key: <YOUR_API_KEY>"
```
**OAuth 2.0 cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/user/login?username=string&password=string" \
-H "accept: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>"
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | successful operation |
| 400  | Invalid username/password supplied |
| default | Unexpected error |
#### Response example
`200: successful operation`
```json
{
  "message": "logged in user session:abcdef12345"
}
```
**Headers:**
| Name| Description |Type|
|------|-------------|----|
| `X-Rate-Limit`| Calls per hour allowed by the user. | integer |
| `X-Expires-After`| Date in UTC when token expires. | string |

#### Parameters
##### Query parameters
| Name   | Type   | Description                                                                                             |
|--------|--------|---------------------------------------------------------------------------------------------------------|
| username   | string  | The username for login. |
| password   | string  | The password for login in clear text. |

### Logging out
Logs out current logged in user session.

Endpoint: https://petstore3.swagger.io/api/v3/user/logout

Operation: `GET`

#### Examples
**API Key cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/user/logout" \
-H "accept: application/json" \
-H "api_key: <YOUR_API_KEY>"
```
**OAuth 2.0 cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/user/logout" \
-H "accept: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>"
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | successful operation |
| default | successful operation |
##### Response example
`200: successful operation`
```json
{
  "message": "Successfully logged out"
}
```
#### Parameters
None

### Getting user by username
Gets a user by their username.

Endpoint: https://petstore3.swagger.io/api/v3/user/{username}

Operation: `GET`

#### Examples
**API Key cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/user/user1" \
-H "accept: application/json" \
-H "api_key: <YOUR_API_KEY>"
```
**OAuth 2.0 cURL Example**
```bash
GET "https://petstore3.swagger.io/api/v3/user/user1" \
-H "accept: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>"
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | successful operation |
| 400  | Invalid username supplied |
| 404  | User not found |
| default | Unexpected error |

`200: successful operation`
```json
{
  "id": 0,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}
```
#### Parameters
##### Path parameters
| Name   | Type   | Description                                                                                             |
|--------|--------|---------------------------------------------------------------------------------------------------------|
| username   | string  | The username of the user to fetch. Use "user1" for testing. |

### Updating a user
Updates a user.

Endpoint: https://petstore3.swagger.io/api/v3/user/{username}

Operation: `PUT`

#### Examples
**API Key cURL Example**
```bash
PUT "https://petstore3.swagger.io/api/v3/user/user1" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "api_key: <YOUR_API_KEY>" \
-d '{
  "id": 0,
  "username": "user1",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}'
```
**OAuth 2.0 cURL Example**
```bash
PUT "https://petstore3.swagger.io/api/v3/user/user1" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>" \
-d '{
  "id": 0,
  "username": "user1",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}'
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | Successful operation |
| 400  | Invalid user supplied |
| 404  | User not found |
| default | Unexpected error |

(A successful update returns a `200` code with no response body.)

#### Parameters
##### Path parameters
| Name   | Type   | Description                               | 
|--------|--------|-------------------------------------------|
| username | string | The username of the user to update |

##### Request body
| Name | Type | Description |
|------|------|-------------|
| body | User object | **(Required)** The `User` object with updated information. |

### Deleting a user
Deletes a user.

Endpoint: https://petstore3.swagger.io/api/v3/user/{username}

Operation: `DELETE`

#### Examples
**API Key cURL Example**
```bash
DELETE "https://petstore3.swagger.io/api/v3/user/user1" \
-H "accept: application/json" \
-H "api_key: <YOUR_API_KEY>"
```
**OAuth 2.0 cURL Example**
```bash
DELETE "https://petstore3.swagger.io/api/v3/user/user1" \
-H "accept: application/json" \
-H "Authorization: Bearer <YOUR_OAUTH_TOKEN>"
```
#### Responses
| Code | Description |
|------|-------------|
| 200  | User deleted |
| 400  | Invalid username supplied |
| 404  | User not found |

(A successful deletion returns a `200` code with no response body.)

#### Parameters
##### Path parameters
| Name   | Type   | Description                                                                                             |
|--------|--------|---------------------------------------------------------------------------------------------------------|
| username   | string  | The username of the user to delete |

# Author's note
This document provides an in-depth guide for the Petstore API as a company's technical writer/documentation specialist would write it. In true "docs-as-code" fashion, it's a living document, continuously improving it based on feedback and changing requirements.

It includes detailed information about the API endpoints, examples of how to make calls to the API, the parameters required for each endpoint, and the expected responses. This should serve as a comprehensive resource for developers working with the Petstore API.

This sample API uses Swagger, a powerful open-source framework for API development. It's not intended for production use but rather as a demonstration of how one would document an API. You can find out more about Swagger at [https://swagger.io](https://swagger.io) or on [irc.freenode.net, #swagger](irc://irc.freenode.net/swagger). 

And the mandatory dog tax: here's [Ace](media/20210327_200932.jpg).
