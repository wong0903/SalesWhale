
**Install Docker CE**

1.Update the apt package index.

    	$ sudo apt-get update
2.Install the latest version of Docker CE, or go to the next step to install a specific version:

    	$ sudo apt-get install docker-ce
3.Verify that Docker CE is installed correctly by running the hello-world image.

		$ sudo docker run hello-world
This command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits.
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
