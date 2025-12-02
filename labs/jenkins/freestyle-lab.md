# Exercise 1: "Hello World" Build 
This foundational exercise demonstrates creating a basic job that runs a simple command. 
Steps:
- On the Jenkins dashboard, click New Item.
- Enter an item name (e.g., "HelloWorld") and select Freestyle project, then click OK.
- In the project configuration, scroll down to the Build section.
- Click Add build step and select Execute shell (or Execute Windows batch command if using Windows).
- In the command box, type echo "Hello, Jenkins Freestyle Exercise!"
- Click Save and then Build Now on the project page.
- Check the Console Output for the "Hello, Jenkins Freestyle Exercise!" message to verify success. 

# Exercise 2: Source Code Management (SCM) Integration
This exercise integrates Jenkins with a version control system (like Git/GitHub) to pull code and perform a build. 

Steps:
- Create a new freestyle project (e.g., "Git-Integration-Build").
- In the Source Code Management section, select Git.
- Enter the Repository URL for a sample or personal GitHub/Bitbucket repository (e.g., github.com).
- If the repository is private, you will need to add credentials (e.g., username/password or a Personal Access Token).
- In Branches to build, specify the target branch (e.g., */main or */master).
- Add a build step (e.g., Execute shell) to run a simple command within the cloned repository directory, like ls -al to list the files.
- Save and run the build to see Jenkins check out the code and execute the command. 

# Exercise 3: Automated CI with Build Triggers 
This exercise automates the build process so Jenkins automatically builds the project when a change is pushed to the SCM. 


Steps:
- Use the "Git-Integration-Build" job from Exercise 2 or create a new one.
- In the job configuration, go to the Build Triggers section.
- Check the box for Poll SCM or Build when a change is pushed to GitHub (depending on your setup and plugins).
- For Poll SCM, define a schedule (e.g., * * * * * for every minute).
- Save the configuration.
- Make a small change to your connected GitHub repository and push the change. Jenkins should detect the change during the next polling interval (or immediately if using webhooks) and start a new build. 