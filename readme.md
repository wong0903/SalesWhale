


**1.Set up the repository**

    	$ sudo apt-get update
    	$ sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
    	$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    	$ sudo apt-key fingerprint 0EBFCD88
		$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

**2.Install Docker CE**

		$ sudo apt-get update
    	$ sudo apt-get install docker-ce

**3.Verify that Docker CE is installed correctly by running the hello-world image.**

		$ sudo docker run hello-world
____________________________________________________________________
**Manage Docker as a non-root user**

1.Create the docker group.

		$ sudo groupadd docker
2.Add your user to the docker group.

		$ sudo usermod -aG docker $USER
Log out and log back in so that your group membership is re-evaluated
____________________________________________________________________
**Run the proxy service from docker hub**

	$ docker run -p 5000:5000 wong0903/get-started:proxy
____________________________________________________________________
**The following endpoints are available:**
-   POST /whales - Add a new whale
    ```
    # Example
    ~ curl -X POST http://localhost:5000/whales -H "Content-Type: application/json" -d '{"name": "orca", "country": "Atlantis" }'
    ```
-   GET /whale/:id -  Find whale by id
    ```
    # Example
    ~ curl -X GET http://localhost:5000/whale/6 
    ```
-   GET /whales - Get all whales
    ```
    # Example
    ~ curl -X GET http://localhost:5000/whales
    ```
-   GET /whales/purge - Purge the cache
	```
	# Example
	~ curl -X GET http://localhost:5000/whales/purge
	```

-	GET /whales/sync - Sync the whales in cache with the whale market
	```	
	# Example
	~ curl -X GET http://localhost:5000/whales/sync
	```

-	GET /whales/cache_info -  Calculate the cache hit ratio
	```
	# Example
	~ curl -X GET http://localhost:5000/whales/cache_info
	```
____________________________________________________________________
**Service Testing**
Download the files and use pytest

	# Example
	$ pytest -v

If you don't have pytest

	sudo apt install -y python3-pip
	pip3 install pytest



