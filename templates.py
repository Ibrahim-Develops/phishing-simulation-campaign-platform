from logger import log_event

class TemplateManager:
    def __init__(self):
        self.templates = []

    def add_template(self, name, subject, body):
        template = {
            "name": name,
            "subject": subject,
            "body": body
        }
        self.templates.append(template)
        log_event("TEMPLATE_ADDED", f"Template '{name}' added.")
        print(f"Template '{name}' added successfully.\n")

    def get_template(self, name):
        for t in self.templates:
            if t["name"].lower() == name.lower():
                return t
        return None
