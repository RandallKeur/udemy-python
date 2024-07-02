"""Class to represent invitations"""
import os

from src.constants.values import INVITATION_TEMPLATE, GUESTS, INVITATION_OUTPUT_FILEPATH


class InvitationBuilder:
    """Class to represent invitations"""

    def __init__(self):
        self.guests = []
        self.gather_guests()
        self.clear_old_invitations()

    def gather_guests(self) -> None:
        """Gather all the guests to invite"""
        with open(f"{GUESTS}", "r", encoding="utf-8") as file:
            for line in file:
                self.guests.append(line.strip())

    @staticmethod
    def clear_old_invitations() -> None:
        """Clear old invitations from the directory"""
        if os.path.exists(INVITATION_OUTPUT_FILEPATH):
            for file in os.listdir(INVITATION_OUTPUT_FILEPATH):
                os.remove(f"{INVITATION_OUTPUT_FILEPATH}/{file}")

    @staticmethod
    def write_invitation(guest: str) -> None:
        """Write the invitation file for a specified guest"""
        with open(f"{INVITATION_TEMPLATE}", "r", encoding="utf-8") as template:
            contents = template.read()
            with open(f"{INVITATION_OUTPUT_FILEPATH}/letter-for-{guest}.txt", "w", encoding="utf-8") as output_file:
                output_file.write(contents.replace("[name]", guest))

    def write_invitations(self) -> None:
        """Write invitations for all guests"""

        for guest in self.guests:
            self.write_invitation(guest)
        print(f"\n🎉 Invitations written to {INVITATION_OUTPUT_FILEPATH} directory 🎉")
