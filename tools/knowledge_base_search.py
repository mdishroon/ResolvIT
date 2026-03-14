class KnowledgeBaseSearch:
    def __init__(self):
        self.articles = {
            "printer": "Resolution: Ensure the HP LaserJet is connected to the network and restart the print spooler service.",
            "softphone": "Resolution: Verify the Mitel MiCollab SIP registration settings and check the user extension routing.",
            "vpn": "Resolution: Reinstall the VPN client and verify the user has the correct multi factor authentication token."
        }

    def search_articles(self, keyword):
        keyword_lower = keyword.lower()
        for key, article in self.articles.items():
            if key in keyword_lower:
                return f"Knowledge Base Article Found: {article}"
        return "No relevant Knowledge Base articles found for this issue."