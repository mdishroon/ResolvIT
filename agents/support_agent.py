from tools.active_directory_mock import ActiveDirectoryMock
from tools.knowledge_base_search import KnowledgeBaseSearch

class SupportAgent:
    def __init__(self):
        self.ad_tool = ActiveDirectoryMock()
        self.kb_tool = KnowledgeBaseSearch()

    def mock_llm_reasoning(self, text):
        # agent analyzes the text to determine the required action and target
        text_lower = text.lower()
        if "locked out" in text_lower or "active directory" in text_lower:
            return {"action": "unlock_ad_user", "target": "treasury_user"}
        elif "softphone" in text_lower or "mitel" in text_lower:
            return {"action": "search_kb", "target": "softphone"}
        elif "printer" in text_lower or "offline" in text_lower:
            return {"action": "search_kb", "target": "printer"}
        return {"action": "escalate", "target": "tier_2"}

    def resolve_issue(self, ticket_notes):
        # Step 1: determine the plan
        decision = self.mock_llm_reasoning(ticket_notes)
        action = decision.get("action")
        target = decision.get("target")
        
        # Step 2: autonomously execute the selected tool
        if action == "unlock_ad_user":
            status_check = self.ad_tool.check_user_status(target)
            
            if "locked" in status_check:
                unlock_result = self.ad_tool.unlock_user(target)
                return f"Action Taken: {unlock_result}"
            return "No action needed. User is already active."
            
        elif action == "search_kb":
            kb_result = self.kb_tool.search_articles(target)
            return f"Action Taken: Consulted Knowledge Base. {kb_result}"
            
        return "Action Taken: Ticket escalated to human Tier 2 technician."