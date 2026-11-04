
contacts = [
    {"name": "Asha Patil", "email": "asha@acme.in", "city": "Pune", "tags": ["lead", "ai"]},
    {"name": "Ravi Shah", "email": "ravi@globex.com", "city": "Mumbai", "tags": ["customer"]},
    {"name": "Meera Iyer", "email": "meera@initech.io", "city": "Mumbai", "tags": ["lead"]},
    {"name": "Asha P", "email": "ASHA@acme.in", "city": "Pune", "tags": ["ai"]},
]

# 1. add_contact(book, name, email, city, tags=None) -> bool — add a new contact dict. Normalise the email to lowercase. Return False (and don't add) if that email already exists in the book. Avoid the mutable-default trap for tags.
def add_contact(book, name, email, city, tags=None) -> bool:
    normalized_email = email.strip().lower()

    for contact in book:
        existing_email = contact.get("email", "").strip().lower()

        if existing_email == normalized_email:
            return False

    new_contact = {
        "name": name,
        "email": normalized_email,
        "city": city,
        "tags": list(tags) if tags is not None else []
    }

    book.append(new_contact)
    return True

# 2. find_by_email(book, email) -> dict | None — case-insensitive lookup; return None if not found.
def find_by_email(book,email) -> dict | None :
    normalized_email = email.strip().lower()

    for contact in book:
        existing_email = contact.get("email", "").strip().lower()

        if existing_email == normalized_email:
            return contact

    return None

# 3. contacts_by_city(book) -> dict[str, list[str]] — group contact names by city.
def contacts_by_city(book) -> dict[str, list[str]]:
    city_contacts ={}
    for contact in book:
        city = contact.get("city","")
        name = contact.get("name","")
        city_contacts.setdefault(city, []).append(name)
        return city_contacts

# 4. unique_tags(book) -> set[str] — every tag used across all contacts.
def unique_tags(book: list[dict]) -> set[str]:
    """Return all unique tags used by contacts."""
    return {
        tag
        for contact in book
        for tag in contact.get("tags", [])
    }

# 5. dedupe(book) -> list[dict] — remove contacts with duplicate emails (case-insensitive), keeping the first one seen, and preserving the original order.
def dedupe(book: list[dict]) -> list[dict]:
		"""Remove contacts with duplicate emails (case-insensitive), keeping the first one seen."""
		seen_emails = set()
		deduped_contacts = []

		for contact in book:
				email = contact.get("email", "").strip().lower()
				if email not in seen_emails:
						seen_emails.add(email)
						deduped_contacts.append(contact)

		return deduped_contacts

# 6. search(book, term) -> list[str] — names of contacts whose name or any tag contains term, case-insensitive. Use a comprehension.
def search(book: list[dict], term: str) -> list[str]:
		"""Return names of contacts whose name or any tag contains term, case-insensitive."""
		normalized_term = term.strip().lower()
		return [
				contact.get("name", "")
				for contact in book
				if normalized_term in contact.get("name", "").strip().lower() or
					 any(normalized_term in tag.strip().lower() for tag in contact.get("tags", []))
		]

# 7. tag_counts(book) -> dict[str, int] — how many contacts carry each tag.At the bottom, inside if __name__ == "__main__": (this means "only run when the file is run directly" — details on Day 4), call each function and print the results neatly with f-strings.
def tag_counts(book: list[dict]) -> dict[str, int]:
		"""Return a dictionary with the count of contacts for each tag."""
		counts = {}
		for contact in book:
				for tag in contact.get("tags", []):
						counts[tag] = counts.get(tag, 0) + 1
		return counts


print("\n========== CONTACT BOOK ==========")

print("\n1. Original contacts:")
for contact in contacts:
        print(contact)

print("\n2. Add a new contact:")
added = add_contact(
        contacts,
        "Priya Desai",
        "priya@example.com",
        "Mumbai",
        ["lead", "python"]
    )
print(f"Contact added: {added}")

print("\n3. Find Ravi:")
ravi = find_by_email(contacts, "RAVI@GLOBEX.COM")
print(f"Ravi found: {ravi}")

print("\n4. Find an unknown email:")
unknown = find_by_email(contacts, "unknown@example.com")
print(f"Unknown contact: {unknown}")

print("\n5. Contacts grouped by city:")
print(contacts_by_city(contacts))

print("\n6. Unique tags:")
print(unique_tags(contacts))

print("\n7. Remove duplicate contacts:")
unique_contacts = dedupe(contacts)
print(f"Contacts before dedupe: {len(contacts)}")
print(f"Contacts after dedupe: {len(unique_contacts)}")

for contact in unique_contacts:
		print(contact)

print("\n8. Search for 'ai':")
print(search(contacts, "AI"))

print("\n9. Tag counts:")
print(tag_counts(contacts))

print("\n10. Check mutable-default protection:")

add_contact(
		contacts,
		"Test User One",
		"test1@example.com",
		"Pune"
)

add_contact(
		contacts,
		"Test User Two",
		"test2@example.com",
		"Mumbai"
)

first_tags = contacts[-2]["tags"]
second_tags = contacts[-1]["tags"]

print(f"First tags: {first_tags}")
print(f"Second tags: {second_tags}")
print(f"Are both lists the same object? {first_tags is second_tags}")

print("\n11. Duplicate email check:")
duplicate_added = add_contact(
		contacts,
		"Another Asha",
		"asha@ACME.in",
		"Pune"
)
print(f"Duplicate contact added: {duplicate_added}")

print("\n======================================")