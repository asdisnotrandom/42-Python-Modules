from alchemy.grimoire.dark_spellbook import dark_spell_record

if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    try:
        print(f"{dark_spell_record("namelesstoo", "eyeball, fire and tomato")}")
    except Exception as e:
        print(e)