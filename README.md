TEAM MEMBERS: Aakash Khurana, Irinel Bandas, Unnati Parekh

PACKAGES: 

The required packages are mentioned in the requirements.txt file and can be downloaded as follows: pip install -r requirements.txt

ABOUT THE IMPLEMENTATION: 

We have implemented a Rasa bot, named Recipe-Bot and have also included integration with Slack. You can see the types of interactions that can be made with the Recipe-Bot in 'video-final.mov' which is a recording of the Bot working on Slack.

You can do either of the following:
[1] Go over ingredients list (whole list)
[2] Go over recipe steps (stepwise)
[3] Go over nutrients list (whole list)

You can also ask How to and What is questions in between and you will be provided a URL relevant to your search.

HOW TO RUN:

Use the following command to run Recipe-Bot in terminal:
``` rasa run & rasa run actions```

If using with Slack, start the ngrok server using following command:
``` ngrok http 5005```

Enter the ngrok redirection URL in Slack Bot and update 'credentials.yml' with Slack Bot User OAuth token. 

BOT GRAPH:

![Graph](https://github.com/AakashKhuranaNU/RASA_NLP/blob/master/Bot%20graph.png)
