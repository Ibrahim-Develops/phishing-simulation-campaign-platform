from templates import TemplateManager
from users import UserManager
from campaign import Campaign

if __name__ == "__main__":
    template_manager = TemplateManager()
    user_manager = UserManager()

    template_manager.add_template(
        "Password Reset",
        "Reset Your Password",
        "Your account password needs to be reset. Click here."
    )

    template_manager.add_template(
        "Bank Alert",
        "Unusual Login Detected",
        "We detected suspicious activity. Confirm your identity."
    )

    user_manager.load_users([
        "ali@example.com",
        "ahmed@example.com",
        "fatima@example.com",
        "sara@example.com",
        "usman@example.com"
    ])

    campaign = Campaign(template_manager, user_manager)
    campaign.start("Bank Alert")

    print()
    campaign.show_results()
