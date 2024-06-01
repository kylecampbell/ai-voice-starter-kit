# AI Voice Starter Kit
With AI voice on the rise, this starter code's goal is to get you set up with a python project using OpenAI to answer calls and text messages on a phone number that you obtain from Twilio and provide to your AI agent. Keep in mind this project serves as a stepping stone rather than a finished project, it highlights the potential of integrating AI with a phone number as a medium of communication. There are a lot of paths you can take from here to make a more interesting AI voice agent, such as using a better voice model than Twilio's built in `TwiML Voice <Say>`. Enjoy!

## Setup

git clone repo  
cd into repo  
copy .env.example file to a .env.local file with this command: cp .env.example .env.local  


### Create Conda environment
conda create -n myenv python=3.11  
conda activate myenv  

### Install dependencies
pip install -r requirements.txt  


### NGROK
brew install --cask ngrok  

In a separate terminal, run: ngrok http 127.0.0.1:5000  
Leave window for now as you will need info in this terminal window later.  

### OpenAI
1. Go to platform.openai.com and signup or login
2. Go to API keys
3. Create new secret key
4. Copy and paste the secret key to the OPENAI_API_KEY=your-secret-key in the .env.local file.

### Twilio
1. Go to twilio.com, signup, purchase a phone number for the same country your personal phone number is.
  - A US phone number is $1.15 per month + usage
  - For minor development, these costs are low
  - Cancel/release phone number when finished
2. You may need to add funds for tax purposes.
3. Go to the Twilio Console.
4. Go to Account > API keys & tokens > Create API key > copy and paste account sid and auth token to your .env.local file.
5. Find your purchased number under Develop > United States (or your country) > Phone Numbers > Manage > Active numbers
6. Select your number.
7. Under Voice Configuration, on the line that says A call comes in, URL, HTTP: replace the URL with the webhook (forwarding) URL for incoming calls to point to your Flask app api endpoint (https://your-ngrok-url/voice).
The URL from ngrok terminal earlier, there is a line that says Forwarding and to the right shows something like this: https://1111-222-333-44-555.ngrok-free.app -> http://127.0.0.1:5000. Grab the URL to the left of the arrow and replace the URL section in Twilio.
Voice URL Example: https://1111-222-333-44-555.ngrok-free.app/voice
8. Under Messaging Configuration, on the line that says A message comes in, URL, HTTP: replace the URL the webhook (forwarding) URL for incoming sms to point to your Flask app api endpoint (https://your-ngrok-url/sms).
SMS URL Example: https://1111-222-333-44-555.ngrok-free.app/sms
9. Select Save configuration at the bottom.
10. Bonus note, you can set up API calls in your code to update these URLs programmatically rather than logging into the console everytime.

For SMS:
You may have to update geo permissions in twilio before able to send a response from your app to other phone number.
Set to the country of your Twilio phone number and ensure your non-Twilio phone number is the same country.
For example: Both Twilio number and non-Twilio number are US numbers, so US and CA are enabled. (CA auto enables with US)
To find the Messaging Geographic Permissions, enter geo permission in the search and it should appear. Then enable appropriate country.

### Run
In a separate terminal from the ngrok terminal, in this project's directory, with your conda environment activated, run: python twilio_api.py

Call and text your Twilio phone number and speak with your AI agent.

To shut down flask app and ngrok, simply close the terminal windows or use the ctrl+c command to stop them.