"""
Script for documenting the Landscape Model oudebeek-beek7-tdi scenario.
"""
import os
import base.documentation

root_folder = os.path.abspath(os.path.join(os.path.dirname(base.__file__), ".."))
base.documentation.document_scenario(
    os.path.join(root_folder, "..", "..", "scenario", "rummen-tdi", "scenario.xproject"),
    os.path.join(root_folder, "..", "..", "scenario", "rummen-tdi", "README.md")
)
base.documentation.write_scenario_changelog(
    os.path.join(root_folder, "..", "..", "scenario", "rummen-tdi", "scenario.xproject"),
    os.path.join(root_folder, "..", "..", "scenario", "rummen-tdi", "CHANGELOG.md")
)
base.documentation.write_contribution_notes(
    os.path.join(root_folder, "..", "..", "scenario", "rummen-tdi", "CONTRIBUTING.md"))
