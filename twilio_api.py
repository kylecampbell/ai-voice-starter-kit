import os
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
from twilio.twiml.messaging_response import MessagingResponse
from open_ai import get_gpt_response

app = Flask(__name__)


@app.route("/voice", methods=['POST'])
def answer_call():
    """Standard text to GPT return GPT text response"""

    resp = VoiceResponse()

    if 'SpeechResult' in request.values:
        # Get the text transcription of what the caller said
        input_text = request.values['SpeechResult']

        # Get response from ChatGPT
        chat_response = get_gpt_response(input_text)
        print('GPT Response:', chat_response)

        # Respond back with ChatGPT's response
        resp.say(chat_response)
    else:
        # First response or no transcription available
        resp.say("Hey hey, what's up?", voice='alice')

    # Collect further speech input
    gather = Gather(input='speech', action='/voice', speech_timeout='auto', hints=["yes", "no", "please", "thank you"])
    resp.append(gather)

    # If no input was received within the timeout, end the call
    resp.say("Later skater!")
    return str(resp)


@app.route("/sms", methods=['POST'])
def answer_sms():
    """
    Standard text to GPT return GPT text response.
    """
    try:
        incoming_msg = request.form['Body']
        print('incoming_msg:', incoming_msg)
        
        chat_response = get_gpt_response(incoming_msg)
        print('sms gpt response:', chat_response)

        resp = MessagingResponse()

        # Add a text message (SMS)
        msg = resp.message(chat_response)

        # Example: Add a picture message (MMS)
        # msg.media(
        #     "https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg"
        # )

        return str(resp)
    except Exception as e:
        print('ERROR', e)
        return str(MessagingResponse())


if __name__ == "__main__":
    app.run(debug=True)