
import json
from pathlib import Path
from datetime import datetime
from uuid import uuid4


# Save tickets in a JSON file in the project folder.
TICKETS_FILE = Path("tickets.json")


def create_support_ticket(category, description, transaction_reference=""):
    """Create and save a support ticket."""

    # Do not collect sensitive information.
    forbidden_terms = [
        "password",
        "pin",
        "full card number",
        "card number"
    ]

    text_to_check = f"{category} {description}".lower()

    if any(term in text_to_check for term in forbidden_terms):
        return {
            "success": False,
            "message": (
                "Please remove sensitive information before "
                "creating a ticket. Never provide passwords, "
                "PINs, or full payment card numbers."
            )
        }

    # Load existing tickets, or start with an empty list.
    if TICKETS_FILE.exists():
        with TICKETS_FILE.open("r", encoding="utf-8") as file:
            tickets = json.load(file)
    else:
        tickets = []

    # Create a unique ticket ID.
    ticket_id = f"TICKET-{uuid4().hex[:8].upper()}"

    # Prepare the new ticket.
    ticket = {
        "ticket_id": ticket_id,
        "category": category,
        "description": description,
        "transaction_reference": transaction_reference,
        "status": "Open",
        "created_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        )
    }

    # Save the ticket.
    tickets.append(ticket)

    with TICKETS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4)

    return {
        "success": True,
        "message": "Support ticket created successfully.",
        "ticket": ticket
    }


# Test the tool when this file is run directly.
if __name__ == "__main__":
    print("Nile Finance Support Ticket Tool")
    print("Use fictional information for this test.\n")

    category = input("Issue category: ")
    description = input("Describe the problem: ")
    reference = input("Transaction reference (optional): ")

    result = create_support_ticket(
        category,
        description,
        reference
    )

    print("\nResult:")
    print(json.dumps(result, indent=4))
