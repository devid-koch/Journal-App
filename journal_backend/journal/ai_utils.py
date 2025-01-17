from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")
generator = pipeline("text-generation", model="gpt2")


def analyze_entry(entry_content):
    try:
        if not entry_content.strip():
            return {"error": "Entry content is empty or invalid."}

        # Perform sentiment analysis
        result = sentiment_analyzer(entry_content)
        
        if not result or len(result) == 0:
            return {"error": "No analysis result returned."}

        sentiment = result[0].get('label', 'Neutral')
        confidence = result[0].get('score', 0.0)
        
        return {
            "insights": {
                "sentiment": sentiment,
                "confidence": round(confidence, 2)
            }
        }
    except Exception as e:
        return {"error": f"Sentiment analysis failed: {str(e)}"}


def generate_prompt(previous_entry):

    try:
        if not previous_entry:
            prompt_text = "Write about something meaningful to you today."
        else:
            prompt_text = previous_entry
        
        result = generator(prompt_text, max_length=100, num_return_sequences=1, temperature=0.7)
        
        if result and len(result) > 0:
            return result[0]['generated_text'].strip()
        else:
            return "Write about an unexpected event in your life."
    except Exception as e:
        return {"error": f"Prompt generation failed: {str(e)}"}
