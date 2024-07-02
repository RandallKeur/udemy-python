""" Day 24 of Coding Challenges for birthday invitations"""
from src.classes.invitation_builder import InvitationBuilder


def prepare_invitations():
    invitation_builder = InvitationBuilder()
    invitation_builder.write_invitations()
