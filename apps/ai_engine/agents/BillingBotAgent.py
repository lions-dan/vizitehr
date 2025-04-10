
from .base_agent import BaseAgent
from apps.ai_engine.models import AgentConversation
from apps.billing.models import Invoice

class BillingBotAgent(BaseAgent):
    def handle_command(self, command: str) -> str:
        if not self.user.has_role('biller', self.clinic):
            return "Access denied. Only billing staff can use this assistant."

        if "balance" in command:
            result = "Total outstanding invoices: $1,200"
        else:
            result = "Billing assistant here. Ask me about charges or invoices."

        AgentConversation.objects.create(
            user=self.user,
            clinic=self.clinic,
            input_text=command,
            response_text=result
        )
        return result