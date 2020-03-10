

# Segway/Princess Margaret Research

## Description
- Our application allows users to easily access the genome software Segway through an instance of a Galaxy server which we have set up.
- This will allow users to easily access the functionality of Segway from any computer without needing to download the program and understand the command line functionality as we have created a simple and understandable interface for users.
- Before the deployment of our galaxy server, the only way to use Segway was to download the software onto ones own computer and use it through the command line. Segway only functions on Linux, so by hosting a public instance of it, we have greatly expanded accessibility to Segway, which is our partners main objective, and their vision of an MVP.

## Key Features
-   Users are now able to upload their genomedata and other necessary files easily to our application through Galaxy's simple user interface. 
-   They are then able to easily configure how they would like to use Segway by filling in any criteria they wish to specify. This is a huge improvement in accessibility as previously users were required to specify long and complicated command line parameters, now they need only click a button.
-   After uploading their data to the train tool and filling in any specifications, users can click execute and easily train their model.
-   After training their model, users can change over to our annotate tool, again upload any required data and specifications easily through a graphic interface, users are then able to simply hit execute and Galaxy will then allow the user to download the results of the Segway analysis, which they can then use for further research.

## Instructions
- To use our application, simply visit: http://segway.matrixdoge.com:8080/
- From there, select Segway from the menu on the left side.
- We have created these tools for galaxy.
- Users then train their models with their data, annotate it, and then download their results.
- For a video demo, see https://youtu.be/nl9Gj3vzey4.

## Development requirements
-  To use our product, a developer would need to download conda, then run the command: 
	conda install -c bioconda segway
This will install Segway, as well as bioconda, which contains the necessary python libraries for Segway.
-  A developer would then need to download and build a galaxy server, which can be found here:
https://galaxyproject.org/admin/get-galaxy/
NOTE: Segway is only supported on Linux
- A user will then copy the tools we have built from our repo into the galaxy configuration file as so:
cp ~/team-project-9-princess-margaret-cancer-centre/segway_tool/tools/segway_tools ~/galaxy/tools/segway_tools
-  Then simply start the server with:
sudo systemctl start galaxy
- And that's it, users are then able to access their own galaxy instances with our product through localhost, as well as choose to access it through a network by following the instructions on:
https://galaxyproject.org/admin/get-galaxy/
NOTE: To see how to test using our product, watch the video in the example folder.

## Deployment and Github Workflow
- In our Git repository, we have created a folder called segway_tool. This folder is essentially our product, and all that is required to get Segway working within Galaxy.
- Within this folder, we choose our tool to work on, update the xml file, and push.
- Then via a simple script, we visit the link:
http://segway.matrixdoge.com:8081/
Where we will be prompted for a password, which is: galaxyS
- This will then tell our server to pull from the repository, copy our tools into the galaxy configuration files, and restart the server.
- When group members are finished working a specific part they are then able to easily update our Galaxy instance so that changes can be visible to all members immediately. 
- We choose this method because team members are able to make small, incremental improvements, and then immediately make them visible to all other members via simple scripts, so deployment is streamlined and easy. 

## Licenses
- We have applied the GPLv2 license to our codebase.
- This is the license our partner is using for Segway, which is what our product is built upon and thus they requested we keep the same license.
- This will not have any effect on the development and use of our codebase.

