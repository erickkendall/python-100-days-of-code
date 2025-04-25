"""
Module for interacting with the Open Trivia Database API.
Handles authentication and fetching questions from the API.
"""
import requests
import json


def get_session_token():
    """
    Get a session token from the Open Trivia DB API.
    
    Session tokens help ensure questions aren't repeated during multiple API calls.
    Tokens expire after 6 hours of inactivity.
    
    Returns:
        str: Session token if successful, None otherwise
    """
    token_url = "https://opentdb.com/api_token.php?command=request"
    
    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        # Sending the request to the token endpoint
        response = requests.get(token_url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response to get the token
            response_data = response.json()
            
            # Check the response code from the API
            if response_data.get("response_code") == 0:
                token = response_data.get("token")
                print(f"Successfully obtained session token")
                return token
            else:
                print(f"API error: {response_data.get('response_message', 'Unknown error')}")
                return None
        else:
            print(f"Failed to obtain token. Status code: {response.status_code}")
            print(f"Error message: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None


def fetch_questions(amount=10, category=None, difficulty=None, question_type=None, token=None, encode=None):
    """
    Fetch questions from the Open Trivia DB API.
    
    Args:
        amount (int): Number of questions to fetch (default: 10)
        category (int, optional): Category ID for the questions
        difficulty (str, optional): Difficulty level ('easy', 'medium', 'hard')
        question_type (str, optional): Type of question ('multiple', 'boolean')
        token (str, optional): Session token to prevent duplicate questions
        encode (str, optional): Encoding format ('urlLegacy', 'url3986', 'base64')
    
    Returns:
        dict: JSON response containing the questions if successful, None otherwise
    """
    # Base URL for the API
    base_url = "https://opentdb.com/api.php"
    
    # Build query parameters
    params = {"amount": amount}
    
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty
    if question_type:
        params["type"] = question_type
    if token:
        params["token"] = token
    if encode:
        params["encode"] = encode
    
    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        # Sending the request to the API
        response = requests.get(base_url, params=params, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Check the response code from the API
            if data.get("response_code") == 0:
                print(f"Successfully fetched {len(data.get('results', []))} questions")
                return data
            else:
                # Handle different response codes
                response_codes = {
                    1: "No results found. The API doesn't have enough questions for your query.",
                    2: "Invalid parameter in the API request.",
                    3: "Session token does not exist.",
                    4: "Session token has returned all possible questions. Reset the token."
                }
                error_msg = response_codes.get(data.get("response_code"), "Unknown API error")
                print(f"API error: {error_msg}")
                return None
        else:
            print(f"Failed to fetch questions. Status code: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None


def reset_token(token):
    """
    Reset a session token to clear its question history.
    
    Args:
        token (str): The session token to reset
    
    Returns:
        bool: True if reset was successful, False otherwise
    """
    reset_url = f"https://opentdb.com/api_token.php?command=reset&token={token}"
    
    try:
        response = requests.get(reset_url)
        data = response.json()
        
        if data.get("response_code") == 0:
            print("Token reset successfully")
            return True
        else:
            print(f"Failed to reset token: {data.get('response_message', 'Unknown error')}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return False


def get_trivia_questions(amount=10, category=None, difficulty=None, question_type="boolean"):
    """
    Main function to get trivia questions with automatic token handling.
    
    Args:
        amount (int): Number of questions to fetch
        category (int, optional): Category ID
        difficulty (str, optional): Difficulty level ('easy', 'medium', 'hard')
        question_type (str): Type of question ('multiple', 'boolean')
    
    Returns:
        list: List of question dictionaries if successful, empty list otherwise
    """
    # Get a session token
    token = get_session_token()
    
    if not token:
        print("Proceeding without session token")
    
    # Fetch questions
    response_data = fetch_questions(
        amount=amount,
        category=category,
        difficulty=difficulty,
        question_type=question_type,
        token=token
    )
    
    if response_data and "results" in response_data:
        return response_data["results"]
    else:
        return []


if __name__ == "__main__":
    # Example usage
    questions = get_trivia_questions(amount=10, question_type="boolean")
    
    if questions:
        print(f"Retrieved {len(questions)} questions:")
        for i, q in enumerate(questions, 1):
            print(f"{i}. {q['question']} (Answer: {q['correct_answer']})")
    else:
        print("Failed to retrieve questions")
