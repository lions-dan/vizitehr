from .base_agent import BaseAgent
from apps.ai_engine.models import AgentConversation
from apps.ehr.scheduling.utils import schedule_appointment
class ClinicCopilotAgent(BaseAgent):
    def handle_command(self, command: str) -> str:
        if not self.user.has_role('provider', self.clinic):
            return "Access denied. Only providers can use this assistant."

        # Dummy intent parsing
        if "schedule" in command:
            result = schedule_appointment(patient_id=1, provider_id=self.user.id, date_time="2025-05-01T09:00")
        else:
            result = "Sorry, I couldn't understand that command."

        # Save conversation
        AgentConversation.objects.create(
            user=self.user,
            clinic=self.clinic,
            input_text=command,
            response_text=result
        )
        return result