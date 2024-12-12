from typing import List
import ell
from flask import current_app

def create_lmps(app=None):
    """Factory para crear Language Model Programs."""
    
    @ell.simple(model=app.config.get('DEFAULT_MODEL', 'gpt-4'), temperature=0.7)
    def chat_response(message: str):
        """You are a helpful and friendly assistant."""
        return message

    @ell.complex(model=app.config.get('DEFAULT_MODEL', 'gpt-4'))
    def structured_chat(message_history: List[ell.Message]) -> List[ell.Message]:
        """You are a professional assistant that maintains context through conversations."""
        return [
            ell.system("Maintain conversation context and provide helpful responses."),
        ] + message_history

    @ell.simple(model=app.config.get('DEFAULT_MODEL', 'gpt-4'), temperature=1.0, n=3)
    def generate_alternatives(prompt: str):
        """You are a creative assistant that generates multiple alternative responses."""
        return f"Generate three different responses for: {prompt}"

    @ell.complex(model=app.config.get('DEFAULT_MODEL', 'gpt-4'), temperature=0.1)
    def select_best_response(responses: List[str]) -> List[ell.Message]:
        """You are an expert at selecting the most appropriate response."""
        return [
            ell.system("Select the best response based on clarity, relevance, and helpfulness."),
            ell.user(f"Choose the best response from these options:\n{'\n'.join(responses)}")
        ]
    
    return {
        'chat_response': chat_response,
        'structured_chat': structured_chat,
        'generate_alternatives': generate_alternatives,
        'select_best_response': select_best_response
    } 