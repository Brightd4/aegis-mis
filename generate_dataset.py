import csv
import random
from pathlib import Path

random.seed(42)


def make_examples(templates, terms, label, target_count):
    all_possible = []

    for template in templates:
        for term in terms:
            text = template.format(term=term).strip()
            all_possible.append((text, label))

    random.shuffle(all_possible)

    if target_count > len(all_possible):
        raise ValueError(
            f"Requested {target_count} examples, but only {len(all_possible)} unique combinations are possible."
        )

    return all_possible[:target_count]


political_terms = [
    "the election", "mail-in ballots", "the senate", "the presidency",
    "parliament", "the opposition party", "the ruling party", "campaign donors",
    "the cabinet", "the supreme court"
]

alien_terms = [
    "aliens", "UFO sightings", "extraterrestrials", "secret spacecraft",
    "hidden alien bases", "Area 51 disclosures", "interstellar messages",
    "government contact with aliens"
]

muslim_terms = [
    "Muslims", "Islam", "mosques", "Muslim communities", "Islamic schools",
    "Muslim charities", "Muslim immigrants", "Muslim families"
]

lgbt_terms = [
    "gay people", "lesbian people", "trans people", "transgender youth",
    "LGBTQ communities", "queer students", "same-sex couples", "gender-affirming care"
]

health_terms = [
    "vaccines", "public health guidance", "medical research", "disease prevention",
    "the new treatment", "health agencies", "clinical trials", "hospital policy"
]

general_terms = [
    "scientists", "journalists", "teachers", "public officials", "researchers",
    "community leaders", "universities", "fact-checkers"
]

misinfo_templates = [
    "They are hiding the truth that {term} are part of a secret plan.",
    "The public is not being told that {term} are controlled by hidden elites.",
    "A secret report proves that {term} are part of a cover-up.",
    "The media refuses to admit that {term} are being used to manipulate society.",
    "Authorities do not want you to know the real story about {term}.",
    "There is a hidden agenda behind {term} that officials are covering up.",
    "The mainstream press is lying about {term} to protect powerful interests.",
    "A whistleblower revealed that {term} are tied to a conspiracy.",
    "The government is suppressing evidence about {term}.",
    "The truth about {term} has been deliberately concealed from the public.",
    "Powerful groups are coordinating a deception involving {term}.",
    "Citizens are being misled because the real facts about {term} are hidden.",
    "There is a coordinated effort to silence discussion about {term}.",
    "A secret network is protecting the real story behind {term}.",
    "Public institutions are spreading false narratives about {term}."
]

anti_muslim_misinfo_templates = [
    "People are being told not to question whether {term} are secretly trying to replace local culture.",
    "A hidden plan involving {term} is being protected by the media.",
    "Authorities are covering up the so-called truth that {term} are part of an infiltration strategy.",
    "The public has been misled about the danger posed by {term}.",
    "There is a suppressed report claiming {term} are tied to a secret takeover plot."
]

anti_lgbt_misinfo_templates = [
    "A hidden agenda involving {term} is being imposed without public consent.",
    "The public is being misled about the real goals behind {term}.",
    "Authorities are suppressing criticism of {term} because of political pressure.",
    "There is a secret effort to normalize dangerous ideas through {term}.",
    "The media refuses to expose the so-called truth about {term}."
]

alien_misinfo_templates = [
    "The government has known for years that {term} are real and is hiding the evidence.",
    "A classified program proves {term} have been secretly monitored.",
    "Officials are covering up the truth about {term}.",
    "The public has been lied to about {term} for decades.",
    "A secret base is being used to hide evidence involving {term}."
]

reliable_templates = [
    "Official sources reported updated information about {term}.",
    "Researchers published evidence-based findings related to {term}.",
    "Public records provide verified information on {term}.",
    "A peer-reviewed study discussed {term} in detail.",
    "A verified news report summarized recent developments about {term}.",
    "Experts provided context and evidence regarding {term}.",
    "A public agency released guidance about {term}.",
    "Community leaders issued a factual statement about {term}.",
    "The report on {term} cited multiple credible sources.",
    "Officials clarified misinformation surrounding {term}.",
    "An educational article explained the facts about {term}.",
    "A university briefing discussed {term} using documented evidence.",
    "Journalists interviewed experts about {term} and published a balanced report.",
    "A fact-checking organization reviewed claims about {term} and found no supporting evidence.",
    "Researchers emphasized that claims about {term} should be evaluated using verified evidence."
]

misinfo_examples = []
reliable_examples = []

misinfo_examples += make_examples(misinfo_templates, political_terms, 1, 60)
misinfo_examples += make_examples(alien_misinfo_templates, alien_terms, 1, 35)
misinfo_examples += make_examples(anti_muslim_misinfo_templates, muslim_terms, 1, 35)
misinfo_examples += make_examples(anti_lgbt_misinfo_templates, lgbt_terms, 1, 35)
misinfo_examples += make_examples(misinfo_templates, health_terms + general_terms, 1, 85)

reliable_examples += make_examples(reliable_templates, political_terms, 0, 50)
reliable_examples += make_examples(reliable_templates, alien_terms, 0, 40)
reliable_examples += make_examples(reliable_templates, muslim_terms, 0, 50)
reliable_examples += make_examples(reliable_templates, lgbt_terms, 0, 50)
reliable_examples += make_examples(reliable_templates, health_terms + general_terms, 0, 60)

dataset = misinfo_examples + reliable_examples
random.shuffle(dataset)

output_path = Path("data") / "training_data.csv"
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label"])
    writer.writerows(dataset)

print(f"Saved {len(dataset)} examples to {output_path}")
print("Label distribution:")
print(f"  misinformation (1): {sum(1 for _, label in dataset if label == 1)}")
print(f"  reliable (0): {sum(1 for _, label in dataset if label == 0)}")