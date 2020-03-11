
# Segway/Princess Margaret Research

## Iteration 2 - Review & Retrospect

-   When: February 28th, 2020
-   Where: Princess Margaret Research Tower, Rm 15-710, 101 College St.

## Process - Reflection

#### Q1. Decisions that turned out well
- Communicating through Facebook group chat
	- The team chose to communicate through a group chat on Facebook’s Messenger which allowed for fluent discussion and prompt responses. This allowed for members to be readily reachable for questions and concerns in an extremely timely manner. All team members were also able to simultaneously interact and provide input in the discussions. Also, this is also the platform where we share the new documentation/example page we found might be useful and helpful.
- Designating a member for communication management
	- The team had designated a team member to employ as the main liaison between the group and the partner, for which she had helped facilitate all communications and foster a stronger relationship between the partner and the team. This had also allowed for much more efficient scheduling of meetings and ensured fluency in all group communications. 
- Using When2meet to plan meetings
	- The use of the When2Meet platform allowed for easy arrangements of meetings. Given there 7 team members, scheduling without When2Meet would have been complicated. However, with When2Meet, individual members are able to independently input their availability and then the group was able to collectively observe an optimal meeting time. 
- Use of Quercus group announcements
	- The clever use of Quercus group announcements allowed the team to easily access information such as shared log in information and instructions. This resolved the group chat problem that team members would have to scroll past a plethora of messages to find a single piece of information. 
- Communicate with the TA frequently
	- What we should do to achieve our MVP is quite different from other normal development projects, especially regarding the fact that the much heavier portion of the project is to setup and understand the "dependencies" rather than to do actual coding. So, we involve Adam in our first meeting, and he helped us to understand what our specific jobs would be like. We also ask for help to get the remote server access when we found that most of our teammates cannot succesfully make the tools we need to work on their own computer. Our frequent commmunication with the TA really made it easier for us to make progress on our project.
- Communicate with the partner frequently
	- Our project is also different from others as we have our partner know much more about the tools we need to combine than us. So we frequently met up with our parter (the research leader and the technical assistant who actually implement one tool (Segway)) to get their help to understand and use the original tool. For example, they suggested us to first try a simple project on Galaxy in order to see how it works. We did so (the galaxy_tool_example) and really got more understanding about what we should do to arrange the deployment in Galaxy.

#### Q2. Decisions that did not turn out as well as we hoped
- Group meetings without a clear objective 
	- The team scheduled weekly group meetings that often did not have clear objectives. Although the meetings were helpful for allowing members to catch up on each individual’s progress, it did not facilitate much group progress.
	- After a couple of meetings, we noticed this issue and made changes by setting a small goal for each meeting. An example would be when we decided to pick a day to deploy the Galaxy server, in which members experienced with AWS and Azure were able to collaborate and make significant progress in deploying the server.
	- Also, before we finally all had access to a server with Galaxy and Segway set up, several members were struggling with getting the software to work properly, (especially regarding Segway, because it only supports Linux). Thus, some of our earlier meetings consisted of some of us catching up without any measurable progress towards our goals.
- Using Trello to manage tasks
	- The Trello application for assigning roles was not successful as our product had so mua high knowledge prerequisite that some roles assigned were too broad and it was impossible to provide specifics, e.g. "Reading and understanding the Galaxy tool shed before we can start coding for the project". Due to this, members were unsure of their tasks. In addition, we later started to work together face-to-face, where there is no point to use Trello. Overall, Trello did not help facilitate much progress.

#### Q3. Planned changes
- As mentioned above we are now scheduling meetings with specific goals so that we are able to accomplish more, and members are better utilizing their skills and time.
	-  For example those experienced with hosting will make sure to all pick a time they're free to meet.
	-  Also, we tried to learn the content/usage of the two tools (Segway && Galaxy) we want to combine together in our meeting, after we realized that we had to much more learning than the actual coding part. We help each other to understand every part of the process, especially help to make sure those who use the OS that not supports Segway/Galaxy to know things at the same level. When it comes to actual coding part, we discussed together how to solve certain problems, and use the machine that supports the tools to test our ideas.
	-  In addition, since we only need to modify certain simple xml files, we always discuss how we might achieve certain goal in the meeting, and then modify the file and see the progress.
- We are creating a weekly When2Meet so we cam quickly set up meetings and know when members are available.
- Instead of letting everyone struggle with the preparing process (installing and exploring the original Segway && Galaxy tools), we finally choose to use a remote server with those tools ready for everyone to use and moniter the progress being made.


## Product - Review

#### Q4. How was your product demo?
- We prepared for our demo by deploying a working version of our product and preparing a small batch of sample data to demonstrate to our partner the functionality we have successfully completed. 
- We were able to demo a working website in which the partner was able to access and use the product successfully. 
- We demoed a simple upload of data, training our model on it, and produced an output file from the partners provided sample data.
- Our partner was very pleased with our progress and asserted it was on track with their vision of the product.
- The partner requested minor changes. For example, Segway 3.0 uses the term "annotate" as opposed to "identify" and requested we change the tool name, which we were able to do.
- Other such changes were input orderings and other information they wanted available. As our partner is far more experienced with the Segway application and its functionality we are adding their suggestions so that it may better fit their vision.
- We found it might be useful for our partner using the tool to further transfer the output (genome result) to some genome browser when we were exploring Segway. We presented this idea in the meeting, and our partner was very pleased with having this feature.
- From this demo we learned that it is important to keep our partner in the loop as development continues because they are far more knowledgable about Segway and have a clear idea of what functionality they want supported. Also, they are used to using other Galaxy tools/certain genome browsers during their daily research, so they have more sense of what the user interface/interaction should be look like.
