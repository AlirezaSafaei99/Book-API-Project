import random
import string

# Sample data lists expanded for uniqueness
NAMES = [
    "John", "Jane", "Alice", "Bob", "Charlie", "David", "Emma", "Olivia", "Sophia", "Liam",
    "Noah", "Ethan", "Mason", "Ava", "Isabella", "Mia", "Amelia", "Harper", "Evelyn", "Abigail",
    "Benjamin", "Elijah", "Lucas", "Michael", "Alexander", "Daniel", "Matthew", "Aiden", "Jackson",
    "Sebastian", "Joseph", "Carter", "Owen", "Wyatt", "Jack", "Luke", "Jayden", "Dylan",
    "Grayson", "Levi", "Isaac", "Gabriel", "Julian", "Anthony", "Nathan", "Christian", "Leo", "Thomas"
]

SURNAMES = [
    "Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin",
    "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall",
    "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Scott", "Green", "Adams", "Baker",
    "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker",
    "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan"
]

COUNTRIES = [
    "USA", "Canada", "UK", "Germany", "France", "Italy", "Spain", "Australia", "Brazil", "Japan",
    "Mexico", "India", "China", "Russia", "South Korea", "Netherlands", "Sweden", "Norway", "Denmark", "Switzerland",
    "Portugal", "Argentina", "South Africa", "New Zealand", "Poland", "Ireland", "Belgium", "Finland", "Austria", "Greece"
]

CITIES = [
    "New York", "Toronto", "London", "Berlin", "Paris", "Rome", "Madrid", "Sydney", "Rio de Janeiro", "Tokyo",
    "Mexico City", "Mumbai", "Shanghai", "Moscow", "Seoul", "Amsterdam", "Stockholm", "Oslo", "Copenhagen", "Zurich",
    "Lisbon", "Buenos Aires", "Cape Town", "Auckland", "Warsaw", "Dublin", "Brussels", "Helsinki", "Vienna", "Athens"
]

STREETS = [
    "Main St.", "High St.", "Maple Ave.", "Oak St.", "Pine St.", "Cedar St.", "Elm St.", "Park Ave.", "Broadway", "Sunset Blvd.",
    "5th Avenue", "Madison Ave.", "Wall St.", "Fleet St.", "King St.", "Queen St.", "Baker St.", "Regent St.", "Victoria Rd.", "George St.",
    "Lincoln Ave.", "Church St.", "Station Rd.", "Oxford St.", "Abbey Rd.", "Bridge St.", "Hill St.", "River Rd.", "Greenwood Ave.", "Lakeview Dr."
]

BOOK_TITLES = [
    "The Lost World", "Infinite Horizons", "Shadow of the Past", "Eternal Echoes", "The Silent Guardian",
    "Winds of Fate", "The Forgotten Realm", "Celestial Tides", "The Crimson Crown", "Echoes of Time",
    "Storm of Destiny", "The Midnight Prophecy", "Chronicles of the Unknown", "The Golden Empire",
    "Whispers in the Dark", "Secrets of the Ancients", "The Phantom's Curse", "The Enchanted Kingdom",
    "Rise of the Fallen", "The Hidden Fortress", "Tales from the Abyss", "Dreams of Infinity", "The Shattered Throne",
    "Legends of the Shadow Realm", "Beneath the Crimson Sky", "The Mystic Journey", "The Forgotten Prophecy",
    "The Time Weaver", "The Silent Assassin", "Echoes of Eternity", "The Burning Sky", "Frostborn Legends"
]

def generate_email(name, surname):
    domains = ["example.com", "mail.com", "test.com", "sample.org", "fictional.net", "domain.io"]
    return f"{name.lower()}.{surname.lower()}@{random.choice(domains)}"

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))