# Changes to original structure

The following changes were made to the file structure to fix any bugs and follow best practices:
* Split original dockerfile into 3 separate dockerfiles and moved them to their respective folders (The original dockerfile is in `original_dockerfile/`)
* Splitting the dockerfiles decreased build runtime (removed unnecessary python package installation for `app` and `mongo` containers)
* Moved `requirements.txt` into django folder (rest)

We highly recommend you go through the setup in `Dockerfile` and `docker-compose.yml`. If you are able to understand and explain the setup, that will be a huge differentiator.

# Setup
1. Clone this repository 
```
git clone https://github.com/VedankPande/adb-test.git
```
2. Change into the cloned directory and set the environment variable for the code path. Replace `path_to_repository` appropriately.
```
export ADBREW_CODEBASE_PATH="{path_to_repository}/test/src"
```
3. Build container
```
sudo docker-compose build
```
4. Once the build is completed, start the containers:
```
docker-compose up -d
```
5. Once complete, `docker ps` should output something like this:
```
CONTAINER ID   IMAGE               COMMAND                  CREATED         STATUS         PORTS                      NAMES
e445be7efa61   adbrew_test_api     "bash -c 'cd /src/re…"   3 minutes ago   Up 2 seconds   0.0.0.0:8000->8000/tcp     api
0fd203f12d8a   adbrew_test_app     "bash -c 'cd /src/ap…"   4 minutes ago   Up 3 minutes   0.0.0.0:3000->3000/tcp     app
884cb9296791   adbrew_test_mongo   "/usr/bin/mongod --b…"   4 minutes ago   Up 3 minutes   0.0.0.0:27017->27017/tcp   mongo
```
6. Check that you are able to access http://localhost:3000 and http://localhost:8000/api/v1/todos

