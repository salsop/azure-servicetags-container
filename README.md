# Azure Service Tags as Palo Alto Networks External Dynamic Lists (EDL)

## Overview

This repository contains a simple Docker container that downloads the Microsoft Azure Service Tags and hosts them on a Webserver for ingestion into a Palo Alto Networks VM-Series firewall as an External Dynamic List.

## Deployment Option 1: Azure Container Instance

Create A Resource Group:
```
az group create --name azure-servicetags --location westeurope
```
Deploy the Container Azure Container Instance with a public IP:
```
az container create --name azure-servicetags --image salsop/azure-servicetags:1.0 --resource-group azure-servicetags --ip-address public --cpu 1 --memory 1 --restart-policy always
```

Deploy the Container in Azure Container Instance within an existing virtual network subnet. *(Note this needs to be an empty subnet)*
```
az container create --name azure-servicetags --image salsop/azure-servicetags:1.0 --resource-group azure-servicetags --vnet existing-vnet --subnet empty-subnet --cpu 1 --memory 1 --restart-policy always
```

## Deployment Option 2: Linux Host running Docker

### Running the Docker Container
First clone this repository to the Linux instance that you are intending to run this docker container on.
```
git clone https://www.github.com/salsop/azure-servicetags-container
```
Then build and execute the docker image:
```
docker build . -i servicetags
```
```
docker exec -d -p 80:80 servicetags
```

This will now be running on your host system. To confirm open a web browser and visit the IP address of the host computer. You should now have access to a webpage hosting all of the text files containing the IPs for ingestion as External Dynamic Lists.

### Configuring the External Dynamic Lists on Palo Alto Networks VM-Series firewalls.

Visit the webpage and select the relevant text file containing the service that you require then copy the URL. 

For **Storage** in the **UK South** region the URL will look similar to this:
```
http://linux/Storage.UKSouth.txt
```

## Support Policy
This solution is released under an as-is, best effort, support policy. These scripts should be seen as community supported. We do not provide technical support or help in using or troubleshooting the components of the project through our normal support options.
