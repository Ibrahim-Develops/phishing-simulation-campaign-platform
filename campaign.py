from utils import simulate_delay, random_click_simulation
from logger import log_event

class Campaign:
    def __init__(self, template_manager, user_manager):
        self.template_manager = template_manager
        self.user_manager = user_manager
        self.results = {}

    def start(self, template_name):
        template = self.template_manager.get_template(template_name)

        if not template:
            print("❌ Template not found.\n")
            return

        print(f"📨 Starting phishing campaign using: {template_name}\n")
        log_event("CAMPAIGN_START", f"Campaign started using template '{template_name}'.")

        for user in self.user_manager.get_all_users():
            simulate_delay()
            clicked = random_click_simulation()
            self.results[user] = "CLICKED" if clicked else "IGNORED"
            
            log_event("EMAIL_SENT", f"Sent to {user}, Action: {self.results[user]}")
            print(f"Sent to {user} → {self.results[user]}")

        print("\n🎉 Campaign Completed.\n")
        log_event("CAMPAIGN_END", "Campaign completed.")

    def show_results(self):
        print("📊 CAMPAIGN RESULTS")
        print("----------------------")
        for user, action in self.results.items():
            print(f"{user}: {action}")
