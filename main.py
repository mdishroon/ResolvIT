import json
from agents.support_agent import SupportAgent

def load_mock_tickets(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def main():
    print("Initializing ResolvIT Support Agent...")
    agent = SupportAgent()
    
    # load simulated IT helpdesk tickets
    tickets = load_mock_tickets('data/mock_tickets.json')
    
    for ticket in tickets:
        print(f"\nProcessing Ticket #{ticket['id']}: {ticket['summary']}")
        
        # pass the detailed notes to the agent for resolution
        resolution_plan = agent.resolve_issue(ticket['notes'])
        
        print("Resolution Plan:")
        print(resolution_plan)

if __name__ == "__main__":
    main()