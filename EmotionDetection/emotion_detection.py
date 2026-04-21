import requests
import json

def emotion_detector(text_to_analyze):
    # URL, Headers, and Input JSON
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Send the POST request
    response = requests.post(url, json=input_json, headers=headers)
    
    # Task 3: Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the emotion scores from the formatted response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Write the code logic to find the dominant emotion
    # The max() function with key=emotions.get finds the key with the highest value
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the dictionary in the exact format required
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }