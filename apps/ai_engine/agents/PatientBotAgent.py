
from .base_agent import BaseAgent
from apps.ai_engine.models import AgentConversation

class PatientBotAgent(BaseAgent):
    def handle_command(self, command: str) -> str:
        # Dummy logic
        if "appointments" in command:
            result = "Your next appointment is on May 1st at 9:00 AM."
        else:
            result = "I'm here to help you with your care questions!"

        AgentConversation.objects.create(
            user=self.user,
            clinic=self.clinic,
            input_text=command,
            response_text=result
        )
        return result