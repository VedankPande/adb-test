# Changes to original structure

The following changes were made to the file structure to fix any bugs and follow best practices:
* Split original dockerfile into 3 separate dockerfiles and moved them to their respective folders (The original dockerfile is in `original_dockerfile/`)
* Splitting the dockerfiles decreased build runtime (removed unnecessary python package installation for `app` and `mongo` containers)
* Moved `requirements.txt` into django folder (rest)

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
5. Run `docker ps` to check if the containers are running

6. Check that you are able to access http://localhost:3000 and http://localhost:8000/api/v1/todos

