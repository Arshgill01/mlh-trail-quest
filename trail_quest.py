#!/usr/bin/env python3
"""Trail Quest: a tiny choose-your-path outdoor adventure."""

import sys

ENDINGS = {
    "summit": (
        "SUMMIT ENDING",
        "You climb above the treeline as the clouds part. The whole valley\n"
        "glows below you. You made it to the top!",
    ),
    "lost": (
        "LOST ENDING",
        "The trail fades and every tree looks the same. You spend a chilly\n"
        "night under the stars before a ranger finds you at dawn.",
    ),
    "lake": (
        "LAKE ENDING",
        "The river opens into a quiet lake. You skip stones, watch the\n"
        "sunset, and set up camp on the shore. A perfect evening.",
    ),
}


def ask(prompt, options):
    """Ask until the player picks a valid option; return the option key."""
    while True:
        print(prompt)
        for key, label in options.items():
            print(f"  {key}) {label}")
        try:
            answer = input("> ").strip().lower()
        except EOFError:
            print("\nThe trail will wait for you. Goodbye!")
            sys.exit(0)
        if answer in options:
            return answer
        print("Please type one of: " + ", ".join(options) + "\n")


def forest_path():
    print("\nTall pines close in around you. The trail splits at a mossy rock.")
    choice = ask(
        "Do you follow the trail markers uphill or take a shortcut?",
        {"1": "Follow the markers uphill", "2": "Take the shortcut"},
    )
    return "summit" if choice == "1" else "lost"


def river_path():
    print("\nThe river sparkles beside you. Ahead, stepping stones cross it.")
    choice = ask(
        "Do you follow the riverbank or hop across the stones?",
        {"1": "Follow the riverbank", "2": "Hop across the stones"},
    )
    return "lake" if choice == "1" else "lost"


def play():
    print("=== TRAIL QUEST ===")
    print("You stand at the trailhead with a backpack and a full water bottle.\n")
    path = ask(
        "Which path do you take?",
        {"1": "The Forest Path", "2": "The River Path"},
    )
    ending = forest_path() if path == "1" else river_path()
    title, text = ENDINGS[ending]
    print(f"\n*** {title} ***")
    print(text)
    print("\nThanks for playing Trail Quest!")
    return ending


def main():
    play()


if __name__ == "__main__":
    main()
