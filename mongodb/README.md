# MongoDB workshop

MongoDB is a NoSQL database, document oriented.

Find out more about some use cases Mongo is good for here:
- https://www.mongodb.com/use-cases

You will use this database to hold all comments written by users on contractors.

## Step 1: Install Mongo

### Start mongo in a container

Like for postgres, you will use a docker setup.

We will create a docker volume to persist mongo data between restarts of the mongo container

Use the `docker-compose` provided:

```bash
# create docker volume for mongo
docker volume create garlaxy-mongo-data
# start containers
docker-compose up -d
```

### Query mongo

#### Using mongo CLI

If you wish to visualized your data directly using MongoDB shell (CLI),
you can enter the MongoDB running container:

```bash
docker exec -it mongo-5 mongo --username sigl2022 --password sigl2022
# >
# MongoDB shell version v5.0.3
# ...
# > 
```

Mongo CLI doc can be found on mongodb website:
- https://docs.mongodb.com/manual/mongo/#working-with-the-mongo-shell


#### Using Robot 3T (formally robotmongo)

Let's install a tool like pgAdmin for mongo.

We recommend using [Robo 3T free tool (download Robo 3T - not studio)](https://robomongo.org/download).

Once downloaded, you can add your mongo connection by:
1. click the connection icon and `create` a new connection. 
![create-connection](docs/create-connection.png)
1. In the `Connection` tab, add `Garlaxy local mongo` as a connection name (you can choose whichever name you like)
![create-connection-name](docs/create-connection-name.png)

1. In the `Authentication` tab, tick `Perform authentication` and fill:
    - `admin` as database
    - `sigl2022` as User Name
    - `sigl2022` as Password
    - `SCRAM-SHA-1` as Auth Mechanism
![config-auth](docs/config-auth.png)
1. Test your connection by clicking `! Test` button; you should see:
![authentication](docs/test-connection-config.png)
1. Save config if test is green as above, and you should be able to connect to your mongo db from the list of connections:
![connection-list](docs/connection-list.png)
1. Click connect, and you should have only a `config` collection and a `System` folder.

## Step 2: Create garlaxy's database and comment collection

### Create garlaxy database in Mongo

From Robot 3T, you can directly create a new database:
1. right click `Garlaxy local mongo` > `Create database`
1. enter `garlaxy` as database name

### Create a schema ?

**There are no notions of database schema in MongoDB!**

You only talk about `collection` of `documents`.

### Create the comment collection

Let's create a collection name "comments" inside garlaxy database, from Robot 3T:
1. click `garlaxy` > right click `Collections` > add `Collection`
1. add `comments` as Collection name

You're all set!

> Note: Equivalent to create a new database with collection using MongoCLI would be:
> ```sh
> # Enter the mongo shell
> docker exec -it mongo-5 mongo -u sigl2022 -p sigl2022
> # MongoDB shell version 5.0.3
> #...
> use garlaxy
> # switched to db garlaxy
> db.createCollection("comments");
> # { "ok" : 1 }
> show collections;
> # will display your collections
> show databases; 
> # will display your databases
>```

## Step 3: Load some comments

We've prepared a script to load all comments based on a [csv file of 16000+ walmart product review, on data.world](https://data.world/opensnippets/walmart-products-reviews-dataset).

> Note: comments are not really matching our garlarxy ressources, but it will do for our case!

We then generated comments TSV (Tab Seperated Value) with comments attached to orders.
You can have a look at file here: [scripts/data/comments.tsv](scripts/data/comments.tsv)

To import those comments, you need to copy scripts folder (containing comments.tsv) inside the mongo container and import them using [mongoimport](https://docs.mongodb.com/database-tools/mongoimport/):
```bash
# from mongodb/
# copy your comments.tsv file to mongo-4 container
docker cp scripts mongo-5:/tmp/
# Load all comments to the garlaxy database on the collection comments.
# Note: you need to authenticate as the user sigl2022 over the admin database to have
#       rights to perform data import.
# --drop is there to empty the collection before importing it again.
docker exec -it mongo-5 mongoimport -u sigl2022 -p sigl2022 \
    --authenticationDatabase=admin \
    --db=garlaxy --collection=comments \
    --type=tsv --headerline --file=/tmp/scripts/data/comments.tsv \
    --drop
```

From Robot 3T, you can view all documents by double clicking on `comments` (or right click on `comments` > View documents)

> Note: You can choose different display options of your documents next to pagination menu

## Step 4: Query comments

Let's query all comments on the contractor with the name `Made In Space Europe`.

In the MongoDB cli or from Robot 3T, enter:
```js
// If you are from MongoDB cli, make sure to type `use garlaxy` before
// (to be on the correct database) 
db.getCollection('comments').find({contractor: "Made In Space Europe"});
```

> Note: You may have noticed that documents are like JSON documents but with some other types like `ObjectID`.
> The real format name of documents in Mongo is [BSON](https://www.mongodb.com/json-and-bson). It stands for Binary JSON, and adds more than > the 5 types of JSON (like `Date`, `NumberLong` etc...)

## Step 5: Integrate comment database to your Web API

Todo during the week...